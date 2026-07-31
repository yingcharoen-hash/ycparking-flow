import os

css_path = 'D:/Company_Workflows/temp_css.txt'
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

html_content = f"""<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>กระบวนการจัดเก็บรายได้ที่จอดรถยนต์ (ลาน 2, 3)</title>
<link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>
{css_content}
</style>
</head>
<body>

<!-- HEADER -->
<div class="header">
  <div style="position:absolute; top:24px; right:40px; display:flex; gap:10px; z-index:10;" class="nav-links">
    <a href="../../../index.html" style="background:rgba(255,255,255,.15); border:1px solid rgba(255,255,255,.3); color:#fff; text-decoration:none; padding:8px 16px; border-radius:8px; font-size:12px; font-weight:700; transition:all .2s; display:flex; align-items:center; gap:6px;">🏢 หน้าหลักบริษัท</a>
    <a href="index.html" style="background:rgba(255,255,255,.15); border:1px solid rgba(255,255,255,.3); color:#fff; text-decoration:none; padding:8px 16px; border-radius:8px; font-size:12px; font-weight:700; transition:all .2s; display:flex; align-items:center; gap:6px;">🏠 กลับหน้าหลักแผนก</a>
    <a href="workflow_swimlane_tabs.html" style="background:rgba(255,255,255,.15); border:1px solid rgba(255,255,255,.3); color:#fff; text-decoration:none; padding:8px 16px; border-radius:8px; font-size:12px; font-weight:700; transition:all .2s; display:flex; align-items:center; gap:6px;">📊 ผังกระบวนการ 1–8</a>
    <button onclick="window.print()" style="background:#fff; color:#1d1d1f; border:none; padding:8px 16px; border-radius:8px; font-weight:700; cursor:pointer; font-size:12px; display:flex; align-items:center; gap:6px;">🖨️ พิมพ์รายงาน</button>
  </div>
  <div class="header-inner">
    <div class="header-badge">กระบวนการจัดเก็บรายได้ · เอกสารตรวจสอบภายใน</div>
    <div class="header-title">จัดเก็บรายได้ค่าบริการ<em>ที่จอดรถยนต์ (ลาน 2, 3)</em></div>
    <div class="header-meta">
      <div class="meta-item"><span class="meta-label">หน่วยงาน</span><span class="meta-value">แผนกบริหารที่จอดรถและห้องน้ำ</span></div>
      <div class="meta-item"><span class="meta-label">ระบบ</span><span class="meta-value">ระบบ CarPark</span></div>
      <div class="meta-item"><span class="meta-label">อัปเดตล่าสุด</span><span class="meta-value">มิถุนายน 2569</span></div>
      <div class="meta-item"><span class="meta-label">คลิกที่ขั้นตอน</span><span class="meta-value">เพื่อดูรายละเอียด →</span></div>
    </div>
  </div>
</div>

<!-- PAGE BODY -->
<div class="page" id="page">

  <!-- ===== SWIMLANE ===== -->
  <div class="swimlane-col" id="sl-col">
    <div class="sl-wrap">
      <table class="sl-table">

        <!-- Header row -->
        <tr>
          <td class="lane-lbl hdr">ผู้รับผิดชอบ</td>
          <td class="sl-steps" style="background:var(--gray50);padding:10px 16px;">
            <span style="font-size:10.5px;font-weight:800;color:var(--gray600);text-transform:uppercase;letter-spacing:.6px;">ขั้นตอน — คลิกที่แต่ละขั้นตอนเพื่อดูรายละเอียด</span>
          </td>
        </tr>

        <!-- Row 1: Ops -->
        <tr>
          <td class="lane-lbl ops">ผู้ปฏิบัติงาน<br>ประจำจุด<br>(รถเข้า-ออก)</td>
          <td class="sl-steps">
            <div style="font-size:11px;font-weight:800;color:var(--gray600);margin-bottom:8px;">กระบวนการหน้างาน (รถเข้า-ออก)</div>
            <div style="display:flex;gap:10px;flex-wrap:wrap;">

              <!-- ขาเข้า -->
              <div class="case-box b">
                <div class="case-title">🔵 รถเข้า (ENTRY)</div>
                <div class="flow" style="flex-wrap:wrap;gap:4px;flex-direction:column;align-items:flex-start;">
                  <div class="flow-item">
                    <div class="step risk" onclick="showPanel('k1')">
                      <div class="step-num">ข-1</div>
                      <div class="step-text">บันทึกทะเบียน 4 หลัก<br>+ แจกบัตรแข็ง/กระดาษสีเขียว</div>
                      <span class="badge r">⚠ R2</span>
                    </div>
                  </div>
                  <div class="flow-item" style="margin-top:6px;">
                    <div class="step ctrl" onclick="showPanel('k2')">
                      <div class="step-num">ข-2</div>
                      <div class="step-text">รถสมาชิกรายเดือน (ตรวจสอบป้ายทะเบียน)</div>
                      <span class="badge c">✓</span>
                    </div>
                  </div>
                  <div class="flow-item" style="margin-top:6px;">
                    <div class="step ops" onclick="showPanel('k3')">
                      <div class="step-num">ข-3</div>
                      <div class="step-text">รถรัฐ / รถเร่ (ปล่อยเข้า)</div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- ขาออก -->
              <div class="case-box y">
                <div class="case-title">🟠 รถออก (EXIT)</div>
                <div class="flow" style="flex-wrap:wrap;gap:4px;flex-direction:column;align-items:flex-start;">
                  <div class="flow-item">
                    <div class="step risk" onclick="showPanel('o1')">
                      <div class="step-num">อ-1</div>
                      <div class="step-text">คิดเงินรถทั่วไป/สมาชิก<br>(เงินสด / สแกน QR)</div>
                      <span class="badge r">⚠ R5</span>
                    </div>
                  </div>
                  <div class="flow-item" style="margin-top:6px;">
                    <div class="step ops" onclick="showPanel('o2')">
                      <div class="step-num">อ-2</div>
                      <div class="step-text">ปล่อยรถรัฐ / รถเร่ ออก</div>
                    </div>
                  </div>
                  <div class="flow-item" style="margin-top:6px;">
                    <div class="step hr-card" onclick="showPanel('o3')">
                      <div class="step-num">อ-3</div>
                      <div class="step-text">บัตรหาย (เก็บค่าปรับ 300)</div>
                    </div>
                  </div>
                </div>
              </div>

            </div>

            <!-- สิ้นรอบ -->
            <div style="margin-top:12px;padding-top:10px;border-top:1.5px dashed var(--gray200);">
              <div style="font-size:11px;font-weight:800;color:var(--gray600);margin-bottom:8px;">สิ้นรอบทำงาน (End of Shift)</div>
              <div class="flow" style="flex-wrap:wrap;gap:4px;">
                <div class="flow-item">
                  <div class="step hr-card" onclick="showPanel('s1')">
                    <div class="step-num">ส-1</div>
                    <div class="step-text">สรุปยอดรายรอบและส่งมอบเอกสาร</div>
                    <span class="badge w">⚠ R3</span>
                  </div>
                </div>
              </div>
            </div>
          </td>
        </tr>

        <!-- Row 2: Finance -->
        <tr>
          <td class="lane-lbl fin-recv">ส่วนงานรับเงิน<br>(การเงิน)</td>
          <td class="sl-steps">
            <div class="flow" style="flex-wrap:wrap;gap:4px;">
              <div class="flow-item">
                <div class="step fin" onclick="showPanel('f1')">
                  <div class="step-num">ง-1</div>
                  <div class="step-text">ตรวจนับเงินสดเทียบใบสรุปมือ<br>&amp; บันทึก Kassone</div>
                  <span class="badge r">⚠ R1</span>
                </div>
              </div>
              <div class="flow-item" style="margin-left:16px;">
                <div class="step ctrl" onclick="showPanel('f2')">
                  <div class="step-num">ง-2</div>
                  <div class="step-text">การเงินสุ่มตรวจหน้างาน<br>(ระหว่างวัน)</div>
                  <span class="badge c">✓</span>
                </div>
              </div>
            </div>
            <div class="risk-callout" style="margin-top:12px;">
              <span class="rc-icon">⚠️</span>
              <div>
                <div class="rc-text">ความเสี่ยงทางระบบ (Systemic gap): การเงินตรวจรับเงินจากเอกสารเขียนมือเท่านั้น</div>
                <div class="rc-sub">ระบบออกใบเสร็จให้ลูกค้าใบเดียว ไม่มีสำเนาให้การเงิน ทำให้บันทึกรายได้แบบ Blind Trust</div>
              </div>
            </div>
          </td>
        </tr>

        <!-- Row 3: Head -->
        <tr>
          <td class="lane-lbl night">หัวหน้า<br>คาร์ปาร์ค<br><span style="font-size:9px;opacity:.7;font-weight:400;">หลังเงินเข้าแบงก์</span></td>
          <td class="sl-steps">
            <div class="flow" style="flex-wrap:wrap;gap:4px;">
              <div class="flow-item">
                <div class="step risk" onclick="showPanel('h1')">
                  <div class="step-num">ห-1</div>
                  <div class="step-text">ดึงรายงานระบบ ทวนสอบและปรับยอด (Adjust)</div>
                  <span class="badge r">⚠ R4</span>
                </div>
              </div>
            </div>
            <div class="risk-callout" style="margin-top:12px;">
              <span class="rc-icon">⚠️</span>
              <div>
                <div class="rc-text">จุดเสี่ยงวิกฤต: ช่องโหว่จากการทวนสอบย้อนหลัง</div>
                <div class="rc-sub">หัวหน้ามีอำนาจ Adjust ปรับลดตัวเลขในระบบให้ตรงกับเงินที่ส่งไปแล้วได้ โดยไม่ถูกบังคับให้ทำบันทึกชี้แจง</div>
              </div>
            </div>
          </td>
        </tr>

        <!-- Row 4: Audit -->
        <tr>
          <td class="lane-lbl audit">ผู้ตรวจสอบ<br>ภายใน<br>(Internal Audit)</td>
          <td class="sl-steps audit-bg">
            <div style="display:flex;gap:12px;flex-wrap:wrap;">
              <div>
                <div style="font-size:10.5px;font-weight:800;color:var(--purple);margin-bottom:6px;">🎲 การสุ่มตรวจระบบ (System Audit)</div>
                <div class="flow" style="gap:4px;flex-wrap:wrap;">
                  <div class="flow-item">
                    <div class="step ctrl" onclick="showPanel('a1')">
                      <div class="step-num">ออดิท-1</div>
                      <div class="step-text">สุ่มตรวจ Log การ Adjust ย้อนหลัง</div>
                      <span class="badge c">✓</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </td>
        </tr>

      </table>
    </div>
    
    <!-- ===== RISK TABLE (BELOW) ===== -->
    <div class="risk-section" style="margin-top:40px; padding:0;">
      <div class="risk-section-title">
        <span class="risk-badge-hd">⚠ การวิเคราะห์ความเสี่ยง</span>
        จุดเสี่ยงที่ระบุได้จากกระบวนการจริง (อิงตามข้อมูลข้อจำกัดของระบบจอดรถยนต์ ลาน 2-3)
      </div>

      <table class="risk-tbl">
        <thead>
          <tr>
            <th style="width:5%">รหัส</th>
            <th style="width:25%">ประเด็นความเสี่ยง</th>
            <th style="width:30%">ผลกระทบ (Impact)</th>
            <th style="width:10%">ระดับ</th>
            <th>แนวทางควบคุม (สำหรับ Internal Audit)</th>
          </tr>
        </thead>
        <tbody>
          <tr style="background:#fff8f8;">
            <td style="font-weight:800;color:var(--red);">R1</td>
            <td><strong style="color:var(--red);">การรับรู้รายได้โดยไร้การตรวจสอบ (Blind Revenue)</strong><div style="font-size:11px;color:var(--gray400);margin-top:2px;">ง-1 | Control: ง-2</div></td>
            <td>การเงินรับเงินและบันทึกเข้า Kassone จาก "ใบสรุปเขียนมือ" เท่านั้น ไม่มีรายงานจากระบบมาประกบตั้งแต่ต้นทาง</td>
            <td><span class="rl v">วิกฤต</span></td>
            <td>• การเงินลงพื้นที่สุ่มนับเงินสดในเก๊ะเทียบกับใบสรุปรายรอบ ณ เวลานั้น</td>
          </tr>
          <tr>
            <td style="font-weight:800;color:var(--red);">R2</td>
            <td><strong>ธุรกรรมนอกระบบ (Off-system) จากบัตรสีเขียว</strong><div style="font-size:11px;color:var(--gray400);margin-top:2px;">ข-1 | Control: ง-2</div></td>
            <td>บัตรสีเขียวไม่มีการคีย์เข้าระบบใดๆ การคิดเงินเกิดจากการหักลบด้วยมือ เสี่ยงต่อการตกหล่นของรายได้ และ Audit ตรวจสอบย้อนหลังจากระบบไม่ได้เลย</td>
            <td><span class="rl h">สูง</span></td>
            <td>• การเงินสุ่มตรวจการใช้บัตรกระดาษสีเขียวหน้างานว่ามีการจดบันทึกหรือไม่</td>
          </tr>
          <tr>
            <td style="font-weight:800;color:var(--orange);">R3</td>
            <td><strong>การนำบัตรฟรีมาวนซ้ำ</strong><div style="font-size:11px;color:var(--gray400);margin-top:2px;">ส-1 | Audit: ออดิท-1</div></td>
            <td>บัตรจอดรถฟรีหากไม่มีการเขียนวันที่หรือทำตำหนิ สามารถนำมาใช้อ้างอิงซ้ำเพื่อ Adjust ยอดเงินในระบบได้</td>
            <td><span class="rl m">กลาง</span></td>
            <td>• ตรวจความถูกต้องของบัตรฟรี ว่ามีการเซ็น/ลงวันที่ป้องกันการใช้ซ้ำ</td>
          </tr>
          <tr style="background:#fff8f8;">
            <td style="font-weight:800;color:var(--red);">R4</td>
            <td><strong style="color:var(--red);">ความเสี่ยงเรื่องการตรวจสอบหลังบ้าน (Post-verification)</strong><div style="font-size:11px;color:var(--gray400);margin-top:2px;">ห-1 | Audit: ออดิท-1</div></td>
            <td>กระบวนการตรวจของหัวหน้าคาร์ปาร์คเกิดขึ้น "หลังจาก" เงินฝากธนาคารไปแล้ว และหากยอดไม่ตรง หัวหน้าสามารถ Adjust ตัวเลขในระบบให้ลดลงจนตรงกับเงินที่ได้ โดยไม่มีบันทึกชี้แจง เป็นช่องโหว่ร้ายแรง</td>
            <td><span class="rl v">วิกฤต</span></td>
            <td>• ดึง Log การ Adjust ยอดจากระบบมาตรวจสอบย้อนหลังเทียบกับบัตรจอดฟรี</td>
          </tr>
          <tr>
            <td style="font-weight:800;color:var(--orange);">R5</td>
            <td><strong>สลิปปลอม (QR PromptPay)</strong><div style="font-size:11px;color:var(--gray400);margin-top:2px;">อ-1</div></td>
            <td>พนักงานต้องส่งรูปเข้ากลุ่มไลน์เหมือนมอเตอร์ไซค์ ลาน 3 ทำให้ไม่มีหน้าจอเช็คเงินเข้าแบบ Real-time เสี่ยงรับสลิปปลอม</td>
            <td><span class="rl m">กลาง</span></td>
            <td>• สุ่มทวนสอบสลิปในกลุ่มไลน์ว่ายอดเข้าบัญชีจริง</td>
          </tr>
        </tbody>
      </table>
    </div>

  </div>

  <!-- ===== DETAIL PANEL ===== -->
  <div class="panel-col" id="panel-col">
    <div class="panel" id="detail-panel">
      <div class="panel-head">
        <div class="panel-head-left">
          <div class="panel-step-id" id="p-id">—</div>
          <div class="panel-title" id="p-title">เลือกขั้นตอนเพื่อดูรายละเอียด</div>
        </div>
        <button class="panel-close" onclick="closePanel()">×</button>
      </div>
      <div class="panel-body" id="p-body">
        <div style="color:#86868b;font-size:13px;text-align:center;padding:40px 20px;">คลิกที่การ์ดขั้นตอนในแผนภาพด้านซ้าย<br>เพื่อดูรายละเอียดการปฏิบัติงาน</div>
      </div>
    </div>
  </div>

</div>

<script>
const roleColors = {{
  'พนักงานคาร์ปาร์ค': '#0071e3',
  'ส่วนงานรับเงิน': '#af52de',
  'หัวหน้าคาร์ปาร์ค': '#ff9500',
  'Internal Audit': '#5ac8fa'
}};

const steps = {{
  k1: {{ id:'ข-1', title:'บันทึกทะเบียน + แจกบัตร', resp:['พนักงานคาร์ปาร์ค'], freq:'ทุกครั้งที่รถเข้า',
         tasks:['บันทึกทะเบียนรถ 4 หลักเข้าระบบ (บันทึกหมวดอักษรเฉพาะเมื่อทะเบียนซ้ำกับรถในลาน)','ส่งบัตรจอดรถ (บัตรแข็ง) ให้ลูกค้า','กรณีบัตรแข็งหมด: ให้แจกบัตรกระดาษอ่อนสีเขียวแทน โดยเขียนเวลาเข้าด้วยมือ'],
         docs:['🎟️ บัตรจอดรถแข็ง / บัตรกระดาษสีเขียว'],
         warn:'จุดเสี่ยง R2: บัตรสีเขียวไม่ถูกบันทึกเข้าระบบ เป็นการทำงานนอกระบบ (Off-system) 100%' }},
  
  k2: {{ id:'ข-2', title:'ตรวจสอบรถสมาชิกรายเดือน', resp:['พนักงานคาร์ปาร์ค'], freq:'ทุกครั้งที่รถเข้า',
         tasks:['รับบัตรจากลูกค้าเพื่อตรวจสอบในระบบ','ดูข้อมูลในระบบว่าบัตรใบนี้ผูกไว้กี่ทะเบียน','เลือกทะเบียนในระบบให้ตรงกับรถคันที่เข้ามาจริง','คืนบัตรให้ลูกค้าสมาชิก'] }},
  
  k3: {{ id:'ข-3', title:'รถหน่วยงานรัฐ / รถเร่', resp:['พนักงานคาร์ปาร์ค'], freq:'ทุกครั้งที่รถเข้า',
         tasks:['อนุญาตให้รถเข้าลานจอดได้เลย ไม่ต้องแจกบัตรจอดรถ','รถรัฐและรถเร่ ปล่อยเข้าได้ตลอด','รถติดต่องานพิเศษ ให้เข้าตามที่ได้รับแจ้งจากหัวหน้า'] }},
  
  o1: {{ id:'อ-1', title:'คิดเงินรถทั่วไป / สมาชิก', resp:['พนักงานคาร์ปาร์ค'], freq:'ทุกครั้งที่รถออก',
         tasks:['รับบัตรคืน ตรวจสอบเวลาจอดกับระบบ (หรือคำนวณด้วยมือจากบัตรสีเขียว)','หากจอดเกินเวลา: แจ้งลูกค้าคิดค่าบริการส่วนเกิน','รับชำระด้วยเงินสด หรือ สแกน QR (ถ่ายรูปสลิปลงกลุ่มไลน์การเงิน)','ออกใบเสร็จรับเงินให้ลูกค้า 1 ใบ (ไม่มีสำเนา)','กรณีมี "บัตรจอดรถฟรี" แนบมา: ให้ยกเว้นค่าบริการส่วนเกิน'],
         docs:['🧾 ใบเสร็จรับเงินระบบคาร์ปาร์ค'],
         warn:'จุดเสี่ยง R5: สแกน QR ตรวจสอบจากกลุ่มไลน์ เสี่ยงได้รับสลิปปลอม' }},
  
  o2: {{ id:'อ-2', title:'ปล่อยรถรัฐ / รถเร่ ออก', resp:['พนักงานคาร์ปาร์ค'], freq:'ทุกครั้งที่รถออก',
         tasks:['ให้ออกได้ตามปกติ ไม่ต้องมีการตรวจบัตรหรือเก็บเงิน'] }},
  
  o3: {{ id:'อ-3', title:'กรณีลูกค้าทำบัตรหาย', resp:['พนักงานคาร์ปาร์ค'], freq:'เมื่อเกิดเหตุ',
         tasks:['ลูกค้าแจ้งทำบัตรแข็งหาย','เก็บค่าปรับ 300 บาท ออกใบเสร็จรับเงิน และให้ลูกค้าออกจากลานจอดได้','เมื่อลูกค้าเจอบัตรภายหลัง ให้นำบัตรมาติดต่อรับเงินคืนที่สำนักงานคาร์ปาร์ค','ทำบันทึกแนบเพื่อส่งให้หัวหน้าตอนสิ้นรอบ (ห-1)','(หมายเหตุ: กรณีบัตรอ่อนหาย รอยืนยันขั้นตอนกับผู้ปฏิบัติงานอีกครั้ง)'],
         docs:['🧾 ใบเสร็จรับเงิน', '📄 บันทึกแจ้งบัตรหาย'] }},
  
  s1: {{ id:'ส-1', title:'สรุปยอดรายรอบและเตรียมส่งมอบ', resp:['พนักงานคาร์ปาร์ค'], freq:'สิ้นรอบทำงาน',
         tasks:['รวบรวมเงินสดและสลิปโอนเงินทั้งหมด','รวบรวมบัตรจอดรถฟรี และ บัตรกระดาษสีเขียวทั้งหมด','เขียนสรุปยอดใส่ "ใบสรุปส่งเงิน"','นำส่งเงินสดให้ส่วนงานรับเงิน และส่งเอกสารทั้งหมดให้หัวหน้าคาร์ปาร์ค'],
         docs:['📄 ใบสรุปส่งเงินเขียนมือ','🎫 บัตรจอดรถฟรี / บัตรกระดาษสีเขียว'],
         warn:'จุดเสี่ยง R3: หากบัตรจอดรถฟรีไม่มีการลงวันที่หรือทำเครื่องหมาย อาจถูกนำกลับมาวนใช้เป็นข้ออ้าง Adjust ยอดเงินภายหลัง' }},
  
  f1: {{ id:'ง-1', title:'นับเงินสดเทียบใบสรุป & เข้า Kassone', resp:['ส่วนงานรับเงิน'], freq:'รายวัน',
         tasks:['รับเงินสด ตรวจนับให้ตรงกับยอดในใบสรุปที่พนักงานเขียนมา','บันทึกรายได้ลงระบบ Kassone','ผจก.การเงิน รวบรวมเงินรายได้ทั้งหมดนำฝากเข้าธนาคาร'],
         warn:'จุดเสี่ยง R1: การเงินรับรู้รายได้ (Revenue Recognition) จากตัวเลขที่พนักงานเขียนด้วยมือ ไม่มีรายงานจากระบบคาร์ปาร์คมายืนยัน (Blind Trust)' }},
  
  h1: {{ id:'ห-1', title:'ทวนสอบรายงานและปรับยอด (Adjust)', resp:['หัวหน้าคาร์ปาร์ค'], freq:'หลังสิ้นรอบการทำงาน (รายวัน)',
         tasks:['รับเอกสารใบสรุปยอด, บัตรจอดฟรี และ บันทึกบัตรหาย จากพนักงาน','เข้าดึงรายงานจากระบบหลังบ้านของคาร์ปาร์ค','ตรวจทานรายการรถเข้า-ออก (เกิดหลังเงินเข้า Kassone ไปแล้ว)','ทำรายการปรับยอด (Adjust) ยกเว้นค่าบริการสำหรับคันที่มีบัตรจอดรถฟรี (ระบบไม่อ่านบัตรฟรีอัตโนมัติ)','หากยอดไม่ตรง: เรียกพนักงานมาชี้แจง (ไม่มีการทำบันทึก Memo ชี้แจงในระบบ)'],
         docs:['📊 รายงานระบบคาร์ปาร์ค'],
         warn:'จุดเสี่ยงวิกฤต R4: กระบวนการนี้เปิดช่องโหว่ให้หัวหน้า Adjust ยอดในระบบให้ลดลงมาตรงกับเงินสดได้โดยไม่มีคนตรวจสอบความโปร่งใส (Manipulation)' }},
  
  a1: {{ id:'ออดิท-1', title:'สุ่มตรวจหน้างาน (Physical Audit)', resp:['Internal Audit'], freq:'สุ่มตรวจไม่แจ้งล่วงหน้า',
         tasks:['ลงพื้นที่สุ่มตรวจ ณ เวลาทำการ (Surprise Check)','นับเงินสดในลิ้นชักเทียบกับใบสรุปที่พนักงานจดไว้ (สกัดความเสี่ยง R1)','ตรวจสอบการใช้งาน "บัตรกระดาษสีเขียว" ว่ามีการจดบันทึกถูกต้องและคิดเงินถูกหรือไม่ (สกัดความเสี่ยง R2)'] }},
  
  a2: {{ id:'ออดิท-2', title:'สุ่มตรวจรายการ Adjust ย้อนหลัง', resp:['Internal Audit'], freq:'ตามรอบการตรวจ',
         tasks:['ดึง System Log หรือรายงานการ Adjust ยอดจากระบบคาร์ปาร์ค','คัดกรองรายการที่มีการ Adjust ยกเว้นค่าบริการ','นำรายการไปสุ่มตรวจสอบเทียบกับหลักฐาน "บัตรจอดรถฟรี" ของจริงที่เก็บไว้','ตรวจสอบว่าบัตรฟรีมีลายเซ็น/วันที่ ป้องกันการวนใช้ซ้ำ (สกัดความเสี่ยง R3, R4)'] }}
}};

let currentStep = null;

function showPanel(id) {{
  const data = steps[id];
  if (!data) return;

  document.querySelectorAll('.step').forEach(s => s.classList.remove('active'));
  event.currentTarget.classList.add('active');
  currentStep = id;

  document.getElementById('p-id').textContent = data.id;
  document.getElementById('p-title').textContent = data.title;

  let html = '';

  html += `<div class="panel-section">
    <div class="panel-section-title">📝 รายละเอียดการปฏิบัติงาน</div>
    <div class="task-list">`;
  data.tasks.forEach(t => {{
    html += `<div class="task-item"><div class="task-dot"></div><div class="task-text">${{t}}</div></div>`;
  }});
  html += `</div></div>`;

  if (data.docs && data.docs.length) {{
    html += `<div class="panel-section">
      <div class="panel-section-title">📂 เอกสารที่เกี่ยวข้อง</div>
      <div class="doc-list">`;
    data.docs.forEach(d => {{
      html += `<div class="doc-item">${{d}}</div>`;
    }});
    html += `</div></div>`;
  }}

  if (data.warn) {{
    html += `<div class="panel-section">
      <div class="warning-box">
        <div class="warning-title">⚠️ จุดเสี่ยง / ช่องโหว่ระบบ</div>
        <div class="warning-text">${{data.warn}}</div>
      </div>
    </div>`;
  }}

  if (data.resp && data.resp.length) {{
    html += `<div class="panel-section">
      <div class="panel-section-title">👤 ผู้รับผิดชอบ</div>
      <div class="resp-list">`;
    data.resp.forEach(r => {{
      const color = roleColors[r] || '#5a6478';
      html += `<div class="resp-item"><div class="resp-dot" style="background:${{color}}"></div>${{r}}</div>`;
    }});
    html += `</div></div>`;
  }}

  if (data.freq) {{
    html += `<div class="panel-section">
      <div class="panel-section-title">🕒 ความถี่</div>
      <div class="freq-tag">🕒 ${{data.freq}}</div>
    </div>`;
  }}

  document.getElementById('p-body').innerHTML = html;

  document.getElementById('panel-col').classList.add('open');
  document.getElementById('sl-col').classList.add('has-panel');
}}

function closePanel() {{
  document.getElementById('panel-col').classList.remove('open');
  document.getElementById('sl-col').classList.remove('has-panel');
  document.querySelectorAll('.step').forEach(s => s.classList.remove('active'));
  currentStep = null;
}}
</script>

</body>
</html>
"""

out_path = 'D:/Company_Workflows/departments/parking_restroom/ycparking/tab3_car.html'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Generated tab3_car.html with proper Apple Look classes successfully.')
