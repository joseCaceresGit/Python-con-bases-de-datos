import psycopg2

def get_connection():
    return psycopg2.connect(
        user="nombre de tu usuario postgres",
        password="tu contraseña",
        host="127.0.0.1",
        port="5432",
        database="nombre de tu base de datos"
    )

def close_connection(connection):
    if connection:
        connection.close()