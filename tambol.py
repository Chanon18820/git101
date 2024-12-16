import re

# ชื่อไฟล์ input และ output
input_file = 'tambol.sql'  # เปลี่ยนชื่อไฟล์ให้ตรงกับไฟล์ที่คุณมี
output_file = 'outputT.txt'

# สร้าง pattern เพื่อจับข้อมูลที่ต้องการ
pattern = r"INSERT INTO `tambol`\(`tcode`, `tname`, `acode`, `aname`, `pcode`, `pname`\) VALUES \((\d+), '(.*?)', \d+, '.*?', \d+, '.*?'\);"

# อ่านไฟล์ .sql และดึงข้อมูล
with open(input_file, 'r', encoding='utf-8') as file:
    sql_content = file.readlines()

# เก็บผลลัพธ์ที่ต้องการ
results = []

# ค้นหาข้อมูลที่ตรงกับ pattern
for line in sql_content:
    match = re.match(pattern, line)
    if match:
        tcode, tname = match.groups()
        results.append(f"{tcode} {tname}")

# บันทึกผลลัพธ์ลงไฟล์ outputT.txt
with open(output_file, 'w', encoding='utf-8') as file:
    file.write("\n".join(results))

print(f"ดึงข้อมูลสำเร็จ! ข้อมูลถูกบันทึกลงในไฟล์ {output_file}")
