import requests
import Helpers.StringBuilder as stringBuilder
from Models import ResponseModels, Constans

# Разобраться почему не работает сокрытие
__all__ = ["getAnalyticsModels"]
head = stringBuilder.getHeaders()
body = stringBuilder.getAnalyticsReport()

def getAnalyticsModels():
    # Параметры. Подумать, как задавать
    # Разобраться с конвертацией, пока это костыль!!!
    # dateStart = datetime.datetime(2021, 12, 1).isoformat()
    analyticsModels = []


    dateStart = '2020-09-01'
    dateEnd = '2022-03-06'
    metricsArr = []
    dimensionArr = []
    filters = []
    key = 'revenue'
    order = 'DESC'


    metricsArr.append('hits_view')
    metricsArr.append('session_view')
    metricsArr.append('hits_tocart')
    metricsArr.append('conv_tocart')
    metricsArr.append('revenue')
    metricsArr.append('returns')
    metricsArr.append('cancellations')
    metricsArr.append('ordered_units')
    metricsArr.append('delivered_units')


    dimensionArr.append('sku')
    dimensionArr.append('day')
    dimensionArr.append('brand')
    dimensionArr.append('modelID')


    baseURL = 'https://api-seller.ozon.ru'
    analyticsUrl = '/v1/analytics/data'
    head = stringBuilder.getHeaders()
    body = stringBuilder.getAnalyticsReport(dateStart, dateEnd, metricsArr, dimensionArr, filters, key, order)

    i = 0
    while i < 1:
        # Подумать над асинхронным запросом
        url = baseURL + analyticsUrl
        # print(url)
        # print(head)
        # print(body)
        response = requests.post(url, headers=head, data=body)

        # Логировать ошибки!
        # print(response.status_code)
        if response.status_code != 200:
            break
        # print(response.json())
        jsonResults = response.json()['result']['data']  #['dimensions'][0]['id']
        # print(jsonResults)
        # Логировать такие случаи, чтобы понимать, сколько записей выгрузили
        if len(jsonResults) == 0:
            break

        analyticsModels += _mapModels(jsonResults)

        print(len(jsonResults))
        i += 1
    return analyticsModels

# На первое время сойдет
# Почитать про мапперы и конвертацию из json в model
def _mapModels(jsonResults):
    analyticsModels = []
    for jsonResult in jsonResults:
        # print(jsonResult)
        analyticsModel = ResponseModels.AnalyticsModel(jsonResult)
        analyticsModels.append(analyticsModel)

    return analyticsModels