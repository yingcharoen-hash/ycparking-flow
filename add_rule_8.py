import os

filepath = "D:/Company_Workflows/SYSTEM_CONSTRAINTS.md"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

rule_text = """
## 8. การเพิ่ม/แก้ไขจุดเสี่ยง (Risk Table Synchronization)
* **กฎเหล็กการแก้ไข HTML:** หากมีการเพิ่มหรือปรับปรุงจุดเสี่ยง (เช่น ใส่ `warn:'จุดเสี่ยง R6...'` ในส่วนของ JavaScript Data) **ห้ามลืม** เลื่อนลงไปเพิ่มข้อมูลจุดเสี่ยงนั้นในตาราง HTML `<table class="risk-table">` ด้านล่างสุดของไฟล์ด้วยเสมอ เพื่อป้องกันปัญหา Risk Code หลุดหรือข้อมูลไม่ตรงกันระหว่าง Process กับตารางสรุป
"""

if "## 8. การเพิ่ม/แก้ไขจุดเสี่ยง" not in content:
    content += rule_text

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Rule 8 added successfully.")
