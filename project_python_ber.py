
from tkinter.tix import COLUMN
from pony.orm import Database, PrimaryKey , Required ,db_session

#This allows the code to communicate with the database.
db = Database(
 provider ="mysql",
 host="127.0.0.1",
 user="root",
 password="Peak.oil1",
 database="college",
)
#a function for listing the sections of the table

#@db_session

#def list_table_columns_and_data(table_name):
   # query_colums = f"DESCRIBE {table_name };"   
   # result_colums = db.excute(query)
   # COLUMN - [row[0] for row in  result_colums.fetchall()]
   ## return columns
   
   #Print column names 
#print ("Colums:")
#for column in columns:
    #print(column)
    
#    print( "\ndata:")
    #for row in data :
     #   print (row)
#table_name ='' 

#list_table_columns_and_data(table_name)
