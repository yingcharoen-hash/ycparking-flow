import os

filepath = "departments/parking_restroom/ycparking/tab6_motorcycle_lot3.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Block 1: กรณี ข
case_b = """              <!-- กรณี ข -->
              <div class="case-box b">
                <div class="case-title">🟩 กรณี ข — บุคลากรตลาด (≤30 ครั้ง/เดือน)</div>
                <div class="flow" style="flex-wrap:wrap;gap:4px;">
                  <div class="flow-item">
                    <div class="step ops" onclick="showPanel('sB1')">
                      <div class="step-num">ข-1</div>
                      <div class="step-text">สแกน QR บุคลากร ผ่าน YC Parking App</div>
                    </div>
                  </div>
                  <span class="arr">→</span>
                  <div class="flow-item">
                    <div class="step ctrl" onclick="showPanel('sB2')">
                      <div class="step-num">ข-2</div>
                      <div class="step-text">ระบบหักโควต้า บันทึก Log</div>
                      <span class="badge c">✓</span>
                    </div>
                  </div>
                </div>
                <div class="strip y">⚠ สิทธิ์หมด → ไปกรณี ก</div>
                <div class="strip r">🔴 ระบบล่ม → จดชื่อ+รหัส ยกเว้นชั่วคราว รายงาน HR ทันที</div>
              </div>"""

content = content.replace(case_b, "")

# Block 2: HR Row
hr_row = """        <!-- Row 3: HR -->
        <tr>
          <td class="lane-lbl hr">ฝ่ายบุคคล<br>(HR)<br><span style="font-size:9px;opacity:.7;font-weight:400;">กรณีระบบล่ม</span></td>
          <td class="sl-steps hr-bg">
            <div class="flow" style="flex-wrap:wrap;gap:4px;">
              <div class="flow-item">
                <div class="step hr-card" onclick="showPanel('sHR1')">
                  <div class="step-num">HR-1</div>
                  <div class="step-text">รับรายงาน ตรวจสอบรายชื่อบุคลากร</div>
                </div>
              </div>
              <span class="arr">→</span>
              <div class="flow-item">
                <div class="step ctrl" onclick="showPanel('sHR2')">
                  <div class="step-num">HR-2</div>
                  <div class="step-text">ปรับหักโควต้าย้อนหลัง เมื่อระบบกลับมา</div>
                  <span class="badge c">✓ ปิด Loop</span>
                </div>
              </div>
            </div>
          </td>
        </tr>"""

content = content.replace(hr_row, "")

# Block 3: Risks R5, R6, R7
risks_b = """      <tr>
        <td style="font-weight:800;color:var(--red);">R5</td>
        <td><strong>QR Code บุคลากรถูกใช้แทนกัน</strong><div style="font-size:11px;color:var(--gray400);margin-top:2px;">ข-1 | Audit: สน-4, ดน-2</div></td>
        <td>ไม่มีการจำกัดครั้งต่อวัน บุคลากรอาจแชร์ QR หรือสแกนหลายครั้งต่อวันได้โดยไม่ผิดเงื่อนไข</td>
        <td><span class="rl h">สูง</span></td>
        <td>• ตรวจ Log รายบุคคลทุกสัปดาห์ (สน-4) สแกนเกิน 2 ครั้ง/วัน เรียกชี้แจง<br>• ต้องเห็นหน้าบุคลากรพร้อม QR ทุกครั้ง<br>• พิจารณากำหนดจำกัด 1–2 ครั้ง/วัน/คนในระบบ</td>
      </tr>
      <tr>
        <td style="font-weight:800;color:var(--orange);">R6</td>
        <td><strong>สิทธิ์บุคลากรหมด — ไม่มีขั้นตอนรองรับ</strong><div style="font-size:11px;color:var(--gray400);margin-top:2px;">ข-1</div></td>
        <td>สแกนไม่ผ่าน แต่ยังไม่มีขั้นตอนชัดเจน อาจยกเว้นค่าบริการโดยไม่มีหลักฐาน</td>
        <td><span class="rl m">กลาง</span></td>
        <td>• สแกนไม่ผ่าน → เก็บเงินปกติ (กรณี ก) ตามที่กำหนดใน Flow แล้ว<br>• ระบบควรแสดงข้อความ "สิทธิ์หมด" ให้เจ้าหน้าที่เห็น</td>
      </tr>
      <tr>
        <td style="font-weight:800;color:var(--orange);">R7</td>
        <td><strong>ระบบ YC Parking หยุดทำงาน</strong><div style="font-size:11px;color:var(--gray400);margin-top:2px;">ข-1 / ข-2 | HR-2</div></td>
        <td>ยกเว้นเงินชั่วคราวได้ตาม SOP แต่หากไม่ Reconcile ย้อนหลัง จะทำให้ยอดรายได้ขาดหาย</td>
        <td><span class="rl m">กลาง</span></td>
        <td>• HR ปรับหักโควต้าย้อนหลังให้ครบเมื่อระบบกลับมา (HR-2)<br>• Audit ตรวจสอบว่าครบทุกรายในรอบสัปดาห์ (สน-4)</td>
      </tr>"""

content = content.replace(risks_b, "")

# Block 4: Rename R8 to R5
content = content.replace('<td style="font-weight:800;color:var(--orange);">R8</td>', '<td style="font-weight:800;color:var(--orange);">R5</td>')

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Cleanup successful.")
