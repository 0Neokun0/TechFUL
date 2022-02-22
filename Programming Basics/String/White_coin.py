n = int(input())                                # for size
import re

str_obj = input()
count = len(re.findall(r'[A]',str_obj))
print(count)