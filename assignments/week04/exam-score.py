# รับคะแนนสอบนักเรียน 5 คน
scores = []

for i in range(5):
    score = int(input(f"Enter score of student {i + 1}: "))
    scores.append(score)

print()

# ตรวจสอบคะแนน
for i in range(5):
    if scores[i] >= 50:
        result = "ผ่าน"
    else:
        result = "ไม่ผ่าน"

    print(f"Student {i + 1}: {scores[i]} => {result}")