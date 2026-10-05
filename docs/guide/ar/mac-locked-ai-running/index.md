Source: https://no-sleep-pika.online/guide/ar/mac-locked-ai-running/
Language: ar

MAC GUIDE · 2026-10-05

# هل يواصل Claude Code وCodex العمل عند قفل Mac؟

ميّز بين قفل الشاشة وإطفائها وسكون النظام عند متابعة مهام الذكاء الاصطناعي المحلية.

## القفل ليس السكون

ظهور شاشة كلمة المرور لا يثبت توقف المهمة. قد تستمر أوامر الخلفية إذا بقي Mac مستيقظاً والتطبيق والاتصالات اللازمة متاحة. قد تتطلب أتمتة الواجهة أو المصادقة فتح القفل. وقد يدخل النظام السكون بعد القفل. أبقِ حماية كلمة المرور مفعلة.

## محلي أم سحابي

يستخدم Codex CLI الملفات والأوامر المحلية، بينما تعمل المهمة المفوضة إلى Codex Cloud في بيئة منفصلة. يتصل Claude Code Remote Control أيضاً بجلسة محلية. إعادة الاتصال لا تعني استمرار التنفيذ أثناء السكون. لا ينقل pika المهام إلى السحابة.

[Codex CLI](https://learn.chatgpt.com/docs/codex/cli) · [Codex Cloud](https://learn.chatgpt.com/docs/cloud) · [Claude Code Remote Control](https://code.claude.com/docs/en/remote-control)

## ما الذي تفحصه أولاً

اقرأ الرسالة الأخيرة بحثاً عن طلب موافقة أو سؤال أو انتهاء أو خطأ. ثم افحص التطبيق وWi-Fi وVPN وتسجيل الدخول. تعرض أوامر القراءة أدناه طلبات الطاقة والأحداث، ولا تثبت تقدم الذكاء الاصطناعي. انخفاض استخدام المعالج لا يثبت الفشل أيضاً.

```
pmset -g assertions
```

```
pmset -g log | tail -n 60
```

## اختبار ثلاث دقائق

شغّل الحلقة والغطاء مفتوح، واترك الطرفية مفتوحة واقفل الشاشة نحو ثلاث دقائق. قارن الأوقات وأوقف الحلقة باستخدام Ctrl+C. قارن الفجوات بسجلات الطاقة ونتائج المهمة. هذا يفحص عملية بسيطة فقط؛ اختبر إغلاق الغطاء بشكل منفصل.

```
while true; do date "+%Y-%m-%d %H:%M:%S"; sleep 10; done
```

## إعداد pika

ثبّت pika وخدمته المساعدة، وفعّل Session واترك Monitor OFF إن لم تحتج الشاشة، ثم أغلق الغطاء. تطبق سياسة الشاشة بعد الإغلاق. يحرر Session OFF منع السكون دون إطفاء الشاشة فوراً. استخدم الطاقة ومكتباً جيد التهوية، لا حقيبة مغلقة. قد توقف الحماية أو أخطاء الخدمة الجلسة.

[تنزيل pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg) · [مساعدة التثبيت](https://no-sleep-pika.online/install/)

## أسئلة شائعة

Monitor OFF ليس أمراً بإنهاء مهمة الذكاء الاصطناعي. لا يمنع tmux سكون النظام، ولا يحل caffeinate مشكلات الشبكة أو الموافقات. حالة pika MCP لا تمثل تقدم جميع المهام.

المصادر والنطاق

رُوجعت الوثائق الرسمية وتنفيذ pika في 5 أكتوبر 2026. دليل من صانع pika، وليس ضماناً للتشغيل المتواصل على كل الأجهزة.

- [Apple · Sleep and wake settings](https://support.apple.com/guide/mac-help/set-sleep-and-wake-settings-mchle41a6ccd/mac)

- [OpenAI · Codex CLI](https://learn.chatgpt.com/docs/codex/cli)

- [OpenAI · Codex Cloud](https://learn.chatgpt.com/docs/cloud)

- [Anthropic · Claude Code Remote Control](https://code.claude.com/docs/en/remote-control)

مقارنة كتبها مطور no-sleep-pika وتشمل تطبيقه.

[تنزيل pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg)[كيف تمنع Mac من السكون: وضع الغطاء المغلق وcaffeinate وpika →](https://no-sleep-pika.online/guide/ar/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/ar/mac-locked-ai-running/index.md)
