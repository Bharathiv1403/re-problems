# 1. Write the pattern for find the email id format 
import re
str = input("Enter the Gmail : ")
match = re.search(r'\w+@\w+', str)
match1=re.search(r'\b\w*gmail\w*\b',str)
if match:
    print("Your Gmail is Correct ",match and match1.group()) 
else:
    print("Not Match")
