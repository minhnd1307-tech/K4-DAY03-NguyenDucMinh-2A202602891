"""
🛠️ TOOL DEFINITIONS & EXECUTION BACKEND
Mã nguồn chứa danh sách Tool Schemas (JSON Schema) và Execution Layer phục vụ cho MCP Server.
"""

import json
from typing import Dict, Any

# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA (TASK 1.2)
# ==============================================================================

TOOLS_SCHEMA = [
    # Tool 1: Đã được định nghĩa mẫu sẵn cho Học viên tham khảo
    {
        "name": "academic_query",
        "description": "Tra cứu hồ sơ và thông tin học vụ của sinh viên VinUni bằng mã sinh viên.",
        "parameters": {
            "type": "object",
            "properties": {
                "student_id": {
                    "type": "string",
                    "description": "Mã sinh viên cần tra cứu (ví dụ: 'SV2026001')"
                }
            },
            "required": ["student_id"]
        }
    },
    
    # --------------------------------------------------------------------------
    # TODO 1.2: HỌC VIÊN HOÀN THIỆN TOOL SCHEMA CHO 'schedule_appointment'
    # --------------------------------------------------------------------------
    {
        "name": "schedule_appointment",
        "description": "Đặt lịch hẹn tư vấn học vụ với Cố vấn học tập VinUni.",
        "parameters": {
            "type": "object",
            "properties": {
                "student_id": {
                    "type": "string",
                    "description": "Mã sinh viên cần đặt lịch (ví dụ: 'SV2026001')"
                },
                "datetime_str": {
                    "type": "string",
                    "description": "Thời gian hẹn (ví dụ: '14:00 15/09/2026')"
                },
                "advisor_name": {
                    "type": "string",
                    "description": "Tên cố vấn học tập (ví dụ: 'PGS.TS Nguyễn Văn A')"
                }
            },
            "required": ["student_id", "datetime_str", "advisor_name"]
        }
    },
    
    # ==========================================================================
    # CÔNG CỤ CHO ĐỀ TÀI 2.1: TRỢ LÝ NHÂN SỰ VINFAST (VINFAST HR ASSISTANT)
    # ==========================================================================
    # Tool 3: Tra cứu hồ sơ nhân viên, số ngày phép và chính sách bảo hiểm
    {
        "name": "hr_leave_query",
        "description": "Tra cứu thông tin nhân sự, số ngày phép năm còn lại và chính sách bảo hiểm của nhân viên VinFast bằng mã nhân viên.",
        "parameters": {
            "type": "object",
            "properties": {
                "employee_id": {
                    "type": "string",
                    "description": "Mã nhân viên VinFast cần tra cứu (ví dụ: 'VF2026001', 'VF2026002')"
                }
            },
            "required": ["employee_id"]
        }
    },
    # Tool 4: Tạo đơn xin nghỉ phép vào hệ thống nhân sự
    {
        "name": "create_leave_request",
        "description": "Tạo đơn xin nghỉ phép trên hệ thống quản trị nhân sự VinFast.",
        "parameters": {
            "type": "object",
            "properties": {
                "employee_id": {
                    "type": "string",
                    "description": "Mã nhân viên VinFast xin nghỉ phép (ví dụ: 'VF2026001')"
                },
                "leave_type": {
                    "type": "string",
                    "description": "Loại nghỉ phép (ví dụ: 'Nghỉ phép năm', 'Nghỉ ốm', 'Nghỉ dưỡng sức', 'Nghỉ việc riêng')"
                },
                "start_date": {
                    "type": "string",
                    "description": "Thời gian hoặc ngày bắt đầu nghỉ (ví dụ: '15/09/2026' hoặc '20/09/2026')"
                },
                "duration_days": {
                    "type": "integer",
                    "description": "Số ngày xin nghỉ phép (ví dụ: 1, 2)"
                },
                "reason": {
                    "type": "string",
                    "description": "Lý do xin nghỉ phép"
                }
            },
            "required": ["employee_id", "leave_type", "start_date"]
        }
    }
]

# ==============================================================================
# 2. MÔ PHỎNG DỮ LIỆU & HÀM THỰC THI TOOL (EXECUTION LAYER)
# ==============================================================================

MOCK_DATABASE = {
    "SV2026001": {
        "full_name": "Nguyễn Văn An",
        "class": "AI-K4",
        "gpa": 3.85,
        "email": "an.nv@vinuni.edu.vn",
        "status": "Đang học",
        "advisor": "PGS.TS Nguyễn Văn A"
    },
    "SV2026002": {
        "full_name": "Trần Thị Bình",
        "class": "AI-K4",
        "gpa": 3.60,
        "email": "binh.tt@vinuni.edu.vn",
        "status": "Đang học",
        "advisor": "TS. Lê Thị B"
    }
}

# Cơ sở dữ liệu nhân viên VinFast phục vụ Đề tài 2.1
VINFAST_HR_DATABASE = {
    "VF2026001": {
        "full_name": "Nguyễn Đức Minh",
        "department": "Khối Nghiên cứu & Phát triển Xe điện (VinFast R&D)",
        "position": "Kỹ sư Tác tử AI (AI Agent Engineer)",
        "email": "minh.nd@vinfast.vn",
        "annual_leave_balance": 12,
        "insurance_tier": "Bảo hiểm Sức khỏe Vingroup VIP (PTI Toàn diện)",
        "manager": "Ông Lê Hoàng Nam - Trưởng phòng R&D"
    },
    "VF2026002": {
        "full_name": "Trần Thị Bình",
        "department": "Khối Vận hành Sản xuất & Chuỗi cung ứng (VinFast Manufacturing)",
        "position": "Chuyên viên Quản lý Chất lượng QC",
        "email": "binh.tt@vinfast.vn",
        "annual_leave_balance": 5,
        "insurance_tier": "Bảo hiểm Sức khỏe Vingroup Tiêu chuẩn",
        "manager": "Bà Nguyễn Thu Trang - Quản đốc Phân xưởng"
    }
}


def execute_academic_query(student_id: str) -> str:
    """Thực thi tra cứu học vụ theo mã sinh viên"""
    student = MOCK_DATABASE.get(student_id.strip().upper())
    if student:
        return json.dumps({
            "status": "SUCCESS",
            "student_id": student_id,
            "data": student
        }, ensure_ascii=False)
    else:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy dữ liệu sinh viên có mã '{student_id}'"
        }, ensure_ascii=False)


def execute_schedule_appointment(student_id: str, datetime_str: str, advisor_name: str = "PGS.TS Nguyễn Văn A") -> str:
    """Thực thi đặt lịch hẹn tư vấn học vụ"""
    return json.dumps({
        "status": "SUCCESS",
        "booking_id": f"BK-{student_id}-99",
        "student_id": student_id,
        "datetime": datetime_str,
        "advisor": advisor_name,
        "message": f"Đặt lịch thành công cho sinh viên {student_id} với {advisor_name} vào lúc {datetime_str}."
    }, ensure_ascii=False)


def execute_hr_leave_query(employee_id: str, **kwargs) -> str:
    """Thực thi tra cứu thông tin nhân sự và ngày phép nhân viên VinFast"""
    clean_id = employee_id.strip().upper()
    emp = VINFAST_HR_DATABASE.get(clean_id)
    if emp:
        return json.dumps({
            "status": "SUCCESS",
            "employee_id": clean_id,
            "data": emp,
            "message": f"Thông tin nhân viên {clean_id} ({emp['full_name']}): Thuộc {emp['department']}, chức vụ {emp['position']}. Số ngày phép năm còn lại: {emp['annual_leave_balance']} ngày. Gói phúc lợi: {emp['insurance_tier']}. Quản lý trực tiếp: {emp['manager']}."
        }, ensure_ascii=False)
    else:
        return json.dumps({
            "status": "NOT_FOUND",
            "employee_id": clean_id,
            "message": f"Không tìm thấy thông tin nhân viên có mã '{clean_id}' trong hệ thống nhân sự VinFast."
        }, ensure_ascii=False)


def execute_create_leave_request(employee_id: str, leave_type: str = "Nghỉ phép năm", start_date: str = "", duration_days: int = 1, reason: str = "Việc cá nhân", **kwargs) -> str:
    """Thực thi tạo đơn xin nghỉ phép trên hệ thống VinFast HR"""
    clean_id = employee_id.strip().upper()
    actual_date = start_date or kwargs.get("from_date") or kwargs.get("date") or "thời gian yêu cầu"
    actual_days = duration_days if duration_days else kwargs.get("days", 1)
    actual_type = leave_type or kwargs.get("type", "Nghỉ phép năm")
    actual_reason = reason or kwargs.get("note", "Việc cá nhân")

    emp = VINFAST_HR_DATABASE.get(clean_id)
    emp_name = emp["full_name"] if emp else f"Nhân viên {clean_id}"

    return json.dumps({
        "status": "SUCCESS",
        "request_id": f"LR-{clean_id}-2026",
        "employee_id": clean_id,
        "employee_name": emp_name,
        "leave_type": actual_type,
        "start_date": actual_date,
        "duration_days": actual_days,
        "reason": actual_reason,
        "message": f"Tạo đơn xin nghỉ phép thành công cho {emp_name} ({clean_id}): Loại '{actual_type}', thời gian: {actual_date} ({actual_days} ngày). Lý do: '{actual_reason}'. Đơn đã được chuyển đến Quản lý trực tiếp để xét duyệt."
    }, ensure_ascii=False)


# Router gọi tool thực tế
TOOL_ROUTER = {
    "academic_query": execute_academic_query,
    "schedule_appointment": execute_schedule_appointment,
    "hr_leave_query": execute_hr_leave_query,
    "create_leave_request": execute_create_leave_request
}

def dispatch_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
    """Hàm trung chuyển thực thi tool"""
    if tool_name in TOOL_ROUTER:
        try:
            return TOOL_ROUTER[tool_name](**arguments)
        except Exception as e:
            return json.dumps({"status": "EXECUTION_ERROR", "error": str(e)}, ensure_ascii=False)
    return json.dumps({"status": "UNKNOWN_TOOL", "error": f"Tool '{tool_name}' không tồn tại!"}, ensure_ascii=False)

