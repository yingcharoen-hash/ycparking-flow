import os

def fix_remaining(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # sA1 task
    content = content.replace("รับได้ทั้งเงินสด / เงินโอน / สแกน QR PromptPay", "รับได้ทั้งเงินสดและสแกน QR PromptPay")
    
    # sR2 task
    content = content.replace("Bank Statement เป็นหลักฐานยืนยันยอดเงินโอนได้อิสระ", "Bank Statement เป็นหลักฐานยืนยันยอดเงินสแกน QR PromptPay ได้อิสระ")
    
    # aD2 task (mostly Lot 3, but safe to apply to both)
    content = content.replace("ยอดเงินสด + เงินโอน", "ยอดเงินสดและยอดสแกน QR PromptPay")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

fix_remaining("D:/Company_Workflows/departments/parking_restroom/ycparking/tab5_motorcycle.html")
fix_remaining("D:/Company_Workflows/departments/parking_restroom/ycparking/tab6_motorcycle_lot3.html")

print("Remaining transfers cleaned up.")
