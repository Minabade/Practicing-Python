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
# first_name = "Yetunde"
# last_name = "Baderinwa"
# middle_name = "Aminat"
# password = "12345"
 
# # Function to validate user input
# def validate_input(prompt, correct_value):
#    while True:
#        user_input = input(prompt)
#        if user_input == correct_value:
#            return True  # Return True if input is correct
#        else:
#            print("This is wrong!\n" * 5)
 
# # Method for user authentication
# def user_authentication():
#    print("Please enter your details for authentication.")

# # Call the user authentication method
# user_authentication()
   
   
# # Validate each input
# validate_input("Enter your first name: ", first_name)

# validate_input("Enter your last name: ", last_name)

# validate_input("Confirm your middle name: ", middle_name)

# validate_input("Enter your password: ", password)

# print("All details are correct! You are logged in.")

# Hi guys,
# I want to add a bit of twist to the project.
# Make the user enter username and password for a maximum of three times, afterwhich they will get the message that they have been blocked, and the program ends (if they enter the wrong password the 3rd time). During this period, if they enter the correct password, they should get a success message and the program ends. If not, they get a message saying incorrect credentials as long as they haven't entered the wrong password more than two times.
# Drop your code in this thread only so as to ensure easy tracking.

# password = "12345"
# username = "Aminat"
# chance = 3
# while chance > 0:
#     user_name = input("Enter your username:")
#     pass_word = input("Enter your password:")

#     if user_name == username and pass_word == password:
#         print("logged in successfully")
#         break
#     else:
#        chance -= 1
#        if chance > 0:
#           print(f"wrong credentials, you have {chance} chance left")
#        else:
#            print("Your accout has been blocked, contact admin")



