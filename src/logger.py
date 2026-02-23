import logging
import os
from datetime import datetime


# Create log file name using timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create logs directory path
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Create logs directory if not exists
os.makedirs(os.path.dirname(logs_path), exist_ok=True)


# Configure logging
logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has started")