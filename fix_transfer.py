import os

def fix_file(filepath, is_lot3):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Remove "เงินโอน" and "โอน" from both Lot 2 and Lot 3
    # Step ก-1: "เงินสด / โอน / QR" -> "เงินสด" (or "เงินสด / QR" if lot 2 has QR. Wait, Lot 2 has personnel QR but they don't pay with QR, the step says "เก็บค่าบริการ เงินสด / โอน / QR". Lot 2 personnel QR is a separate step (ข-1). So customers only pay cash.)
    # Let's assume general payment is just "เงินสด"
    content = content.replace("เงินสด / โอน / QR", "เงินสด")
    content = content.replace("เงินสด / โอน", "เงินสด")
    
    # In formula
    content = content.replace("= เงินสด + เงินโอน", "= เงินสด")
    content = content.replace("รายได้จริงที่รับมา = เงินสด + เงินโอน", "รายได้จริงที่รับมา = เงินสด")
    
    # In step data if any
    content = content.replace("รับเงินสด/โอน", "รับเงินสด")
    content = content.replace("เงินสด/โอน", "เงินสด")

    # 2. Fix รง-1 "บัตรจอดรถฟรี" in Lot 3
    if is_lot3:
        # Check for any remaining "บัตรจอดรถฟรี" or "บัตรฟรี"
        # รง-1 text: "ตรวจนับเงิน + สแกน QR + บัตรฟรี ให้ตรงใบสรุป" might have been missed due to spacing
        content = content.replace("ตรวจนับเงิน + สแกน QR + บัตรฟรี ให้ตรงใบสรุป", "ตรวจนับเงินให้ตรงใบสรุป")
        content = content.replace("ตรวจนับเงิน + บัตรฟรี ให้ตรงใบสรุป", "ตรวจนับเงินให้ตรงใบสรุป")
        content = content.replace("+ บัตรฟรี", "")
        # Remove any lingering "บัตรฟรี" in the step text block
        # For รง-1 step text directly:
        content = content.replace('<div class="step-text">ตรวจนับเงิน + สแกน QR + บัตรฟรี ให้ตรงใบสรุป</div>', '<div class="step-text">ตรวจนับเงินให้ตรงใบสรุป</div>')
        content = content.replace('<div class="step-text">ตรวจนับเงินให้ตรงใบสรุป ให้ตรงใบสรุป</div>', '<div class="step-text">ตรวจนับเงินให้ตรงใบสรุป</div>') # fix if double
        content = content.replace('ตรวจนับเงิน +  ให้ตรงใบสรุป', 'ตรวจนับเงินให้ตรงใบสรุป')
        
        # Look specifically in sR1 stepData for lot 3
        # If there's any text in sR1 tasks referencing "บัตรฟรี"
        content = content.replace("③ จำนวนบัตรจอดรถฟรี", "")
        content = content.replace("③ ", "") # If it was just "③ " left over
        content = content.replace("บัตรจอดรถฟรี", "") # aggressively remove remaining

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

# Fix Lot 2
fix_file("D:/Company_Workflows/departments/parking_restroom/ycparking/tab5_motorcycle.html", is_lot3=False)
# Fix Lot 3
fix_file("D:/Company_Workflows/departments/parking_restroom/ycparking/tab6_motorcycle_lot3.html", is_lot3=True)

print("Fixes applied.")
