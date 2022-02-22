a = input();
b = input();


if a.isdigit() and b.isdigit():
  a = int(a)
  b = int(b)
  c = a + b
  print (c)
elif a.isdigit() and b.isalpha():
  print(a+b)
elif a.isalpha() and b.isdigit():
  print(a+b)
else:
 print (a+b)
