ls -l 
rm /home/test/test/csv
echo "this is test running "

import subprocess
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

try:
    # Equivalent to ls -l
    subprocess.run(["ls", "-l"], check=True)
    logging.info("Command 'ls -l' executed successfully.")

    # Equivalent to rm /home/test/test.csv
    file_path = "/home/test/test.csv"
    if os.path.exists(file_path):
        os.remove(file_path)
        logging.info(f"File {file_path} removed successfully.")
    else:
        logging.warning(f"File {file_path} does not exist.")

    # Equivalent to echo "this is test running"
    print("this is test running")

    # $? in shell represents the exit status of the last command. In Python, you can access this via the return value of subprocess.run().
    result = subprocess.run(["echo", "$?"], capture_output=True, text=True, check=True)
    exit_status = result.returncode
    logging.info(f"Exit status: {exit_status}")

except subprocess.CalledProcessError as e:
    logging.error(f"Error executing command: {e}")
except OSError as e:
    logging.error(f"Error removing file {file_path}: {e}")
except Exception as e:
    logging.error(f"An error occurred: {e}")
