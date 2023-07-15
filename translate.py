s = input()
line = input()
d = str.maketrans('abcdefghijklmnopqrstuvwxyz', s)
print(line.lower().translate(d))
