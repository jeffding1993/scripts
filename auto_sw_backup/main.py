from auto_backup_sw import *
import auto_backup_asa
from settings import *
from concurrent.futures import ThreadPoolExecutor
import time


def switch_backup(host):
    backup_sw(host)
    modify_backup(host)


def asa_backup(host):
    auto_backup_asa.backup_asa(host)
    auto_backup_asa.modify_backup(host)


if __name__ == '__main__':
    # 使用多进程提高运行效率
    p = ThreadPoolExecutor()

    start_time = time.time()

    for host in HUAWEI_HOSTS:
        p.submit(switch_backup, host)

    for host in CISCO_HOSTS:
        p.submit(asa_backup, host)
    p.shutdown()
    print("use time: %s " % (time.time() - start_time,))
