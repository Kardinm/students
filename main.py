from db import connect_db, create_table


def add_student():
    name = input("Ім'я: ")
    age = int(input("Вік: "))
    major = input("Спеціальність: ")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, age, major) VALUES (?, ?, ?)",
        (name, age, major)
    )

    conn.commit()
    conn.close()


def add_course():
    name = input("Назва курсу: ")
    instructor = input("Викладач: ")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO courses (course_name, instructor) VALUES (?, ?)",
        (name, instructor)
    )

    conn.commit()
    conn.close()


def show_students():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    for student in students:
        print(student)

    conn.close()


def show_courses():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM courses")
    courses = cursor.fetchall()

    for cours in courses:
        print(cours)

    conn.close()


def add_student_to_course():
    student_id = int(input("ID студента: "))
    course_id = int(input("ID курсу: "))

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT OR IGNORE INTO student_courses VALUES (?, ?)",
        (student_id, course_id)
    )

    conn.commit()
    conn.close()


def students_by_course():
    course_id = int(input("ID курсу: "))

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""SELECT students.name FROM students JOIN student_courses ON students.id = student_courses.student_id
    WHERE student_courses.course_id = ?""", (course_id,))

    result = cursor.fetchall()
    for r in result:
        print(r[0])

    conn.close()


def menu():
    print("""
1 — Додати студента
2 — Додати курс
3 — Показати студентів
4 — Показати курси
5 — Записати студента на курс
6 — Студенти курсу
0 — Вихід
""")
    

def main():
    create_table()

    while True:
        menu()
        choice = input("Вибір: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            add_course()
        elif choice == "3":
            show_students()
        elif choice == "4":
            show_courses()
        elif choice == "5":
            add_student_to_course()
        elif choice == "6":
            students_by_course()
        elif choice == "0":
            break
        else:
            print("Невірний вибір")


if __name__ == "__main__":
    main()





