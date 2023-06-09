import os
import sys
from modules.app import run_main_loop
from modules.utils import clear_screen
from modules.utils import ExitException
from modules.custom_logger import CustomLogger

if __name__ == '__main__':
    # Initialize the singleton logger - used everywhere
    logger = CustomLogger("gpt4_shell")  

    # Get API Key
    API_KEY = os.environ.get('GPT4_API_KEY')
    if not API_KEY:
        log_entry = f"Error: API key not found in environment variables"
        logger.log_and_print(log_entry, log_type="error", style="bold red")
        sys.exit()

    clear_screen()

    # Start main loop and handle all exceptions, exit on exception   
    try:
        run_main_loop(API_KEY) # main loop from app.py
    except ExitException:
        log_message = "Exiting the program."
        logger.log_and_print(log_message, style="bold yellow")
        sys.exit(0)
    except KeyboardInterrupt:
        log_message = "Detected keyboard interrupt. Exiting the program."
        logger.log_and_print(log_message, style="bold yellow")
        sys.exit(0)
    except Exception as e:
        log_message = f"An unexpected error occurred: {e}"
        logger.log_and_print(log_message, log_type="exception", style="bold red")
        sys.exit(1)