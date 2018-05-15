import MySQLdb
import sys
from database import *

db = MySQLdb.connect(host="localhost",  # your host
              					user="root",  # username
                                                passwd="p2950",  # password
                                                db="test_dwarven")  # name of $
cur = db.cursor()


class Transaction:
	def __init__(self,unit_idA, unit_idB,itemTypeA,quantityA,itemTypeB,quantityB):
		self.unit_idA = unit_idA
		self.unit_idB = unit_idB
		self.itemTypeA = itemTypeA
		self.quantityA = quantityA
		self.itemTypeB = itemTypeB
		self.quantityB = quantityB
	def update(self,database):
		self.updateItems(database,self.unit_idA,self.unit_idB,self.quantityA,self.itemTypeA)
                self.updateItems(database,self.unit_idB,self.unit_idA,self.quantityB,self.itemTypeB)

	def updateItems(self,database, buyer, seller, quantity, item_id):
		print(str(buyer))
		print(str(seller))
		
		connection = database.cursor()
	        query = "select * from items where ownerID = " + str(buyer) + " and itemID =" + str(item_id) 
		print(query)
		connection.execute(query)
		
		values = connection.fetchall()
		# add to quantityA to unit unitA
		if values.__len__() > 0: #did the unit already have an entry for this item?
			oldValue = values[0]
			sqlCommand = "UPDATE items  SET quantity ="  + str(oldValue + quantity) + " WHERE ownerID = "  + str(buyer) + " and itemType = " + str(item_id)
		else:
                        sqlCommand = "UPDATE  items SET quantity =" + str(quantity) + " WHERE ownerID = "  + str(buyer) + " and itemType = " + str(item_id)
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
			oldValue = values[0]
			sqlCommand = "UPDATE  items  SET quantity ="+ str(oldValue - quantity) + " WHERE ownerID = "  + self.unit_idB + " and itemType = " + self.itemType

		#remove transaction from transactions
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
		transactions.append(Transaction(t[1],t[2],t[3],t[4],t[6],t[7]))
	#update items to reflect change in total from transactions
	for t in transactions:
		t.update(database)
	#cache transactions into a historicalTransactionsTable to be used by AI
	#clear table transactions

updateItemsFromTransactions(db)
