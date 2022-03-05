class URLs:
    def __init__(self) -> None:
        self.baseURL = 'https://api-seller.ozon.ru'
        self.orderUrl = '/v3/finance/transaction/list'

# Первое, что нужно убрать отсюда
# Или доработать
class Headers:
    def __init__(self) -> None:
        self.ClientId = 'Client-Id'
        self.authorization = 'Api-Key'

        self.ClientIdValue = '265496'
        self.APIKey = '0d77b05f-16f0-4d06-a877-d815e3aa18f8'

class OrderParameters:
    def __init__(self) -> None:
        self.dateStart = 'from'
        self.dateEnd = 'to'
        self.status = 'operation_type'


# Вынести в конфиги, либо как-то еще избавиться от них
class PathsToFiles:
    def __init__(self) -> None:
        self.catalogPath = r'C:\Users\Lenovo\Downloads\01_Текущие\05_ozon'
        self.dealPath = 'dealTest'