# 1. Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

import re
def change_date_format(dt):
        return re.sub(r'(\d{4}\-\d{2}\-\d{2}', '\\3-\\2-\\1', dt)    #\\3-\\2-\\1--> Position of date, month, year.
dt1 = "2026-01-02"
print("Original date in YYY-MM-DD Format: ",dt1)
print("New date in DD-MM-YYYY Format: ",change_date_format(dt1))

# import re
# def coverting(string):
#     result=re.split(r"-",string)
# #print(result)
#     final_result=[i for i in reversed(result)]
#     print("-".join(final_result))

# coverting("2020-04-02")