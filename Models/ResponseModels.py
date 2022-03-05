# Модель сделок
class DealModel:
    def __init__(self, json) -> None:
        self.dateCreated = json['operation_date']      # Дата создания заказа (RFC3339)
        self.orderId = json['operation_id']              # Идентификатор заказа
        self.itemsName = json['items']['name']    # название товара
        self.itemsSku = json['items']['sku']                # Идентификатор товара
        self.userStatus = json['userStatus']        # Статус товара с позиции пользователя
        self.totalPrice = json['amount']        # Стоимость товара