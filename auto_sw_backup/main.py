from auto_backup_sw import *
import auto_backup_asa
from settings import *

if __name__ == '__main__':
    for host in HUAWEI_HOSTS:
        backup_sw(host)
        modify_backup(host)

    for host in CISCO_HOSTS:
        auto_backup_asa.backup_asa(host)
        auto_backup_asa.modify_backup(host)
