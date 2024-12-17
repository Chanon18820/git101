import time
import Sorting as mi
import sys
sys.setrecursionlimit(10**6)

with open('outputA.txt', 'r',encoding='utf-8') as fin:
    all_records = []

    for record in fin:
        record = record.strip()
        if not record:
            continue

        data = record.split()
        new_record = ' '.join(data)
        all_records.append(new_record)

if __name__ == '__main__':
    bu = list(all_records)
    In = list(all_records)
    se = list(all_records)
    me = list(all_records)
    qu = list(all_records)

    start_B = time.time()
    mi.BubbleSort(bu)
    end_B = time.time()
    b = (end_B-start_B) * 10**3
    print ("เวลาทั้งหมด",b,"มิลลิวินาที")
    time_bu = b
    print()
                              
    start_I = time.time()
    mi.InsertionSort(In)
    end_I = time.time()
    i = (end_I-start_I) * 10**3
    print ("เวลาทั้งหมด",i,"มิลลิวินาที")
    time_in = i
    print()

    start_S = time.time()
    mi.SelectionSort(se)
    end_S = time.time()
    s = (end_S-start_S) * 10**3
    print ("เวลาทั้งหมด",s,"มิลลิวินาที")
    time_se = s
    print()

    start_M = time.time()
    mi.MergeSort(me)
    end_M = time.time()
    m = (end_M-start_M) * 10**3
    print ("เวลาทั้งหมด",m,"มิลลิวินาที")
    time_me = m
    print()

    start_Q = time.time()
    mi.QuickSort(qu,0, len(qu)-1)
    end_Q = time.time()
    q = (end_Q-start_Q) * 10**3
    print ("เวลาทั้งหมด",q,"มิลลิวินาที")
    time_qu = q
    print()

    total_time = [time_bu, time_in, time_se, time_me, time_qu]

    mi.BubbleSortA(total_time)

    print(total_time[0])
    a = input("กรุณาใส่ชื่อ Algorithm =")
    total_time[0] = f"{total_time[0]}{a}"

    print(total_time[1])
    b = input("กรุณาใส่ชื่อ Algorithm =")
    total_time[1] = f"{total_time[1]}{b}"

    print(total_time[2])
    c = input("กรุณาใส่ชื่อ Algorithm =")
    total_time[2] = f"{total_time[2]}{c}"

    print(total_time[3])
    d = input("กรุณาใส่ชื่อ Algorithm =")
    total_time[3] = f"{total_time[3]}{d}"

    print(total_time[4])
    e = input("กรุณาใส่ชื่อ Algorithm =")
    total_time[4] = f"{total_time[4]}{e}"

    print("เรียงเวลาที่ Algorithm ใช้เวลาในการทำจาก น้อยไปมาก", total_time)
    print()
    print("ใช้เวลามากสุด", total_time[-1])
    print()
    print("ใช้เวลาน้อยสุด", total_time[0])
    print()
    print("ใช้เวลากลางๆ", total_time[2])
    



