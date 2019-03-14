import sqlite3

class CreatePerson():
    def __init__(self, first, last, age, pay):
        self.first = first
        self.last = last
        self.age = age
        self.pay = pay

conn = sqlite3.connect(':memory:')

c = conn.cursor()

def add_person(person):
    with conn:
        c.execute("INSERT INTO people VALUES (:first, :last, :age, :pay)", 
                {'first':person.first, 'last':person.last, 'age':person.age, 'pay':person.pay})

def find_person(lastname):
    c.execute("SELECT * FROM people WHERE last = :last", 
                {'last': lastname}) 
    return c.fetchall()

def change_attr(person, column, value):
    try: getattr(person, column)
    except: print('Thats not a valid attribute.')
    with conn:
        c.execute(f"UPDATE people SET {column} = {value} WHERE first=? AND last=?", (person.first, person.last)) 
        # {'column':'age', 'value':value, 'first':person.first, 'last':person.last})


c.execute("""CREATE TABLE people (
            first text,
            last text,
            age integer,
            pay integer
            )""")

me = CreatePerson('Will', 'Dove', 30, 90000)
add_person(me)

print(find_person('Dove'))
change_attr(me, 'pay', 40000)
print(find_person('Dove'))

conn.commit()
conn.close()