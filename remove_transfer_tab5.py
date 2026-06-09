import os

filepath = "D:/Company_Workflows/departments/parking_restroom/ycparking/tab5_motorcycle.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Swimlane Text: "เก็บค่าบริการ เงินสด / โอน / QR" -> "เก็บค่าบริการ เงินสด / QR" (assuming QR means standard PromptPay QR or personnel QR, but wait: the text says "เงินสด / โอน / QR". Since "โอน" is what we are removing, let's just make it "เงินสด / QR")
content = content.replace("เก็บค่าบริการ<br>เงินสด / โอน / QR", "เก็บค่าบริการ<br>เงินสด / QR")

# 2. Formula: "รายได้จริงที่รับมา = เงินสด + เงินโอน" -> "รายได้จริงที่รับมา = เงินสด"
content = content.replace("รายได้จริงที่รับมา = เงินสด + เงินโอน", "รายได้จริงที่รับมา = เงินสด")
content = content.replace("= เงินสด + เงินโอน", "= เงินสด")

# 3. Step s4 (จัดทำใบสรุปส่งเงิน)
content = content.replace("รวบรวมเงินสดและเงินโอนทั้งหมด", "รวบรวมเงินสดทั้งหมด")

# 4. Step sR1 (รับเอกสารและตรวจนับเงิน 4 รายการ -> 3 รายการ)
content = content.replace("ตรวจนับ 4 รายการ", "ตรวจนับ 3 รายการ")
# '① เงินสด','② เงินโอน','③ จำนวนสแกน QR บุคลากร...', '④ จำนวนบัตรจอดรถฟรี'
content = content.replace("'① เงินสด','② เงินโอน','③ จำนวนสแกน", "'① เงินสด','② จำนวนสแกน")
content = content.replace("'④ จำนวนบัตรจอดรถฟรี'", "'③ จำนวนบัตรจอดรถฟรี'")

# 5. Step aD2 (ขอสรุปยอดรายได้จากฝ่ายการเงิน)
content = content.replace("สรุปยอดเงินสด + เงินโอนที่รับจริง", "สรุปยอดเงินสดที่รับจริง")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Lot 2 transfer removal successful.")
