import time
import Sorting as mi
import sys
sys.setrecursionlimit(10**6)

# อ่านไฟล์และจัดการข้อมูล
with open('outputP.txt', 'r', encoding='utf-8') as fin:
    all_records = [' '.join(record.strip().split()) for record in fin if record.strip()]

# ฟังก์ชันวัดเวลาการทำงานของอัลกอริทึมการเรียงลำดับ
def measure_sort_time(sort_function, data, *args):
    start = time.time()
    sort_function(data, *args)
    return (time.time() - start) * 10

if __name__ == '__main__':
    algorithms = [
        ("BubbleSort", mi.BubbleSort, list(all_records)),
        ("InsertionSort", mi.InsertionSort, list(all_records)),
        ("SelectionSort", mi.SelectionSort, list(all_records)),
        ("MergeSort", mi.MergeSort, list(all_records)),
        ("QuickSort", mi.QuickSort, list(all_records), 0, len(all_records) - 1)
    ]

    total_time = []

    for name, func, *args in algorithms:
        time_taken = measure_sort_time(func, *args)
<<<<<<< Updated upstream
        print(f"{name} ใช้เวลาทั้งหมด {time_taken:.2f} วินาที\n")
=======
        print(f"{name} ใช้เวลาทั้งหมด {time_taken:.2f} มิลลิวินาที\n")
>>>>>>> Stashed changes
        total_time.append((time_taken, name))

    # เรียงเวลาและให้ผู้ใช้เพิ่มชื่ออัลกอริทึม
    total_time.sort()

    for i, (time_val, name) in enumerate(total_time):
        new_name = input(f"กรุณาใส่ชื่อ Algorithm สำหรับ {name} = ")
        total_time[i] = (time_val, f"{time_val:.2f} {new_name}")

    # แสดงผลลัพธ์
    print("\nเรียงเวลาที่ Algorithm ใช้เวลาในการทำจากน้อยไปมาก:")
    for time_val, name in total_time:
        print(name)

    print(f"\nใช้เวลามากสุด: {total_time[-1][1]}")
    print(f"ใช้เวลาน้อยสุด: {total_time[0][1]}")
<<<<<<< Updated upstream
    print(f"ใช้เวลากลางๆ: {total_time[len(total_time)//2][1]}")

    



=======
    print(f"ใช้เวลากลางๆ: {total_time[len(total_time)//2][1]}")
>>>>>>> Stashed changes
