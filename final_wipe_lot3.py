import os

filepath = "D:/Company_Workflows/departments/parking_restroom/ycparking/tab6_motorcycle_lot3.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# aW1 tasks
content = content.replace("ดึงยอดรถออกสะสม + สแกน QR สะสม + สะสม จากระบบก่อนลงพื้นที่", "ดึงยอดรถออกสะสมจากมิเตอร์นับรถก่อนลงพื้นที่")
content = content.replace("🖥️ YC Parking + ตัวนับรถ", "🖥️ ระบบมิเตอร์นับรถ")

# aW4 tasks
old_aW4_tasks = "['ดึง Log การสแกน QR จากระบบ YC Parking แยกรายบุคคล','วิเคราะห์ความผิดปกติ (เช่น สแกนเข้า-ออกถี่เกินไป, มีการนำ QR ไปให้บุคคลอื่นใช้ซ้ำ)','ตรวจสอบว่า HR ปรับหักโควต้าย้อนหลังครบ (กรณีระบบล่ม)']"
new_aW4_tasks = "['ตรวจสอบความสอดคล้องของรถค้างจอดจากกะกลางคืน','เทียบกับรายงานรถค้างจอดประจำคืน (กค-1)','หาความผิดปกติของยอดรถค้างจอด']"
content = content.replace(old_aW4_tasks, new_aW4_tasks)
content = content.replace("'🖥️ YC Parking — Log รายบุคคล'", "'📋 รายงานรถค้างจอด'")

# aM2 tasks
old_aM2_tasks = "['ตรวจสอบจำนวนสิทธิ์ที่ใช้ทั้งเดือนเทียบกับโควต้า 30 ครั้ง/บุคลากร','เทียบกับรายชื่อบุคลากรที่ HR ออกสิทธิ์ไว้','ตรวจสอบว่าบุคลากรที่ออกจากงานแล้วยังมี QR ที่ใช้งานได้หรือไม่']"
new_aM2_tasks = "['สุ่มตรวจความสมบูรณ์ของเอกสารและลายเซ็น','ตรวจสอบว่าเอกสารมีการลงนามครบถ้วนทุกจุด','สรุปรายการเอกสารที่ไม่สมบูรณ์เพื่อปรับปรุง']"
content = content.replace(old_aM2_tasks, new_aM2_tasks)
content = content.replace("'🖥️ YC Parking — สรุปรายเดือน','📋 รายชื่อบุคลากรที่ HR ออกสิทธิ์'", "'📁 แฟ้มเอกสารรายเดือน'")

# Role color
content = content.replace("'ระบบ YC Parking (อัตโนมัติ)': '#1779a0',", "")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Final wipe successful.")
