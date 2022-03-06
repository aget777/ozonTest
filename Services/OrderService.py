import requests
import Helpers.StringBuilder as stringBuilder
from Models import ResponseModels, Constans

# Разобраться почему не работает сокрытие
__all__ = ["getDealModels"]
head = stringBuilder.getHeaders()
body = stringBuilder.getOrderUrl()

def getDealModels():
    # Параметры. Подумать, как задавать
    # Разобраться с конвертацией, пока это костыль!!!
    # dateStart = datetime.datetime(2021, 12, 1).isoformat()
    dealModels = []
    statusModels = "OperationAgentDeliveredToCustomer"

    dateStart = '2021-09-01T00:00:00.000Z'
    dateEnd = '2022-03-02T00:00:00.000Z'
    page_size = 1000
    baseURL = 'https://api-seller.ozon.ru'
    orderUrl = '/v3/finance/transaction/list'
    head = stringBuilder.getHeaders()
    body = stringBuilder.getOrderUrl(dateStart, dateEnd, statusModels, page_size)

    i = 0
    while i < 1:
        # Подумать над асинхронным запросом
        url = baseURL + orderUrl
        # print(url)
        # print(head)
        # print(body)
        response = requests.post(url, headers=head, data=body)

        # Логировать ошибки!
        # print(response.status_code)
        if response.status_code != 200:
            break
        print(response.json())
        jsonResults = response.json()['result']['operations']
        print(jsonResults)
        # Логировать такие случаи, чтобы понимать, сколько записей выгрузили
        if len(jsonResults) == 0:
            break

        dealModels += _mapModels(jsonResults)

        print(len(jsonResults))
        i += 1
    return dealModels

# На первое время сойдет
# Почитать про мапперы и конвертацию из json в model
def _mapModels(jsonResults):
    dealModels = []
    for jsonResult in jsonResults:
        dealModel = ResponseModels.DealModel(jsonResult)
        dealModels.append(dealModel)

    return dealModels