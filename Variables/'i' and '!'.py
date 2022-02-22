number = input()
s = input()[::-1]
print(s.translate(str.maketrans({'i': '!', '!': 'i'})))