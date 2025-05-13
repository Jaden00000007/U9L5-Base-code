import mysql.connector


connection = mysql.connector.connect(user='evanl127',
                                  password='234642536',
                                  host='10.8.37.226',
                                  database='evanl127_db')




cursor = connection.cursor()


stid = int(input("pick a student id from 1-5,000:  "))


query = "call sched_get(" + str(stid) + ");"


cursor.execute(query)


for row in cursor:
   print("Period: "+ str(row[0]))
   print("Course: " + row[1])
   print("Room: " + row[2])
   print("Teacher: " + row[3])




cursor.close()
connection.close()
