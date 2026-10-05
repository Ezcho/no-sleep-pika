Source: https://no-sleep-pika.online/guide/hi/mac-locked-ai-running/
Language: hi

MAC GUIDE · 2026-10-05

# Mac लॉक होने पर क्या Claude Code और Codex काम करते रहते हैं?

स्थानीय AI काम के लिए स्क्रीन लॉक, डिस्प्ले बंद होने और सिस्टम स्लीप का अंतर समझें।

## लॉक और स्लीप अलग हैं

पासवर्ड स्क्रीन दिखना काम रुकने का प्रमाण नहीं है। Mac जागा रहे, ऐप खुला हो और आवश्यक कनेक्शन उपलब्ध हों तो सामान्य बैकग्राउंड कमांड चल सकते हैं। स्क्रीन पर क्लिक या प्रमाणीकरण वाले चरणों में अनलॉक करना पड़ सकता है। लॉक के बाद सिस्टम स्लीप में जा सकता है। पासवर्ड सुरक्षा बनाए रखें।

## स्थानीय या क्लाउड

Codex CLI स्थानीय फ़ाइलों और कमांड पर काम करता है; Codex Cloud को सौंपे काम अलग वातावरण में चलते हैं। Claude Code Remote Control भी स्थानीय सत्र से जुड़ता है। दोबारा जुड़ना स्लीप के दौरान काम होने का प्रमाण नहीं है। pika काम को क्लाउड में नहीं भेजता।

[Codex CLI](https://learn.chatgpt.com/docs/codex/cli) · [Codex Cloud](https://learn.chatgpt.com/docs/cloud) · [Claude Code Remote Control](https://code.claude.com/docs/en/remote-control)

## पहले क्या जाँचें

आखिरी संदेश में अनुमति, सवाल, समाप्ति या त्रुटि देखें। फिर ऐप, Wi-Fi, VPN और लॉगिन जाँचें। नीचे के केवल पढ़ने वाले कमांड पावर अनुरोध और घटनाएँ दिखाते हैं, AI की प्रगति नहीं। कम CPU उपयोग भी विफलता का प्रमाण नहीं है।

```
pmset -g assertions
```

```
pmset -g log | tail -n 60
```

## तीन मिनट की जाँच

ढक्कन खुला रखकर लूप चलाएँ, टर्मिनल खुला छोड़ें और लगभग तीन मिनट लॉक करें। समय की तुलना करें और Ctrl+C से रोकें। बड़े अंतर को पावर लॉग और AI परिणामों से मिलाएँ। यह केवल साधारण प्रक्रिया जाँचता है; बंद ढक्कन का परीक्षण अलग करें।

```
while true; do date "+%Y-%m-%d %H:%M:%S"; sleep 10; done
```

## pika की सेटिंग

pika और सहायक सेवा स्थापित करें, Session ON करें, स्क्रीन आवश्यक न हो तो Monitor OFF रखें और ढक्कन बंद करें। स्क्रीन नीति ढक्कन बंद होने के बाद लागू होती है। Session OFF स्लीप रोकना हटाता है, तुरंत स्क्रीन बंद नहीं करता। बिजली और हवादार मेज का उपयोग करें, बंद बैग का नहीं। सुरक्षा या सेवा त्रुटि सत्र रोक सकती है।

[pika डाउनलोड करें](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg) · [इंस्टॉलेशन सहायता](https://no-sleep-pika.online/install/)

## आम सवाल

Monitor OFF AI समाप्त करने का आदेश नहीं है। tmux स्लीप नहीं रोकता; caffeinate नेटवर्क या अनुमति की समस्या नहीं सुलझाता। pika MCP की स्थिति सभी AI काम की प्रगति नहीं दर्शाती।

स्रोत और दायरा

5 अक्टूबर 2026 को आधिकारिक दस्तावेज़ और pika कोड जाँचे गए। pika निर्माता की गाइड; हर उपकरण पर लगातार चलने की गारंटी नहीं।

- [Apple · Sleep and wake settings](https://support.apple.com/guide/mac-help/set-sleep-and-wake-settings-mchle41a6ccd/mac)

- [OpenAI · Codex CLI](https://learn.chatgpt.com/docs/codex/cli)

- [OpenAI · Codex Cloud](https://learn.chatgpt.com/docs/cloud)

- [Anthropic · Claude Code Remote Control](https://code.claude.com/docs/en/remote-control)

no-sleep-pika निर्माता की अपनी ऐप सहित तुलना।

[pika डाउनलोड करें](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg)[Mac को स्लीप में जाने से कैसे रोकें: क्लैमशेल, caffeinate और pika →](https://no-sleep-pika.online/guide/hi/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/hi/mac-locked-ai-running/index.md)
