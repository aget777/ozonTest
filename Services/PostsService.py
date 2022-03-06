import requests
import Helpers.StringBuilder as stringBuilder
from Models import ResponseModels, Constans

# Разобраться почему не работает сокрытие
__all__ = ["getPostsModels"]
head = stringBuilder.getHeaders()
body = stringBuilder.getPostsReport()

def getPostsModels():
    # Параметры. Подумать, как задавать
    # Разобраться с конвертацией, пока это костыль!!!
    # dateStart = datetime.datetime(2021, 12, 1).isoformat()
    postsModels = []

    dir = 'ASC'
    dateStart = '2021-11-01T00:00:00.000Z'
    status = 'delivered'
    dateEnd = '2022-03-06T23:59:59.000Z'
    limit = 1000
    offset = 0
    translit = True
    analytics_data = True
    financial_data = True

    baseURL = 'https://api-seller.ozon.ru'
    postsUrl = '/v3/posting/fbs/list'
    head = stringBuilder.getHeaders()
    body = stringBuilder.getPostsReport(dir, dateStart, status, dateEnd, limit, offset, translit, analytics_data, financial_data)

    i = 0
    while i < 1:
        # Подумать над асинхронным запросом
        url = baseURL + postsUrl
        # print(url)
        # print(head)
        # print(body)
        response = requests.post(url, headers=head, data=body)

        # Логировать ошибки!
        # print(response.status_code)
        if response.status_code != 200:
            break
        # print(response.json())
        jsonResults = response.json()['result']['postings']
        # print(jsonResults)
        # Логировать такие случаи, чтобы понимать, сколько записей выгрузили
        if len(jsonResults) == 0:
            break

        postsModels += _mapModels(jsonResults)

        print(len(jsonResults))
        i += 1
    return postsModels

# На первое время сойдет
# Почитать про мапперы и конвертацию из json в model
def _mapModels(jsonResults):
    postsModels = []
    for jsonResult in jsonResults:
        # print(jsonResult)
        postsModel = ResponseModels.PostsModel(jsonResult)
        postsModels.append(postsModel)

    return postsModels