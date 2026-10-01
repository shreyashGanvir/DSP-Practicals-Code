# Python Building Blocks and Control Flow Examples

name = "Rahul"
marks = 75

print("Hello")

x = 5
x += 2

x = 10
if x > 5:
    print("Greater than 5")

x = 3
if x % 2 == 0:
    print("Even")
else:
    print("Odd")

if marks >= 90:
    print("A Grade")
elif marks >= 60:
    print("B Grade")
else:
    print("C Grade")

for i in range(5):
    print(i)

i = 0
while i < 5:
    print(i)
    i += 1

for i in range(5):
    if i == 3:
        break
    print(i)
