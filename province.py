import re

# อ่านไฟล์ .sql
input_file = 'province.sql'  # เปลี่ยนเป็นชื่อไฟล์จริง
output_file = 'outputP.txt'

# สร้าง regex pattern เพื่อค้นหาข้อมูล
pattern = re.compile(
    r"INSERT INTO `province`\(`pcode`, `pname`, `type_soilder`\) VALUES \((?P<pcode>\d+), '(?P<pname>[^']+)',",
    re.DOTALL
)


# เก็บผลลัพธ์
results = []

with open(input_file, 'r', encoding='utf-8') as f:
    for line in f:
        match = pattern.search(line)
        if match:
            pcode = match.group('pcode')
            pname = match.group('pname')
            results.append(f"{pcode} {pname}")

# บันทึกผลลัพธ์ลงไฟล์
with open(output_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(results))

print("ข้อมูลถูกบันทึกแล้ว")