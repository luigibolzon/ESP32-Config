* gerar spiffs.bin
Verbose mode can be enabled via `-v, --verbose` option
CONFIGURATION: https://docs.platformio.org/page/boards/espressif32/esp32-poe-iso.html
PLATFORM: Espressif 32 (6.6.0) > OLIMEX ESP32-PoE-ISO
HARDWARE: ESP32 240MHz, 320KB RAM, 4MB Flash
DEBUG: Current (cmsis-dap) External (cmsis-dap, esp-bridge, esp-prog, iot-bus-jtag, jlink, minimodule, olimex-arm-usb-ocd, olimex-arm-usb-ocd-h, olimex-arm-usb-tiny-h, olimex-jtag-tiny, tumpa)
PACKAGES: 
 - framework-arduinoespressif32 @ 3.20014.231204 (2.0.14) 
 - tool-esptoolpy @ 1.40501.0 (4.5.1) 
 - tool-mkspiffs @ 2.230.0 (2.30) 
 - toolchain-xtensa-esp32 @ 8.4.0+2021r2-patch5
LDF: Library Dependency Finder -> https://bit.ly/configure-pio-ldf
LDF Modes: Finder ~ chain, Compatibility ~ soft
Found 33 compatible libraries
Scanning dependencies...
No dependencies
Building in release mode
Building FS image from 'data' directory to build/esp32-poe-iso/spiffs.bin
/config/io2Settings.json
/config/securitySettings.json
/config/brokerSettings.json
/config/apSettings.json
/config/io0Settings.json
/config/ntpSettings.json
/config/wifiSettings.json
/config/io1Settings.json
/config/mqttSettings.json
/certs/private.pem.key
/certs/certificate.pem.crt
/certs/AmazonRootCA1.pem
============================================================== [SUCCESS] Took 0.66 seconds ==============================================================
 *  Terminal will be reused by tasks, press any key to close it. 

* gravar no esp32 somente o spiffs.bin para verificar se atualiza a configuração

[nadolny@inspiron3583 scripts]$ python spiffs_flash_script.py 
esptool.py v4.5.1
Serial port /dev/ttyUSB0
Connecting....
Chip is ESP32-D0WD-V3 (revision v3.1)
Features: WiFi, BT, Dual Core, 240MHz, VRef calibration in efuse, Coding Scheme None
Crystal is 40MHz
MAC: b0:a7:32:81:0a:30
Uploading stub...
Running stub...
Stub running...
Configuring flash size...
Flash will be erased from 0x003d0000 to 0x003effff...
Compressed 131072 bytes to 4851...
Wrote 131072 bytes (4851 compressed) at 0x003d0000 in 1.2 seconds (effective 879.0 kbit/s)...
Hash of data verified.

Leaving...
Hard resetting via RTS pin...
ESP32 successfully flashed.
[nadolny@inspiron3583 scripts]$ 

O esp se manteve funcionando mas resetou 