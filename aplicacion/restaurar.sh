#!/bin/bash

# Variables
DB_NAME="sociodemografico"
DB_USER="root"
DB_PASS="ale123"
SQL_DIR="/home/ale/Escritorio/proyecto/sociodemografico"

# Restaurar todos los archivos .sql en la carpeta
for sql_file in $SQL_DIR/*.sql; do
  echo "Restaurando $sql_file en la base de datos $DB_NAME..."
  mysql -u $DB_USER -p$DB_PASS $DB_NAME < $sql_file
done

echo "Restauración completa."
