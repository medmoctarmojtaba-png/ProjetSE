#!/bin/bash
# script.sh - Automatisation ProjetSE
# Usage: chmod +x script.sh && ./script.sh

set -e  # stop si une commande échoue

DB_NAME="gestion_commande"
DB_USER="root"
DB_PASS="root_password"
SQL_FILE="requete.sql"
COMPOSE_FILE="docker-compose.yml"

echo "=== 1. Vérification des fichiers ==="
if [[ ! -f "$COMPOSE_FILE" ]]; then
    echo "Erreur: $COMPOSE_FILE introuvable"
    exit 1
fi
if [[ ! -f "$SQL_FILE" ]]; then
    echo "Erreur: $SQL_FILE introuvable"
    exit 1
fi

echo "=== 2. Lancement de la stack Docker ==="
docker-compose -f "$COMPOSE_FILE" down -v 2>/dev/null || true
docker-compose -f "$COMPOSE_FILE" up -d --build

echo "=== 3. Attente du démarrage MySQL ==="
echo "Attente 10s pour que MySQL soit prêt..."
sleep 10

# Boucle de vérification que MySQL répond
until docker exec mysql_server mysqladmin ping -h"localhost" -u"$DB_USER" -p"$DB_PASS" --silent; do
    echo "MySQL n'est pas encore prêt, on attend 3s..."
    sleep 3
done
echo "MySQL est prêt !"

echo "=== 4. Exécution du script SQL ==="
docker exec -i mysql_server mysql -u"$DB_USER" -p"$DB_PASS" < "$SQL_FILE"
echo "Base $DB_NAME initialisée avec succès"

echo "=== 5. Vérification des conteneurs ==="
docker-compose ps

echo "=== 6. Test connexion web ==="
sleep 2
curl -s http://localhost:8080 || echo "Vérifie que le service web tourne sur le port 8080"

echo "=== TERMINÉ ==="
echo "Accès web: http://localhost:8080"
echo "Accès MySQL: docker exec -it mysql_server mysql -u$DB_USER -p$DB_PASS $DB_NAME"