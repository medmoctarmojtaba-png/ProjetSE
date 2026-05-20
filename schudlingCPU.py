class Processus:
    def __init__(self, pid, arrivee, burst):
        self.pid = pid
        self.arrivee = arrivee
        self.burst = burst
        self.restant = burst
        self.temps_fin = 0
        self.temps_attente = 0
        self.temps_rotation = 0
        self.premiere_exec = -1

def srtf(processus_liste):
    n = len(processus_liste)
    temps = 0
    termines = 0
    gantt = []
    proc_courant = None
    proc_temps_debut = 0
    
    # Copie pour ne pas modifier l'original
    proc = [Processus(p.pid, p.arrivee, p.burst) for p in processus_liste]
    
    while termines < n:
        # Trouver le processus avec le plus petit temps restant parmi ceux arrivés
        candidats = [p for p in proc if p.arrivee <= temps and p.restant > 0]
        
        if not candidats:
            temps += 1
            continue
            
        proc_elu = min(candidats, key=lambda x: x.restant)
        
        # Si changement de processus, log Gantt
        if proc_courant != proc_elu:
            if proc_courant is not None:
                gantt.append((proc_courant.pid, proc_temps_debut, temps))
            proc_courant = proc_elu
            proc_temps_debut = temps
            if proc_elu.premiere_exec == -1:
                proc_elu.premiere_exec = temps
        
        # Exécuter 1 unité de temps
        proc_elu.restant -= 1
        temps += 1
        
        # Si terminé
        if proc_elu.restant == 0:
            proc_elu.temps_fin = temps
            proc_elu.temps_rotation = proc_elu.temps_fin - proc_elu.arrivee
            proc_elu.temps_attente = proc_elu.temps_rotation - proc_elu.burst
            termines += 1
    
    # Dernier segment Gantt
    if proc_courant is not None:
        gantt.append((proc_courant.pid, proc_temps_debut, temps))
    
    return proc, gantt

def round_robin(processus_liste, quantum=2):
    n = len(processus_liste)
    temps = 0
    termines = 0
    gantt = []
    file_attente = []
    proc = [Processus(p.pid, p.arrivee, p.burst) for p in processus_liste]
    
    # Ajouter les processus arrivés au temps 0
    for p in proc:
        if p.arrivee <= temps:
            file_attente.append(p)
    
    idx_arrivee = n  # Index pour suivre les nouveaux arrivants
    
    while termines < n:
        if not file_attente:
            temps += 1
            # Ajouter les nouveaux arrivants
            for p in proc:
                if p.arrivee == temps and p.restant > 0:
                    file_attente.append(p)
            continue
        
        p_courant = file_attente.pop(0)
        if p_courant.premiere_exec == -1:
            p_courant.premiere_exec = temps
        
        temps_exec = min(quantum, p_courant.restant)
        gantt.append((p_courant.pid, temps, temps + temps_exec))
        
        p_courant.restant -= temps_exec
        temps += temps_exec
        
        # Ajouter les processus arrivés pendant l'exécution
        for p in proc:
            if p.arrivee > (temps - temps_exec) and p.arrivee <= temps and p.restant > 0 and p not in file_attente and p != p_courant:
                file_attente.append(p)
        
        if p_courant.restant > 0:
            file_attente.append(p_courant)
        else:
            p_courant.temps_fin = temps
            p_courant.temps_rotation = p_courant.temps_fin - p_courant.arrivee
            p_courant.temps_attente = p_courant.temps_rotation - p_courant.burst
            termines += 1
    
    return proc, gantt

def afficher_resultats(nom_algo, processus, gantt):
    print(f"\n=== {nom_algo} ===")
    print("Gantt Chart:")
    for pid, debut, fin in gantt:
        print(f"| P{pid} [{debut}-{fin}] ", end="")
    print("|")
    
    print("\nPID | Arrivée | Burst | Fin | Rotation | Attente")
    print("-" * 50)
    total_attente = 0
    total_rotation = 0
    for p in processus:
        print(f"P{p.pid}  |   {p.arrivee}    |  {p.burst}   | {p.temps_fin}  |    {p.temps_rotation}    |   {p.temps_attente}")
        total_attente += p.temps_attente
        total_rotation += p.temps_rotation
    
    print(f"\nTemps d'attente moyen: {total_attente/len(processus):.2f}")
    print(f"Temps de rotation moyen: {total_rotation/len(processus):.2f}")

if __name__ == "__main__":
    # Exemple de test
    processus_test = [
        Processus(1, 0, 8),
        Processus(2, 1, 4),
        Processus(3, 2, 9),
        Processus(4, 3, 5)
    ]
    
    print("Données d'entrée:")
    print("PID | Arrivée | Burst")
    for p in processus_test:
        print(f"P{p.pid}  |   {p.arrivee}    |  {p.burst}")
    
    # Exécuter SRTF
    proc_srtf, gantt_srtf = srtf(processus_test)
    afficher_resultats("SRTF", proc_srtf, gantt_srtf)
    
    # Exécuter Round Robin quantum=2
    proc_rr, gantt_rr = round_robin(processus_test, quantum=2)
    afficher_resultats("Round Robin Q=2", proc_rr, gantt_rr)