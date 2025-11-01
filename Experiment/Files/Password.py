# Importing the 'digit' function from the unicodedata module (though it’s not used in this code)
from unicodedata import digit

# Asking the user to input a new password
password = input("Enter new password: ")

# Creating an empty list to store True/False results for each condition
result = []

# Checking if the password length is at least 10 characters
if len(password) >= 10:
    result.append(True)   # Condition satisfied
else:
    result.append(False)  # Condition not satisfied

# Initializing a variable to check if the password contains a digit
digit = False

# Loop through each character in the password
for i in password:
    if i.isdigit():       # Check if the character is a digit (0–9)
        digit = True       # If found, set 'digit' to True

# Append the result (True/False) of the digit check
result.append(digit)

# Initialize a variable to check if the password contains an uppercase letter
uppercase = False

# Loop through each character again
for i in password:
    if i.isupper():        # Check if the character is an uppercase letter (A–Z)
        uppercase = True    # If found, set 'uppercase' to True

# Append the result (True/False) of the uppercase check
result.append(uppercase)

# The 'all()' function checks if all values in the result list are True
# If all conditions are met (length, digit, uppercase), it returns True
print(all(result))

# If all conditions are True, password is strong
if all(result):
    print('Strong Password:')
else:
    print("Weak Password")
