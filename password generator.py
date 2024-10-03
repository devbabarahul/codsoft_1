import random
import string

def generate_password(length):
    # Define the character sets to choose from
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase + uppercase + digits + special_characters

    # Generate a password using random.choices
    password = ''.join(random.choices(all_characters, k=length))
    return password

def main():
    print("Welcome to the Password Generator!")

    # Input: Get the desired password length from the user
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 6 characters): "))
            if length < 6:
                print("Password length must be at least 6 characters.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    # Generate the password
    generated_password = generate_password(length)

    # Display the generated password
    print(f"Generated Password: {generated_password}")

# Run the password generator
if __name__ == "__main__":
    main()
