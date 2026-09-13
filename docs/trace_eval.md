# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** Nguyễn Đức Minh  
> **Mã Sinh Viên / Mã Học viên:** 2A202602891  
> **Chủ đề Lựa chọn:** Gợi ý 2.1: Trợ lý Nhân sự VinFast (HR Assistant) — Tra cứu ngày phép còn lại, chính sách bảo hiểm và tạo đơn xin nghỉ phép  

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | 4 / 5 | Yêu cầu nghiệp vụ nhân sự thường gồm nhiều bước suy luận liên hoàn: Trước khi duyệt tạo đơn nghỉ phép cần tra cứu số ngày phép tồn, kiểm tra thời gian hợp lệ và quyền hạn phê duyệt của quản lý. |
| **2. Tool Interaction** | 5 / 5 | Bắt buộc phải tích hợp với hệ thống phần mềm quản lý nhân sự (HRMS) thông qua MCP Server để truy vấn dữ liệu ngày phép/bảo hiểm thực tế và lưu đơn xin nghỉ phép vào database. |
| **3. Dynamic Decision** | 4 / 5 | Quyết định hành động tiếp theo phụ thuộc trực tiếp vào Observation từ bước trước: Nếu nhân viên còn đủ ngày phép thì tiến hành tạo đơn; nếu vượt quá số ngày phép cho phép thì đề xuất chuyển sang nghỉ không lương hoặc yêu cầu điều chỉnh ngày. |
| **4. Long Horizon Goal** | 4 / 5 | Hệ thống phải duy trì ngữ cảnh và mục tiêu xuyên suốt phiên làm việc (hoàn tất quy trình nộp đơn nghỉ phép), đồng thời xử lý các tình huống biên như mã nhân viên không hợp lệ hoặc thiếu thông tin lý do. |
| **TỔNG ĐIỂM AGENTIC FIT** | **17 / 20** | *Tổng điểm 17/20 (> 12/20): Bài toán nghiệp vụ rất phù hợp để triển khai Agentic System với ReAct Loop.* |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
[
  {
    "step": 1,
    "action_type": "TOOL_EXECUTION",
    "tool_name": "academic_query",
    "arguments": {
      "student_id": "SV2026001"
    },
    "observation": {
      "status": "SUCCESS",
      "student_id": "SV2026001",
      "data": {
        "full_name": "Nguyễn Văn An",
        "gpa": 3.85
      }
    },
    "latency_ms": 120.5
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [ ] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).
- **Tổng số Test Cases đã chạy thành công:** ___ / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** ___ lượt.
- **Kết quả đẩy Repo nộp bài:** [ ] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
