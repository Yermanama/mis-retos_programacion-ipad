""" Realiza una conexión desde el lenguaje que hayas seleccionado a la siguiente
base de datos MySQL:
- Host: mysql-5707.dinaserver.com
- Port: 3306
- User: mouredev_read
- Password: mouredev_pass
- Database: moure_test
Una vez realices la conexión, lanza la siguiente consulta e imprime el resultado:
- SELECT * FROM `challenges`
Se pueden usar librerías para realizar la lógica de conexión a la base de datos."""

import mysql.connector

conexion = mysql.connector.connect(host='mysql-5707.dinaserver.com', port='3306', user='mouredev_read',
                                   password='mouredev_pass', database='moure_test')
cursor = conexion.cursor()
query = 'SELECT * FROM challenges'
cursor.execute(query)

resultados = cursor.fetchall()
for row in resultados:
    print(row)

conexion.close()
