import sys
import logging

def error_message_detail(error, sys):
    _, _, exc_tb = sys.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error in {file_name}, line {line_number}: {str(error)}"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, sys)
        logging.error(self.error_message)

    def __str__(self):
        return self.error_message
