import psycopg2
from db_connetion import *

def insertar_estudiante(id_estudiante, nombre, apellido, codigo_sis, edad):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        insert_estudiante_query="""
        INSERT INTO "ESTUDIANTE" ("id", "NOMBRE", "APELLIDO", "CODIGO SIS.", "EDAD")
        VALUES (%s, %s, %s, %s, %s)"""

        cursor.execute(insert_estudiante_query, (id_estudiante, nombre, apellido, codigo_sis, edad))

        connection.commit()

        print("Se ha insertado al estudiante con exito")
    except(Exception, psycopg2.Error) as error:
        print("Erro al insertar estudiante,", error)
    finally:
        if connection:
            cursor.close()
            close_connection(connection)

def consulta_edad():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        consultar_query="""
        SELECT * FROM "ESTUDIANTE" WHERE "EDAD" > 22
        """

        cursor.execute(consultar_query)

        estudiante = cursor.fetchall()

        return estudiante
    
    except (Exception, psycopg2.Error) as error:
        print("Erro al hacer la consulta,", error)
    
    finally:
        if connection:
            cursor.close()
            close_connection(connection)

print(consulta_edad())