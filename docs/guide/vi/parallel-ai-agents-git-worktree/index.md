Source: https://no-sleep-pika.online/guide/vi/parallel-ai-agents-git-worktree/
Language: vi

MAC GUIDE · 2026-11-24

# Hai tác nhân AI cùng sửa một tệp? Hãy tách thư mục trước.

Git worktree tạo thư mục làm việc riêng cho từng tác nhân. Chia việc, kiểm tra thay đổi rồi lần lượt hợp nhất để tránh trộn công việc chưa xong.

## Vì sao dùng chung thư mục dễ chồng chéo

Một tác nhân sửa giao diện, tác nhân kia viết kiểm thử. Nếu chung thư mục, cả hai vẫn đọc và sửa cùng các tệp. Tạo hai tên nhánh không tạo hai bộ tệp độc lập trong thư mục đó. Chuyển nhánh ở đây cũng đổi các tệp tác nhân kia đang dùng.

Git worktree thêm thư mục làm việc vào cùng kho mã. Mỗi thư mục có thể có nhánh và tệp riêng nhưng chia sẻ lịch sử. Cách này tách công việc đang làm, không bảo đảm hết xung đột khi hợp nhất sau đó.

- 1 Tách thư mục

- 2 Giao nhiệm vụ

- 3 Kiểm tra thay đổi

- 4 Hợp nhất lần lượt

## Chuẩn bị điểm xuất phát đã kiểm tra

Chạy lệnh dưới đây trong dự án Git hiện có. Cần ít nhất một commit; HEAD trỏ tới điểm xuất phát đã lưu vào Git. Không có đầu ra nghĩa là không báo thay đổi hoặc tệp chưa được theo dõi. Tệp bị bỏ qua vẫn có thể tồn tại.

Nếu có danh sách, kiểm tra trước. Chỉ commit thay đổi cần thiết đã xem xét hoặc chọn một commit có sẵn. Đừng thêm cả thư mục mà không kiểm tra thông tin bí mật và việc ngoài phạm vi. Thư mục mới bắt đầu từ HEAD, không mang theo chỉnh sửa chưa commit.

```
git status --short
```

## Tạo hai thư mục làm việc

Chạy cả hai lệnh từ dự án gốc để tạo nhánh ai-ui, ai-tests và hai thư mục bên cạnh. Tên nhánh và đường dẫn phải chưa được sử dụng. Nếu đã có, chọn tên khác thay vì ghi đè cưỡng bức.

Các thư viện đã cài, tệp .env bị bỏ qua và cấu hình cục bộ không tự động được sao chép đầy đủ. Chuẩn bị theo hướng dẫn dự án, chỉ cấp thông tin xác thực cần thiết và dùng cổng khác nhau cho các máy chủ chạy cùng lúc. Worktree không phải vùng cách ly bảo mật: công cụ có quyền vẫn có thể truy cập thư mục khác.

```
git worktree add -b ai-ui ../project-ai-ui HEAD
git worktree add -b ai-tests ../project-ai-tests HEAD
```

## Giao rõ thư mục và phạm vi

Mở một tác nhân ở project-ai-ui, tác nhân kia ở project-ai-tests. Ghi rõ đường dẫn tuyệt đối và nhiệm vụ hẹp: “chỉ sửa thành phần giao diện” và “thêm kiểm thử cho hành vi hiện có, không sửa mã ứng dụng”.

Chỉ định người phụ trách các tệp chung như danh sách thư viện và tệp khóa phiên bản. Nếu cả hai phải sửa cùng tệp, làm lần lượt. Yêu cầu báo cáo tệp đã đổi, kiểm tra đã chạy và phần còn lại.

## Kiểm tra rồi hợp nhất từng nhánh

Chạy ba lệnh dưới đây ở từng thư mục. Status liệt kê thay đổi và tệp chưa theo dõi. Diff hiển thị sửa đổi chưa đưa vào vùng chuẩn bị commit của tệp đã theo dõi; diff --cached hiển thị phần đã chuẩn bị. Tệp mới chưa theo dõi không xuất hiện trong các diff này, cần mở riêng để xem.

Chạy kiểm tra phù hợp và commit thay đổi đã duyệt vào từng nhánh. Về dự án gốc, xem xét và hợp nhất từng nhánh vào nhánh đích. Worktree không tự động hợp nhất kết quả. Giải quyết xung đột và kiểm tra kết quả chung trước khi thêm nhánh tiếp theo.

```
git status --short
git diff
git diff --cached
```

## pika giúp ở đâu

pika giúp Mac duy trì trạng thái thức khi AI chạy cục bộ, tùy cài đặt phiên và cơ chế bảo vệ. Nó không giao việc, hợp nhất nhánh hay giải quyết xung đột. QR của pika 1.3 hiển thị trạng thái Mac và điều khiển nguồn được phép, không phải đầu ra AI hay tỷ lệ hoàn thành chính xác. Hãy đánh giá bằng kết quả tác nhân và kiểm tra dự án.

[Tải pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.3.0/pika-1.3.0.pkg) · [Trợ giúp cài đặt](https://no-sleep-pika.online/install/)

Nguồn và phạm vi bài viết

Bài viết của nhà phát triển no-sleep-pika dựa trên tài liệu Git chính thức, nói về tác nhân nói chung, không giả định tính năng hay quyền của sản phẩm cụ thể. Hãy tuân thủ thêm quy tắc đóng góp và bảo vệ bí mật của dự án.

- [Git · git-worktree](https://git-scm.com/docs/git-worktree)

- [Git · git-status](https://git-scm.com/docs/git-status)

- [Git · git-diff](https://git-scm.com/docs/git-diff)

Do nhà phát triển no-sleep-pika viết, có giới thiệu ứng dụng của mình.

[Cách giữ Mac không ngủ: clamshell, caffeinate và pika →](https://no-sleep-pika.online/guide/vi/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/vi/parallel-ai-agents-git-worktree/index.md)
