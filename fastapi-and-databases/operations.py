from sqlalchemy import insert, select, update, delete
from db import engine
from models import students

conn = engine.connect()

def insert_students():
    query = insert(students).values([
        {"name": "Rahul", "age": 22, "city": "Delhi"},
        {"name": "Anita", "age": 19, "city": "Mumbai"},
        {"name": "Vikas", "age": 21, "city": "Pune"}
    ])
    conn.execute(query)
    conn.commit()


def fetch_students():
    result = conn.execute(select(students))
    for row in result:
        print(row)


def update_city():
    query = (
        update(students)
        .where(students.c.name == "Rahul")
        .values(city="Bangalore")
    )
    conn.execute(query)
    conn.commit()


def delete_students():
    query = delete(students).where(students.c.age < 20)
    conn.execute(query)
    conn.commit()
