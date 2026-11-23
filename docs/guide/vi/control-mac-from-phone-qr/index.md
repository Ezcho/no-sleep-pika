Source: https://no-sleep-pika.online/guide/vi/control-mac-from-phone-qr/
Language: vi

MAC GUIDE · 2026-11-23

# Điều khiển Mac bằng QR: phiên, hẹn giờ và tắt máy từ điện thoại

pika 1.3.0 cho phép đổi Session và điều kiện nguồn điện trên điện thoại sau khi bạn chấp thuận ngay trên Mac.

## Không chỉ xem trạng thái

Để Mac tiếp tục build hoặc tải xuống, rồi dùng điện thoại đổi Session, đặt hẹn giờ hay yêu cầu tắt và khởi động lại. pika 1.3.0 bổ sung điều khiển vào trang trạng thái QR.

Tính năng này không gửi lệnh mới cho AI, không hiển thị hội thoại, đầu ra terminal, phần trăm công việc hay màn hình điều khiển từ xa.

## Cập nhật ứng dụng Mac trước

Chạy pika 1.3.0 trở lên trên Mac. Chống ngủ khi đóng nắp cần dịch vụ hỗ trợ hoạt động bình thường. Cả hai thiết bị cần internet.

Nếu macOS không xác minh được nhà phát triển, kiểm tra tệp đến từ trang chính thức. Sau khi thử mở, vào Cài đặt hệ thống → Quyền riêng tư & Bảo mật → Vẫn mở cho tệp đó rồi làm theo xác nhận của macOS. Tên có thể khác; xem hướng dẫn cài đặt. Không tắt bảo vệ toàn hệ thống và không áp dụng cách này cho cảnh báo phần mềm độc hại hoặc tệp hỏng.

[Tải pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.3.0/pika-1.3.0.pkg) · [Trợ giúp cài đặt](https://no-sleep-pika.online/install/)

## Quét rồi chấp thuận trên Mac

Yêu cầu tạo QR pika trong cuộc trò chuyện AI đã nối công cụ pika qua MCP. Quét bằng camera trong năm phút rồi bấm kết nối Mac. QR dùng một lần; ban đầu chỉ được xem trạng thái và Session không tự bật.

Yêu cầu quyền điều khiển trên điện thoại, rồi chấp thuận cửa sổ trên Mac. Làm trước khi rời đi, lúc thấy cả hai thiết bị. Không có chấp thuận từ Mac thì không điều khiển được. Trang chủ có hướng dẫn nối MCP lần đầu.

Nút trên điện thoại hiện bằng tiếng Hàn: “이 Mac에 연결” để nối, “Mac에 제어 허용 요청” để xin quyền, rồi chấp thuận trên Mac. “예약·카운트다운 취소” hủy lịch và đếm ngược. Xem hướng dẫn dưới đây để nối MCP lần đầu.

[Hướng dẫn kết nối MCP →](https://no-sleep-pika.online/vi/#mcp)

## Những gì có thể điều khiển

Session bật hoặc giải phóng chống ngủ. Monitor chỉ đổi được khi Session ON; cấu hình màn hình ở chế độ đóng nắp áp dụng sau khi đóng. Giá trị Monitor là thiết lập đã yêu cầu, không phải xác nhận màn hình thực tế.

Chọn chỉ duy trì khi cắm nguồn, dừng Session khi rút sạc, hoặc ở mức pin 30, 40, 50%. Bảo vệ pin và nhiệt hiện có vẫn hoạt động. Nhiệt là mức trạng thái macOS, không phải số °C.

## Hẹn giờ và 60 giây để hủy

Chọn 15, 30, 60, 180 hoặc 360 phút, rồi giải phóng Session, ngủ, tắt máy hoặc khởi động lại. Giải phóng Session không buộc ứng dụng đóng.

Tắt hoặc khởi động lại ngay cần xác nhận, sau đó Mac đếm ngược 60 giây và có thể hủy. Dùng nút hủy lịch/đếm ngược nếu đổi ý. pika khôi phục thiết lập ngủ trước. Hộp thoại tài liệu chưa lưu có thể trì hoãn hoặc hủy thao tác: gửi yêu cầu không có nghĩa là đã xong.

## Quyền đi cùng kết nối

Quyền chỉ dành cho kết nối đang được duyệt. Ngắt kết nối hoặc thu hồi quyền hủy hẹn giờ từ xa và đếm ngược; kết nối mới cần duyệt lại. Tối đa 24 giờ từ lúc tạo QR. Hẹn giờ không tiếp tục sau khi thoát pika hoặc Mac ngủ.

Phát hiện mất kết nối có thể mất hàng chục giây. Để ngăn tắt máy, bấm “예약·카운트다운 취소” và xác nhận trạng thái đã hủy thay vì chỉ ngắt kết nối. Hẹn giờ từ xa cần tín hiệu kết nối liên tục từ trình duyệt; đưa trình duyệt xuống nền có thể làm mất kết nối và hủy hẹn giờ.

Không chia sẻ QR. Thử thay đổi Session đơn giản và hủy trước. Trang mất kết nối có thể chỉ hiện trạng thái cũ, không chứng minh Mac đã tắt. Mạng và việc AI hoàn tất không được bảo đảm.

Nguồn và phạm vi

Hướng dẫn do nhà phát triển no-sleep-pika viết cho ứng dụng 1.3.0 ngày 23 tháng 11 năm 2026. Xem thêm hướng dẫn chính thức của Apple về cảnh báo cài đặt.

- [pika 1.3.0 · Release notes](https://github.com/Ezcho/no-sleep-pika/releases/tag/v1.3.0)

- [pika · Remote connection and permissions](https://github.com/Ezcho/no-sleep-pika/blob/v1.3.0/Remote/README.md)

- [Apple · Safely open apps on your Mac](https://support.apple.com/en-us/102445)

Do nhà phát triển no-sleep-pika viết, có giới thiệu ứng dụng của mình.

[Tải pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.3.0/pika-1.3.0.pkg)[Cách giữ Mac không ngủ: clamshell, caffeinate và pika →](https://no-sleep-pika.online/guide/vi/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/vi/control-mac-from-phone-qr/index.md)
