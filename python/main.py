import logging
import os
from logging.config import fileConfig


if __name__ == '__main__':
    # 初始化 logger
    logging_config_file_path = os.path.join(os.path.dirname(__file__), 'logging_config.ini')
    logging.config.fileConfig(logging_config_file_path)
    logger = logging.getLogger(__name__)
