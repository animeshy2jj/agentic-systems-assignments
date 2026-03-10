from pydantic import BaseModel, EmailStr, field_validator


class UserRegister(BaseModel):
    username: str
    email: EmailStr
    age: int

    @field_validator('username')
    @classmethod
    def username_min_length(cls, v):
        if len(v) < 5:
            raise ValueError('Username must be at least 5 characters long')
        return v

    @field_validator('age')
    @classmethod
    def age_min_value(cls, v):
        if v < 18:
            raise ValueError('Age must be at least 18')
        return v


# Example usage and validation
if __name__ == '__main__':
    # Valid user
    try:
        user = UserRegister(username='john_doe', email='john@example.com', age=25)
        print(f"Valid user: {user}")
    except Exception as e:
        print(f"Error: {e}")

    # Invalid username (too short)
    try:
        user = UserRegister(username='john', email='john@example.com', age=25)
        print(f"Valid user: {user}")
    except Exception as e:
        print(f"Error: {e}")

    # Invalid email
    try:
        user = UserRegister(username='john_doe', email='invalid-email', age=25)
        print(f"Valid user: {user}")
    except Exception as e:
        print(f"Error: {e}")

    # Invalid age (less than 18)
    try:
        user = UserRegister(username='john_doe', email='john@example.com', age=16)
        print(f"Valid user: {user}")
    except Exception as e:
        print(f"Error: {e}")
