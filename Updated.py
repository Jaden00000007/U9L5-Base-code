import mysql.connector

def data_base_connector():
    connection = mysql.connector.connect(user='evanl127',
                                      password='234642536',
                                      host='10.8.37.226',
                                      database='evanl127_db')

    return connection

def executeStatement(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    for row in cursor:
        print("Period: "+ str(row[0]))
        print("Course: " + row[1])
        print("Room: " + row[2])
        print("Teacher: " + row[3])
    cursor.close()
    connection.close()

connection = data_base_connector()
stid = int(input("pick a student id from 1-5,000:  "))
query = "call sched_get(" + str(stid) + ");"
executeStatement(connection, query)
