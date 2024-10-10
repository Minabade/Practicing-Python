# Given two integer numbers, write a Python code to return their product only 
# if the product is equal to or lower than 1000. Otherwise, return their sum.

# num1 = 20
# num2 = 30
# if num1*num2 <= 1000:
#     print(num1*num2)
# else:
#     print(num1+num2)

# def calc_number(n1,n2):
#     if n1*n2 <= 1000:
#         return n1*n2
#     else:
#         return n1+n2


# result = calc_number(40,30)
# print(result)
# calc_number(20,30)


# Write a Python code to iterate the first 10 numbers, 
# and in each iteration, print the sum of the current and previous number.
# Printing current and previous number sum in a range(10)
# Current Number 0 Previous Number  0  Sum:  0
# Current Number 1 Previous Number  0  Sum:  1
# Current Number 2 Previous Number  1  Sum:  3
# Current Number 3 Previous Number  2  Sum:  5
# Current Number 4 Previous Number  3  Sum:  7
# Current Number 5 Previous Number  4  Sum:  9
# Current Number 6 Previous Number  5  Sum:  11
# Current Number 7 Previous Number  6  Sum:  13
# Current Number 8 Previous Number  7  Sum:  15
# Current Number 9 Previous Number  8  Sum:  17

# for i in range(10):
#     sum=i+x
#     print(f"Current number {i} Previous Number {x} Sum {sum} ")
# x= 0
# for i in range(10):
#     if i <=0 and x == 0:
#         print(f"Sum of {i} and {x} is {0}")
#     else:
#         print(f"Sum of {i} and {x} is {x + i}")
#         x+=1
# print("Printing current and previous number and their sum in a range(10)")
# previous_num = 0

# for i in range (1,10):
#     j = i - 1
#     sum = i + j
#     print(f"current number is {i} Previous number is {j} and sum is {sum}")

# # loop from 1 to 10
# for i in range(1, 11):
#     x_sum = previous_num + i
#     print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
#     # modify previous number
#     # set it to the current number
#     previous_num = i 

# for i in range(10):
#     if i == 0:


#         c = i
#         x = 0
#     else:
#         x = i -1
#         c = i


#     print(f"{i}{x} {x + i}")

#     i = 10
#     x = 9      


# print(f"{i}{x} {x + i}") 
# x=0
# for i in range(10):
#     if i <=0 and x == 0:
#         print(f"Sum of {i} and {x} is {0}")
#     else:
#         print(f"Sum of {i} and {x} is {x + i}")
#         x+=1

# print("Printing current and previous number and their sum in a range(10)")
# previous_num = 0   
    
# x= 0
# for i in range(1, 11):
#     print(f"Sum of {x} and {i} is {x + i}")
#     previous_num = i 
#     x+=1 

# Write a Python code to accept a string from the user and display characters present at an even index number.

# For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.
# string=input("please type anything: ")
# length= len(string)
# for i in range (0, length, 2):
#     print(string[i])

# Write a Python code to remove characters from a string from 0 to n and return a new string.
# For Example:
# remove_chars("PYnative", 4) so output must be tive. Here, you need to remove the first four characters from a string.
# remove_chars("PYnative", 2) so output must be native. Here, you need to remove the first two characters from a string.
# Note: n must be less than the length of the string.

# string="Pynative"
# new_string=string[2:8]
# print(new_string)

# Write a code to return True if the list’s first and last numbers are the same. 
# If the numbers are different, return False.

# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]


# def check_list(a):
#     if a[0]==a[-1]:
#         print ("True")
#     else:
#         print("False")
    
# check_list(numbers_x)
# list1=[10, 20, 33, 46, 55]
# # Write a Python code to display numbers from a list divisible by 5

# for num in list1:
#     if num % 5 == 0:
#         print (num)


# str_x = "Emma is good developer. Emma is a writer"

# # Write a Python code to find how often the substring “Emma” appears in the given string.
# print(str_x.count("Emma"))

# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

# for i in range (1,6):
#     for j in range(i):
#         print (i, end =" ")        
#     print("\n")  


# Write a Python code to check if the given number is palindrome. 
# A palindrome number is a number that is the same after reverse. 
# For example, 545 is the palindrome number.

# num=541
# if str(num) == str(num)[::-1]:
#     print("This is a palindrome")
# else:
#     print("No be palindrome")

def palindrome(number):
    print("original number", number)
    original_num = number
    
    # reverse the given number
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10
        if original_num == reverse_num:
              print("Given number palindrome")
        else:
              print("Given number is not palindrome")
        
          

palindrome(121)
palindrome(125)


# Exercise 10: Merge two lists using the following condition
# Given two lists of numbers, 
# write a Python code to create a new list such that the latest list should contain 
# odd numbers from the first list and even numbers from the second list.

# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# list3=[]

# for i in list1:
#     if i % 2 == 1:
#         list3.append(i)
# for i in list2:
#     if i % 2 == 0:
#         list3.append(i)


# print (list3)


# Exercise 11: Get each digit from a number in the reverse order.
# For example, If the given integer number is 7536, the output shall be 
# “6 3 5 7“, with a space separating the digits.

# num=7536
# reverse=0
# while num > 0:
#     remainder=num%10
#     reverse=(reverse*10)+remainder
#     num=num//10
#     print (remainder, end=" ")
    

# Calculate income tax for the given income by adhering to the rules below
# Taxable Income	Rate (in %)
# First $10,000	0
# Next $10,000	10
# The remaining	20
# Expected Output:
# For example, suppose the income is 45000, and the income tax payable is
# 10000*0% + 10000*10%  + 25000*20% = $6000.

# def calc_tax(amount):
#     if amount <= 10000:
#         tax=amount*0
#         print(int(tax))

#     elif amount > 10000 and amount <= 20000:
#         amt_to_tax=amount-10000
#         tax=amt_to_tax*0.1
#         print (int(tax))

#     elif amount>20000:
#         amount-10000
#         level1_tax=10000*0.1
#         level2_tax=(amount-20000)*0.2
#         print(int(level1_tax+level2_tax))
        
# calc_tax(45000)


# income = 45000
# tax_payable = 0
# print("Given income", income)

# if income <= 10000:
#     tax_payable = 0
# elif income <= 20000:
#     # no tax on first 10,000
#     x = income - 10000
#     # 10% tax
#     tax_payable = x * 10 / 100
# else:
#     # first 10,000
#     tax_payable = 0

#     # next 10,000 10% tax
#     tax_payable = 10000 * 10 / 100

#     # remaining 20%tax
#     tax_payable += (income - 20000) * 20 / 100

# print("Total tax to pay is", tax_payable)


# Exercise 13: Print multiplication table from 1 to 10

# for x in range(1, 11):
#     for y in range(1, 11):
#         print(x*y, end=" ")
#     print("\t\t")

# Exercise 14: Print a downward half-pyramid pattern of stars

# rows=5
# for x in range(rows+1, 0, -1):
#     for y in range(0, x-1):
#         print("*", end= " ")
#     print("\n")

# Exercise 15: Get an int value of base raises to the power of exponent
# Write a function called exponent(base, exp) 
# that returns an int value of base raises to the power of exp.

# base = 5
# exponent = 4

# 5 raises to the power of 4 is: 625 
# i.e. (5 *5 * 5 *5 = 625)


# def expo(a,b):
#     ans = 1
#     for x in range (b):
#         ans*=a
#     return ans

# result=expo(5,5)
# print(result)

# def exponent(base, exp):
#     num = exp
#     result = 1
#     while num > 0:
#         result = result * base
#         num = num - 1
#     print(base, "raises to the power of", exp, "is: ", result)

# exponent(5, 4)

# def exponent(base, exp):
#     return pow(base, exp)

# base = 2
# exp = 5
# print(f"{base} raises to the power of {exp}: {exponent(base, exp)}")

# base = 5
# exp = 4
# print(f"{base} raises to the power of {exp}: {exponent(base, exp)}") 
