#รับคำชื่อจริงจากผู้ใช้ 
#เขียน loop เพื่อนับจำนวน "สระที่มีอยู่ในชื่อที่รับมา" นั้นว่ามีจำนวนกี่ตัว

#ตัวอย่าง

# What is your name?: Siradanai

# Your name have 5 vowels.
# รับชื่อจากผู้ใช้
name = input("What is your name?: ")

count = 0

for ch in name:
    if ch == "a":
        count = count + 1
    if ch == "e":
        count = count + 1
    if ch == "i":
        count = count + 1
    if ch == "o":
        count = count + 1
    if ch == "u":
        count = count + 1
    if ch == "A":
        count = count + 1
    if ch == "E":
        count = count + 1
    if ch == "I":
        count = count + 1
    if ch == "O":
        count = count + 1
    if ch == "U":
        count = count + 1

print("Your name have", count, "vowels.")