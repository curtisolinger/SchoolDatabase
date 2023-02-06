import sqlite3
from schoolclass import SchoolClass

conn = sqlite3.connect("school.db")
c = conn.cursor()

# c.execute("""CREATE TABLE classes (
#             ID INT PRIMARY KEY NOT NULL,
#             class TEXT NOT NULL)
#             """)


# c.execute("""INSERT INTO classes VALUES (
#             3, 
#             'topology', 
#             'Hansell 001', 
#             'Dr. Clader'
#             )""")

world_war_II = SchoolClass('world_war_II', 'Science 201', 'Dr. Smith')
calculus_2 = SchoolClass('calculus_2', 'Helms 99', 'Dr. Schuster')

# c.execute("INSERT INTO classes VALUES (:id, :class, :location, :teacher)",
#     {'id': 4, 
#     'class': world_war_II.class_name, 
#     'location': world_war_II.location, 
#     'teacher': world_war_II.teacher})

# c.execute("INSERT INTO classes VALUES (:id, :class, :location, :teacher)",
#     {'id': 5, 
#     'class': calculus_2.class_name, 
#     'location': calculus_2.location, 
#     'teacher': calculus_2.teacher})


class_name = input("Class: ")
location = input("Location: ")
teacher = input("Teacher: ")

new_class = SchoolClass(class_name, location, teacher)

c.execute("INSERT INTO classes VALUES (:id, :class, :location, :teacher)",
    {'id': 6, 
    'class': new_class.class_name, 
    'location': new_class.location, 
    'teacher': new_class.teacher})

conn.commit()

c.execute("SELECT * FROM classes")

print(c.fetchall())

conn.commit()

conn.close()
# res.fetchone()

# algebra = SchoolClass("algebra", "Helms 201", "Dr. Smith")

# print(algebra.class_name)
