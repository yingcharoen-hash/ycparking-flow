import os

filepath = "D:/Company_Workflows/departments/parking_restroom/ycparking/tab6_motorcycle_lot3.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Fix Audit Swimlane
content = content.replace("ดึง YC Parking โดยตรง", "ดึงข้อมูลจากมิเตอร์นับรถ")
content = content.replace("ตรวจ QR รายบุคคล", "ตรวจสอบรถค้างจอด")
content = content.replace("ตรวจโควต้าบุคลากร", "สอบทานความสมบูรณ์เอกสาร")

# 2. Fix Leftovers in Risk R2
content = content.replace("ไม่รวมสแกน QR และที่เกิดขึ้นในช่วงนั้น", "ไม่รวมรถค้างจอดที่เกิดขึ้นในช่วงนั้น")
content = content.replace("หักจำนวนสแกน QR และในช่วงเวลานั้นออกด้วย", "หักจำนวนรถค้างจอดในช่วงเวลานั้นออกด้วย")
content = content.replace("− สแกน QR − เงินทอน 200", "− เงินทอน 200")

# 3. Fix Leftovers in stepData
content = content.replace("ดึงข้อมูลจากระบบ YC Parking (Dashboard/Export)", "ตรวจสอบข้อมูลจากบันทึกมิเตอร์นับรถ")
content = content.replace("ตรวจสอบจำนวนการสแกน QR รายบุคคลจาก Log", "ตรวจสอบความสอดคล้องของรถค้างจอดจากกะกลางคืน")
content = content.replace("ดึง Log สิทธิ์บุคลากรทั้งหมด", "สุ่มตรวจความสมบูรณ์ของเอกสารและลายเซ็น")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Audit wording fixed successfully.")
