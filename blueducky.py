import bluetooth
import time

def discover_devices():
    print("BLUETOOTH QURILMALARI QIDIRILMOQDA...")
    return bluetooth.discover_devices(duration=8, lookup_names=True)

def show_devices(devices):
    if not devices:
        print("HECH QANDAY BLUETOOTH QURILMASI TOPILMADI")
        return False
    else:
        print("TOPILGAN BLUETOOTH QURILMALARI:")
        for idx, (addr, name) in enumerate(devices, 1):
            print(f"{idx}. {name} - {addr}")
        return True

def get_user_choice(max_choice):
    while True:
        try:
            choice = int(input("RAQAMNI KIRIT: "))
            if 1 <= choice <= max_choice:
                return choice
            else:
                print("NOTO'G'RI RAQAM. ILTIMOS, QAYTADAN URUNING.")
        except ValueError:
            print("FAQAT RAQAM KIRITING.")

def send_signal(target_address, target_name):
    print(f"{target_name} QURILMASIGA SIGNAL YUBORILMOQDA...")
    while True:
        try:
            sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            sock.settimeout(10)
            sock.connect((target_address, 1))
            sock.send("BU TEST SIGNAL")
            print("SIGNAL YUBORILDI!")
            time.sleep(0.5)
            sock.close()
        except bluetooth.BluetoothError as e:
            print(f"PACKETLAR YUBORILMADI: {e}")
            time.sleep(2)
        except Exception as e:
            print(f"XATOLIK: {e}")
            break
        else:
            print("QURILMA TOPILMADI")

def main():
    nearby_devices = discover_devices()
    if show_devices(nearby_devices):
        choice = get_user_choice(len(nearby_devices))
        target_address = nearby_devices[choice - 1][0]
        target_name = nearby_devices[choice - 1][1]
        print(f"TANLANGAN QURILMA: {target_name} | MAC: {target_address}")
        send_signal(target_address, target_name)

if __name__ == "__main__":
    main()
