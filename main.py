import requests
import random
import time
import os
from colorama import Fore

print("""
                   ██████╗ ███╗   ██╗    ████████╗ ██████╗ ██████╗ 
                  ██╔═══██╗████╗  ██║    ╚══██╔══╝██╔═══██╗██╔══██╗
                  ██║   ██║██╔██╗ ██║       ██║   ██║   ██║██████╔╝
                  ██║   ██║██║╚██╗██║       ██║   ██║   ██║██╔═══╝ 
                  ╚██████╔╝██║ ╚████║       ██║   ╚██████╔╝██║     
                   ╚═════╝ ╚═╝  ╚═══╝       ╚═╝    ╚═════╝ ╚═╝ 
""")
print("=================================================")
tac_gia = "Tiều Phu"
print("Tác giả: " + tac_gia)
kich_ban = "https://github.com/nongdancryptos"
print("Github: " + kich_ban)
telegram = "@OnTopAirdrop"
print("Telegram: " + telegram)
Twitter = "@OnTopAirdrop"
print("Twitter: " + Twitter)
print("===========================================")
print('Cảnh báo: KHÔNG ĐƯỢC MUA BÁN TRAO ĐỔI')
print("===========================================\n")

time.sleep(1)

channel_id = input("Nhập ID kênh: ")
thoi_gian_xoa = int(input("Đặt thời gian xóa tin nhắn: "))
thoi_gian_gui = int(input("Đặt thời gian gửi tin nhắn: "))

time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

os.system('cls' if os.name == 'nt' else 'clear')

with open("chat.txt", "r") as f:
    cac_tin_nhan = f.readlines()

with open("token.txt", "r") as f:
    authorization = f.readline().strip()

while True:
        channel_id = channel_id.strip()

        payload = {
            'content': random.choice(cac_tin_nhan).strip()
        }

        headers = {
            'Authorization': authorization
        }

        r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers=headers)
        print(Fore.WHITE + "Đã gửi tin nhắn: ")
        print(Fore.YELLOW + payload['content'])

        response = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers)

        if response.status_code == 200:
            messages = response.json()
            if len(messages) == 0:
                is_running = False
                break
            else:
                time.sleep(thoi_gian_xoa)

                message_id = messages[0]['id']
                response = requests.delete(f'https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}', headers=headers)
                if response.status_code == 204:
                    print(Fore.GREEN + f'Tin nhắn với ID {message_id} đã được xóa thành công')
                else:
                    print(Fore.RED + f'Không thể xóa tin nhắn với ID {message_id}: {response.status_code}')
        else:
            print(f'Không thể lấy tin nhắn từ kênh: {response.status_code}')

        time.sleep(thoi_gian_gui)
