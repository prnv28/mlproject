import sys
import logger

def error_message_detail(error,error_detail:sys):
    """
    This function is used to format the error message with details.
    """
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in script [{0}] at line number [{1}] with message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    return error_message

class CustomException(Exception):
    """
    Custom exception class to handle exceptions with detailed error messages.
    """
    def __init__ (self,error,error_detail:sys):
        super().__init__(error)
        self.error_message = error_message_detail(error,error_detail)    

    def __str__(self):
        return self.error_message
    
if __name__ == "__main__":
    try:
        1/0
    except Exception as e:
        logger.logging.info("Divide by zero")
        raise CustomException(e,sys)
    
