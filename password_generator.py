import random
import string

def generate_password():
    while True:
        try:
            length = int(input("\nEnter the length of password (or 0 to exit): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if length == 0:
            print("Exited from current session.")
            break

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        print("Generated Password is:", password)

while True:
    print("\nWelcome to Password Generator!")
    generate_password()

    again = input("\nDo you want to generate more passwords? (y/n): ").lower()
    if again != 'y':
        print("Goodbye! Thank you for using Password Generator.")
        break

