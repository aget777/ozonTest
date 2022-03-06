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

def getAnalyticsReport(dateStart='', dateEnd='', metricsArr=[], dimensionArr=[], filtersArr=[], key='', order='', limit=1000, offset=0):
    body = {'date_from': dateStart, 'date_to': dateEnd, 'metrics': metricsArr,'dimension': dimensionArr, 'filters': filtersArr, 'sort': [{'key': key, 'order': order}], 'limit': limit, 'offset': offset}
    body = json.dumps(body)
    return body


def getPostsReport(dir='ASC', dateStart='', status='delivered' , dateEnd='', limit=1000, offset=0, translit=True, analytics_data=True, financial_data=True):
    body = {'dir': dir, 'filter': {'since': dateStart, 'status':status, 'to': dateEnd}, 'limit': limit, 'offset': offset, translit:translit, 'with': {'analytics_data':analytics_data, 'financial_data':financial_data}}
    body = json.dumps(body)
    return body

