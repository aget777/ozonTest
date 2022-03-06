# Модель сделок
class DealModel:
    def __init__(self, json) -> None:
        self.dateCreated = json['operation_date']                 # Дата создания заказа (RFC3339)
        self.orderId = json['operation_id']                       # Идентификатор заказа
        self.itemsName = json['items'][0]['name']                 # название товара
        self.itemsSku = json['items'][0]['sku']                   # Идентификатор товара
        self.totalPrice = json['accruals_for_sale']               # Сумма заказа
        self.totalCommission = json['sale_commission']            # Сумма комиссии
        self.orderDate = json['posting']['order_date']            # Дата доставки
        self.warehouseId = json['posting']['warehouse_id']        # Id склада


class AnalyticsModel:
    def __init__(self, json) -> None:
        self.skuId = json['dimensions'][0]['id']                 # SKU идентификатор товара
        self.skuName = json['dimensions'][0]['name']             # Название товара
        self.orderDay = json['dimensions'][1]['id']              # Дата доставки
        self.brandId = json['dimensions'][2]['id']                # ID бренда
        self.brandName = json['dimensions'][2]['name']            # Название бренда
        self.modelId = json['dimensions'][3]['id']                # ID модели
        self.modelName = json['dimensions'][3]['name']            # Название модели

        self.hitsView = json['metrics'][0]                        # всего показов
        self.sessionView = json['metrics'][1]                      # всего сессий
        self.hitsToCart = json['metrics'][2]                       # всего добавлено в корзину
        self.convToCart = json['metrics'][3]                       # общая конверсия в корзину  (всего добавлено в корзину/всего добавлено в корзину)
        self.revenue = json['metrics'][4]                          # заказано на сумму
        self.returns = json['metrics'][5]                          # возвращено товаров
        self.cancellations = json['metrics'][6]                    # отменено товаров
        self.orderedUnits = json['metrics'][7]                     # заказано товаров


class PostsModel:
    def __init__(self, json) -> None:
        self.orderId = json['order_id']                                          # ID идентификатор поставки
        self.orderNumber = json['order_number']                                  # Номер поставки
        self.inProcessAt = json['in_process_at']                                 # Дата заказа
        self.price = json['products'][0]['price']                                # Стоимость товара
        self.name = json['products'][0]['name']                                  # Название товара
        self.sku = json['products'][0]['sku']                                    # sku товара
        self.quantity = json['products'][0]['quantity']                          # Количество товара
        self.region = json['analytics_data']['region']                           # Регион доставки
        self.city = json['analytics_data']['city']                               # Город доставки
        self.deliveryDateEnd = json['analytics_data']['delivery_date_end']                  # Дата доставки
        self.commissionAmount = json['financial_data']['products'][0]['commission_amount']  # Сумма комиссии
        self.commissionPercent = json['financial_data']['products'][0]['commission_percent']  # Процент комиссии
        self.payout = json['financial_data']['products'][0]['payout']                         # Итого К получению
        self.productId = json['financial_data']['products'][0]['product_id']                  # ID идентификатор продукта
        self.productPrice = json['financial_data']['products'][0]['price']                           # Стоимость продукта

