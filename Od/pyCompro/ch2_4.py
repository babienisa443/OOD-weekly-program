print(" *** Integer division ***")
x = input("Enter a 3-digit number : ")
print(x, type(x))  # ตรวจสอบข้อมูลที่รับเข้ามา
x = float(x)    # type casting เปลี่ยน string(ข้อความ) เป็น float(ทศนิยม)
print(x, type(x))    # แสดงผลทศนิยม และ type ข้อมูล
# type casting เปลี่ยน float(ทศนิยม) เป็น integer(จำนวนเต็ม
x = int(x)
print(x, type(x))    # แสดงผลทศนิยม และ type ข้อมูล
# การหารจำนวนเต็ม ผลลัพธ์ที่ได้ เป็นข้อมูลประเภททศนิยม
print("divided by 25 =", x/25)
# การหารแบบเหลือเศษ ใช้เครื่องหมาย // (double-slash)
print("divided by 25 =", x//25, " remainder = ", x % 25)
# สามารถหาเศษ ได้โดยใช้เครื่องหมาย % (mod)
print("tenth-digit =", (x // 10)-((x//100) * 10))
