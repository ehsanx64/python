import os

user = os.getenv("USER")

if user is not None:
    print(f"Hello {user}!")
else:
    print(f"Hello stranger!")
