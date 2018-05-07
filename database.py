import MySQLdb
import sys

db = MySQLdb.connect(host="localhost",  # your host
						 user="root",  # username
						 passwd="p2950",  # password
						 db="test_dwarven")  # name of the database
cur = db.cursor()

def getFromDatabaseSumOfFieldInTableByGroupWhereXisY(database,field,table,group,x,y):
	connection = database.cursor()
	query = "select sum(" +  field + ")  from " + table +  " where " +str(x) +  " = " + str(y) + " group by " + group + ";"
	print(query)
	connection.execute(query)
	values = connection.fetchall()
	ret = []
	for v in values:
		ret.append(v)
	return ret
def insertIntoDatabase(database,tableName,names,values):
	connection = database.cursor()
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
	e = connection.execute(sqlCommand)
	print(e)
	print("commit insert")
	database.commit()

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
def updateCombatDB(connection,playerID, strength, aglility, currentHP, maxHP, encounterID):
	names = ["playerID","strength","agility","currentHP","maxHP","encounterID"]
	values = [playerID, strength, aglility, currentHP, maxHP, encounterID]
	c = updateDatabaseData(connection, "units" , names, values)

def updateUnitData(connection, tableName, collummNames, values, extra):
	collummString = ""
	i = 0
	for name in collummNames:
		if i == 7:
			collummString += " " + name + " = '" + str(values[i]) + "'"
		else:
			collummString += " " + name + " = " + str(values[i])
		collummString += ","
		i+=1
	collummString = collummString.strip(',')
	sqlCommand = "UPDATE " + tableName + " SET" + collummString + " WHERE id = " + extra + ";"
	print(sqlCommand)
	connection.execute(sqlCommand)
def updateUnitDB(connection, id, strength, aglility, currentHP, maxHP, encounterID, level, name, advantage):
	names = ["id","strength","agility","currentHP","maxHP","encounterID","level","name","advantage"]
	values = [id, strength, aglility, currentHP, maxHP, encounterID,level,name,advantage]
	c = updateUnitData(connection, "units" , names, values, id)
	
def getDataFromTableByID(connection, table, idName, id):
	#returns a list of all entries matching the id to idName
	sqlCommand = "SELECT * FROM  " + table + " WHERE " + idName + " = '" +  str(id) + "';"
	connection.execute(sqlCommand)
	values = connection.fetchall();
	ret = []
	for v in values:
		ret.append(v)
#	print(ret)
	return ret
	
if sys.argv[1] != None:
	if sys.argv[1] == "updateUnits":
		print("updating player" + sys.argv[8])
		updateUnitDB(cur,sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8],sys.argv[9],sys.argv[10])
		print("commit update")
		db.commit();
		print("close")
		db.close();

'''
elif sys.argv[7] == "update":
	print("updating player data")
	updateCombatDB(cur,sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])
	print("commit update")
	db.commit();
	print("close")
	db.close();
'''
#x = getDataFromTableByID(cur,"player","player_name","Billy")

def getAllDataInTable(database, table):
	connection = database.cursor()
	sqlCommand = "SELECT * FROM  " + table +";"
	print(sqlCommand)
	connection.execute(sqlCommand)
	
	values = connection.fetchall();
	ret = []
	for v in values:
		ret.append(v)
#	print(ret)
	return ret
