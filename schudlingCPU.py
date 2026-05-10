def round_robin(process_list,time_quanta):
    t=0
    gantt = []
    completed = {}
    process_list.sort()
    burst_times ={}
    for p in process_list:
        pid =p[2]
        burst_time =p[1]
        burst_times[pid] = burst_time
    print(burst_times)

    while process_list !=[]:
        valable =[]
        for p in process_list:
            at = p[0]
            if p[0] <= t :
                valable.append(p)
        #no process valable
        if valable ==[]:
            gantt.append("Idle")
            t += 1
            continue
        else:
            process = valable[0]
            #process serve maintenat
            gantt.append(process[2])
            #puis deplacer le process
            process_list.remove(process)
            #update le temps d'execution
            rem_burst = process[1]
            if rem_burst <= time_quanta:
                t += rem_burst
                ct = t
                pid = process[2]
                arrival_time = process[0]
                burst_time = burst_times[pid]
                tt = ct - arrival_time
                wt = tt -burst_time
                completed[process[2]] = [ct,tt,wt]
                continue
            else:
                t +=time_quanta
                process[1] -= time_quanta
                process_list.append(process)
    print(gantt)
    print(completed)



if __name__=="__main__":
    process_list = [[2,6,"p1"],[5,2,"p2"],[1,8,"p3"],[0,3,"p4"],[4,4,"p5"]]
    time_quanta = 2
    round_robin(process_list,time_quanta)
