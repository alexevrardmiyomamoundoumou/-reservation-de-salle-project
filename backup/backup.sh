#!/bin/bash

PROJECT_DIR="/home/alex/Bureau/-reservation-de-salle-project"
BACKUP_DIR="$PROJECT_DIR/backup/files/$(date +'%Y-%m-%d_%H-%M')"
mkdir -p "$BACKUP_DIR"

declare -A CONTAINERS
CONTAINERS=(
  ["reservation"]="reservation-de-salle-project-reservation-db-1"
  ["salle"]="reservation-de-salle-project-salle-db-1"
  ["user"]="reservation-de-salle-project-user-db-1"
)

for service in reservation salle user; do
  echo " Sauvegarde du code de ${service}-service..."
  if [ -d "$PROJECT_DIR/${service}-service" ]; then
    cp -r "$PROJECT_DIR/${service}-service" "$BACKUP_DIR/"
  else
    echo "  ❌ Dossier ${service}-service introuvable"
  fi

  echo " Sauvegarde de la base de données de $service (conteneur: ${CONTAINERS[$service]})..."
  docker exec "${CONTAINERS[$service]}" pg_dump -U postgres -d ${service}_db > "$BACKUP_DIR/${service}_db.sql" 2>/dev/null || echo "  ❌ Conteneur ${CONTAINERS[$service]} introuvable ou erreur pg_dump"
done

echo "✅ Sauvegardes locales terminées dans : $BACKUP_DIR"
echo "📂 Dossiers trouvés dans $PROJECT_DIR :"
ls "$PROJECT_DIR"

