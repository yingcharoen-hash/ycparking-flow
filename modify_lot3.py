import re

with open("departments/parking_restroom/ycparking/tab6_motorcycle_lot3.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Title and Header
content = content.replace("กระบวนการที่ 5", "กระบวนการที่ 6")
content = content.replace("ลาน 2", "ลาน 3")

# 2. Meta Items
content = content.replace("เครื่องนับรถ + YC Parking App", "เครื่องนับรถ")
content = re.sub(r'<div class="meta-item"><span class="meta-label">สิทธิ์บุคลากร</span><span class="meta-value">30 ครั้ง/เดือน</span></div>\s*', '', content)
content = content.replace("วิกฤต 1 · สูง 4 · กลาง 3", "วิกฤต 1 · สูง 3 · กลาง 3")
content = content.replace("7 ฝ่าย", "6 ฝ่าย") # Removed HR/Personnel since no QR

# 3. Remove Swimlane Case B (QR Code)
case_b_pattern = r'<!-- Case B -->\s*<div class="case-box b">\s*<div class="case-title">บุคลากร YC</div>\s*<div class="flow-item"><div class="step ops" onclick="showPanel\(\'sB1\'\)"><div class="step-num">ข-1</div><div class="step-text">สแกน QR บุคลากร</div></div></div>\s*</div>'
content = re.sub(case_b_pattern, '', content)

# 4. Update Formula Display
old_formula = r'<span class="f-blue">สแกน QR บุคลากร \(YC Parking โดยตรง\)</span> −\s*'
content = re.sub(old_formula, '', content)

# 5. Update stepData JS
# Remove sB1 entirely
sb1_pattern = r"sB1: \{.*?\},"
content = re.sub(sb1_pattern, '', content, flags=re.DOTALL)

# Modify sA1 tasks
content = content.replace("'กรณีบุคลากรสิทธิ์หมด (สแกนไม่ผ่าน) → เก็บเงินปกติกรณีนี้',", "")
content = content.replace(",'กรณีบุคลากรสิทธิ์หมด (สแกนไม่ผ่าน) → เก็บเงินปกติกรณีนี้'", "")

# Modify sR1 (4 items -> 3 items)
content = content.replace("รับเอกสารและตรวจนับเงิน 4 รายการ", "รับเอกสารและตรวจนับเงิน 3 รายการ")
content = content.replace("ตรวจนับ 4 รายการ", "ตรวจนับ 3 รายการ")
content = content.replace("③ จำนวนสแกน QR บุคลากร (บวกด้วยใบจดชื่อกรณีระบบล่ม ที่มีลายเซ็นหัวหน้างาน)','④ จำนวนบัตรจอดรถฟรี", "③ จำนวนบัตรจอดรถฟรี")
content = content.replace("📊 รายงาน YC Parking / 📋 ใบจดชื่อกรณีระบบล่ม (เซ็นกำกับ)", "")
content = content.replace("การตรวจสอบที่แท้จริงต้องเทียบกับ YC Parking โดยตรง", "การตรวจสอบที่แท้จริงต้องเทียบกับระบบเครื่องนับรถโดยตรง")

# Modify aD3 formula
content = content.replace("สแกน QR บุคลากร − ", "")

# Update Risk Table rows:
# Remove the row about YC Parking System Down
risk_row_pattern = r"<tr>\s*<td><strong>แอป YC Parking ล่ม.*?</tr>"
content = re.sub(risk_row_pattern, '', content, flags=re.DOTALL)

with open("departments/parking_restroom/ycparking/tab6_motorcycle_lot3.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Modifications to tab6_motorcycle_lot3.html completed successfully.")
