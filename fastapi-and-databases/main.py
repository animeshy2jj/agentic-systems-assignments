from db import engine, metadata
from models import students
import operations

metadata.create_all(engine)

operations.insert_students()

print("All Students:")
operations.fetch_students()

operations.update_city()
print("\nAfter Update:")
operations.fetch_students()

operations.delete_students()
print("\nAfter Delete:")
operations.fetch_students()
