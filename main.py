import requests, json
import time

def send_discord_webhook(message, webhook):
    headers = {
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(webhook, data=json.dumps(message), headers=headers)
        if response.ok:
            print("Succeded to send webhook.")
        else:
            print("Failed to send webhook.")
    except:
        print("No Response for DISCORD API")

headers = {"Accept":"text/html", "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0"}

url = input("Type URL about product (including'HTTP(s)://'): ")
webhook = input("Type URL that gets notification when stock is filled (including'HTTP(s)://'): ")

content = {"content": f"{url} is in stock"}

while True:
    send_request = requests.get(url, headers=headers).text.find("재고가 일시 품절된 상품입니다.")
    if send_request == -1:
        send_discord_webhook(message=content, webhook=webhook)
    elif send_request == None:
        print("Error occurs")
    else:
        time.sleep(30)