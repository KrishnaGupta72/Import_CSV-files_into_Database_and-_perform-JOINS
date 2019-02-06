##Applying LEFT JOIN b/w both tables
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

##Applying SELF JOIN
cur.execute("SELECT a.ID, b.NAME, a.SALARY FROM Customer a, Customer b WHERE a.SALARY < b.SALARY;")
rows = cur.fetchall()
for row in rows:
    print(row)#It will print all row for all columns.
con.close()
#o/p:
# ('1', ' Chaitali ', '2000')
# ('1', ' Hardik   ', '2000')
# ('1', ' Komal    ', '2000')
# ('2', ' Ramesh   ', '1500')
# ('2', ' kaushik  ', '1500')
# ('2', ' Chaitali ', '1500')
# ('2', ' Hardik   ', '1500')
# ('2', ' Komal    ', '1500')
# ('3', ' Chaitali ', '2000')
# ('3', ' Hardik   ', '2000')
# ('3', ' Komal    ', '2000')
# ('4', ' Hardik   ', '6500')
# ('6', ' Chaitali ', '4500')
# ('6', ' Hardik   ', '4500')
# ('7', ' Ramesh   ', '10000')
# ('7', ' Khilan   ', '10000')
# ('7', ' kaushik  ', '10000')
# ('7', ' Chaitali ', '10000')
# ('7', ' Hardik   ', '10000')
# ('7', ' Komal    ', '10000')
