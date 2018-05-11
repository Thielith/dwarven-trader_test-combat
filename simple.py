from database import *
import random
d = MySQLdb.connect(host="localhost",  # your host
user="root",  # username
passwd="p2950",  # password
db="test_dwarven")  # name of the database
cur = d.cursor()

#insertIntoDatabase(d,"_item_",['nameID','commodity','basePrice'],["Wheat",1,1])
#insertIntoDatabase(d,"_item_",['nameID','commodity','basePrice'],["Iron",2,2])
#insertIntoDatabase(d,"_item_",['nameID','commodity','basePrice'],["WOOD",2,5])
#insertIntoDatabase(d,"_item_",['nameID','commodity','basePrice'],["Bread",1,0])

def create_tools():
	#tools are commodity type 3
	insertIntoDatabase(d,"_item_",['nameID','commodity','basePrice'],["Oven",3,10]) #base price is a hidden figure that will act as a reference point for value
	insertIntoDatabase(d,"_item_",['nameID','commodity','basePrice'],["Forge",3,30])
	insertIntoDatabase(d,"_item_",['nameID','commodity','basePrice'],["Hammer",3,0])

def create_recipes():
	WHEAT = 1
	IRON = 2
	WOOD = 3 
	OVEN = 4
	FORGE = 5
	STONE = 6
	BREAD = 7
	HAMMER = 8
        insertIntoDatabase(d,"_recipe_",['itemA','quantityA','itemB','quantityB','toolA','resultA','resultQuantityA'],[WHEAT,1,WOOD,1,OVEN,BREAD,10])
        insertIntoDatabase(d,"_recipe_",['itemA','quantityA','itemB','quantityB','itemC','quantityC','toolA','resultA','resultQuantityA'],[STONE,5,IRON,8,WOOD,3,5,5,1])
        insertIntoDatabase(d,"_recipe_",['itemA','quantityA','itemB','quantityB','resultA'],[WOOD,1,IRON,1,HAMMER,20])



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
		print(x)
		for v in x:
			print(v[0])

def calculateIndividualValue(unit_id,item_id):
	sumOfItem = getFromDatabaseSumOfFieldInTableByGroupWhereXisY(d , "quantity","items","itemType","id",id)
	
	#is this something I want purely for luxury?
	#is this a staple that I need?
	#is this something I believe is liquid enough to trade?
	#is this something that I use to make more valuable items?

def calculatePrices():
    pass
#getTransactionDetails()
getSumOfItemsForID(d,1,1)

#create_recipes()
#create_tools()
