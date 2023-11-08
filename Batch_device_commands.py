from netmiko import ConnectHandler
from datetime import datetime
import configparser

def export_config(hostname, username, password, command):
    try:
        device = {
            'device_type': 'huawei',
            'ip': hostname,
            'username': username,
            'password': password,
        }

        net_connect = ConnectHandler(**device)

        output = net_connect.send_command(command)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f'{hostname}_config_{timestamp}.txt'

        with open(filename, 'w') as file:
            file.write(output)

        print(f"配置已成功导出到{filename}")

        net_connect.disconnect()

    except Exception as e:
        print(f"导出配置失败: {e}")

print("                                                                              ")
print("[%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%| $a,        |%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]")
print("[%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%| $S`?a,     |%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]")
print("[%%%%%%%%%%%%%%%%%%%%&%%%%%%%%%%%|       `?a, |%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]")
print("[%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%|       .,a$%|%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]")
print("[%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%|  ,,aS$""`  |%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]")
print("[%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%|%$P'`       |%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]")
print("[%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%| `'a,       |%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]")
print("[%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%|____`'a,$$__|%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]")
print("[%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%        `'$   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]")
print("[%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]")
print("                                                                              ")
print("+ -- --=[ Simonforw made it, no need to thank~]=-- -- +               ")
print("+ -- --=[ 别急，程序不是卡住了，而是和网络环境有关，执行的慢而已~ ]=-- -- +")  
print("+ -- --=[ 检查好switches.ini写没写错~ ]=-- -- +")
print("+ -- --=[ ⬇ 下 ⬇ 面 ⬇ 是 ⬇ 完 ⬇ 成 ⬇ 度 ⬇ 提 ⬇ 醒 ⬇  ]=-- -- +")   
print("                                                               ") 

config = configparser.ConfigParser()
config.read('switches.ini')

switches = []
for section in config.sections():
    switch = {
        'hostname': config.get(section, 'hostname'),
        'username': config.get(section, 'username'),
        'password': config.get(section, 'password'),
        'command': config.get(section, 'command')
    }
    switches.append(switch)
    
for switch in switches:
    export_config(switch['hostname'], switch['username'], switch['password'], switch['command'])
