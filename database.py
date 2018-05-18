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
def deleteFromTableWhereID(database,table,id, idName = "id"):
        connection = database.cursor()
	query = "delete from " + table + " where " + idName + " == " + id + ";"
        connection.execute(query)

def getSumOfItemsForID(database,item,id):
	connection = database.cursor()
	query = "select sum(quantity) from items where itemid = " + str(item) + " and ownerID = " + str(id) +";"
	print(query)
	values = connection.fetchall()
	return values


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

def updateDatabaseData(connection,tableName,collummNames, values, idName = "playerID"):
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

def updateStatusData(connection, tableName, collummNames, values):
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
def updateStatusDB(connection, unitID, statusID, magnitude):
	names = ["unitID", "statusID", "magnitude"]
	values = [unitID, statusID, magnitude]
	c = updateStatusData(connection, "statuses", names, values)
def deleteStatusByUnitID(connection, tableName, unitID):
	sqlCommand = "DELETE FROM " + tableName + " WHERE unitID = " + unitID
	print(sqlCommand)
	connection.execute(sqlCommand)

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
try:
	if sys.argv[1] != None:
		if sys.argv[1] == "updateUnits":
			print("updating player" + sys.argv[8])
			updateUnitDB(cur,sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8],sys.argv[9],sys.argv[10])
			print("commit update")
			db.commit();
			print("close")
			db.close();
	
		elif sys.argv[1] == "deleteStatusByUnitID":
			print("deleting statuses with userID of " + sys.argv[2])
			deleteStatusByUnitID(cur, "statuses", sys.argv[2])
			print("commit update")
			db.commit();
			print("close")
			db.close();
	
		elif sys.argv[1] == "updateStatus":
			print("adding statuses")
			updateStatusDB(cur, sys.argv[2], sys.argv[3], sys.argv[4])
			print("commit update")
			db.commit();
			print("close")
			db.close();
except:
	print("invaild call to system variable")
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
