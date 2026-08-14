# เขียน function ชื่อ calculate_shpere(radius):
# คำนวณหา ปริมาตร ของทรงกลม
# volume = 4.0 / 3 * pi * radius ** 3
# จากนั้นแสดงผลลัพธ์ที่เหมาะสมออกทางหน้าจอ
# อย่าลืมที่จะเขียนโปรแกรมเพื่อการทดสอบการใช้งาน



def calculate_sphere(radius):
    pi = 3.14159  
    volume = 4.0 / 3 * pi * radius ** 3
    print(f"Sphere with radius {radius}")
    print(f"Volume = {volume}")
    print()
 
calculate_sphere(7)
calculate_sphere(13)