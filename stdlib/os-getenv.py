import os

# The basic usage
def demo_basic():
    user = os.getenv("USER")
    if user is not None:
        print(f"Hello {user}!")
    else:
        print(f"Hello stranger!")

# Set a default value for environment variables
def demo_default_value():
    # We can pass an argument to getenv to set a default value
    user = os.getenv("USER", "stranger")
    print(f"Hello {user}!")

demo_basic()
demo_default_value()
