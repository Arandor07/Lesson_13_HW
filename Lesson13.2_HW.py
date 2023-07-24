import sqlite3


def get_student_by_name(name):
    info = sql.execute(f'SELECT * FROM students WHERE name="{name}";').fetchall()
    print(f'Info about {name}:\nID - {info[0][0]}\nAge - {info[0][2]}\nGrade - {info[0][3]}')


def update_student_grade(name, grade):
    sql.execute(f'UPDATE students SET grade="{grade}" WHERE name="{name}";')
    connection.commit()
    print('Grade is updated!')


def delete_student(name):
    sql.execute(f'DELETE FROM students WHERE name="{name}"')
    connection.commit()
    print('Student is deleted')


connection = sqlite3.connect('my_database.db')
sql = connection.cursor()
sql.execute('CREATE TABLE IF NOT EXISTS students(id INTEGER, name TEXT, age INTEGER, grade TEXT);')

sql.execute(f'INSERT INTO students(id, name, age, grade) VALUES(2934, "Ruslan", 12, "5");')
sql.execute(f'INSERT INTO students(id, name, age, grade) VALUES(4753, "Kira", 15, "3");')
sql.execute(f'INSERT INTO students(id, name, age, grade) VALUES(9465, "Michael", 9, "4");')

while True:
    print('\nActions: Get info by name(1), Update student grade(2), Delete student(3)')
    action = input('Enter your action: ')
    if action.lower() == 'get info by name' or action == '1':
        name = input('Enter name whose info you want to see: ')
        get_student_by_name(name)
    elif action.lower() == 'update student grade' or action == '2':
        name = input('Enter name whose grade you want upgrade: ')
        new_grade = input('Enter new grade for student: ')
        update_student_grade(name, new_grade)
    elif action.lower() == 'delete student' or action == '3':
        name = input('Enter name of student whose you want delete: ')
        delete_student(name)
    else:
        print('Error')

