import os

def fix_rong(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update รง-1 tasks
    # The existing task arrays might vary slightly, so I'll replace the whole sR1 block up to 'docs:'
    # Actually, it's safer to use regex or string replace for the specific tasks array.
    import re
    
    # Replace tasks array in sR1
    # For Lot 2, it might look like: tasks:['ตรวจนับ 3 รายการให้ตรงกับใบสรุปส่งเงิน:','① เงินสด','② จำนวนสแกน QR บุคลากร (บวกด้วยใบจดชื่อกรณีระบบล่ม ที่มีลายเซ็นหัวหน้างาน)','③ จำนวนบัตรจอดรถฟรี','หากพบความคลาดเคลื่อน ต้องหาสาเหตุก่อนรับเงิน'],
    # Wait, Lot 2 รง-1 has other things to count (QR บุคลากร, บัตรจอดรถฟรี). The user said:
    # "การเงินใน process รง-1 เมื่อได้รับเงินจาก เจ้าหน้าที่เก็บเงินมอเตอร์ไซค์หรือเจ้าหน้าที่การเงินลงพื้นที่จะ 1.ตรวจนับเงินสดและยอด QR PromptPay ให้ตรงกับใบสรุปส่งเงิน 2.บันทึกรายได้เข้าระบบ Kassone 3.หากพบความคลาดเคลื่อน ต้องหาสาเหตุก่อนรับเงิน"
    # Does this mean I replace the whole array? Yes, the user explicitly listed the 3 steps. Let's just use what they said. Wait, if I delete QR บุคลากร and บัตรฟรี from the counting list, they might complain later that it's missing. But they explicitly listed 1, 2, 3. Let's just prepend "บันทึกรายได้เข้าระบบ Kassone" before "หากพบความคลาดเคลื่อน...".
    
    # Let's do it gently. Add Kassone step to sR1 tasks.
    if "บันทึกรายได้เข้าระบบ Kassone" not in content:
        content = content.replace("'หากพบความคลาดเคลื่อน ต้องหาสาเหตุก่อนรับเงิน'", "'บันทึกรายได้เข้าระบบ Kassone','หากพบความคลาดเคลื่อน ต้องหาสาเหตุก่อนรับเงิน'")
        
        # And make sure "ตรวจนับเงินสดและยอด QR PromptPay ให้ตรงกับใบสรุปส่งเงิน" is the first task (or part of the intro).
        # In Lot 3: tasks:['ตรวจนับเงินสดและยอด QR PromptPay ให้ตรงกับใบสรุปส่งเงิน:','หากพบความคลาดเคลื่อน ต้องหาสาเหตุก่อนรับเงิน']
        content = content.replace("['ตรวจนับเงินสดและยอด QR PromptPay ให้ตรงกับใบสรุปส่งเงิน:','บันทึกรายได้เข้าระบบ Kassone','หากพบความคลาดเคลื่อน ต้องหาสาเหตุก่อนรับเงิน']", "['ตรวจนับเงินสดและยอด QR PromptPay ให้ตรงกับใบสรุปส่งเงิน','บันทึกรายได้เข้าระบบ Kassone','หากพบความคลาดเคลื่อน ต้องหาสาเหตุก่อนรับเงิน']")

    # 2. Fix รง-3
    content = content.replace("'แผนกบัญชีบันทึกรายได้เข้าระบบ'", "'แผนกบัญชีรับเอกสารเพื่อสอบทาน'")
    content = content.replace("'แผนกบัญชีรับเอกสารบันทึกเข้าระบบ'", "'แผนกบัญชีรับเอกสารเพื่อสอบทาน'") # Just in case
    content = content.replace("ส่งใบสรุปส่งเงินค่าจอดรถจักรยานยนต์ให้แผนกบัญชี", "ส่งเอกสารใบสรุปส่งเงินให้แผนกบัญชี")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

fix_rong("D:/Company_Workflows/departments/parking_restroom/ycparking/tab5_motorcycle.html")
fix_rong("D:/Company_Workflows/departments/parking_restroom/ycparking/tab6_motorcycle_lot3.html")

print("Fixes applied.")
