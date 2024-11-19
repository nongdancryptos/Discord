import requests
import random
import time
import os
import openai
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
openai_api_key = input("Nhập OpenAI API Key của bạn: ")

# Cấu hình khóa API cho OpenAI
openai.api_key = openai_api_key

time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

os.system('cls' if os.name == 'nt' else 'clear')

with open("token.txt", "r") as f:
    authorization = f.readline().strip()

while True:
    channel_id = channel_id.strip()

    # Sử dụng OpenAI để tạo nội dung tin nhắn
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt="Hãy tạo một tin nhắn thú vị cho kênh Discord.",
            max_tokens=50
        )
        content = response.choices[0].text.strip()
    except Exception as e:
        print(Fore.RED + f"Lỗi khi gọi OpenAI API: {str(e)}")
        break

    payload = {
        'content': content
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
