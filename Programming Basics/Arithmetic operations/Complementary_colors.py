number1, number2, number3 = map(int, input().split())
list = [number1, number2, number3]
r = (max(list)+min(list)-number1)
g = (max(list)+min(list)-number2)
b = (max(list)+min(list)-number3)
print(r, g ,b)