Source: https://no-sleep-pika.online/guide/ar/macbook-downloads-stop/
Language: ar

MAC GUIDE · 2026-10-15

# توقف التنزيل على MacBook: الشاشة أم السكون أم الغطاء؟

افحص الشبكة والمساحة قبل اختيار caffeinate أو pika.

## حدد وقت التوقف

افحص رسائل الإيقاف المؤقت والشبكة والمساحة وتسجيل الدخول. إذا توقف أثناء الاستخدام، افحص Wi-Fi وVPN والخادم أولاً. منع السكون لا يصلح رابطاً منتهي الصلاحية.

## الشاشة والسكون

انطفاء الشاشة لا يعني سكون النظام. قد يستمر النقل لكن السكون التلقائي قد يأتي بعد القفل. افحص خيار البقاء مستيقظاً على الطاقة إن كان متاحاً. أبقِ حماية كلمة المرور.

## caffeinate والغطاء مفتوح

يطلب الأمر أدناه منع سكون الخمول لساعة. اترك الطرفية مفتوحة ونزّل بالتطبيق المعتاد. يوقفه Ctrl+C مبكراً؛ -t بالثواني، و-i للنظام و-d للشاشة. لا يضمن الشبكة ولا يمنع كل أنواع السكون.

```
caffeinate -i -t 3600
```

```
man caffeinate
```

## شروط إغلاق الغطاء

مع شاشة خارجية افحص الطاقة ولوحة المفاتيح والفأرة ودعم الطراز. الشاحن وحده لا يكمل الإعداد. دون شاشة خارجية اختبر نقلاً قصيراً وقارن البايتات قبل الإغلاق وبعده.

## التنزيل مع pika

جهّز pika وخدمته، ابدأ التنزيل وفعّل Session واترك Monitor OFF إن لم تحتج الشاشة، ثم أغلق الغطاء. تطبق سياسة الشاشة بعد الإغلاق. عند الانتهاء استخدم Session OFF. استخدم الطاقة ومكتباً مهوّى لا حقيبة مغلقة. قد توقف الحماية أو الأخطاء الجلسة.

[تنزيل pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg) · [مساعدة التثبيت](https://no-sleep-pika.online/install/)

## تحقق من النتيجة

تحقق من الاكتمال وحجم الملف وقيمة التحقق إن توفرت. استأنف عبر التطبيق. لا يصلح pika الشبكة ولا يكتشف انتهاء التنزيل؛ إطفاء الشاشة لا يضمن السرعة.

المصادر

رُوجع في 11 أكتوبر 2026 وفق Apple وcaffeinate(8) وكود pika. دليل من صانع pika.

- [Apple · Sleep and wake settings](https://support.apple.com/guide/mac-help/set-sleep-and-wake-settings-mchle41a6ccd/mac)

- [Apple · External displays](https://support.apple.com/en-us/102501)

- `man caffeinate` · macOS System Manager’s Manual

[إذا عمل الذكاء الاصطناعي طوال الليل، فمن يدفع فاتورة الكهرباء؟ →](https://no-sleep-pika.online/guide/ar/ai-overnight-electricity-cost/)

مقارنة كتبها مطور no-sleep-pika وتشمل تطبيقه.

[تنزيل pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg)[كيف تمنع Mac من السكون: وضع الغطاء المغلق وcaffeinate وpika →](https://no-sleep-pika.online/guide/ar/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/ar/macbook-downloads-stop/index.md)
