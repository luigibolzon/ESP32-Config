import os
import subprocess

firmware_path = "../firmware_bins/update_firmware/firmware.bin"

def flash_esp32():
    esptool_path = os.path.expanduser("~/.platformio/packages/tool-esptoolpy/esptool.py")  # Expand the '~' to full path
    command = [
        "python3",  # Explicitly call the Python interpreter
        esptool_path, 
        "--chip", "esp32",
        "--port", "/dev/ttyUSB0",
        "--baud", "115200",
        "--before", "default_reset",
        "--after", "hard_reset",
        "write_flash", "-z",
        "--flash_mode", "dio",
        "--flash_freq", "40m",
        "--flash_size", "4MB",
        "0x10000", firmware_path  # Flash only the firmware
    ]

    try:
        subprocess.run(command, check=True)
        print("ESP32 successfully flashed with firmware.")
    except subprocess.CalledProcessError as e:
        print(f"Flashing failed with error: {e}")

if __name__ == "__main__":
    flash_esp32()

