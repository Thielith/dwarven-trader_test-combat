from database import *
db = MySQLdb.connect(host="localhost",  # your host
user="root",  # username
passwd="p2950",  # password
db="test_dwarven")  # name of the database
cur = db.cursor()

insertIntoDatabase(cur,"units",['strength','agility','currentHP','maxHP','encounterID','level','name'],[7,6,5,6,1,1,'Syr'])
