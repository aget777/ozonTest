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

    while True:
        # Подумать над асинхронным запросом
        url = baseURL + orderUrl
        response = requests.post(url, headers=head, data=body)

        # Логировать ошибки!
        if response.status_code != 200:
            break

        jsonResults = response.json()['operations']
        print(jsonResults)
        # Логировать такие случаи, чтобы понимать, сколько записей выгрузили
        if len(jsonResults) == 0:
            break

        dealModels += _mapModels(jsonResults)

        print(len(jsonResults))

    return dealModels

# На первое время сойдет
# Почитать про мапперы и конвертацию из json в model
def _mapModels(jsonResults):
    dealModels = []
    for jsonResult in jsonResults:
        dealModel = ResponseModels.DealModel(jsonResult)
        dealModels.append(dealModel)

    return dealModels