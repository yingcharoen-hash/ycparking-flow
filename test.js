
  // Setup Defaults
  document.getElementById('docDate').valueAsDate = new Date();
  
  const now = new Date();
  const hours = String(now.getHours()).padStart(2, '0');
  const minutes = String(now.getMinutes()).padStart(2, '0');
  document.getElementById('docTime').value = `${hours}:${minutes}`;

  // URL of Google Apps Script
  const scriptUrl = 'https://script.google.com/macros/s/AKfycbx9VgBmGLjVAvDEBCK2ruTMnQswLtB1oZoiMzDlhwuRC9MI95GJoId_QTdQJE8kOw-XPw/exec';

  // Fetch Latest Meter Data
  async function fetchLatestMeter() {
    const lot = document.getElementById('parkingLot').value;
    const fetchBtn = document.getElementById('fetchBtn');
    const fetchSpinner = document.getElementById('fetchSpinner');
    const fetchText = document.getElementById('fetchBtnText');
    const msg = document.getElementById('fetchMsg');

    fetchBtn.disabled = true;
    fetchSpinner.style.display = 'block';
    fetchText.style.display = 'none';
    msg.style.display = 'none';
    msg.className = 'status-msg';

    try {
      // Use GET parameter to fetch data
      const url = `${scriptUrl}?action=getLast&lot=${encodeURIComponent(lot)}`;
      const response = await fetch(url);
      const data = await response.json();

      if (data.status === 'success') {
        document.getElementById('inStartMeter').value = data.inEndMeter || '';
        document.getElementById('outStartMeter').value = data.outEndMeter || '';
        
        if (!data.inEndMeter && !data.outEndMeter) {
          msg.innerText = 'ℹ️ ยังไม่มีประวัติของลานจอดนี้ (ปลดล็อกให้กรอกเลขตั้งต้นเอง)';
          msg.classList.add('info');
          document.getElementById('inStartMeter').removeAttribute('readonly');
          document.getElementById('outStartMeter').removeAttribute('readonly');
        } else {
          msg.innerText = '✅ ดึงข้อมูลสำเร็จ! ล็อกเลขมิเตอร์เริ่มให้แล้ว';
          msg.classList.add('success');
          // Re-apply readonly just in case it was removed previously
          document.getElementById('inStartMeter').setAttribute('readonly', 'readonly');
          document.getElementById('outStartMeter').setAttribute('readonly', 'readonly');
        }
        calculate();
      } else {
        throw new Error(data.message || 'ดึงข้อมูลไม่สำเร็จ');
      }
    } catch (error) {
      msg.innerText = '⚠️ Error: ' + error.message;
      msg.classList.add('error');
      // If error, unlock the fields temporarily so they can input manually if needed?
      // Actually, keeping them locked prevents bypass. But if it's the very first time, they need to unlock.
      document.getElementById('inStartMeter').removeAttribute('readonly');
      document.getElementById('outStartMeter').removeAttribute('readonly');
      msg.innerText += ' (ปลดล็อกช่องให้กรอกเองได้ชั่วคราว)';
    } finally {
      fetchBtn.disabled = false;
      fetchSpinner.style.display = 'none';
      fetchText.style.display = 'block';
    }
  }

  // Calculate Logic (+1 Car)
  function calculate() {
    const start = parseFloat(document.getElementById('outStartMeter').value) || 0;
    const end = parseFloat(document.getElementById('outEndMeter').value) || 0;
    const deductFloat = parseFloat(document.getElementById('deductFloat').value) || 0;
    
    if (end > 0 && end >= start) {
      const units = (end - start) + 1; // CASE 2 Logic: +1 Car
      const total = units * 5; // 1 unit = 5 baht
      const netCash = total - deductFloat;
      
      document.getElementById('units').value = units;
      document.getElementById('totalMoney').value = total;
      document.getElementById('netCash').value = netCash;
    } else {
      document.getElementById('units').value = '';
      document.getElementById('totalMoney').value = '';
      document.getElementById('netCash').value = '';
    }
  }

  // Camera Implementation (WebRTC)
  let photoData = { in: '', out: '' };
  let videoStream = null;
  let currentCamType = '';

  async function startCamera(type) {
    currentCamType = type;
    const isIN = type === 'in';
    const suffix = isIN ? 'In' : 'Out';
    
    const video = document.getElementById('videoElement' + suffix);
    const camWrap = document.getElementById('cameraWrap' + suffix);
    const openBtn = document.getElementById('openCamBtn' + suffix);
    const preview = document.getElementById('photoPreview' + suffix);
    const retakeBtn = document.getElementById('retakeBtn' + suffix);

    openBtn.style.display = 'none';
    preview.style.display = 'none';
    retakeBtn.style.display = 'none';
    camWrap.style.display = 'block';

    try {
      if(videoStream) {
        videoStream.getTracks().forEach(track => track.stop());
      }
      videoStream = await navigator.mediaDevices.getUserMedia({ 
        video: { facingMode: "environment" } 
      });
      video.srcObject = videoStream;
    } catch (err) {
      alert("ไม่สามารถเข้าถึงกล้องได้: " + err.message + "\n\nหมายเหตุ: ฟังก์ชันกล้องต้องใช้งานผ่านลิงก์ https:// เท่านั้น");
      camWrap.style.display = 'none';
      openBtn.style.display = 'flex';
    }
  }

  function cancelCamera(type) {
    const isIN = type === 'in';
    const suffix = isIN ? 'In' : 'Out';
    
    if (videoStream) {
      videoStream.getTracks().forEach(track => track.stop());
      videoStream = null;
    }
    
    document.getElementById('cameraWrap' + suffix).style.display = 'none';
    document.getElementById('openCamBtn' + suffix).style.display = 'flex';
  }

  function capturePhoto(type) {
    const isIN = type === 'in';
    const suffix = isIN ? 'In' : 'Out';
    
    const video = document.getElementById('videoElement' + suffix);
    const canvas = document.createElement('canvas');
    
    const MAX_WIDTH = 800;
    let width = video.videoWidth;
    let height = video.videoHeight;
    if (width > MAX_WIDTH) {
      height *= MAX_WIDTH / width;
      width = MAX_WIDTH;
    }
    
    canvas.width = width;
    canvas.height = height;
    const ctx = canvas.getContext('2d');
    ctx.drawImage(video, 0, 0, width, height);
    
    photoData[type] = canvas.toDataURL('image/jpeg', 0.6);
    
    if (videoStream) {
      videoStream.getTracks().forEach(track => track.stop());
      videoStream = null;
    }
    
    document.getElementById('cameraWrap' + suffix).style.display = 'none';
    const preview = document.getElementById('photoPreview' + suffix);
    preview.src = photoData[type];
    preview.style.display = 'block';
    document.getElementById('retakeBtn' + suffix).style.display = 'inline-block';
  }

  // Signature Pad Implementation
  function setupCanvas(canvasId) {
    const canvas = document.getElementById(canvasId);
    const ctx = canvas.getContext('2d');
    let isDrawing = false;
    let lastX = 0;
    let lastY = 0;

    const rect = canvas.getBoundingClientRect();
    canvas.width = rect.width;
    canvas.height = rect.height;

    ctx.lineWidth = 2;
    ctx.lineCap = 'round';
    ctx.strokeStyle = '#000';

    function getMousePos(evt) {
      const rect = canvas.getBoundingClientRect();
      const scaleX = canvas.width / rect.width;
      const scaleY = canvas.height / rect.height;
      if(evt.touches) {
        return {
          x: (evt.touches[0].clientX - rect.left) * scaleX,
          y: (evt.touches[0].clientY - rect.top) * scaleY
        };
      }
      return {
        x: (evt.clientX - rect.left) * scaleX,
        y: (evt.clientY - rect.top) * scaleY
      };
    }

    function startDraw(e) {
      e.preventDefault();
      isDrawing = true;
      const pos = getMousePos(e);
      lastX = pos.x;
      lastY = pos.y;
    }

    function draw(e) {
      if (!isDrawing) return;
      e.preventDefault();
      const pos = getMousePos(e);
      ctx.beginPath();
      ctx.moveTo(lastX, lastY);
      ctx.lineTo(pos.x, pos.y);
      ctx.stroke();
      lastX = pos.x;
      lastY = pos.y;
    }

    function endDraw(e) {
      e.preventDefault();
      isDrawing = false;
    }

    canvas.addEventListener('mousedown', startDraw);
    canvas.addEventListener('mousemove', draw);
    canvas.addEventListener('mouseup', endDraw);
    canvas.addEventListener('mouseout', endDraw);

    canvas.addEventListener('touchstart', startDraw, {passive: false});
    canvas.addEventListener('touchmove', draw, {passive: false});
    canvas.addEventListener('touchend', endDraw, {passive: false});

    return { canvas, ctx };
  }

  const senderPad = setupCanvas('senderCanvas');
  const receiverPad = setupCanvas('receiverCanvas');

  function clearCanvas(pad) {
    pad.ctx.clearRect(0, 0, pad.canvas.width, pad.canvas.height);
  }
  
  function isCanvasBlank(canvas) {
    const blank = document.createElement('canvas');
    blank.width = canvas.width;
    blank.height = canvas.height;
    return canvas.toDataURL() === blank.toDataURL();
  }

  // Load History
  function loadHistory() {
    const history = JSON.parse(localStorage.getItem('meterApp_history') || '[]');
    const tbody = document.querySelector('#historyTable tbody');
    tbody.innerHTML = '';
    history.slice().reverse().forEach(h => {
      const tr = document.createElement('tr');
      tr.innerHTML = `
        <td>${h.date || '-'}<br><span style="font-size: 10px; color: #888;">${h.time || '-'}</span></td>
        <td>${h.outStart || '?'}-${h.outEnd || '?'}</td>
        <td>${h.units || '-'}</td>
        <td>${h.netCash || '-'} ฿</td>
      `;
      tbody.appendChild(tr);
    });
  }
  loadHistory();

  // Submit Data
  async function submitData() {
    if (!scriptUrl) {
      alert('ยังไม่ได้ใส่ Web App URL ในโค้ดครับ');
      return;
    }

    const parkingLot = document.getElementById('parkingLot').value;
    const date = document.getElementById('docDate').value;
    const time = document.getElementById('docTime').value;
    const inStartMeter = document.getElementById('inStartMeter').value;
    const inEndMeter = document.getElementById('inEndMeter').value;
    const outStartMeter = document.getElementById('outStartMeter').value;
    const outEndMeter = document.getElementById('outEndMeter').value;
    
    const units = document.getElementById('units').value;
    const totalMoney = document.getElementById('totalMoney').value;
    const deductFloat = document.getElementById('deductFloat').value;
    const netCash = document.getElementById('netCash').value;
    
    const cash = document.getElementById('cash').value;
    const transfer = document.getElementById('transfer').value;

    if(!outStartMeter || !outEndMeter || !units || !netCash) {
      alert('กรุณากรอกเลขมิเตอร์ขาออกให้ครบถ้วน');
      return;
    }
    if(!cash && !transfer) {
      alert('กรุณากรอกจำนวน "เงินสด" หรือ "เงินโอน" อย่างน้อย 1 ช่องครับ');
      return;
    }

    const numNetCash = parseFloat(netCash) || 0;
    const numCash = parseFloat(cash) || 0;
    const numTransfer = parseFloat(transfer) || 0;
    
    if (numCash + numTransfer !== numNetCash) {
      if (!confirm('⚠️ ยอดรวมเงินส่ง (' + (numCash + numTransfer) + ' บาท) ไม่ตรงกับ ยอดสุทธิที่ต้องส่ง (' + numNetCash + ' บาท)\n\nคุณต้องการยืนยันการบันทึกข้อมูลหรือไม่?')) {
        return;
      }
    }
    
    let sSign = isCanvasBlank(senderPad.canvas) ? '' : senderPad.canvas.toDataURL('image/png');
    let rSign = isCanvasBlank(receiverPad.canvas) ? '' : receiverPad.canvas.toDataURL('image/png');

    const payload = {
      parkingLot: parkingLot,
      date: date,
      time: time,
      inStartMeter: inStartMeter,
      inEndMeter: inEndMeter,
      outStartMeter: outStartMeter,
      outEndMeter: outEndMeter,
      units: units,
      totalMoney: totalMoney,
      deductFloat: deductFloat,
      netCash: netCash,
      cash: cash,
      transfer: transfer,
      senderSign: sSign,
      receiverSign: rSign,
      photoIn: photoData.in,
      photoOut: photoData.out
    };

    const btn = document.getElementById('submitBtn');
    const spinner = document.getElementById('spinner');
    const btnText = btn.querySelector('.btn-text');
    const msg = document.getElementById('statusMsg');

    btn.disabled = true;
    spinner.style.display = 'block';
    btnText.style.display = 'none';
    msg.style.display = 'none';
    msg.className = 'status-msg';

    try {
      const response = await fetch(scriptUrl, {
        method: 'POST',
        mode: 'no-cors',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      
      // Save local history
      const history = JSON.parse(localStorage.getItem('meterApp_history') || '[]');
      history.push({ date: date, time: time, outStart: outStartMeter, outEnd: outEndMeter, units: units, netCash: netCash });
      if (history.length > 10) history.shift();
      localStorage.setItem('meterApp_history', JSON.stringify(history));
      
      msg.innerText = '✅ บันทึกข้อมูลและสร้างใบเสร็จ PDF สำเร็จ!';
      msg.classList.add('success');
      loadHistory();
      
      // Clear forms
      document.getElementById('inEndMeter').value = '';
      document.getElementById('outEndMeter').value = '';
      document.getElementById('cash').value = '';
      document.getElementById('transfer').value = '';
      clearCanvas(senderPad);
      clearCanvas(receiverPad);
      
      // Clear photos
      photoData = { in: '', out: '' };
      document.getElementById('photoPreviewIn').style.display = 'none';
      document.getElementById('openCamBtnIn').style.display = 'flex';
      document.getElementById('retakeBtnIn').style.display = 'none';
      
      document.getElementById('photoPreviewOut').style.display = 'none';
      document.getElementById('openCamBtnOut').style.display = 'flex';
      document.getElementById('retakeBtnOut').style.display = 'none';
      
      // Automatically run fetch for next round? No, they usually refresh. But we can unlock the inputs.
      document.getElementById('inStartMeter').value = '';
      document.getElementById('outStartMeter').value = '';
      document.getElementById('fetchMsg').style.display = 'none';
      
      calculate();

    } catch (error) {
      msg.innerText = '❌ เกิดข้อผิดพลาด: ' + error.message;
      msg.classList.add('error');
    } finally {
      btn.disabled = false;
      spinner.style.display = 'none';
      btnText.style.display = 'block';
    }
  }
