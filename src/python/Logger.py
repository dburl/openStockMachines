import logging, os

global_log = None

def set_global_logger():
    log_path = 'logs'
    global global_log
    logging.basicConfig(level=logging.INFO)
    global_log = logging.getLogger('ExeLog')
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    global_log.addHandler(logging.FileHandler(log_path+'/execution.log', mode='w'))

def get_global_log():
    global global_log
    return global_log