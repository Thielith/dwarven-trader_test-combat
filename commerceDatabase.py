import MySQLdb
import sys
from database import *
import random
db = MySQLdb.connect(host="localhost",  # your host
              					user="root",  # username
                                                passwd="p2950",  # password
                                                db="test_dwarven")  # name of $
cur = db.cursor()


class Transaction:
	def __init__(self,id,unit_idA, unit_idB,itemTypeA,quantityA,itemTypeB,quantityB):
		self.id = id
		self.unit_idA = unit_idA
		self.unit_idB = unit_idB
		self.itemTypeA = itemTypeA
		self.quantityA = quantityA
		self.itemTypeB = itemTypeB
		self.quantityB = quantityB
	def update(self,database):
		self.updateItems(database,self.unit_idA,self.unit_idB,self.quantityA,self.itemTypeA)
                self.updateItems(database,self.unit_idB,self.unit_idA,self.quantityB,self.itemTypeB)

	def updateItems(self, database, buyer, seller, quantity, item_id):
		print(str(buyer))
		print(str(seller))
		
		connection = database.cursor()
	        query = "select * from items where ownerID = " + str(buyer) + " and itemID =" + str(item_id) 
		print(query)
		connection.execute(query)
		
		values = connection.fetchall()
		# add quantityA to unit unitA
		if values.__len__() > 0: #did the unit already have an entry for this item?
			oldValue = values[0][1]
			#print("old value next")
			#print(oldValue)
			#print(quantity)
			newValue = int(oldValue) + int(quantity)
			print(newValue)
			sqlCommand = "UPDATE items  SET quantity ="  + str(newValue) + " WHERE ownerID = "  + str(buyer) + " and itemID = " + str(item_id)
			connection.execute(sqlCommand)
			database.commit()			
			print("a")
		else:
			#insert
	                fields = ["ownerID","quantity","qualityID","itemID"]
			values = [buyer,quantity,1,item_id]
	                insertIntoDatabase(database,"items",fields,values)
     
			print("b")
		#print(sqlCommand)
	       	if values.__len__()>1:
                        print("error in update items duplicate entries for unit id")

		#take away quantityA from unitB
                
		query = "select * from items where ownerID = " + str(seller) + " and itemID =" + str(item_id)
                print(query)
		connection.execute(query)
                values = connection.fetchall()
		if values.__len__()>1:
			print("error in update items duplicate entries for unit id") 
		for value in values:
			print(value)
		if values.__len__() == 0:
			print("sold item that was not owned")
		else:
			oldValue = values[0][1]
			print("old:" + str(oldValue))
			print("quantity" + str(quantity))
			sqlCommand = "UPDATE  items  SET quantity ="+ str(oldValue - quantity) 
			sqlCommand += " WHERE ownerID = "  + str(self.unit_idB) + " and itemID = " + str(item_id)

		#remove transaction from transactions
		deleteFromTableWhereID(database,"transactions",self.id)
		#add transaction to historical transactions
def updateItemsFromTransactions(database):
	#read all transactions
        transactions = []
	connection = database.cursor()
	query = "select * from transactions"
        connection.execute(query)

	values = connection.fetchall()
	for t in values:
		print(t)
		transactions.append(Transaction(t[0],t[1],t[2],t[3],t[4],t[6],t[7]))
	#update items to reflect change in total from transactions
	for t in transactions:
		t.update(database)
	#cache transactions into a historicalTransactionsTable to be used by AI
	#clear table transactions
def createTestTransaction(database):
        #connection = database.cursor()
	itemStart =  594
	itemEnd =  641

	for i in range(1000):
		seller = i
		while seller == i:
			seller = random.randint(1,10)
		fields = ["buyerID","sellerID","itemType","quantity","location","itemTypeB","quantityB"]
		values = [i,seller,random.randint(itemStart,itemEnd),random.randint(1,2),1,random.randint(itemStart,itemEnd),random.randint(11,20)]
                insertIntoDatabase(database,"transactions",fields,values)

def createTransaction(database,buyerID,sellerID,itemType,quantity,location,itemTypeB,quantityB):
	fields = ["buyerID","sellerID","itemType","quantity","location","itemTypeB","quantityB"]
        values = [buyerID,sellerID,itemType,quantity,location,itemTypeB,quantityB]
        insertIntoDatabase(database,"transactions",fields,values)
	

createTestTransaction(db)
updateItemsFromTransactions(db)
