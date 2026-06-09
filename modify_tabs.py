import re

with open("departments/parking_restroom/ycparking/workflow_swimlane_tabs.html", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("8 กระบวนการ", "9 กระบวนการ")
content = content.replace("ผังกระบวนการ 1–8", "ผังกระบวนการ 1–9")
content = content.replace("กระบวนการทั้งหมด 8 กระบวนการ", "กระบวนการทั้งหมด 9 กระบวนการ")

with open("departments/parking_restroom/ycparking/workflow_swimlane_tabs.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated workflow_swimlane_tabs.html successfully.")
