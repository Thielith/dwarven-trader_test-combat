import MySQLdb
import sys
class dbConnection:
	db = MySQLdb.connect(host="localhost",  # your host
						 user="root",  # username
						 passwd="p2950",  # password
						 db="test_dwarven")  # name of the database
	cur = db.cursor()

db = MySQLdb.connect(host="localhost",  # your host
						 user="root",  # username
						 passwd="p2950",  # password
						 db="test_dwarven")  # name of the database
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

def updateDatabaseData(connection,tableName,collummNames, values):
	collummString = ""
	i = 0
	for name in collummNames:
		collummString += " " + name + " = " + str(values[i])
		collummString += ","
		i+=1
	collummString = collummString.strip(',')
	sqlCommand = "UPDATE " + tableName + " SET" + collummString + " WHERE playerID = " + sys.argv[1] + ";"
	print(sqlCommand)
	connection.execute(sqlCommand)


def addToCombatEncountersDB(connection,playerID, strength, aglility, currentHP, maxHP, encounterID):
	names = ["playerID","strength","agility","currentHP","maxHP","encounterID"]
	values = [playerID, strength, aglility, currentHP, maxHP, encounterID]
	c = insertIntoDatabase(connection, "units", names, values)

def updateCombatDB(connection,playerID, strength, aglility, currentHP, maxHP, encounterID):
	names = ["playerID","strength","agility","currentHP","maxHP","encounterID"]
	values = [playerID, strength, aglility, currentHP, maxHP, encounterID]
	c = updateDatabaseData(connection, "units" , names, values)


def getDataFromTableByID(connection, table, idName, id):
	#returns a list of all entries matching the id to idName
	sqlCommand = "SELECT * FROM  " + table + " WHERE " + idName + " = '" +  str(id) + "';"
	connection.execute(sqlCommand)
	values = connection.fetchall();
	ret = []
	for v in values:
		ret.append(v)
	print(ret)
	return ret
	

if sys.argv[7] == "units":
	print("adding transaction")
	addToCombatDB(cur,sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])
	print("commit update")
	db.commit();
	print("close")
	db.close();
	
elif sys.argv[7] == "update":
	print("updating player data")
	updateCombatDB(cur,sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])
	print("commit update")
	db.commit();
	print("close")
	db.close();

#x = getDataFromTableByID(cur,"player","player_name","Billy")


