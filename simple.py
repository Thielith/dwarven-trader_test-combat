from database import *
d = MySQLdb.connect(host="localhost",  # your host
user="root",  # username
passwd="p2950",  # password
db="test_dwarven")  # name of the database
cur = d.cursor()

insertIntoDatabase(d,"units",['strength','agility','currentHP','maxHP','encounterID','level','name'],[7,6,5,6,1,1,'Syr'])
