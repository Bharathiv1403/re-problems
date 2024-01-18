#1. Write a Python program that matches a word containing 'z', not the start or end of the word.

import re
text="""Oh do you know the zookeeper,
The zookeeper, the zookeeper?
Oh, do you know the zookeeper
Who works down at the zoo?"""
texture=r'\b\w*z\w*\b'
match=re.findall(texture,text)
print(match)
