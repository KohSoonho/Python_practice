# 8-1
test1 = "This is a test of the emergency text system."

with open("test.txt", "wt") as file :
    file.write(test1)

# 8-2
with open("test.txt", "rt") as file :
    test2 = file.read()

print(test2 == test1)

# 8-3
books = '''author,book
J R R Tolkien,The Hobbit
Lynee Truss,"Eats, Shoots & Leaves"
'''

with open("books.csv", "wt") as file :
    file.write(books)

# 8-4
import csv
with open("books.csv", "rt") as file :
    books = csv.DictReader(file)

    for book in books :
        print(book)

# by pandas
import pandas as pd
print(pd.read_csv("books.csv"))

# 8-5
new_books = """title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Mieville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992
"""

with open("books2.csv", "wt") as file :
    file.write(new_books)

# 8-6
import sqlite3
conn = sqlite3.connect("books.db")
curs = conn.cursor()

curs.execute("""CREATE TABLE book (title VARCHAR(20), author VARCHAR(20), year INT)""")
conn.commit()

# 8-7
ins = "INSERT INTO book VALUES(?, ?, ?)"

with open("books2.csv", "rt") as file :
    books2 = csv.DictReader(file)
    for book in books2 :
        curs.execute(ins, (book["title"], book["author"], book["year"]))

conn.commit()

# 8-8
query = "SELECT title FROM book ORDER BY title"
for row in conn.execute(query) :
    print(row[0])

# 8-9
for row in conn.execute("SELECT * FROM book ORDER BY year") :
    print(row[0])

# 8-10
import sqlalchemy
con = sqlalchemy.create_engine("sqlite:///books.db")
rows = con.execute("SELECT * FROM book ORDER BY year")
for row in rows :
    print(row)
