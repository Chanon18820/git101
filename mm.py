import re

# อ่านไฟล์ .sql
input_file = 'mm.sql'  # เปลี่ยนเป็นชื่อไฟล์จริง
output_file = 'outputM.txt'

# สร้าง regex pattern เพื่อค้นหาข้อมูล
pattern = re.compile(
    r"INSERT INTO `mm`\(`mcode`, `mname`, .+?\) VALUES \('(?P<mcode>\d+)', '(?P<mname>[^']+)',",
    re.DOTALL
)

# เก็บผลลัพธ์
results = []

with open(input_file, 'r', encoding='utf-8') as f:
    for line in f:
        match = pattern.search(line)
        if match:
            mcode = match.group('mcode')
            mname = match.group('mname')
            results.append(f"{mcode} {mname}")

# บันทึกผลลัพธ์ลงไฟล์
with open(output_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(results))

print("ข้อมูลถูกบันทึกแล้ว")