import os

def fix_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Fix PromptPay
    # Swimlane step text
    content = content.replace("เก็บค่าบริการ<br>เงินสด / QR", "เก็บค่าบริการ<br>เงินสด / สแกน QR PromptPay")
    content = content.replace("เก็บค่าบริการ<br>เงินสด", "เก็บค่าบริการ<br>เงินสด / สแกน QR PromptPay") # in case Lot 3 was just 'เงินสด'

    # Formula updates
    content = content.replace("= เงินสด<br>", "= เงินสด + ยอดสแกน QR PromptPay<br>")
    
    # Step s4 and sR1 tasks
    content = content.replace("'รวบรวมเงินสดทั้งหมด'", "'รวบรวมเงินสดและสลิปสแกน QR PromptPay ทั้งหมด'")
    # in sR1
    content = content.replace("ตรวจนับเงินสดให้ตรงกับ", "ตรวจนับเงินสดและยอด QR PromptPay ให้ตรงกับ")
    content = content.replace("'① เงินสด','② จำนวนสแกน", "'① เงินสด','② ยอดสแกน QR PromptPay','③ จำนวนสแกน")
    # For Lot 3, it was 3 รายการ. Let's make it more generic.
    
    # 2. Fix กง-1
    content = content.replace("จดมิเตอร์เริ่ม กันเงินทอน 200 บ.", "จดบันทึกเลขมิเตอร์ทั้งเข้าและออก กันเงินทอน 200 บ.")
    
    # 3. Fix warn in s4 and sR1 matching R1
    # The string: warn:'ใบสรุปส่งเงินจัดทำโดยเจ้าหน้าที่เก็บเงินเอง ซึ่งเป็นจุดเสี่ยง R1 — การเงินต้องตรวจเทียบกับ YC Parking โดยตรง'
    content = content.replace("การเงินต้องตรวจเทียบกับ YC Parking โดยตรง", "การเงินต้องตรวจเทียบกับรายงานบันทึกมิเตอร์รถเข้า-ออกโดยตรง")
    # warn:'จุดเสี่ยง R1: ใบสรุปส่งเงินจัดทำโดยเจ้าหน้าที่เก็บเงินเอง การตรวจสอบที่แท้จริงต้องเทียบกับระบบเครื่องนับรถโดยตรง ไม่ใช่แค่เทียบกับใบสรุปที่ส่งมา'
    # Actually, in Lot 3 sR1 I already fixed it to "เครื่องนับรถโดยตรง". But in Lot 2 it might still say "YC Parking โดยตรง".
    content = content.replace("เทียบกับ YC Parking โดยตรง", "เทียบกับรายงานบันทึกมิเตอร์รถเข้า-ออกโดยตรง")

    # Double check s4
    content = content.replace("จุดเสี่ยง R1 — การเงินต้องตรวจเทียบกับรายงานบันทึกมิเตอร์รถเข้า-ออกโดยตรง", "จุดเสี่ยง R1 — ต้องตรวจเทียบกับรายงานบันทึกมิเตอร์รถเข้า-ออกโดยตรง")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

fix_file("D:/Company_Workflows/departments/parking_restroom/ycparking/tab5_motorcycle.html")
fix_file("D:/Company_Workflows/departments/parking_restroom/ycparking/tab6_motorcycle_lot3.html")

print("Detailed fixes applied.")
