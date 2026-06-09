import os

filepath = "D:/Company_Workflows/departments/parking_restroom/ycparking/tab6_motorcycle_lot3.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Fix "สิทธิ์หมด"
content = content.replace(" / สิทธิ์หมด", "")
content = content.replace("สิทธิ์หมด", "")

# Fix "ปลายวัน"
content = content.replace("ปลายวัน", "รายวัน")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Wording fixed successfully.")
