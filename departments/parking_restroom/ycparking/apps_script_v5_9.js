function doPost(e) {
  try {
    let data = JSON.parse(e.postData.contents);
    let ts = new Date().getTime().toString();
    
    // ตั้งค่ารหัสต่างๆ ตรงนี้
    let SHEET_ID = "1VtTFuhbxVVUGvCPjEtmK9RbnDzW2XOmWYZ49rfLoZNw"; // ID ของ Google Sheet
    
    // ค้นหาหรือสร้างโฟลเดอร์สำหรับเก็บรูปและ PDF (ใช้แบบเก่าที่ปลอดภัยที่สุด)
    let folderNamePdf = "YC_Meter_PDFs";
    let foldersPdf = DriveApp.getFoldersByName(folderNamePdf);
    let folderPdf = foldersPdf.hasNext() ? foldersPdf.next() : DriveApp.createFolder(folderNamePdf);
    try { folderPdf.setSharing(DriveApp.Access.ANYONE_WITH_LINK, DriveApp.Permission.VIEW); } catch(e) {}
    
    let folderNameImages = "YC_Meter_Images";
    let foldersImages = DriveApp.getFoldersByName(folderNameImages);
    let folderImages = foldersImages.hasNext() ? foldersImages.next() : DriveApp.createFolder(folderNameImages);
    try { folderImages.setSharing(DriveApp.Access.ANYONE_WITH_LINK, DriveApp.Permission.VIEW); } catch(e) {}

    function saveImageToDrive(base64String, filename) {
      if (!base64String || typeof base64String !== 'string' || !base64String.includes('base64,')) return "";
      let contentType = base64String.substring(5, base64String.indexOf(';'));
      let base64Data = base64String.split(',')[1];
      if (!base64Data) return "";
      
      let blob = Utilities.newBlob(Utilities.base64Decode(base64Data), contentType || 'image/jpeg', filename);
      let file = folderImages.createFile(blob);
      try { file.setSharing(DriveApp.Access.ANYONE_WITH_LINK, DriveApp.Permission.VIEW); } catch(e) {}
      return file.getUrl();
    }

    let selfieUrl = saveImageToDrive(data.photoSelfie, 'selfie_' + ts + '.jpg');
    let photoInUrl = saveImageToDrive(data.photoIn, 'photoIn_' + ts + '.jpg');
    let photoOutUrl = saveImageToDrive(data.photoOut, 'photoOut_' + ts + '.jpg');

    let htmlContent = `
      <div style="font-family: 'Sarabun', sans-serif; padding: 10px; color: #333;">
        <h2 style="text-align: center; color: #2c3e50; margin-bottom: 5px;">ใบเสร็จรับเงิน / บันทึกข้อมูลรถคงค้าง</h2>
        
        <table style="width: 100%; border-collapse: collapse; margin-bottom: 5px;">
          <tr>
            <td style="padding: 5px; border-bottom: 1px solid #eee;"><strong>ลานจอด:</strong></td>
            <td style="padding: 5px; border-bottom: 1px solid #eee;">${data.parkingLot || '-'}</td>
          </tr>
          <tr>
            <td style="padding: 5px; border-bottom: 1px solid #eee;"><strong>วันที่และเวลา:</strong></td>
            <td style="padding: 5px; border-bottom: 1px solid #eee;">${data.date || '-'} ${data.time || '-'}</td>
          </tr>
          <tr style="background-color: #f8f9fa;">
            <td style="padding: 5px; border-bottom: 1px solid #eee;"><strong>มิเตอร์ขาเข้า (เริ่ม - จบ):</strong></td>
            <td style="padding: 5px; border-bottom: 1px solid #eee;">${data.inStartMeter || 0} - ${data.inEndMeter || 0}</td>
          </tr>
          <tr>
            <td style="padding: 5px; border-bottom: 1px solid #eee;"><strong>มิเตอร์ขาออก (เริ่ม - จบ):</strong></td>
            <td style="padding: 5px; border-bottom: 1px solid #eee;">${data.outStartMeter || 0} - ${data.outEndMeter || 0}</td>
          </tr>
          <tr style="background-color: #f8f9fa;">
            <td style="padding: 5px; border-bottom: 1px solid #eee;"><strong>รวมเงิน (บาท):</strong></td>
            <td style="padding: 5px; border-bottom: 1px solid #eee; color: #e74c3c; font-weight: bold;">${data.totalMoney || 0}</td>
          </tr>
          <tr>
            <td style="padding: 5px; border-bottom: 1px solid #eee;"><strong>หักเงินทอน (บาท):</strong></td>
            <td style="padding: 5px; border-bottom: 1px solid #eee;">${data.deductFloat || 0}</td>
          </tr>
          <tr style="background-color: #e8f6f3;">
            <td style="padding: 5px; border-bottom: 1px solid #eee;"><strong>ยอดเงินสุทธิที่ต้องส่ง (บาท):</strong></td>
            <td style="padding: 5px; border-bottom: 1px solid #eee; color: #16a085; font-weight: bold;">${data.netCash || 0}</td>
          </tr>
          <tr>
            <td style="padding: 5px; border-bottom: 1px solid #eee;"><strong>เงินสด:</strong> ${data.cash || 0}</td>
            <td style="padding: 5px; border-bottom: 1px solid #eee;"><strong>เงินโอน:</strong> ${data.transfer || 0}</td>
          </tr>
          <tr>
            <td style="padding: 5px; border-bottom: 1px solid #eee;"><strong>ยอดพนักงาน (บาท):</strong></td>
            <td style="padding: 5px; border-bottom: 1px solid #eee;">${data.empAmount || 0}</td>
          </tr>
          <tr>
            <td style="padding: 5px; border-bottom: 1px solid #eee;"><strong>คูปองจอดรถฟรี:</strong></td>
            <td style="padding: 5px; border-bottom: 1px solid #eee;">${data.freeCoupon || 0}</td>
          </tr>
        </table>
        
        <div style="text-align: center; margin-top: 5px;">
          <strong>รูปถ่ายยืนยันตัวตน ณ จุดรับฝาก</strong><br>
          ${selfieUrl ? '<img src="' + selfieUrl + '" style="height:120px; border-radius:8px; margin-top:5px;">' : '<span style="color:#888;">ไม่มีรูปถ่าย</span>'}
        </div>
        
        <table style="width:100%; text-align: center; margin-top: 10px; font-size: 12px;">
          <tr>
            <td style="width:50%;">
              <strong>(${data.senderName || '-'})</strong><br>เจ้าหน้าที่จุดรับฝากรถมอเตอร์ไซค์
            </td>
            <td style="width:50%;">
              <strong>(${data.receiverName || '-'})</strong><br>ผู้จดมิเตอร์ (การเงิน)
            </td>
          </tr>
        </table>
      </div>
    `;

    let pdfBlob = Utilities.newBlob(htmlContent, MimeType.HTML).getAs(MimeType.PDF);
    let safeLot = (data.parkingLot || 'Lot').replace(/\s+/g, '_');
    pdfBlob.setName(`Receipt_${safeLot}_${data.date}_${data.time.replace(':','')}.pdf`);
    let pdfFile = folderPdf.createFile(pdfBlob);
    try { pdfFile.setSharing(DriveApp.Access.ANYONE_WITH_LINK, DriveApp.Permission.VIEW); } catch(e) {}
    let pdfUrl = pdfFile.getUrl();

    let ss = SpreadsheetApp.openById(SHEET_ID);
    let sheet = ss.getSheetByName("บันทึกข้อมูล") || ss.getSheetByName("Sheet1") || ss.getSheets()[0];
    
    // จัดเรียงคอลัมน์ให้ตรงกับชีต (23 คอลัมน์)
    sheet.appendRow([
      data.parkingLot,       // A
      data.date,             // B
      data.time,             // C
      data.inStartMeter,     // D
      data.inEndMeter,       // E
      data.outStartMeter,    // F
      data.outEndMeter,      // G
      data.units,            // H
      data.totalMoney,       // I
      data.netCash,          // J
      data.cash,             // K
      data.transfer,         // L
      data.empAmount,        // M
      data.freeCoupon,       // N
      data.senderName,       // O
      data.receiverName,     // P
      selfieUrl,             // Q (แทนลายเซ็นผู้ส่ง)
      "",                    // R (แทนลายเซ็นผู้รับ)
      photoInUrl,            // S
      photoOutUrl,           // T
      pdfUrl,                // U
      new Date(),            // V
      data.deductFloat       // W (หักเงินทอน)
    ]);

    let message = `📝 <b>บันทึกข้อมูลใหม่</b>\n`
                + `ลานจอด: ${data.parkingLot || '-'}\n`
                + `วันที่: ${data.date || '-'} เวลา: ${data.time || '-'}\n`
                + `💰 ยอดเงินสุทธิ: ${data.netCash || 0} บาท\n`
                + `💵 เงินสด: ${data.cash || 0} | 📱 เงินโอน: ${data.transfer || 0}\n`
                + `🧑‍💼 ยอดพนักงาน: ${data.empAmount || 0}\n`
                + `🎟️ คูปองจอดฟรี: ${data.freeCoupon || 0}\n`
                + `ส่ง: ${data.senderName || '-'}\n`
                + `รับ: ${data.receiverName || '-'}\n`
                + `📄 ดูใบเสร็จ: ${pdfUrl}`;

    try { sendLineNotify(message); } catch(e) {} // ป้องกัน LINE พังแล้วดึงระบบพัง

    return ContentService.createTextOutput(JSON.stringify({ "status": "success", "pdfUrl": pdfUrl })).setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({ "status": "error", "message": error.message })).setMimeType(ContentService.MimeType.JSON);
  }
}

function sendLineNotify(message) {
  let token = "nF32d9F97K2n0aB1X5JqW7oO4uC9G2eF0V6N7zK8"; // Your LINE Token
  let options = {
    "method": "post",
    "payload": { "message": message },
    "headers": { "Authorization": "Bearer " + token },
    "muteHttpExceptions": true
  };
  UrlFetchApp.fetch("https://notify-api.line.me/api/notify", options);
}

function doGet(e) {
  try {
    let SHEET_ID = "1VtTFuhbxVVUGvCPjEtmK9RbnDzW2XOmWYZ49rfLoZNw"; // ID ของ Google Sheet
    
    if (e.parameter.action === "getLast") {
      let parkingLot = e.parameter.lot;
      let ss = SpreadsheetApp.openById(SHEET_ID);
      let sheet = ss.getSheetByName("บันทึกข้อมูล") || ss.getSheetByName("Sheet1") || ss.getSheets()[0];
      let data = sheet.getDataRange().getValues();
      let lastInEnd = "";
      let lastOutEnd = "";
      
      for (let i = data.length - 1; i >= 1; i--) {
        if (data[i][0] === parkingLot) {
          lastInEnd = data[i][4] || ""; 
          lastOutEnd = data[i][6] || ""; 
          break;
        }
      }
      
      let result = {
        "status": "success",
        "inEndMeter": lastInEnd,
        "outEndMeter": lastOutEnd
      };

      if (e.parameter.callback) {
        return ContentService.createTextOutput(e.parameter.callback + "(" + JSON.stringify(result) + ")")
          .setMimeType(ContentService.MimeType.JAVASCRIPT);
      }
      return ContentService.createTextOutput(JSON.stringify(result)).setMimeType(ContentService.MimeType.JSON);
    }
    
    if (e.parameter.action === "getInitialData") {
      let ss = SpreadsheetApp.openById(SHEET_ID);
      let staffSheet = ss.getSheetByName("รายชื่อเจ้าหน้าที่") || ss.getSheetByName("setting");
      let lotSheet = ss.getSheetByName("ชื่อลานจอด");
      
      let senders = [];
      let receivers = [];
      let parkingLots = [];

      if (staffSheet) {
        let staffData = staffSheet.getDataRange().getValues();
        for (let i = 1; i < staffData.length; i++) {
          if (staffData[i][0]) senders.push(staffData[i][0].toString());
          if (staffData[i][1]) receivers.push(staffData[i][1].toString());
        }
      }
      
      if (lotSheet) {
        let lotData = lotSheet.getDataRange().getValues();
        for (let i = 1; i < lotData.length; i++) {
          if (lotData[i][0]) parkingLots.push(lotData[i][0].toString());
        }
      }
      
      let result = { 
        status: "success", 
        senders: senders, 
        receivers: receivers, 
        parkingLots: parkingLots 
      };
      
      if (e.parameter.callback) {
        return ContentService.createTextOutput(e.parameter.callback + '(' + JSON.stringify(result) + ')').setMimeType(ContentService.MimeType.JAVASCRIPT);
      }
      return ContentService.createTextOutput(JSON.stringify(result)).setMimeType(ContentService.MimeType.JSON);
    }
    
    if (e.parameter.action === "getAllData") {
      let ss = SpreadsheetApp.openById(SHEET_ID);
      let sheet = ss.getSheetByName("บันทึกข้อมูล") || ss.getSheetByName("Sheet1") || ss.getSheets()[0];
      let data = sheet.getDataRange().getValues();
      let allRecords = [];
      
      for (let i = 1; i < data.length; i++) {
        let isNewFormat = false;
        let pdfUrl = "";
        let photoSelfie = "";
        let senderName = "";
        let receiverName = "";
        
        if (data[i].length > 20 && String(data[i][20]).includes("drive.google.com")) {
          isNewFormat = true;
          pdfUrl = data[i][20];
          photoSelfie = data[i][16] ? data[i][16].toString() : ""; // Q column
          senderName = data[i][14]; // O column
          receiverName = data[i][15]; // P column
        } else if (data[i].length > 19 && String(data[i][19]).includes("drive.google.com")) {
          isNewFormat = true;
          pdfUrl = data[i][19];
          photoSelfie = data[i][16] ? data[i][16].toString() : "";
          senderName = data[i][14];
          receiverName = data[i][15];
        } else {
          pdfUrl = data[i][17] ? data[i][17].toString() : "";
        }

        if (!photoSelfie || !photoSelfie.includes("drive.google.com")) {
           if (data[i][17] && String(data[i][17]).includes("drive.google.com")) {
              photoSelfie = data[i][17].toString();
           } else if (data[i][18] && String(data[i][18]).includes("drive.google.com")) {
              photoSelfie = data[i][18].toString();
           } else if (data[i][16] && String(data[i][16]).includes("drive.google.com")) {
              photoSelfie = data[i][16].toString();
           }
        }

        let record = {
          parkingLot: data[i][0] ? data[i][0].toString() : "",
          date: data[i][1] ? data[i][1].toString() : "",
          time: data[i][2] ? data[i][2].toString() : "",
          inStartMeter: data[i][3] || 0,
          inEndMeter: data[i][4] || 0,
          outStartMeter: data[i][5] || 0,
          outEndMeter: data[i][6] || 0,
          units: data[i][7] || 0,
          totalMoney: data[i][8] || 0,
          deductFloat: data[i][22] || 0, // W column
          netCash: data[i][9] || 0, // J column
          cash: data[i][10] || 0, // K column
          transfer: data[i][11] || 0, // L column
          empAmount: data[i][12] || 0, // M column
          freeCoupon: data[i][13] || 0, // N column
          senderName: isNewFormat ? (senderName || "-") : "-",
          receiverName: isNewFormat ? (receiverName || "-") : "-",
          photoSelfie: photoSelfie,
          pdfUrl: pdfUrl
        };
        allRecords.push(record);
      }
      
      let result = { status: "success", records: allRecords };
      
      if (e.parameter.callback) {
        return ContentService.createTextOutput(e.parameter.callback + '(' + JSON.stringify(result) + ')').setMimeType(ContentService.MimeType.JAVASCRIPT);
      }
      return ContentService.createTextOutput(JSON.stringify(result)).setMimeType(ContentService.MimeType.JSON);
    }
  } catch (error) {
    let result = { status: "error", message: error.toString() };
    if (e.parameter && e.parameter.callback) {
      return ContentService.createTextOutput(e.parameter.callback + '(' + JSON.stringify(result) + ')').setMimeType(ContentService.MimeType.JAVASCRIPT);
    }
    return ContentService.createTextOutput(JSON.stringify(result)).setMimeType(ContentService.MimeType.JSON);
  }
}
