import re

# ตั้งค่าชื่อไฟล์
input_file = 'amphoe.sql'  # เปลี่ยนเป็นชื่อไฟล์จริง
output_file = 'outputA.txt'

# ปรับ regex ให้เหมาะสม
pattern = re.compile(
    r"INSERT INTO `amphoe`\s*\(\s*`acode`\s*,\s*`aname`.+?\)\s*VALUES\s*\(\s*(\d+),\s*'([^']+)'\s*",
    re.IGNORECASE
)

# เก็บผลลัพธ์
results = []

try:
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            match = pattern.search(line)
            if match:
                acode, aname = match.groups()
                results.append(f"{acode} {aname}")

    # บันทึกผลลัพธ์ลงไฟล์
    if results:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(results))
        print(f"ข้อมูลถูกบันทึกลงไฟล์ '{output_file}' แล้ว")
    else:
        print("ไม่พบข้อมูลที่ตรงกับรูปแบบที่กำหนดในไฟล์ SQL")

except FileNotFoundError:
    print(f"ไม่พบไฟล์ '{input_file}' โปรดตรวจสอบชื่อไฟล์และตำแหน่ง")
