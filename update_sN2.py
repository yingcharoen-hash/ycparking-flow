import os

def update_sN2(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # We want to add the physical count to sN2 tasks
    old_tasks = "'รีเซ็ตตัวนับรถเข้าและรถออกกลับเป็นศูนย์','ต้องบันทึกรถค้างจอด (กค-1) ก่อนรีเซ็ตทุกครั้ง','บันทึกวันที่และเวลาที่รีเซ็ต'"
    new_tasks = "'เดินนับจำนวนรถจริงทั้งลาน 1 ครั้ง (Physical Count) เพื่อตั้งต้นยอดยกมาใหม่ให้แม่นยำ','รีเซ็ตตัวนับรถเข้าและรถออกกลับเป็นศูนย์','บันทึกวันที่และเวลาที่รีเซ็ตพร้อมยอดตั้งต้นใหม่'"
    
    content = content.replace(old_tasks, new_tasks)

    # Also update the title of sN2 to reflect the baseline count
    content = content.replace("id:'กค-2', title:'รีเซ็ตมิเตอร์นับรถ'", "id:'กค-2', title:'นับรถตั้งต้นและรีเซ็ตมิเตอร์'")
    content = content.replace("<div class=\"step-text\">รีเซ็ตมิเตอร์นับรถ</div>", "<div class=\"step-text\">นับรถตั้งต้นและรีเซ็ตมิเตอร์</div>")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

update_sN2("D:/Company_Workflows/departments/parking_restroom/ycparking/tab5_motorcycle.html")
update_sN2("D:/Company_Workflows/departments/parking_restroom/ycparking/tab6_motorcycle_lot3.html")

print("sN2 updated with Baseline logic.")
