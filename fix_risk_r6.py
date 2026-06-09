import os

# 1. Update SYSTEM_CONSTRAINTS.md
filepath_md = "D:/Company_Workflows/SYSTEM_CONSTRAINTS.md"
with open(filepath_md, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("⚠️ ความเสี่ยง (R4):", "⚠️ ความเสี่ยง (R6):")

with open(filepath_md, "w", encoding="utf-8") as f:
    f.write(content)


# 2. Update tab6_motorcycle_lot3.html
filepath_lot3 = "D:/Company_Workflows/departments/parking_restroom/ycparking/tab6_motorcycle_lot3.html"
with open(filepath_lot3, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
in_r5 = False
for line in lines:
    # Fix the warn string
    if "เสี่ยงต่อการรับสลิปปลอม (R4)" in line:
        line = line.replace("เสี่ยงต่อการรับสลิปปลอม (R4)", "เสี่ยงต่อการรับสลิปปลอม (R6)")
    
    new_lines.append(line)
    
    # Check for end of R5 block to insert R6
    if '<td style="font-weight:800;color:var(--orange);">R5</td>' in line:
        in_r5 = True
        
    if in_r5 and "</tr>" in line:
        # We reached the end of R5, let's append R6
        r6_html = """      <tr>
        <td style="font-weight:800;color:var(--orange);">R6</td>
        <td><strong>สลิปปลอม (QR PromptPay)</strong><div style="font-size:11px;color:var(--gray400);margin-top:2px;">1 | Audit: สน-3</div></td>
        <td>ลาน 3 ไม่มีอุปกรณ์ตรวจสอบเงินเข้าหน้างาน ทำให้เสี่ยงต่อการรับสลิปโอนเงินปลอมหรือสลิปเก่า</td>
        <td><span class="rl h">สูง</span></td>
        <td>• ส่งรูปเข้ากลุ่มไลน์เพื่อให้การเงินช่วยตรวจสอบ<br>• สุ่มตรวจความถูกต้องของสลิปย้อนหลัง<br>• เสนอให้จัดหามือถือส่วนกลางประจำจุด</td>
      </tr>
"""
        new_lines.append(r6_html)
        in_r5 = False

with open(filepath_lot3, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("R6 appended and R4 collision fixed.")
