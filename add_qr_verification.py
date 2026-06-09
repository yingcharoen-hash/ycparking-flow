import os

# 1. Update SYSTEM_CONSTRAINTS.md
filepath = "D:/Company_Workflows/SYSTEM_CONSTRAINTS.md"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

qr_verification_text = """
## 7. การตรวจสอบยอดชำระ QR PromptPay (หน้างาน)
* **ลาน 2:** มี **"มือถือส่วนกลาง"** ประจำจุดจอด ซึ่งผูกกับแจ้งเตือนเงินเข้าธนาคารกรุงศรี เจ้าหน้าที่สามารถตรวจสอบยอดเงินเข้าได้ทันที
* **ลาน 3:** **ไม่มีมือถือส่วนกลาง** เจ้าหน้าที่ต้องใช้วิธี **"ถ่ายภาพสลิปของลูกค้า"** แล้วส่งเข้ากลุ่มไลน์ (LINE Group) ที่มีเจ้าหน้าที่การเงินอยู่ในกลุ่ม เพื่อเป็นหลักฐานยืนยันการรับชำระ
"""

if "## 7. การตรวจสอบยอดชำระ" not in content:
    content += qr_verification_text

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)


# 2. Update Lot 2 sA1
filepath_lot2 = "D:/Company_Workflows/departments/parking_restroom/ycparking/tab5_motorcycle.html"
with open(filepath_lot2, "r", encoding="utf-8") as f:
    content2 = f.read()

# Add task to Lot 2 sA1. We know the old tasks contained: "'รับได้ทั้งเงินสดและสแกน QR PromptPay'"
content2 = content2.replace("'รับได้ทั้งเงินสดและสแกน QR PromptPay'", "'รับได้ทั้งเงินสดและสแกน QR PromptPay','ตรวจสอบยอดเงินสแกน QR จากแอปธนาคารกรุงศรีบนมือถือส่วนกลางประจำจุด'")

with open(filepath_lot2, "w", encoding="utf-8") as f:
    f.write(content2)


# 3. Update Lot 3 sA1
filepath_lot3 = "D:/Company_Workflows/departments/parking_restroom/ycparking/tab6_motorcycle_lot3.html"
with open(filepath_lot3, "r", encoding="utf-8") as f:
    content3 = f.read()

# Add task to Lot 3 sA1
content3 = content3.replace("'รับได้ทั้งเงินสดและสแกน QR PromptPay'", "'รับได้ทั้งเงินสดและสแกน QR PromptPay','กรณีสแกน QR ให้ถ่ายภาพสลิปลูกค้าส่งเข้ากลุ่มไลน์ (การเงินรับทราบยอดในกลุ่ม)'")

with open(filepath_lot3, "w", encoding="utf-8") as f:
    f.write(content3)

print("QR verification constraints added.")
