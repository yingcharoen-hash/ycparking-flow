import os

filepath = "D:/Company_Workflows/departments/parking_restroom/ycparking/tab6_motorcycle_lot3.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Fix aD1
content = content.replace("id:'ตว-1', title:'ดึงรายงาน YC Parking โดยตรง'", "id:'ตว-1', title:'ดึงข้อมูลจากมิเตอร์นับรถโดยตรง'")
content = content.replace("'เข้าระบบ YC Parking ดึงรายงานสแกน QR บุคลากรรายวันโดยตรง'", "'ตรวจสอบข้อมูลจากบันทึกมิเตอร์นับรถ'")
content = content.replace("'🖥️ YC Parking System — รายงานรายวัน'", "'📋 รายงานบันทึกมิเตอร์เข้า-ออก'")

# Fix aW4
content = content.replace("id:'สน-4', title:'ตรวจประวัติสแกน QR รายบุคคล'", "id:'สน-4', title:'ตรวจสอบรถค้างจอด'")
content = content.replace("'ดึง Log การสแกน QR ของบุคลากรแต่ละคนมาวิเคราะห์'", "'ตรวจสอบความสอดคล้องของรถค้างจอดจากกะกลางคืน'")
content = content.replace("'หาความผิดปกติ เช่น สแกนเข้า-ออกถี่เกินไป หรือสแกนแทนกัน (R5)'", "'เทียบกับรายงานรถค้างจอดประจำคืน (กค-1)'")
content = content.replace("'🖥️ YC Parking Log'", "'📋 รายงานรถค้างจอด'")

# Fix aM2
content = content.replace("id:'ดน-2', title:'ตรวจสอบโควต้าบุคลากรทั้งเดือน'", "id:'ดน-2', title:'สอบทานความสมบูรณ์เอกสาร'")
content = content.replace("'ดึง Log สิทธิ์บุคลากรทั้งหมดมาตรวจสอบกับรอบบิล'", "'สุ่มตรวจความสมบูรณ์ของเอกสารและลายเซ็น'")
content = content.replace("'ตรวจหาสิทธิ์ที่ถูกใช้เกินโควต้า 30 ครั้ง/เดือน หรือการเรียกเก็บเงินกรณีสิทธิ์หมด (R6)'", "'ตรวจสอบว่าเอกสารมีการลงนามครบถ้วนทุกจุด'")
content = content.replace("'🖥️ YC Parking Monthly Report'", "'📁 แฟ้มเอกสารรายเดือน'")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Audit JS fixes applied to Lot 3.")
