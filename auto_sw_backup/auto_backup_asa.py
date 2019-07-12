# encoding:utf-8

from settings import *
import telnetlib
import os
import re


def backup_asa(asa_ip):
    # 连接sw
    tn = telnetlib.Telnet(asa_ip, port=23, timeout=50)

    tn.read_until(b'Password:')
    tn.write(ASA_PASSWD + b'\n')
    time.sleep(1)

    tn.write(b'enable\n')
    time.sleep(1)
    tn.write(ASA_PASSWD + b'\n')

    if not os.path.exists(asa_ip):
        os.mkdir(asa_ip)

    file_path = os.path.join(asa_ip, FILE_FORM)

    if os.path.exists(file_path):
        return "%s备份已存在" % asa_ip

    with open(file_path, 'wb') as f:
        tn.write(ASA_COMMAND + b"\n")
        for i in range(25):
            time.sleep(1)
            tn.write(b" ")

        result = tn.read_very_eager()
        f.write(result)
        print("%s backup finished" % asa_ip)

    tn.close()


def modify_backup(asa_ip):
    file_path = os.path.join(asa_ip, FILE_FORM)

    with open(file_path, "r", encoding="utf-8") as r, open(file_path + ".swap", "w", encoding="utf-8") as w:
        l = []
        for line in r:
            line = re.sub(r"<--- More --->", "", line)
            line = re.sub(r"[ ]+?\n", "", line)
            if line != "\n" and line:  # 去除空行
                l.append(line)

        res_l = l[4:-1]  # 去除首尾多余行

        for line in res_l:
            w.write(line.strip() + "\n")

    os.remove(file_path)
    os.rename(file_path + ".swap", file_path)


if __name__ == '__main__':
    modify_backup("10.0.0.1")
