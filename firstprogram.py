print ("helloworld")
message = "helloworld"
print (message)
a=100
b=200
print (a+b)

def withdrawal(first: int , second: int)  -> int :
    res  = second - first
    return res

balance = withdrawal(a,b)

print("The balance is: ", balance)
if (a > b):
    print ("A is greater than B") 
elif(a<b):
    print("A is less than B")