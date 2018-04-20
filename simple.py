from database import *
import random
d = MySQLdb.connect(host="localhost",  # your host
user="root",  # username
passwd="p2950",  # password
db="test_dwarven")  # name of the database
cur = d.cursor()

#insertIntoDatabase(d,"_item_",['nameID','commodity','basePrice'],["Wheat",1,1])
#insertIntoDatabase(d,"_item_",['nameID','commodity','basePrice'],["Iron",2,2])
#insertIntoDatabase(d,"_item_",['nameID','commodity','basePrice'],["Lumber",2,5])

#for i in range(1000):
#	insertIntoDatabase(d,"items",['ownerID','quantity','qualityID'],[random.randint(1,5),random.randint(1,10),random.randint(1,3)])

def getWorldEconData():
	data = getAllDataInTable(d,'items')
	sums = []
	for i in range(5):
		sums.append(0)
	for da in data:
		for i in range(5):
			if i+1 == da[0]:
				sums[i-1] += int(da[1])
	print(sums)
def calculatePrices():
    pass
getWorldEconData()

