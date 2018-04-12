import MySQLdb
import sys

db = MySQLdb.connect(host="localhost",  # your host
                     user="root",  # username
                     passwd="p2950",  # password
                     db="calverdwarven")  # name of the database
cur = db.cursor()

def insertIntoDatabase(connection,tableName,names,values):
	insertString = "("
	valueString = "("
	i = 0
	for name in names:
		insertString += name +","
		valueString += "'" + str(values[i]) + "'"
		valueString += ","
		i+=1
	insertString = insertString.strip(',')
	valueString = valueString.strip(',')
	insertString += ")"
	valueString += ")"
	sqlCommand = "INSERT INTO " + tableName + " " + insertString + " VALUES " + valueString + ";"
	print(sqlCommand)
	connection.execute(sqlCommand)
	print("commit insert")
	db.commit();
#def updateDatabaseData(connection,tableName,collummNames, values):
#	collummString = ""
#	i = 0
#	for name in collummNames:
#		collummString += " " + name + " = " + str(values[i])
#		collummString += ","
#		i+=1
#	collummString = collummString.strip(',')
#	sqlCommand = "UPDATE " + tableName + " SET" + collummString + " WHERE playerID = " + sys.argv[1] + ";"
#	print(sqlCommand)
#	connection.execute(sqlCommand)


def insertUnitsDB(connection,id):
	names = ["id"]
	values = [id]
	c = insertIntoDatabase(connection, "units", names, values)

#def updateUnitsDB(connection,id):
#	names = ["id"]
#	values = [id]
#	c = updateIntoDatabase(connection, "units", names, values)
	

if sys.argv[2] == "insert":
	print("adding data")
	insertUnitsDB(cur,sys.argv[1])
	print("commit update")
	db.commit();
	print("close")
	db.close();
	
#elif sys.argv[2] == "update":
#	print("updating unit data")
#	updateUnitsDB(cur,sys.argv[1])
#	print("commit update")
#	db.commit();
#	print("close")
#	db.close();

#x = getDataFromTableByID(cur,"player","player_name","Billy")


