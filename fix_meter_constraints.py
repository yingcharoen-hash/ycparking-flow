import os

# 1. Create SYSTEM_CONSTRAINTS.md
md_content = """# System Constraints & Physical Rules

ไฟล์นี้รวบรวมข้อจำกัดทางกายภาพและข้อกำหนดของระบบ เพื่อป้องกันการออกแบบ Workflow ที่ขัดแย้งกับความเป็นจริง

## 1. เครื่องนับรถ (Hardware Meters)
* **ข้อจำกัด:** เป็นเพียงจอตัวเลขโง่ๆ (Dumb Counter) ที่นับจำนวนเวลารถทับเซ็นเซอร์
* **ไม่มีออนไลน์:** ไม่มีการเชื่อมต่ออินเทอร์เน็ต ไม่มี Dashboard และ **ไม่สามารถออกรายงาน (Export Report) ได้**
* **การอ่านค่า:** เจ้าหน้าที่หรือ Audit ต้อง "เดินไปดูที่หน้าตู้" และจดด้วยมือ (Manual Record) เท่านั้น

## 2. ระบบ YC Parking
* **ลาน 2:** **มีระบบนี้** แต่ใช้สำหรับ "การสแกน QR Code บุคลากรพนักงาน" เท่านั้น (สามารถดึงรายงาน Dashboard ออนไลน์ได้)
* **ลาน 3:** **ไม่มีระบบนี้เลย** (ไม่มีบุคลากรจอดฟรี) การทำงานทั้งหมดเป็นเงินสดและพร้อมเพย์ลูกค้าทั่วไป

## 3. ช่องทางการชำระเงิน
* **อนุญาต:** เงินสด (Cash) และ สแกน QR PromptPay ของลูกค้าทั่วไป
* **ไม่อนุญาต:** **ไม่มีการรับเงินโอนเข้าบัญชี (Bank Transfer)** ในกระบวนการเก็บเงินรายวันของเจ้าหน้าที่ลานจอดรถเด็ดขาด เพื่อลดความซ้ำซ้อนในการตรวจสอบ

## 4. บัตรจอดรถฟรี (Free Parking Pass)
* **ลาน 2:** ยังคงมีกระบวนการรับบัตรจอดรถฟรี
* **ลาน 3:** ไม่มีนโยบายรับบัตรจอดรถฟรี

## 5. การตรวจสอบของฝ่ายตรวจสอบภายใน (Internal Audit)
* เนื่องจากข้อจำกัดของเครื่องนับรถ (ไม่มีระบบออนไลน์) ทำให้ Audit **ไม่สามารถดึงข้อมูลจำนวนรถล่วงหน้า** ก่อนลงพื้นที่ได้
* ข้อมูลอิสระ (Independent Data) ที่แท้จริงเพียงอย่างเดียวที่ Audit มี คือการ **"สุ่มลงพื้นที่โดยไม่แจ้งล่วงหน้า"** เพื่อไปจดเลขมิเตอร์และนับเงินจริง ณ เวลานั้น
* การทำแผน Audit ต้องอิงการลงพื้นที่ (Physical Audit) เป็นหลัก ไม่ใช่การนั่งดู Dashboard
"""

with open("D:/Company_Workflows/SYSTEM_CONSTRAINTS.md", "w", encoding="utf-8") as f:
    f.write(md_content)


# 2. Fix aD1 and aW1 in Lot 3
filepath_lot3 = "D:/Company_Workflows/departments/parking_restroom/ycparking/tab6_motorcycle_lot3.html"
with open(filepath_lot3, "r", encoding="utf-8") as f:
    content3 = f.read()

# Fix aD1 in Lot 3
content3 = content3.replace("id:'ตว-1', title:'ดึงข้อมูลจากมิเตอร์นับรถโดยตรง'", "id:'ตว-1', title:'ข้อจำกัดการดึงข้อมูลอิสระ'")
content3 = content3.replace("'ตรวจสอบข้อมูลจากบันทึกมิเตอร์นับรถ','ไม่รับตัวเลขจากเจ้าหน้าที่เก็บเงินหรือฝ่ายการเงิน','ตัวเลขนี้เป็นแหล่งข้อมูลอิสระเพียงแหล่งเดียวที่มีในปัจจุบัน'", "'ระบบมิเตอร์นับรถไม่มีรายงานแบบออนไลน์ (Dumb Counter)','ผู้ตรวจสอบไม่สามารถดึงข้อมูลจำนวนรถอิสระล่วงหน้าได้','ต้องอาศัยการลงพื้นที่สุ่มตรวจหน้าตู้ (สน-2) เป็นหลัก'")
content3 = content3.replace("'📋 รายงานบันทึกมิเตอร์เข้า-ออก'", "'❌ ไม่มีระบบ Dashboard'")
content3 = content3.replace("'นี่คือจุดเดียวที่ผู้ตรวจสอบได้ข้อมูลอิสระจริง ข้อมูลอื่นยังผ่านเจ้าหน้าที่เก็บเงิน'", "'ข้อจำกัดสำคัญ: ข้อมูลอิสระจะเกิดขึ้นเมื่อผู้ตรวจสอบลงพื้นที่ไปดูด้วยตาตัวเองเท่านั้น'")

# Fix aW1 in Lot 3
content3 = content3.replace("'ดึงยอดรถออกสะสมจากมิเตอร์นับรถก่อนลงพื้นที่','คำนวณยอดเงินที่ควรมีในกระเป๋าเจ้าหน้าที่ ณ ช่วงเวลาปัจจุบัน','ไม่แจ้งเจ้าหน้าที่ล่วงหน้า'", "'เนื่องจากไม่มีระบบออนไลน์ จึงไม่สามารถรู้ยอดเงินล่วงหน้าได้','เตรียมฟอร์มจดบันทึกและกล้องถ่ายรูปเพื่อลงพื้นที่','ห้ามแจ้งเจ้าหน้าที่ล่วงหน้าเด็ดขาด'")
content3 = content3.replace("'🖥️ ระบบมิเตอร์นับรถ'", "'📋 แบบฟอร์มสุ่มตรวจ'")

# Also fix the swimlane text for aW1 in Lot 3
content3 = content3.replace("<div class=\"step-text\">ดึงยอดก่อนลงพื้นที่</div>", "<div class=\"step-text\">เตรียมตัวลงพื้นที่ (ไม่แจ้งล่วงหน้า)</div>")
# Also fix the swimlane text for aD1 in Lot 3
content3 = content3.replace("<div class=\"step-text\">ดึงข้อมูลจากมิเตอร์นับรถ</div>", "<div class=\"step-text\">ข้อจำกัด: ไม่มีระบบรายงานออนไลน์</div>")

with open(filepath_lot3, "w", encoding="utf-8") as f:
    f.write(content3)


# 3. Fix aW1 in Lot 2 (Lot 2 aD1 is fine because they have YC Parking for personnel QR)
filepath_lot2 = "D:/Company_Workflows/departments/parking_restroom/ycparking/tab5_motorcycle.html"
with open(filepath_lot2, "r", encoding="utf-8") as f:
    content2 = f.read()

# Fix aW1 in Lot 2
content2 = content2.replace("'ดึงยอดรถออกสะสม + สแกน QR สะสม จากระบบก่อนลงพื้นที่','คำนวณยอดเงินที่ควรมีในกระเป๋าเจ้าหน้าที่ ณ ช่วงเวลาปัจจุบัน','ไม่แจ้งเจ้าหน้าที่ล่วงหน้า'", "'ดึงยอดสแกน QR สะสม จากระบบ YC Parking ก่อนลงพื้นที่','ยอดเงินสดจะไม่สามารถรู้ล่วงหน้าได้เพราะเครื่องนับรถไม่มีออนไลน์','ห้ามแจ้งเจ้าหน้าที่ล่วงหน้าเด็ดขาด'")

with open(filepath_lot2, "w", encoding="utf-8") as f:
    f.write(content2)

print("Constraints written and JS fixed.")
