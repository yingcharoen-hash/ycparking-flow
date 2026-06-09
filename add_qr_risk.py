import os

# 1. Update SYSTEM_CONSTRAINTS.md
filepath = "D:/Company_Workflows/SYSTEM_CONSTRAINTS.md"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

old_lot3_text = "* **ลาน 3:** **ไม่มีมือถือส่วนกลาง** เจ้าหน้าที่ต้องใช้วิธี **\"ถ่ายภาพสลิปของลูกค้า\"** แล้วส่งเข้ากลุ่มไลน์ (LINE Group) ที่มีเจ้าหน้าที่การเงินอยู่ในกลุ่ม เพื่อเป็นหลักฐานยืนยันการรับชำระ"
new_lot3_text = """* **ลาน 3:** **ไม่มีมือถือส่วนกลาง** เจ้าหน้าที่ต้องใช้วิธี **"ถ่ายภาพสลิปของลูกค้า"** แล้วส่งเข้ากลุ่มไลน์ (LINE Group) ที่มีเจ้าหน้าที่การเงินอยู่ในกลุ่ม เพื่อเป็นหลักฐานยืนยันการรับชำระ
  * **⚠️ ความเสี่ยง (R4):** ลาน 3 ไม่สามารถตรวจสอบเงินเข้าได้แบบ Real-time ณ จุดจอด มีความเสี่ยงที่ลูกค้าอาจใช้ **สลิปปลอม หรือ สลิปเก่า** หลอกลวงเจ้าหน้าที่ได้"""

content = content.replace(old_lot3_text, new_lot3_text)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

# 2. Update tab6_motorcycle_lot3.html
filepath_lot3 = "D:/Company_Workflows/departments/parking_restroom/ycparking/tab6_motorcycle_lot3.html"
with open(filepath_lot3, "r", encoding="utf-8") as f:
    content3 = f.read()

# Update warn string in sA1
old_warn = "warn:'ไม่มีใบเสร็จรายคัน — ตรวจสอบย้อนหลังได้ยาก ควรพิจารณาออกสลิปย่อหรือติดกล้องวงจรปิด'"
new_warn = "warn:'ไม่มีใบเสร็จรายคัน (R3) และเสี่ยงต่อการรับสลิปปลอม (R4) เนื่องจากลาน 3 ไม่มีเครื่องตรวจสอบเงินเข้าแบบ Real-time'"

content3 = content3.replace(old_warn, new_warn)

with open(filepath_lot3, "w", encoding="utf-8") as f:
    f.write(content3)

print("Lot 3 QR Risk added.")
