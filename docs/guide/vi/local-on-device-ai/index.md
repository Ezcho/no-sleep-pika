Source: https://no-sleep-pika.online/guide/vi/local-on-device-ai/
Language: vi

MAC GUIDE · 2026-10-22

# Claude Code có phải AI cục bộ? Hiểu Llama, Qwen và AI trên thiết bị

Cài ứng dụng trên Mac không cho biết mô hình tính toán ở đâu. Phân biệt công cụ, mô hình và nơi thực thi.

Minh họa: tính toán trong thiết bị bên trái, kết nối máy chủ từ xa bên phải.

## Nơi cài và nơi tính toán

Claude Code có thể sửa tệp trong cửa sổ lệnh nhưng gửi yêu cầu tới mô hình từ xa. Nơi cài ứng dụng không chứng minh nơi tạo câu trả lời. Hãy tách công cụ, mô hình và địa điểm tính toán.

## Cục bộ và trên thiết bị

AI cục bộ thường chỉ mô hình trên máy tính hoặc máy chủ gần do bạn quản lý. AI trên thiết bị nhấn mạnh chính thiết bị đang dùng. Máy chủ riêng ở nhà không phải tính toán trong Mac. Tạo câu trả lời gọi là suy luận, khác với huấn luyện. Bạn không cần huấn luyện từ đầu; cách dùng thuật ngữ có thể khác giữa sản phẩm.

## Công cụ khác mô hình

Claude Code xử lý tệp và lệnh. Llama, Qwen là các họ mô hình với kích thước và khả năng khác nhau. Ollama chạy hoặc kết nối mô hình, có tài liệu kết nối Claude Code với mô hình cục bộ và đám mây. Không phải mọi mô hình hỗ trợ cùng công cụ. Bảng so sánh vai trò, không xếp hạng hiệu năng.

Công cụ khác mô hình
| Tên | Vai trò | Cần kiểm tra
| Claude Code | Công cụ xử lý tệp và lệnh | Nơi mô hình kết nối chạy
| Llama · Qwen | Các họ mô hình | Chạy cục bộ hay máy chủ
| Ollama | Chạy hoặc kết nối mô hình | Mô hình cục bộ hay đám mây

## Điều gì thay đổi khi chạy cục bộ?

Khi mô hình và phần mềm đã sẵn sàng, suy luận cục bộ có thể hoạt động ngoại tuyến. Tìm kiếm web, dịch vụ ngoài và tải xuống vẫn cần mạng.

Bộ nhớ và tốc độ phụ thuộc kích thước, cách nén và lượng hội thoại xử lý. Cục bộ không luôn nhanh hơn. Tránh phí tạo câu trả lời từ dịch vụ ngoài không loại bỏ chi phí thiết bị, điện và bảo trì.

Xử lý tại máy không bảo đảm đồng bộ, nhật ký hay tiện ích không gửi dữ liệu.

## Ba bước kiểm tra

Đầu tiên, kiểm tra mô hình và địa chỉ kết nối: Llama hoặc Qwen cũng có thể do máy chủ cung cấp; Ollama hỗ trợ cả hai cách.

Tiếp theo, tách các tính năng cần mạng. Sau khi chuẩn bị, khi không có việc quan trọng đang chạy, thử hỏi câu ngắn mới lúc ngắt mạng. Điều này không chứng minh ứng dụng không gửi dữ liệu khi dùng bình thường.

Cuối cùng, đọc cài đặt và tài liệu. Chế độ cục bộ Ollama tắt mô hình đám mây và tìm kiếm web của nó, không chặn mạng của ứng dụng khác. Bắt đầu bằng tài liệu ngắn không nhạy cảm.

## Vai trò của pika

Chế độ ngủ có thể ngắt hoặc làm chậm việc tại máy, khác với tác vụ máy chủ độc lập. pika không chạy mô hình hay biến đám mây thành cục bộ; nó giữ Mac thức. Kiểm tra dịch vụ hỗ trợ, bật Session và thử đóng rồi mở nắp trong thời gian ngắn. Cắm nguồn, đặt trên bàn thông thoáng, xong thì tắt Session.

[Tải pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg) · [Trợ giúp cài đặt](https://no-sleep-pika.online/install/)

Nguồn và phạm vi

Hướng dẫn của người tạo pika, kiểm tra nguồn chính thức ngày 22/10/2026. Không phải đo kiểm mọi mô hình hoặc Mac; khả năng tương thích thay đổi theo phiên bản.

- [Anthropic · Claude Code overview](https://code.claude.com/docs/en/overview)

- [Ollama · Claude Code integration](https://docs.ollama.com/integrations/claude-code)

- [Ollama · Local-only mode and data](https://docs.ollama.com/faq)

- [Qwen · Run locally with Ollama](https://qwen.readthedocs.io/en/latest/run_locally/ollama.html)

- [Meta · Llama models](https://github.com/meta-llama/llama-models)

Do nhà phát triển no-sleep-pika viết, có giới thiệu ứng dụng của mình.

[Tải pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg)[Cách giữ Mac không ngủ: clamshell, caffeinate và pika →](https://no-sleep-pika.online/guide/vi/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/vi/local-on-device-ai/index.md)
