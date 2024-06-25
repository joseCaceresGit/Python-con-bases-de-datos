# Python-con-bases-de-datos

Este repositorio contiene el codigo desarrollado en el curso introductorio a Python con bases de datos.

Para ejecutar el programa es nesario instalar Psycopg 2 con el siguiente comando en el directorio del proyecto:

pip install psycopg2-binary

Tambien es necesario tener un base de datos con la siguiente tabla:

CREATE TABLE "ESTUDIANTE" (
  "id" int4 NOT NULL,
  "NOMBRE" varchar(255),
  "APELLIDO" varchar(255),
  "CODIGO SIS." varchar(255),
  "EDAD" int2,
  PRIMARY KEY ("id")
);

Para correr el programa ejecutar:

main.py