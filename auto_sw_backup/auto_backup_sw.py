# encoding:utf-8

from settings import *
import telnetlib
import os
import re


def backup_sw(sw_ip):
    # 连接sw
    tn = telnetlib.Telnet(sw_ip, port=23, timeout=50)

    # 读取用户名,并输入
    tn.read_until(b'Username:')
    tn.write(SW_USERNAME + b'\n')

    # 并输入密码
    if sw_ip == "核心交换机ip":  # 核心密码不同
        tn.read_until(b'Password:')
        tn.write(CORE_PASSWD + b'\n')
        time.sleep(1)
    else:
        tn.read_until(b'Password:')
        tn.write(SW_PASSWD + b'\n')
        time.sleep(1)

    if not os.path.exists(sw_ip):
        os.mkdir(sw_ip)

    file_path = os.path.join(sw_ip, FILE_FORM)

    if os.path.exists(file_path):
        return "%s备份已存在" % sw_ip

    with open(file_path, 'wb') as f:
        tn.write(SW_COMMAND + b"\n")
        for i in range(25):
            time.sleep(1)
            tn.write(b" ")

        result = tn.read_very_eager()
        f.write(result)
        print("%s backup finished" % sw_ip)

    tn.close()


def modify_backup(sw_ip):
    file_path = os.path.join(sw_ip, FILE_FORM)

    with open(file_path, "r", encoding="utf-8") as r, open(file_path + ".swap", "w", encoding="utf-8") as w:
        l = []
        for line in r:
            line = re.sub(r"---- More ----.*42D", "", line)
            l.append(line)

        res_l = l[5:-1]  # 去除首尾多余行

        for line in res_l:
            w.write(line.strip() + "\n")

    os.remove(file_path)
    os.rename(file_path + ".swap", file_path)
