import os
import json
import shutil

# Insira aqui os valores de configuração
new_mac = "NEW_MAC"
new_ap_mac = "NEW_AP_MAC"
new_resourcekey = "NEW_RESOURCE_UKEY"
new_ip = "NEW_IP"
new_gateway = "192.168.101.1"
SSID = "JJP-40_2.4G"
SSID_password = "Netedge,40"
MQTT_url = "192.168.100.11"
MQTT_PORT = "1883"
MQTT_username = "admin"
MQTT_password = "Ap@690#KptLmn8"

# Quais arquivos quer criar?
settings_flags = {
    "apSettings": True,
    "brokenSettings": True,
    "mqttSettings": True,
    "ntpSettings": True,
    "wifiSettings": True,
    "oeeSettings": True,
    "snmpSettings": True,
    "securitySettings": False,
    "io0Settings": False,
    "io1Settings": False,
    "io2Settings": False,
    "tempSettings": False,
    "relaySettings": False,
    "debug1" : True
}

# Definir o caminho da pasta
folder_path = "../data/config"

# Apagar a pasta "config" e todo o seu conteúdo, se ela existir
if os.path.exists(folder_path):
    shutil.rmtree(folder_path)
    print(f"Pasta {folder_path} removida com sucesso.")

# Recriar a pasta "config"
os.makedirs(folder_path)
print(f"Pasta {folder_path} criada novamente.")

# Lista de configurações de arquivos e seus dados
json_data    = [
    { # 1
        "filename": "apSettings.json",
        "data": {
        "provision_mode": 1,
        "ssid": "SmartIoT-"+new_ap_mac,
        "password": "smartiot",
        "channel": 1,
        "ssid_hidden": False,
        "max_clients": 4,
        "local_ip": "192.168.4.1",
        "gateway_ip": "192.168.4.1",
        "subnet_mask": "255.255.255.0"
    }
    },
    { #2
        "filename": "brokenSettings.json",
        "data": {
        "mqtt_path": "smartiot/sensors/"+new_mac,
        "name": "sensors-"+new_mac,
        "unique_id": "sensors-"+new_mac
    }
    },
    { #3
        "filename": "mqttSettings.json",
        "data": {
        "enabled": True,
        "uri": "mqtt://"+MQTT_url+":"+MQTT_PORT,
        "username": MQTT_username,
        "password": MQTT_password,
        "client_id": "esp32-"+new_mac,
        "keep_alive": 120,
        "clean_session": True
    }
    },
    { #4
        "filename": "ntpSettings.json",
        "data": {
        "enabled": True,
        "server": "time.google.com",
        "tz_label": "America/Sao_Paulo",
        "tz_format": "UNK3"
    }
    },
    { #5
        "filename": "wifiSettings.json",
        "data": {
        "hostname": "esp32-"+new_mac,
        "priority_RSSI": True,
        "wifi_networks": [
            {
                "ssid": SSID,
                "password": SSID_password,
                "static_ip_config": True
            }
        ],
        "local_ip": new_ip,
        "gateway_ip": new_gateway,
        "subnet_mask": "255.255.255.0",
        "dns_ip_1": new_gateway,
        "dns_ip_2": "8.8.8.8"
    }
    },
    { #6
        "filename": "oeeSettings.json",
        "data": {
        "enabled": True,
        "client_id": "esp32-"+new_mac,
        "i2c_address": 160,
        "resource_key": new_resourcekey,
        "simulator_enabled": False,
        "simulator_frequency": 2
    }
    },
    { #7
        "filename": "snmpSettings.json",
        "data": {
        "snmp_agent_enabled": True,
        "snmp_agent_read_community": "zabbix.gtiit.com.br",
        "snmp_agent_read_write_community": "zabbix.gtiit.com.br",
        "snmp_agent_sys_contact": "user@email.com.br",
        "snmp_agent_sys_name": "SmartIoT-JJP",
        "snmp_agent_sys_location": "Machine-"+new_mac
    }
    },
    { #8
        "filename": "securitySettings.json",
        "data": {
        "jwt_secret": "784fc466-5c053861",
        "users": [
            {
                "username": "admin",
                "password": "admin",
                "admin": True
            },
            {
                "username": "guest",
                "password": "guest",
                "admin": False
            }
        ]
    }
    },
    { #9
        "filename": "io0Settings.json",
        "data": {
        "enabled": True,
        "client_id": "esp32-"+new_mac,
        "i2c_address": 161,
        "resource_key": new_resourcekey,
        "simulator_enabled": False,
        "simulator_frequency": 1
    }
    },
    { #10
        "filename": "io1Settings.json",
        "data": {
        "enabled": True,
        "client_id": "esp32-"+new_mac,
        "i2c_address": 162,
        "resource_key": new_resourcekey,
        "simulator_enabled": False,
        "simulator_frequency": 1
    }
    },
    { #11
        "filename": "io2Settings.json",
        "data": {
        "enabled": True,
        "client_id": "esp32-"+new_mac,
        "i2c_address": 163,
        "resource_key": new_resourcekey,
        "simulator_enabled": False,
        "simulator_frequency": 1
    }
    },
    { #12
        "filename": "tempSettings.json",
        "data": {
        "enabled": True,
        "client_id": "esp32-"+new_mac,
        "i2c_address": 160,
        "resource_key": new_resourcekey,
        "simulator_enabled": False,
        "simulator_frequency": 1
    }
    },
    { #13
        "filename": "relaySettings.json",
        "data": {
        "enabled": True,
        "set": False,
        "client_id": "esp32-"+new_mac,
        "i2c_address": 160,
        "resource_key": new_resourcekey,
        "simulator_enabled": False,
        "simulator_frequency": 1
    }
    }
]  

debug1_data = {
    "filename": "debug1.json",
    "data": {
        "numi2cok": 34347,
        "numi2cfault": 10,
        "datetime": 1727458216
    }
}

# Loop para criar os arquivos JSON
for setting in json_data:
    filename = setting["filename"]
    if settings_flags.get(filename.split('.')[0], False):
        file_path = os.path.join(folder_path, filename)
        # Escrever os dados no arquivo JSON
        with open(file_path, 'w') as json_file:
            json.dump(setting["data"], json_file, indent=4)
        print(f"Arquivo {file_path} criado com sucesso!")

# criar o debug1
if settings_flags.get("debug1"):
    filename = "debug1.json"
    file_path = os.path.dirname(folder_path)
    file_path = os.path.join(file_path, filename)
    with open(file_path, 'w') as json_file:
        json.dump(debug1_data["data"], json_file, indent=4)
    print(f"Arquivo {file_path} criado com sucesso!")

file_path = "../build/esp32-poe-iso/spiffs.bin"
if os.path.exists(file_path):
    os.remove(file_path)  # Corrigido para remover arquivo
    print(f"Arquivo {file_path} removido com sucesso.")
else:
    print(f"Arquivo {file_path} não encontrado.")