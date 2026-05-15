# wap a program to print all the total of even numbers from 1 to 15.
#wap to check the give string by user is "polindromes" or "not polindrome"
# a=1
# sum=0
# for i in range(1, 16):
#     if i%2==0:
#         sum=+0
    
# print(sum,sum)

# text="madam"
# copy_text=text
# rev=""
# i=len(text)-1

# while i>=0:
#     rev=rev+text[i]
#     i-=1

# if copy_text==rev:
#     print("palindrome")

#wap to reverse the digit:1234 output:4321
# number="1234"
# reverse_number=""
# for i in number:
#     reverse_number=i+reverse_number
# print(reverse_number)

num=1234
reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num//10
print(reverse_number,reverse)