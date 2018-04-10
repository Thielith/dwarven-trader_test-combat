import MySQLdb
import sys

db = MySQLdb.connect(host="localhost",  # your host
				 user="root",  # username
				 passwd="p2950",  # password
				 db="test_dwarven")  # name of the database
cur = db.cursor()

def execute():
	cur.execute('create database test_dwarven;')
	
	cur.execute('create table units (id INT NOT NULL, strength INT, aglility INT, currentHP INT, maxHP INT, encounterID INT, level INT, PRIMARY KEY (id);')
	cur.execute('insert into units (unitID, strength, aglility, currentHP, maxHP, encounterID, level) values (0, 5, 10, 80, 80, 0, 1);')
	cur.execute('insert into units (unitID, strength, aglility, currentHP, maxHP, encounterID, level) values (1, 5, 10, 80, 80, 0, 1);')

	cur.execute('create table statuses (unitID INT, statusID INT);')
	
	cur.execute('create table combat_encounters (id INT, playerID INT, currentTurn INT, PRIMARY KEY (id));')
	cur.execute('insert into combat (id, playerID, currentTurn) values (0, 0, 0);')
	cur.execute('insert into combat (id, playerID, currentTurn) values (0, 1, 0);')

	cur.execute('create table status_e (id INT, statusName VARCHAR(16),PRIMARY KEY (id));')
	cur.execute('insert into status_e (id, statusName) values (0, "Fell");')
	cur.execute('insert into status_e (id, statusName) values (1, "Crouch");')

	cur.execute('create table _attack_ (id INT, level INT, advantage INT, advantageCost INT, attackID INT, typeID INT, effectGive INT, effectGet INT, effectClear INT, PRIMARY KEY (id));')
	cur.execute('insert into attacks (level, advantage, advantageCost, attackID, typeID, effectGive, effectGet, effectClear) values (1, 1, 1, 0, 0, 0, 1, -1);')

	cur.execute('create table combat_style_e (id INT, styleName INT, PRIMARY KEY (id));')
	cur.execute('insert into combat_style_e (id, styleName) values (0, "Melee");')
	cur.execute('insert into combat_style_e (id, styleName) values (1, "Ranged");')
	cur.execute('insert into combat_style_e (id, styleName) values (2, "Magic");')

	cur.execute('create table attack_e (attackID INT, attackName VARCHAR(16));')
	cur.execute('insert into attack_e (attackID, attackName) values (0, "Kick");')

	cur.execute('create table item_e (nameID INT, name VARCHAR(16));')

	cur.execute('create table commodity_e (classID INT, className VARCHAR(16));')
	
	cur.execute('create table quality_e (id INT, qualityName VARCHAR(16), PRIMARY KEY (id));')

	cur.execute('create table _item_ (id INT, nameID INT, qualityID INT, commodity INT, basePrice INT, PRIMARY KEY (id));')
	
	cur.execute('create table _recipe_ (id INT, itemA INT, quantityA INT, itemB INT, quantityB INT, itemC INT, quantityC INT, itemD INT, quantityD INT, toolA INT, toolB INT, time INT, resultA INT, resultB INT, resultC INT, resultD INT, PRIMARY KEY(id));')
	
	cur.execute('create table recipes (ownerID INT, timesUsed INT, recipeID INT);')

	cur.execute('create table items (ownerID INT, quantity INT, classID INT, qualityID INT);')
