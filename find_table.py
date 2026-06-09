import sys

with open('D:/Company_Workflows/departments/parking_restroom/ycparking/tab6_motorcycle_lot3.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if 'R1' in line and '<td' in line:
            for j in range(max(0, i-5), min(len(lines), i+15)):
                print(f"Line {j+1}: {lines[j].strip().encode('unicode_escape').decode('utf-8')}")
            break
