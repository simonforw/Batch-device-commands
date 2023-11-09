## 介绍 ##
叫GPT帮了大部分忙写的网络设备命令批量执行导出的脚本，支持华为交换机、路由器。
如果想支持其他品牌的设备，需要修改`device_type': 'huawei'`，把华为
修改为其他标签。
[https://github.com/ktbyers/netmiko/blob/develop/EXAMPLES.md](https://github.com/ktbyers/netmiko/blob/develop/EXAMPLES.md "https://github.com/ktbyers/netmiko/blob/develop/EXAMPLES.md")

----------

## 使用 ##
修改switchs.ini文件内容,包括网络设备设备IP地址、用户名、密码、要执行的命令。
如果有多个设备，依次往下写就好。
``` bash
[Switch1]
hostname = 10.0.0.1
username = admin
password = Admin@123
commands = dis cu, dis arp

[Switch2]
hostname = 10.0.0.2
username = admin
password = Admin@123
commands = dis acl all, dis access-user

[Switch3]
hostname = 10.0.0.3
username = admin
password = Admin@123
commands = dis cu

[Switch4]
······

```

确保switches.ini内容没问题后双击程序，即可运行。

----------

## 封装 ##
``` bash
pyinstaller --onefile Batch-device-commands_v1.1.py
```

----------

## 前提！ ##
网络设备开启SSH登录，添加了aaa认证足够权限的账户。
