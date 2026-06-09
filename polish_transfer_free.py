import os

filepath = "D:/Company_Workflows/departments/parking_restroom/ycparking/tab6_motorcycle_lot3.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Fix broken task lists
content = content.replace("รวบรวมเงินสดและเงินโอนทั้งหมด','รวบรวมที่ได้รับทั้งหมด", "รวบรวมเงินสดทั้งหมด")
content = content.replace("🎫  (รวบรวม)','", "")
content = content.replace("ตรวจนับ 3 รายการให้ตรงกับใบสรุปส่งเงิน:','① เงินสด','② เงินโอน','③',", "ตรวจนับเงินสดให้ตรงกับใบสรุปส่งเงิน:',")
content = content.replace("ตรวจนับ 3 รายการให้ตรงกับใบสรุปส่งเงิน:','① เงินสด','② เงินโอน','③',", "ตรวจนับเงินสดให้ตรงกับใบสรุปส่งเงิน:',") # if any
content = content.replace("ตรวจนับ 3 รายการ", "ตรวจนับเงินสด")
content = content.replace("'① เงินสด','② เงินโอน',", "")

# Since I missed "เงินโอน" in Lot 2, I'll fix Lot 2 as well
filepath5 = "D:/Company_Workflows/departments/parking_restroom/ycparking/tab5_motorcycle.html"
with open(filepath5, "r", encoding="utf-8") as f:
    content5 = f.read()

content5 = content5.replace("เงินสดและเงินโอน", "เงินสด")
content5 = content5.replace("เงินสด / โอน / QR", "เงินสด / QR")
content5 = content5.replace("เงินสด / โอน", "เงินสด")
content5 = content5.replace("เงินสด + เงินโอน", "เงินสด")
content5 = content5.replace("② เงินโอน',", "")
content5 = content5.replace("4 รายการ", "3 รายการ")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
with open(filepath5, "w", encoding="utf-8") as f:
    f.write(content5)

print("Polish successful.")
