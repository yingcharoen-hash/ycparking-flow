import re

def set_sr1(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract the whole sR1 block and rebuild it to be safe
    # We will just replace everything between `tasks:['` and `],` in sR1
    # Actually, let's just do simple regex replacement
    pattern = r"(sR1:\s*\{.*?tasks:\[).*?(\],\s*docs:)"
    replacement = r"\g<1>'1. ตรวจนับเงินสดและยอด QR PromptPay ให้ตรงกับใบสรุปส่งเงิน', '2. บันทึกรายได้เข้าระบบ Kassone', '3. หากพบความคลาดเคลื่อน ต้องหาสาเหตุก่อนรับเงิน'\g<2>"
    
    # Wait, Lot 2 has other things in sR1 (บัตรจอดรถฟรี, QR บุคลากร). The user said:
    # "process รง-1 เมื่อได้รับเงินจาก เจ้าหน้าที่เก็บเงินมอเตอร์ไซค์หรือเจ้าหน้าที่การเงินลงพื้นที่จะ 1.ตรวจนับเงินสดและยอด QR PromptPay ให้ตรงกับใบสรุปส่งเงิน 2.บันทึกรายได้เข้าระบบ Kassone 3.หากพบความคลาดเคลื่อน ต้องหาสาเหตุก่อนรับเงิน"
    # The user gave EXACTLY 3 steps. Let's just use EXACTLY 3 steps for both Lot 2 and Lot 3, overriding any other items. If they want "บัตรฟรี" checked, they can add it later. They were very specific.
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

set_sr1("D:/Company_Workflows/departments/parking_restroom/ycparking/tab5_motorcycle.html")
set_sr1("D:/Company_Workflows/departments/parking_restroom/ycparking/tab6_motorcycle_lot3.html")
