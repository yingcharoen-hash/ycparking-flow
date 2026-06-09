import os

def fix_sN1(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # The title for sN1 might be "บันทึกรถค้างจอด ณ เที่ยงคืน"
    content = content.replace("id:'กค-1', title:'บันทึกรถค้างจอด ณ เที่ยงคืน'", "id:'กค-1', title:'จดมิเตอร์และคำนวณรถค้างจอด'")

    # Replace the tasks array for sN1
    # Currently: ['นับและบันทึกจำนวนรถที่ยังค้างจอดอยู่ ณ เวลาเที่ยงคืน','บันทึกในรายงานประจำวัน','ข้อมูลนี้ใช้ปรับสูตรตรวจสอบรายได้วันถัดไป: รถออกจริง = รถออก − รถค้างเมื่อวาน + รถค้างวันนี้']
    old_tasks = "['นับและบันทึกจำนวนรถที่ยังค้างจอดอยู่ ณ เวลาเที่ยงคืน','บันทึกในรายงานประจำวัน','ข้อมูลนี้ใช้ปรับสูตรตรวจสอบรายได้วันถัดไป: รถออกจริง = รถออก − รถค้างเมื่อวาน + รถค้างวันนี้']"
    new_tasks = "['จดเลขมิเตอร์รถเข้า-ออก ณ เวลาเที่ยงคืนตรง (ไม่ต้องเดินนับรถทีละคัน)','คำนวณรถค้างจอดด้วยสูตร: รถค้างจอดเมื่อวาน + รถเข้าวันนี้ - รถออกวันนี้','บันทึกในรายงานประจำวัน เพื่อเป็นฐานคำนวณรายได้วันถัดไป']"
    content = content.replace(old_tasks, new_tasks)
    
    # Also update swimlane step text
    content = content.replace("<div class=\"step-text\">บันทึกรถค้างจอด ณ เที่ยงคืน ทุกวัน</div>", "<div class=\"step-text\">จดมิเตอร์&คำนวณรถค้างจอด เที่ยงคืน</div>")
    # For Lot 3 it might be slightly different: 
    # `<div class="step-text">บันทึกรถค้างจอด ณ เที่ยงคืน</div>`
    content = content.replace("<div class=\"step-text\">บันทึกรถค้างจอด ณ เที่ยงคืน</div>", "<div class=\"step-text\">จดมิเตอร์&คำนวณรถค้างจอด</div>")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

fix_sN1("D:/Company_Workflows/departments/parking_restroom/ycparking/tab5_motorcycle.html")
fix_sN1("D:/Company_Workflows/departments/parking_restroom/ycparking/tab6_motorcycle_lot3.html")

print("sN1 calculation logic fixed.")
