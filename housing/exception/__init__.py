import os 
import sys

class HousingException(Exception):
    
    def __init__(self, error_messaage:Exception,  error_details:sys):
        super().__init__(error_messaage)
        self.error_message=error_messaage

    @staticmethod
    def get_detailed_error_message(error_messaage:Exception,  error_details:sys)->str:
        """
        error_message: Exception object
        error_detail: object of sys module
        """
        _,_ ,exec_tb = error_details.exc_info()
        line_number = exec_tb.tb_frame.f_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename
        error_messaage = f"Error occured in scrip: [{file_name}] at line number: [{line_number}] error message: [{error_messaage}]"
        return error_messaage