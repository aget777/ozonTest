import requests
import json

url = "https://api-seller.ozon.ru" # Cсылку нужно поменять на боевую среду
method = "/v3/finance/transaction/list" # Сюда вбиваем нужный метод
print(url + method)
head = {
  "Client-Id": "265496", # сюда клиент id
  "Api-Key": "0d77b05f-16f0-4d06-a877-d815e3aa18f8" # Сюда Api-Key
}

# Сюда пишем параметры запроса
body = {
    "filter": {
        "date": {
            "from": "2021-09-01T00:00:00.000Z",
            "to": "2022-03-02T00:00:00.000Z"
        },
        "operation_type": [],
        "posting_number": "",
        "transaction_type": "all"
    },
    "page": 1,
    "page_size": 1000
}
body = json.dumps(body) # Нужно передавать в озон именно так, потому что string он как json не понимает
response = requests.post(url + method, headers=head, data=body)

print(response.text) # ответ сервера Озон
