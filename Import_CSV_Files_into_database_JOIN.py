##Applying JOIN b/w both tables
import csv, sqlite3
con = sqlite3.connect(":memory:")#It creates database on RAM, everytime it flush the database and create.
# con = sqlite3.connect("Shop.db")
cur = con.cursor()

##Creating Customer table from Customer.csv file.
cur.execute("CREATE TABLE Customer (ID, NAME, AGE, ADDRESS, SALARY);") # use your column names here
with open('Customer.csv','r') as fin: # `with` statement available in 2.5+
# csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['ID'], i['NAME'],i['AGE'], i['ADDRESS'],i['SALARY']) for i in dr]#Column names are exactly same as in csv files.
cur.executemany("INSERT INTO Customer (ID, NAME, AGE, ADDRESS, SALARY) VALUES (?, ?, ?, ?, ?);", to_db)
con.commit()

#Creating Orderr table from Order.csv file.
cur.execute("CREATE TABLE Orderr (OID, DATE, CUSTOMER_ID, AMOUNT);") # use your column names here
with open('Order.csv','r') as f: # `with` statement available in 2.5+
# csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(f) # comma is default delimiter
    to_db = [(i['OID'], i['DATE'],i['CUSTOMER_ID'], i['AMOUNT']) for i in dr]
cur.executemany("INSERT INTO Orderr (OID, DATE, CUSTOMER_ID, AMOUNT) VALUES (?, ?, ?, ?);", to_db)
con.commit()

##Applying JOIN b/w both tables
cur.execute("SELECT ID, NAME, AGE, AMOUNT FROM Customer, Orderr WHERE  Customer.ID = Orderr.CUSTOMER_ID;")
rows = cur.fetchall()
for row in rows:
    print(row)#It will print all row for all columns.
con.close()
#o/p:
# ('2', ' Khilan   ', '25', '1560')
# ('3', ' kaushik  ', '23', '1500')
# ('3', ' kaushik  ', '23', '3000')
# ('4', ' Chaitali ', '25', '2060')




