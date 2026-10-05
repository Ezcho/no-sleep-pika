Source: https://no-sleep-pika.online/guide/th/mac-locked-ai-running/
Language: th

MAC GUIDE · 2026-10-05

# ล็อก Mac แล้ว Claude Code และ Codex ยังทำงานต่อหรือไม่?

แยกการล็อกหน้าจอ ปิดจอ และพักเครื่อง เพื่อตรวจงาน AI ที่ทำบน Mac ก่อนปิดฝา

## ล็อกกับพักเครื่องต่างกัน

หน้าจอรหัสผ่านไม่ได้ยืนยันว่างานหยุด คำสั่งเบื้องหลังอาจทำต่อได้หาก Mac ยังตื่น แอปเปิด และการเชื่อมต่อพร้อม แต่การควบคุมหน้าจอหรือยืนยันตัวตนอาจต้องปลดล็อก ระบบอาจพักเครื่องภายหลังการล็อก ควรคงการป้องกันด้วยรหัสผ่านไว้

## ทำงานในเครื่องหรือคลาวด์

Codex CLI ใช้ไฟล์และคำสั่งในเครื่อง ส่วนงานที่ส่งให้ Codex Cloud ทำงานในสภาพแวดล้อมอื่น Claude Code Remote Control ก็ยังเชื่อมกับเซสชันในเครื่อง การเชื่อมใหม่ไม่ได้แปลว่าทำงานระหว่างพักเครื่อง pika ไม่ได้ย้ายงานขึ้นคลาวด์

[Codex CLI](https://learn.chatgpt.com/docs/codex/cli) · [Codex Cloud](https://learn.chatgpt.com/docs/cloud) · [Claude Code Remote Control](https://code.claude.com/docs/en/remote-control)

## ตรวจสาเหตุก่อน

อ่านข้อความล่าสุดว่ารออนุมัติ คำตอบ จบงาน หรือมีข้อผิดพลาด แล้วตรวจแอป Wi-Fi VPN และการเข้าสู่ระบบ คำสั่งอ่านอย่างเดียวด้านล่างแสดงคำขอพลังงานและเหตุการณ์ ไม่ใช่หลักฐานความคืบหน้า AI และ CPU ต่ำก็ไม่ได้ยืนยันว่างานเสีย

```
pmset -g assertions
```

```
pmset -g log | tail -n 60
```

## ทดสอบสามนาที

เปิดฝา รันลูป เปิดเทอร์มินัลค้างไว้ แล้วล็อกประมาณสามนาที เปรียบเทียบเวลาและหยุดด้วย Ctrl+C เทียบช่วงเวลาที่หายไปกับบันทึกพลังงานและผลลัพธ์ AI วิธีนี้ตรวจเพียงโปรเซสง่าย ๆ ต้องทดสอบตอนปิดฝาแยกต่างหาก

```
while true; do date "+%Y-%m-%d %H:%M:%S"; sleep 10; done
```

## ตั้งค่า pika

ติดตั้ง pika และบริการช่วย เปิด Session และให้ Monitor OFF หากไม่ต้องใช้จอ แล้วปิดฝา นโยบายจอใช้หลังปิดฝา Session OFF ยกเลิกการป้องกันพักเครื่องโดยไม่ดับจอทันที ใช้ไฟเลี้ยงและโต๊ะระบายอากาศ ไม่ใช้ในกระเป๋าปิด ระบบป้องกันหรือบริการผิดพลาดอาจหยุดเซสชัน

[ดาวน์โหลด pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg) · [ช่วยเหลือติดตั้ง](https://no-sleep-pika.online/install/)

## คำถามทั่วไป

Monitor OFF ไม่ได้สั่งจบงาน AI ส่วน tmux ไม่ป้องกันพักเครื่อง และ caffeinate ไม่แก้เครือข่ายหรือการรออนุมัติ สถานะ pika MCP ไม่ใช่ความคืบหน้าของงาน AI ทั้งหมด

แหล่งข้อมูลและขอบเขต

ตรวจเอกสารทางการและโค้ด pika วันที่ 5 ตุลาคม 2026 คู่มือโดยผู้สร้าง pika ไม่ได้รับประกันการทำงานต่อเนื่องบนทุกเครื่อง

- [Apple · Sleep and wake settings](https://support.apple.com/guide/mac-help/set-sleep-and-wake-settings-mchle41a6ccd/mac)

- [OpenAI · Codex CLI](https://learn.chatgpt.com/docs/codex/cli)

- [OpenAI · Codex Cloud](https://learn.chatgpt.com/docs/cloud)

- [Anthropic · Claude Code Remote Control](https://code.claude.com/docs/en/remote-control)

เขียนโดยผู้พัฒนา no-sleep-pika และแนะนำแอปของตนเอง

[ดาวน์โหลด pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg)[วิธีทำให้ Mac ไม่พักเครื่อง: clamshell, caffeinate และ pika →](https://no-sleep-pika.online/guide/th/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/th/mac-locked-ai-running/index.md)
