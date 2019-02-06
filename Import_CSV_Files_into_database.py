#Create databse-tables from csv files.
import csv, sqlite3
# con = sqlite3.connect(":memory:")#It creates database on RAM, everytime it flush the database and create.
con = sqlite3.connect("Shop.db")
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

cur.execute("SELECT * FROM Customer;")
rows = cur.fetchall()
for row in rows:
    print(row)#It will print all row for all columns.

#o/p:
# ('1', ' Ramesh   ', '32', ' Ahmedabad ', '2000')
# ('2', ' Khilan   ', '25', ' Delhi     ', '1500')
# ('3', ' kaushik  ', '23', ' Kota      ', '2000')
# ('4', ' Chaitali ', '25', ' Mumbai    ', '6500')
# ('5', ' Hardik   ', '27', ' Bhopal    ', '8500')
# ('6', ' Komal    ', '22', ' MP        ', '4500')
# ('7', ' Muffy    ', '24', ' Indore    ', '10000')

