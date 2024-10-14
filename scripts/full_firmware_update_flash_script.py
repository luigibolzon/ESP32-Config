import os
import subprocess

# Define the file paths

boot_app0_path  = "../firmware_bins/update_full_firmware/boot_app0.bin"
bootloader_path = "../firmware_bins/update_full_firmware/bootloader.bin"
firmware_path   = "../firmware_bins/update_full_firmware/firmware.bin"
partitions_path = "../firmware_bins/update_full_firmware/partitions.bin"
spiffs_path     = "../build/esp32-poe-iso/spiffs.bin"
#spiffs_path     = "../firmware_bins/update_full_firmware/spiffs.bin"

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
        "0x1000", bootloader_path,
        "0x8000", partitions_path,
        "0xe000", boot_app0_path,
        "0x10000", firmware_path,
        "0x3d0000", spiffs_path
    ]

    try:
        subprocess.run(command, check=True)
        print("ESP32 successfully flashed.")
    except subprocess.CalledProcessError as e:
        print(f"Flashing failed with error: {e}")

if __name__ == "__main__":
    flash_esp32()
