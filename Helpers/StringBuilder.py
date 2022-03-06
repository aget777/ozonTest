from Models import Constans
import json

# Разобраться почему не работает сокрытие
__all__ = ["getHeaders", "getOrderUrl"]

urls = Constans.URLs()
headers = Constans.Headers()
parameters = Constans.OrderParameters()

# добавить нормальную сборку заголовков, почитать про это
def getHeaders() -> dict:
    head = {headers.ClientId: headers.ClientIdValue, headers.authorization: headers.APIKey}

    return head

def getOrderUrl(dateStart='', dateEnd='', statusModels='', page_size=1000):
    body = {'filter':{'date':{'from': dateStart, 'to': dateEnd}, 'operation_type': [statusModels], 'transaction_type': 'all'}, 'page': 1, 'page_size': page_size}
    body = json.dumps(body)
    return body


