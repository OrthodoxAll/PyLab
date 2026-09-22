import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    filename='logs/log.log',  # Запись логов в файл
                    filemode='w')  # Перезапись файла при каждом запуске

utils_logger = logging.getLogger('utils')

masks_logger = logging.getLogger('masks')



