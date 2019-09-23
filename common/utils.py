import json
import logging
import logging.handlers

import requests

from conf.config import cf, logs_log


def phone(phone_number):
    '''
    手机号码脱敏
    :param phone_number:
    :return: '135******86'
    '''
    return phone_number[:3] + '******' + phone_number[9:]


def get_logger(logger_name):
    '''
    日志
    :param logger_name:
    :return:
    '''
    logger = logging.getLogger(logger_name)
    if not logger.handlers:
        logger.setLevel('DEBUG')  # 直接设置为最低
        # 定义输出格式
        fmt = cf.get_section_option("log", "formatter")
        formate = logging.Formatter(fmt)

        file_handler = logging.handlers.RotatingFileHandler(logs_log, maxBytes=20 * 1024 * 1024, backupCount=10,
                                                            encoding="utf-8")
        level = cf.get_section_option('log', 'file_handler')
        file_handler.setLevel(level)
        file_handler.setFormatter(formate)

        console_handler = logging.StreamHandler()
        level = cf.get_section_option('log', 'console_handler')
        console_handler.setLevel(level)
        console_handler.setFormatter(formate)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

def xiao_ding(err):
    header = {
        "Content-Type": "application/json"
    }
    my_data = {
        "msgtype": "text",
        "text": {
            "content": ""
        }
    }

    my_data['text']['content'] = err
    my_url = "https://oapi.dingtalk.com/robot/send?access_token=%s" % cf.access_token

    send_data = json.dumps(my_data)
    # res = requests.post(url=my_url, data=send_data, headers=header)
    # return res
