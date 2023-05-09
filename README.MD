# Ejercicio de Airflow en un contenedor de Docker

En este conjunto de archivos están el Dockerfile que utilizo para modificar la imagen base de Apache Airflow y le agrego librerías adicionales necesarios para la consulta al API. Luego, construyo la imagen a partir de un docker-compose.yaml proporcionado por el propio Apache con algunas modificaciones para que utilice el Dockerfile como base y otros detalles. Posteriormente se levanta el contenedor y ya se puede ejecutar el código de Python que contiene la carpeta "dags" llamado "ETL.py y que forma el DAG del ejercicio. Para ingresar al servidor web de localhost que creaa Airflow se usa la palabra "airflow" como usuario y contraseña.

Dentro del pipeline, se conecta a la base de datos PostgreSQL creada también en el contenedor, se crea la tabla necesaria y posteriormente se consulta la API y se envía la información a dicha base de datos.

## RECORDATORIO

Si se clona este repositorio desde Github, recuerden por favor crear las carpetas "logs" y "plugins" antes de ejecutar el yaml para que el contenedor almacene bien los archivos que necesita.