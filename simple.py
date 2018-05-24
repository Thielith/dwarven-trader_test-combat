from database import *
import random
d = MySQLdb.connect(host="localhost",  # your host
user="root",  # username
passwd="p2950",  # password
db="test_dwarven")  # name of the database
cur = d.cursor()

NEVER = 0
FINERY = 1
SHOP = 2
MARTIAL = 3
FOODIE = 4
KNOWLEDGE = 5

FOOD = 1
SMITH_COMPONENT = 2
TOOLS = 3
CURRENCY  = 4
WEAPON = 5
ARMOR = 6
ARCANE_ARTIFACT = 7
HISTORICAL_ARTIFACT = 8
HISTORICAL_WRITING = 9

def create_components():

	#base materials
	insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Wheat",1,1,0])
	insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Iron",2,2,0])
	insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Wood",2,5,0])
	insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Bread",1,0,0])
        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Stone",2,0,0])
        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Wool",2,0,0])
        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Cotton",2,0,0])
        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Leather",2,0,0])
        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Gold",4,100,0])
        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Silver",4,10,0])
        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Copper",4,1,0])
        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Diamond",4,1000,0])
        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Ruby",4,50,0])



def create_finery():
        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Fancy Clothes",4,2,1])
        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Diamond Ring",4,25,1])
        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Ruby Necklace",4,10,1])


#insertIntoDatabase(d,"items",['ownerID','quantity','qualityID','itemID'],[random.randint(1,100),random.randint(5,200),1,random.randint(1,8)])
def create_weapons():

        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Short Sword",WEAPON,1,MARTIAL])
        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Long Sword",WEAPON,4,MARTIAL])
        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Great Sword",WEAPON,10,MARTIAL])

	insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Hand Axe",WEAPON,1,MARTIAL])
        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Battle Axe",WEAPON,4,MARTIAL])
        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Giant Axe",WEAPON,10,MARTIAL])

	insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Mace",WEAPON,1,MARTIAL])
        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["War Hammer",WEAPON,3,MARTIAL])
        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Maul",WEAPON,2,MARTIAL])

        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Repeating Crossbow",WEAPON,20,MARTIAL])
        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Hand Crossbow",WEAPON,12,MARTIAL])
        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Crossbow",WEAPON,7,MARTIAL])
        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Heavy Crossbow",WEAPON,8,MARTIAL])

        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Spear",WEAPON,1,MARTIAL])
        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Halberd",WEAPON,4,MARTIAL])
        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Javelin",WEAPON,1,MARTIAL])

        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Longbow",WEAPON,1,MARTIAL])
        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Shortbow",WEAPON,1,MARTIAL])

def create_armors():
        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Shield",ARMOR,1,MARTIAL])
        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Tower Shield",ARMOR,2,MARTIAL])
        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Kite Shield",ARMOR,1,MARTIAL])

        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Leather ARMOR",ARMOR,1,MARTIAL])
        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Chainmail",ARMOR,5,MARTIAL])
        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Scale Mail",ARMOR,15,MARTIAL])
        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Plate Mail",ARMOR,100,MARTIAL])


def create_tools():
	#tools are commodity type 3
	insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Forge",3,30,2])
	insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Oven",3,10,2]) #base price is a hidden figure that will act as a reference point for value
	insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["Hammer",3,0,2])


def create_artifacts():
	ARCANE_ARTIFACT = 7
	HISTORICAL_ARTIFACT = 8
	HISTORICAL_WRITING = 9

        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["tome",HISTORICAL_WRITING,30,KNOWLEDGE])
        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["scrap of writ",HISTORICAL_WRITING,30,KNOWLEDGE])
        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["old statue",HISTORICAL_ARTIFACT,30,KNOWLEDGE])
        insertIntoDatabase(d,"_item_",['nameID','commodity','baseprice','luxury_E'],["archaic pottery",ARCANE_ARTIFACT,30,KNOWLEDGE])




def create_recipes():
	#update with new ids!!!!
	WHEAT = 594
	IRON = 595
	WOOD = 596
	BREAD = 597
	STONE = 598
	OVEN = 636
	FORGE = 635
	HAMMER = 637
        insertIntoDatabase(d,"_recipe_",['itemA','quantityA','itemB','quantityB','toolA','resultA','resultQuantityA'],[WHEAT,1,WOOD,1,OVEN,BREAD,10])
        insertIntoDatabase(d,"_recipe_",['itemA','quantityA','itemB','quantityB','itemC','quantityC','toolA','resultA','resultQuantityA'],[STONE,5,IRON,8,WOOD,3,5,5,1])
        insertIntoDatabase(d,"_recipe_",['itemA','quantityA','itemB','quantityB','resultA'],[WOOD,1,IRON,1,HAMMER,20])


def populateRecipes():
	insertIntoDatabase(d,"recipes",["ownerID","timesUsed","recipeID"],[2,1,1])

def getWorldEconDataP():
	pass
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


def calculateIndividualValue(database,ownerID,itemID):
	FOOD = 1

	listA = ["ownerID","itemID"]
	listB = [ownerID, itemID]	
	currentStock = getFromDatabaseSumOfFieldInTableWhereListAisListB(database,"quantity","items",listA,listB)
	#is this something I want purely for luxury?

	#is this a staple that I need?
	item = getDataFromTableByID(database,"_item_","id",itemID)
	itemType = item[0][1]
		#get all current food stores
	sql = "select sum(items.quantity) from items inner join _item_ on items.itemID = _item_.id where items.ownerID  = " + str(ownerID) + "  and _item_.commodity  = " + str(FOOD) +";"
	foodStores = dbGet(database,sql)[0][0]
	print(foodStores)
	desire = 0
	if itemType == FOOD:
		if foodStores < 50:
			#will need food in the next week
			print("low food need")
			desire += 1	
		if foodStores < 10:
			print("mid food need")
			desire += 5
			#will need food by tomorrow
		if foodStores == 0:
			print("need food now")
			desire += 10
			#need food now
	else:
		if foodStores == 0:
			print("will purchase nothing but food")
			desire = 0
			
	#is this something I believe is liquid enough to trade?
	if item[0][1] == 4 and item[0][3] == 1: 
		#is a base valuable item i.e. gold silver etc
		desire = 1

	#is this something that I use to make more valuable items?
	sql = "select * from recipes inner join _recipe_ on recipes.recipeID where _recipe_.itemA = " + str(itemID) +" or _recipe_.itemB = " + str(itemID) + "   and recipes.ownerID = " + str(ownerID)+ ";"
	recipes = dbGet(database,sql)
	desire += recipes.__len__()*2
	print("final desire for product = "+ str(desire))

def calculatePrices():
    pass
def createTestGuy():
	names = ["Abe","Bob","Carl","Doug","Earl","Fred","Gary","Hal","IGOR","Jayce","Kayle","Larry","Mo","Ned","Onsrud","Peta","Quirk","Ryaun","Sel","Tau","Upsillon","Vindic","Wend","Xan","Yed","Zeal"]
	name = random.choice(names) + " " +  random.choice(names)+"son"
	finery = random.randint(1,10)
	shop = random.randint(1,10)
	martial = random.randint(1,10)
	foodie = random.randint(1,10)
	knowledge = random.randint(1,10)
	strength = random.randint(1,10)
	agility = random.randint(1,10)
	currentHP = strength * 10 + random.randint(1,4)*10
	maxHP = currentHP
	encounterID = 0
	level = 1
	advantage = 0

        insertIntoDatabase(d,"units",["name","finery","shop","martial","foodie","knowledge","strength","agility","currentHP","maxHP","encounterID","level","advantage"],[name,finery,shop,martial,foodie,knowledge,strength,agility,currentHP,maxHP,encounterID,level,advantage])

#getTransactionDetails()
#getSumOfItemsForID(d,1,1)

#create_recipes()
#create_tools()

print("calc value start")

for i in range(594,630):
	calculateIndividualValue(db,2,i)
print("calc value end")
for i in range(0):
	createTestGuy()

def createStuff():
	create_components()
	create_finery()
	create_weapons()
	create_armors()
	create_tools()
	create_artifacts()

#populateRecipes()
#createStuff()

