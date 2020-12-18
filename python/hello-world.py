import os

print("Hello Jenkins")

if os.path.exists("software.txt"):
  os.remove("software.txt")
else:
  print("The file does not exist")
  f = open("software.txt", "x")
  f.close