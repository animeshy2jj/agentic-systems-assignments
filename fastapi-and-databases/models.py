from sqlalchemy import Table, Column, Integer, String, CheckConstraint
from db import metadata

students = Table(
    "students",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), nullable=False),
    Column("age", Integer),
    Column("city", String(50), nullable=True),
    CheckConstraint("age >= 18", name="age_check")
)
