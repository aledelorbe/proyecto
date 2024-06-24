#! /usr/bin/env python

import mysql.connector

try:
    # Configuración de conexión
    config = {
        'user': 'root',
        'password': '12345678',
        'host': 'localhost',
        'database': 'sociodemografico',
        'port': '3306',
        'raise_on_warnings': True
    }

    # Conectarse a MySQL
    conn = mysql.connector.connect(**config)

    # Preparar la consulta SQL
    query = "SELECT * FROM cancer;"

    # Crear un cursor para ejecutar la consulta
    cursor = conn.cursor()

    # Ejecutar la consulta
    cursor.execute(query)

    # Obtener todos los registros
    records = cursor.fetchall()

    # Mostrar los registros obtenidos
    for row in records:
        print(row)  # Aquí puedes procesar cada fila como desees

    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()

except mysql.connector.Error as e:
    print(f"Error al conectar a MySQL: {e}")

