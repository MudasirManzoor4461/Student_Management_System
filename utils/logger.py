import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/student_management.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)