# Модель сделок
class DealModel:
    def __init__(self, json) -> None:
        self.dateCreated = json['operation_date']          # Дата создания заказа (RFC3339)
        self.orderId = json['operation_id']                # Идентификатор заказа
        self.itemsName = json['items'][0]['name']          # название товара
        self.itemsSku = json['items'][0]['sku']            # Идентификатор товара
        self.totalPrice = json['accruals_for_sale']        # Сумма заказа
        self.totalCommission = json['sale_commission']     # Сумма комиссии
        self.orderDate = json['posting']['order_date']     # Дата доставки
        self.warehouseId = json['posting']['warehouse_id']  # Id склада


class AnalyticsModel:
    def __init__(self, json) -> None:
        self.skuId = json['dimensions'][0]['id']  # SKU идентификатор товара
        self.skuName = json['dimensions'][0]['name']  # Название товара
        self.orderDay = json['dimensions'][1]['id']  # Дата доставки
        self.brandId = json['dimensions'][2]['id']  # ID бренда
        self.brandName = json['dimensions'][2]['name']  # Название бренда
        self.modelId = json['dimensions'][3]['id']  # ID модели
        self.modelName = json['dimensions'][3]['name']  # Название модели

        self.hitsView = json['metrics'][0]  # всего показов
        self.sessionView = json['metrics'][1]  # всего сессий
        self.hitsToCart = json['metrics'][2]  # всего добавлено в корзину
        self.convToCart = json['metrics'][3]  # общая конверсия в корзину  (всего добавлено в корзину/всего добавлено в корзину)
        self.revenue = json['metrics'][4]  # заказано на сумму
        self.returns = json['metrics'][5]  # возвращено товаров
        self.cancellations = json['metrics'][6]  # отменено товаров
        self.orderedUnits = json['metrics'][7]  # заказано товаров