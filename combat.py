import MySQLdb
import sys
from database import *
db = MySQLdb.connect(host="localhost",  # your host
						 user="root",  # username
						 passwd="p2950",  # password
						 db="test_dwarven")  # name of the database
cur = db.cursor()

if sys.argv[1] != None:
		if sys.argv[1] == "updateUnits":
			print("updating player" + sys.argv[8])
			updateUnitDB(cur,sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8],sys.argv[9],sys.argv[10])
			print("commit update")
			db.commit();
			print("close")
			db.close();
	
		elif sys.argv[1] == "deleteStatusByUnitID":
			print("deleting statuses with userID of " + sys.argv[2])
			deleteStatusByUnitID(cur, "statuses", sys.argv[2])
			print("commit update")
			db.commit();
			print("close")
			db.close();
	
		elif sys.argv[1] == "updateStatus":
			print("adding statuses")
			updateStatusDB(cur, sys.argv[2], sys.argv[3], sys.argv[4])
			print("commit update")
			db.commit();
			print("close")
			db.close();