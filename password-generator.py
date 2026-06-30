import random
import string

#VALIDATION LENGTH
while True:
    password_length = input("Enter the password length: ")

    if not password_length.isdigit():
        print("Please enter digits.")
        continue

    password_length = int(password_length)

    if password_length < 8:
        print("Password must be at least 8 characters.")
        continue

    break  # όλα σωστά → βγαίνει από loop

length = password_length
print("Valid length:", length)


# χαρακτήρες
level1_ch = string.ascii_letters
level2_ch = string.digits
level3_ch = string.ascii_letters + string.digits
level4_ch = string.ascii_letters + string.punctuation
level5_ch = string.ascii_letters + string.digits + string.punctuation


#VALIDATION LEVEL
while True:
    password_level = input("Enter the password level (1-5): ")

    if password_level not in ["1", "2", "3", "4", "5"]:
        print("Please enter a number from 1 to 5.")
        continue

    break


# δημιουργία password
chars = None

if password_level == "1":
    chars = level1_ch
elif password_level == "2":
    chars = level2_ch
elif password_level == "3":
    chars = level3_ch
elif password_level == "4":
    chars = level4_ch
elif password_level == "5":
    chars = level5_ch


password = "".join(random.choice(chars) for i in range(length))

print("Your password is:", password)
print("MAKE SURE YOU SAVED THE CODE!")