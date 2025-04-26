from flask import Flask, jsonify

from app.exception import AppException


def register_error_handlers(app: Flask):
    @app.errorhandler(AppException)
    def handle_app_exception(error):
        response = jsonify(error.to_dict())
        response.status = error.status
        return response

    @app.errorhandler(Exception)
    def handle_generic_exception(error):
        app.logger.error(f"Unhandled error: {error}")
        return jsonify({"error": "Có lỗi trong quá trình xử lý, vui lòng thử lại sau ít phút"}), 500
