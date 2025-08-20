#  here we will setup our logging
import os
import sys
import logging

logging_str = '[%(asctime)s - %(levelname)s - %(module)s - %(message)s]'
log_dir = "logs"
log_filepath = os.path.join(log_dir,"logging.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[logging.FileHandler(log_filepath),logging.StreamHandler(sys.stdout)] # stream handler will help in showing the message in our terminal when we run the program
)

logger = logging.getLogger("datasciencelogger")  # used for calling in other file 