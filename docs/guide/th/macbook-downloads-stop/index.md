Source: https://no-sleep-pika.online/guide/th/macbook-downloads-stop/
Language: th

MAC GUIDE · 2026-10-15

# ดาวน์โหลดบน MacBook หยุด: ปิดจอ พักเครื่อง หรือปิดฝา?

ตรวจเครือข่ายและพื้นที่ก่อนเลือกใช้ caffeinate หรือ pika

## ดูว่าหยุดเมื่อใด

ตรวจข้อความหยุดชั่วคราว เครือข่าย พื้นที่ และการเข้าสู่ระบบในแอป หากหยุดขณะใช้งานให้ตรวจ Wi-Fi VPN และเซิร์ฟเวอร์ก่อน การกันพักเครื่องไม่แก้ลิงก์หมดอายุ

## จอกับการพักเครื่อง

จอดับไม่ได้แปลว่าระบบพักเครื่อง การส่งข้อมูลอาจทำต่อแต่ระบบอาจพักภายหลังการล็อก ตรวจตัวเลือกไม่พักอัตโนมัติเมื่อเสียบไฟหากรองรับ คงรหัสผ่านไว้

## ใช้ caffeinate เมื่อเปิดฝา

คำสั่งด้านล่างขอกันพักเครื่องจากการไม่ใช้งานหนึ่งชั่วโมง เปิดเทอร์มินัลไว้และดาวน์โหลดในแอปเดิม หยุดก่อนด้วย Ctrl+C โดย -t เป็นวินาที -i สำหรับระบบและ -d สำหรับจอ ไม่รับประกันเครือข่ายหรือกันการพักทุกกรณี

```
caffeinate -i -t 3600
```

```
man caffeinate
```

## เงื่อนไขเมื่อปิดฝา

เมื่อใช้จอนอกให้ตรวจไฟเลี้ยง คีย์บอร์ด เมาส์ และรุ่นที่รองรับ มีเพียงที่ชาร์จยังไม่ครบ หากไม่มีจอนอกให้ลองดาวน์โหลดสั้น ๆ และเทียบปริมาณก่อนกับหลังปิดฝา

## ดาวน์โหลดด้วย pika

เตรียม pika และบริการช่วย เริ่มดาวน์โหลด เปิด Session และให้ Monitor OFF หากไม่ต้องใช้จอ แล้วปิดฝา นโยบายจอทำงานหลังปิดฝา เสร็จแล้ว Session OFF ใช้ไฟและโต๊ะระบายอากาศ ไม่ใช่กระเป๋าปิด ระบบป้องกันหรือข้อผิดพลาดอาจหยุดเซสชัน

[ดาวน์โหลด pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg) · [ช่วยเหลือติดตั้ง](https://no-sleep-pika.online/install/)

## ตรวจผลลัพธ์

ตรวจสถานะเสร็จ ขนาดไฟล์ และ checksum หากมี ใช้ฟังก์ชันของแอปเพื่อดาวน์โหลดต่อ pika ไม่แก้เครือข่ายหรือตรวจการเสร็จสิ้น และจอดับไม่รับประกันความเร็ว

แหล่งข้อมูล

ตรวจวันที่ 11 ตุลาคม 2026 จาก Apple, caffeinate(8) และโค้ด pika คู่มือโดยผู้สร้าง pika

- [Apple · Sleep and wake settings](https://support.apple.com/guide/mac-help/set-sleep-and-wake-settings-mchle41a6ccd/mac)

- [Apple · External displays](https://support.apple.com/en-us/102501)

- `man caffeinate` · macOS System Manager’s Manual

[ให้ AI ทำงานทั้งคืน ใครจ่ายค่าไฟ? →](https://no-sleep-pika.online/guide/th/ai-overnight-electricity-cost/)

เขียนโดยผู้พัฒนา no-sleep-pika และแนะนำแอปของตนเอง

[ดาวน์โหลด pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg)[วิธีทำให้ Mac ไม่พักเครื่อง: clamshell, caffeinate และ pika →](https://no-sleep-pika.online/guide/th/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/th/macbook-downloads-stop/index.md)
