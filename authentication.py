# A simple username and password authentication.
# If the username and password specified are correct, then print
# a success message, else print "You're are wrong!" five times.

#Creating a simple user authentication without functions
password = "12345"
username = "Aminat"
user_name = input("Enter your username")
pass_word = input("Enter your password")
if user_name == username and pass_word == password:
    print("logged in successfully")
else:
    print("You are wrong\n" * 5)




#Creating a user authentication using Functions
first_name = "Yetunde"
last_name = "Baderinwa"
middle_name = "Aminat"
password = "12345"
 
# Function to validate user input
def validate_input(prompt, correct_value):
   while True:
       user_input = input(prompt)
       if user_input == correct_value:
           return True  # Return True if input is correct
       else:
           print("This is incorrect. Please try again.")
 
# Method for user authentication
def user_authentication():
   print("Please enter your details for authentication.")

# Call the user authentication method
user_authentication()
   
   
# Validate each input
validate_input("Enter your first name: ", first_name)

validate_input("Enter your last name: ", last_name)

validate_input("Confirm your middle name: ", middle_name)

validate_input("Enter your password: ", password)

print("All details are correct! You are logged in.")
