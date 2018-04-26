from database import *
import random
d = MySQLdb.connect(host="localhost",  # your host
user="root",  # username
passwd="p2950",  # password
db="test_dwarven")  # name of the database
cur = d.cursor()

#insertIntoDatabase(d,"_item_",['nameID','commodity','basePrice'],["Wheat",1,1])
#insertIntoDatabase(d,"_item_",['nameID','commodity','basePrice'],["Iron",2,2])
insertIntoDatabase(d,"_item_",['nameID','commodity','basePrice'],["Lumber",2,5])

def create_tools():
	pass	
def create_recipes():
#	insertIntoDatabase(d,"_recipe_",['itemA','quantityA','itemB','quantityB','toolA','resultA','resultQuantityA'],[1,1,3,1,1,4,10])
        insertIntoDatabase(d,"_recipe_",['itemA','quantityA','itemB','quantityB','toolA','resultA','resultQuantityA'],[1,1,3,1,1,4,10])
	insertIntoDatabase(d,"_item_",['nameID','commodity','basePrice'],["Stone",2,5])
        insertIntoDatabase(d,"_recipe_",['itemA','quantityA','itemB','quantityB','toolA','resultA','resultQuantityA'],[4,3,2,1,2,4,10])


def getWorldEconDataP():
	'''
	data = getAllDataInTable(d,'transactions')
	sums = []
	for i in range(5):
		sums.append(0)
	for transaction in data:
		for i in range(5):
			if i+1 == transaction[3]:
				sums[i-1] += int(transaction[4])
	print(sums)
	'''
def getTransactionDetails():
	for i in range(4):
		x = getFromDatabaseSumOfFieldInTableByGroupWhereXisY(d , "quantity","transactions","itemType","location",i+1)
		for v in x:
			print(v[0])

def calculateIndividualValue():
	pass
	#is this something I want purely for luxury?
	#is this a staple that I need?
	#is this something I believe is liquid enough to trade?
	#is this something that I use to make more valuable items?

def calculatePrices():
    pass
#getTransactionDetails()
create_recipes()
