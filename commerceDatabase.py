
import MySQLdb
import sys
from database.py import *

db = MySQLdb.connect(host="localhost",  # your host
              					user="root",  # username
                                                passwd="p2950",  # password
                                                db="test_dwarven")  # name of $
cur = db.cursor()

def getSumOfItemsForID(database,item,id):
        connection = database.cursor()
        query = "select sum(quantity) from items where itemid = " + str(item) +$
        print(query)
        values = connection.fetchall()
        return values

class Transaction:
	def __init__(self,buyerID, sellerID,itemType,quantity,itemTypeB,quantityB):
		self.buyerID = buyerID
		self.sellerID = sellerID
		self.itemType = itemType
		self.quantity = quantiy
		self.itemTypeB = itemTypeB
		self.quantityB = quantityB
	
	def updateItems(self,database):
		#add to buyers quantity
		#see if buyer already had this item
		connection = database.cursor()
	        query = "select * from items where playerID = " + str(self.buyerID) + " and itemID =" + self.itemType 
		connection.execute(query)
		values = connection.fetchall()
		if values.__len__() > 0: #did the unit already have an entry for this item?
			sqlCommand = "UPDATE " + items + " SET" + quantity + " WHERE playerID = "  + self.buyerID + " and itemType = " + self.itemType
	        	connection.execute(sqlCommand)

		#take away from sellers quantiy
		#remove transaction from transactions
		#add transaction to historical transactions
def updateItemsFromTransactions(database):
	#read all transactions
        transactions = []
	connection = database.cursor()
	query = "select * from transactions"
        connection.execute(sqlCommand)

	values = connection.fetchall()
	for t in values:
		transactions.append(Transaction(t[1],t[2],t[3],t[4],t[6],t[7])
	
	#update items to reflect change in total from transactions
	#cache transactions into a historicalTransactionsTable to be used by AI
	#clear table transactions

