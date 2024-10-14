import os
import subprocess

spiffs_path = "../build/esp32-poe-iso/spiffs.bin"

def flash_esp32():
    esptool_path = os.path.expanduser("~/.platformio/packages/tool-esptoolpy/esptool.py")  # Expand the '~' to full path
    command = [
        "python3",  # Explicitly call the Python interpreter
        esptool_path, 
        "--chip", "esp32",
        "--port", "/dev/ttyUSB0",
        "--baud", "115200",
        "--after", "hard_reset",
        "write_flash", "-z",
        "--flash_mode", "dio",
        "--flash_freq", "40m",
        "--flash_size", "4MB",
        "0x3d0000", spiffs_path
    ]

    try:
        subprocess.run(command, check=True)
        print("ESP32 successfully flashed.")
    except subprocess.CalledProcessError as e:
        print(f"Flashing failed with error: {e}")

if __name__ == "__main__":
    flash_esp32()
