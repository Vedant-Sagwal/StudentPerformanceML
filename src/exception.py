import sys
import logging

def error_msg_details(error, error_detail:sys):
    _,_, tb_obj = sys.exc_info()
    error_message = "Error Occured at file {0}, line no {1}, with the error message : {2}".format(
        tb_obj.tb_frame.f_code.co_filename, tb_obj.tb_frame.f_lineno, str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message = error_msg_details(error_message, error_detail=error_details)
    def __str__(self):
        return self.error_message


# if __name__ == "__main__":
#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info("Divide By Zero Error!!")
#         raise CustomException(e, sys)