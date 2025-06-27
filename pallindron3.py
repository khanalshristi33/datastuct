num = int (input("enter the number:"))
original = num121
rev = 0

while num > 0 :
    digit = num % 10
    rev  = rev *10 + digit
    num = num  // 10
if original  == rev:
    print (f"{original} is a palindrome")
else:
    print(f"{original} is not palindrome" )
