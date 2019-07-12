import time

SW_USERNAME = b"交换机用户名"
SW_PASSWD = b"交换机密码"
CORE_PASSWD = b"核心交换机密码"
ASA_PASSWD = b"asa防火墙密码"
SW_COMMAND = b"dis cur"  # 交换机命令
ASA_COMMAND = b"show run"  # asa命令
TODAY = time.strftime("%Y-%m-%d", time.localtime())  # 时间格式
FILE_FORM = "%s.bak" % TODAY  # 备份文件格式
HUAWEI_HOSTS = [
    "交换机内网ip1",
    "交换机内网ip2"
]
CISCO_HOSTS = [
    "asa内网ip"
]
