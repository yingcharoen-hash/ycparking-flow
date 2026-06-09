import os

filepath = "departments/parking_restroom/ycparking/tab6_motorcycle_lot3.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove กรณี ค Block
case_c = """              <!-- กรณี ค -->
              <div class="case-box c">
                <div class="case-title">🟧 กรณี ค — บัตรจอดรถฟรี (ฟิตเนส)</div>
                <div class="step ctrl" onclick="showPanel('sC1')">
                  <div class="step-num">ค-1</div>
                  <div class="step-text">รับบัตรจอดรถฟรี ยกเว้นค่าบริการ</div>
                  <span class="badge c">✓ มีบัตร</span>
                </div>
              </div>"""

content = content.replace(case_c, "")

# 2. Rename กรณี ก to just "ทั่วไป" or remove the "ก" to make it just "เก็บเงิน"
content = content.replace("🟦 กรณี ก — ทั่วไป / สิทธิ์หมด", "🟦 ทั่วไป")
content = content.replace("ก-1", "1")
content = content.replace("⚠ สิทธิ์หมด → ไปกรณี ก", "")

# 3. Clean up formulas in HTML
content = content.replace("− <span class=\"f-orange\">บัตรจอดรถฟรี</span>", "")
content = content.replace("− บัตรจอดรถฟรี", "")
content = content.replace("บัตรฟรี", "")

# 4. Clean up "ขั้น 4", "กง-2", "รง-1"
content = content.replace("จัดทำใบสรุปส่งเงิน + ", "จัดทำใบสรุปส่งเงิน")
content = content.replace("ตรวจนับเงิน + สแกน QR +  ให้ตรงใบสรุป", "ตรวจนับเงินให้ตรงใบสรุป") # Handle previous replacement side-effect
content = content.replace("ตรวจนับเงิน + สแกน QR + บัตรฟรี ให้ตรงใบสรุป", "ตรวจนับเงินให้ตรงใบสรุป")
content = content.replace("ตรวจนับเงิน +  ให้ตรงใบสรุป", "ตรวจนับเงินให้ตรงใบสรุป")

# 5. Remove sC1 from JS data
import re
content = re.sub(r"sC1: \{.*?\},", "", content, flags=re.DOTALL)

# 6. Update formula text in stepData aD3
content = content.replace("รายได้ที่ควรได้รับ = (รถออกจากตัวนับ − รถค้างจอดเมื่อวาน) × อัตราค่าบริการ", "รายได้ที่ควรได้รับ = (รถออกจากตัวนับ − รถค้างจอดเมื่อวาน) × อัตราค่าบริการ")
# Wait, formula text might still have บัตรจอดรถฟรี
content = content.replace("− บัตรจอดรถฟรี −", "−")
content = content.replace("−  −", "−")
content = content.replace("③ จำนวน", "③") # cleanup

# 7. Update Risk Table R2 formula
content = content.replace("ไม่รวมสแกน QR และบัตรฟรีที่เกิดขึ้นในช่วงนั้น", "ไม่รวมรถค้างจอดที่เกิดขึ้น")
content = content.replace("หักจำนวนสแกน QR และบัตรฟรีในช่วงเวลานั้น", "หักจำนวนรถค้างจอด")
content = content.replace("− สแกน QR − บัตรฟรี −", "−")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

# Update index.html
index_path = "departments/parking_restroom/ycparking/index.html"
with open(index_path, "r", encoding="utf-8") as f:
    index_content = f.read()

index_content = index_content.replace('<span class="proc-step-tag">รับบัตรฟรี</span>', '')
with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_content)

print("Cleanup Case C successful.")
