Source: https://no-sleep-pika.online/guide/vi/mac-locked-ai-running/
Language: vi

MAC GUIDE · 2026-10-05

# Mac đã khóa: Claude Code và Codex có tiếp tục chạy không?

Phân biệt khóa màn hình, tắt màn hình và ngủ hệ thống để kiểm tra tác vụ AI cục bộ.

## Khóa khác với ngủ

Màn hình mật khẩu không chứng minh tác vụ đã dừng. Lệnh nền có thể tiếp tục khi Mac còn thức, ứng dụng mở và kết nối cần thiết hoạt động. Tự động hóa giao diện hoặc xác thực có thể cần mở khóa. Máy cũng có thể ngủ sau khi khóa. Hãy giữ bảo vệ mật khẩu.

## Cục bộ hay đám mây

Codex CLI xử lý tệp và lệnh cục bộ; tác vụ giao cho Codex Cloud chạy ở môi trường khác. Claude Code Remote Control vẫn kết nối phiên cục bộ. Kết nối lại không có nghĩa là đã chạy trong lúc ngủ. pika không chuyển tác vụ lên đám mây.

[Codex CLI](https://learn.chatgpt.com/docs/codex/cli) · [Codex Cloud](https://learn.chatgpt.com/docs/cloud) · [Claude Code Remote Control](https://code.claude.com/docs/en/remote-control)

## Kiểm tra nguyên nhân

Đọc thông báo cuối: chờ duyệt, câu hỏi, hoàn tất hay lỗi. Sau đó kiểm tra ứng dụng, Wi-Fi, VPN và đăng nhập. Lệnh chỉ đọc bên dưới hiển thị yêu cầu nguồn và sự kiện, không chứng minh tiến độ AI. CPU thấp cũng không chứng minh lỗi.

```
pmset -g assertions
```

```
pmset -g log | tail -n 60
```

## Thử trong ba phút

Mở nắp, chạy vòng lặp, giữ terminal mở và khóa khoảng ba phút. So sánh thời gian, dừng bằng Ctrl+C. Đối chiếu khoảng trống với nhật ký nguồn và kết quả AI. Đây chỉ là kiểm tra tiến trình đơn giản; cần thử đóng nắp riêng.

```
while true; do date "+%Y-%m-%d %H:%M:%S"; sleep 10; done
```

## Thiết lập pika

Cài pika và dịch vụ hỗ trợ, bật Session, để Monitor OFF nếu không cần màn hình, rồi đóng nắp. Chính sách màn hình áp dụng sau khi đóng. Session OFF bỏ ngăn ngủ mà không tắt ngay màn hình. Dùng nguồn điện và bàn thoáng, không đặt trong túi kín. Bảo vệ hoặc lỗi dịch vụ có thể dừng phiên.

[Tải pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg) · [Trợ giúp cài đặt](https://no-sleep-pika.online/install/)

## Câu hỏi thường gặp

Monitor OFF không kết thúc AI. tmux không ngăn ngủ; caffeinate không xử lý mạng hoặc chờ duyệt. Trạng thái pika MCP không phản ánh mọi tác vụ AI.

Nguồn và phạm vi

Đối chiếu tài liệu chính thức và mã pika ngày 5 tháng 10 năm 2026. Hướng dẫn do nhà phát triển pika viết, không bảo đảm chạy liên tục trên mọi máy.

- [Apple · Sleep and wake settings](https://support.apple.com/guide/mac-help/set-sleep-and-wake-settings-mchle41a6ccd/mac)

- [OpenAI · Codex CLI](https://learn.chatgpt.com/docs/codex/cli)

- [OpenAI · Codex Cloud](https://learn.chatgpt.com/docs/cloud)

- [Anthropic · Claude Code Remote Control](https://code.claude.com/docs/en/remote-control)

Do nhà phát triển no-sleep-pika viết, có giới thiệu ứng dụng của mình.

[Tải pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg)[Cách giữ Mac không ngủ: clamshell, caffeinate và pika →](https://no-sleep-pika.online/guide/vi/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/vi/mac-locked-ai-running/index.md)
