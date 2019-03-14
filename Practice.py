import sqlite3

class CreatePerson():
    def __init__(self, first, last, age, pay):
        self.first = first
        self.last = last
        self.age = age
        self.pay = pay

conn = sqlite3.connect(':memory:')

c = conn.cursor()

#  START DB table creation
c.execute("""CREATE TABLE people (
            first text,
            last text,
            age integer,
            pay integer
            )""")
#  END DB table creation

#  Funtions for working with DB
def add_person(*args):
    with conn:
        persons = [*args]
        for person in persons:
                c.execute("INSERT INTO people VALUES (?, ?, ?, ?)", 
                        (person.first, person.last, person.age, person.pay))

def find_person(lastname):
    c.execute("SELECT * FROM people WHERE last = :last", (lastname, )) 
    return c.fetchall()

def change_attr(person, column, value):
    try: getattr(person, column)
    except: print('Thats not a valid attribute.')
    with conn:
        c.execute(f"UPDATE people SET {column} = {value} WHERE first=? AND last=?", 
        (person.first, person.last)) 
        # F-String substitution required. Unable to set variables for Table/Column names

#  Test additions and modifications
per1 = CreatePerson('Will', 'Dove', 30, 90000)
per2 = CreatePerson('Ryann', 'Rambo', 32, 100000)
per3 = CreatePerson('Tom', 'Dove', 61, 89999)
per4 = CreatePerson('Ronie', 'Dove', 66, 20000)

add_person(per1, per2, per3, per4)

print(find_person('Dove'))
change_attr(per1, 'pay', 40000)
print(find_person('Dove'))

conn.commit()
conn.close()