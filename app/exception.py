class AppException(Exception):
    status = 500
    msg = "Có lỗi trong quá trình xử lý, vui lòng thử lại sau ít phút"

    def __init__(self, msg=None):
        if msg:
            self.msg = msg

    def to_dict(self):
        return {
            "status": self.status,
            "msg": self.msg
        }


class DatabaseException(AppException):
    status = 500
    msg = "Kết nối hệ thống lỗi, vui lòng thử lại sau ít phút"


class WrongParamException(AppException):
    status = 400
    msg = "Sai thông tin đầu vào, vui lòng kiểm tra lại thông tin"


class RateLimitException(AppException):
    status = 429
    msg = "Bạn truy cập quá nhanh."


class TokenRequiredException(AppException):
    status = 401
    msg = "Token không tồn tại"


class TokenExpiredException(AppException):
    status = 401
    msg = "Token hết hạn"


class InvalidTokenException(AppException):
    status = 401
    msg = "Token không hợp lệ"


class SystemBusyException(AppException):
    status = 503
    msg = "Hệ thống đang bận, vui lòng thử lại sau ít phút"


class SystemErrorException(AppException):
    status = 500
    msg = "Có lỗi trong quá trình xử lý, vui lòng thử lại sau ít phút"
