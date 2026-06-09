import re

with open("departments/parking_restroom/ycparking/index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Shift 8 to 9
content = content.replace("กระบวนการทั้งหมด 8 กระบวนการ", "กระบวนการทั้งหมด 9 กระบวนการ")
content = content.replace("กระบวนการหลัก</span><span class=\"meta-value\">8 กระบวนการ", "กระบวนการหลัก</span><span class=\"meta-value\">9 กระบวนการ")
content = content.replace("ผังกระบวนการ 1–8", "ผังกระบวนการ 1–9")

content = content.replace("กระบวนการที่ 8</div>", "กระบวนการที่ 9</div>")
content = content.replace("กระบวนการที่ 7</div>", "กระบวนการที่ 8</div>")
content = content.replace("กระบวนการที่ 6</div>", "กระบวนการที่ 7</div>")

# Adjust the stats row
content = re.sub(r'<div class="stat-num">8</div>', '<div class="stat-num">9</div>', content)

# Create the new card for กระบวนการที่ 6 (Lot 3)
new_card = """
    <a class="proc-card" href="tab6_motorcycle_lot3.html">
      <div class="proc-card-top">
        <div class="proc-num">กระบวนการที่ 6</div>
        <div class="proc-icon-row">
          <div class="proc-icon" style="background:#eef2f7;">🏍️</div>
          <div>
            <div class="proc-title">จัดเก็บรายได้ที่จอดรถจักรยานยนต์ (ลาน 3)</div>
            <div class="proc-sub">Motorcycle Parking Lot 3 · เครื่องนับรถ</div>
          </div>
        </div>
      </div>
      <div class="proc-card-body">
        <div class="proc-steps">
          <span class="proc-step-tag">เครื่องนับรถ</span>
          <span class="proc-step-tag">เก็บเงินปกติ</span>
          <span class="proc-step-tag">รับบัตรฟรี</span>
          <span class="proc-step-tag">ส่งการเงิน</span>
          <span class="proc-step-tag">Audit</span>
        </div>
        <div class="proc-footer">
          <div class="proc-badges"><span class="risk-chip r">🔴 วิกฤต 1 + สูง 3</span><span class="risk-chip g">✓ 6 Lane</span></div>
          <span class="proc-link">ดูผัง →</span>
        </div>
      </div>
    </a>
"""

# Find where to insert (right after the กระบวนการที่ 5 card)
card5_end = content.find('</a>\n\n    <a class="proc-card" href="workflow_swimlane_tabs.html?tab=5">')
if card5_end != -1:
    content = content[:card5_end + 4] + "\n" + new_card + content[card5_end + 4:]

with open("departments/parking_restroom/ycparking/index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated index.html successfully.")
