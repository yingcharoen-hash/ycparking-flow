import os
import glob

# Search for all HTML files in ycparking
directory = "D:/Company_Workflows/departments/parking_restroom/ycparking/"
html_files = glob.glob(directory + "*.html")

for filepath in html_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    modified = False
    
    if "ปลายวัน" in content:
        content = content.replace("ปลายวัน", "รายวัน")
        modified = True
        
    # Only remove "สิทธิ์หมด" from lot 3, because it might be valid for Lot 2
    if "tab6_motorcycle_lot3" in filepath:
        if "สิทธิ์หมด" in content:
            content = content.replace(" / สิทธิ์หมด", "")
            content = content.replace("สิทธิ์หมด", "")
            modified = True
            
    if modified:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fixed {os.path.basename(filepath)}")

print("All wording checks completed.")
