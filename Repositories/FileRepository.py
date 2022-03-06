import os

# Добавить нормальные проверки и нормальное отслеживание состояния файлов в каталоге
# Возможно, свои эксепшены. Логировать.
def setDealInFile(dealModels) -> None:
    # path = 'E:\\Wildberries\\API\\WildbberiesData\\DataTest'
    path = r'C:\Users\Lenovo\Downloads\01_Текущие'
    if not os.path.exists(path):
        createCatalog(path)

    file = open(path + '\\postTestResult', 'w', encoding='utf-8')

    for dealModel in dealModels:
        file.writelines('dateCreated: ' + str(dealModel.dateCreated) + '\n')
        file.writelines('orderId: ' + str(dealModel.orderId) + '\n')
        file.writelines('itemsName: ' + str(dealModel.itemsName) + '\n')
        file.writelines('itemsSku: ' + str(dealModel.itemsSku) + '\n')
        file.writelines('totalPrice: ' + str(dealModel.totalPrice) + '\n')
        file.writelines('totalCommission: ' + str(dealModel.totalCommission) + '\n')
        file.writelines('orderDate: ' + str(dealModel.orderDate) + '\n')
        file.writelines('warehouseId: ' + str(dealModel.warehouseId) + '\n')
        file.writelines('\n')

    file.close()


def setAnalyticsInFile(analyticsModels) -> None:
    # path = 'E:\\Wildberries\\API\\WildbberiesData\\DataTest'
    path = r'C:\Users\Lenovo\Downloads\01_Текущие'
    if not os.path.exists(path):
        createCatalog(path)

    file = open(path + '\\analyticsTestResult', 'w', encoding='utf-8')

    for analyticsModel in analyticsModels:
        file.writelines('skuId: ' + str(analyticsModel.skuId) + '\n')
        file.writelines('skuName: ' + str(analyticsModel.skuName) + '\n')
        file.writelines('orderDay: ' + str(analyticsModel.orderDay) + '\n')
        file.writelines('brandId: ' + str(analyticsModel.brandId) + '\n')
        file.writelines('brandName: ' + str(analyticsModel.brandName) + '\n')
        file.writelines('modelId: ' + str(analyticsModel.modelId) + '\n')
        file.writelines('modelName: ' + str(analyticsModel.modelName) + '\n')
        file.writelines('hitsView: ' + str(analyticsModel.hitsView) + '\n')
        file.writelines('sessionView: ' + str(analyticsModel.sessionView) + '\n')
        file.writelines('hitsToCart: ' + str(analyticsModel.hitsToCart) + '\n')
        file.writelines('convToCart: ' + str(analyticsModel.convToCart) + '\n')
        file.writelines('revenue: ' + str(analyticsModel.revenue) + '\n')
        file.writelines('returns: ' + str(analyticsModel.returns) + '\n')
        file.writelines('cancellations: ' + str(analyticsModel.cancellations) + '\n')
        file.writelines('orderedUnits: ' + str(analyticsModel.orderedUnits) + '\n')
        file.writelines('\n')

    file.close()

def setPostsInFile(postsModels) -> None:
    # path = 'E:\\Wildberries\\API\\WildbberiesData\\DataTest'
    path = r'C:\Users\Lenovo\Downloads\01_Текущие'
    if not os.path.exists(path):
        createCatalog(path)

    file = open(path + '\\postsTestResult', 'w', encoding='utf-8')

    for postsModel in postsModels:
        file.writelines('orderId: ' + str(postsModel.orderId) + '\n')
        file.writelines('orderNumber: ' + str(postsModel.orderNumber) + '\n')
        file.writelines('inProcessAt: ' + str(postsModel.inProcessAt) + '\n')
        file.writelines('price: ' + str(postsModel.price) + '\n')
        file.writelines('name: ' + str(postsModel.name) + '\n')
        file.writelines('sku: ' + str(postsModel.sku) + '\n')
        file.writelines('quantity: ' + str(postsModel.quantity) + '\n')
        file.writelines('region: ' + str(postsModel.region) + '\n')
        file.writelines('city: ' + str(postsModel.city) + '\n')
        file.writelines('deliveryDateEnd: ' + str(postsModel.deliveryDateEnd) + '\n')
        file.writelines('commissionAmount: ' + str(postsModel.commissionAmount) + '\n')
        file.writelines('commissionPercent: ' + str(postsModel.commissionPercent) + '\n')
        file.writelines('payout: ' + str(postsModel.payout) + '\n')
        file.writelines('productId: ' + str(postsModel.productId) + '\n')
        file.writelines('productPrice: ' + str(postsModel.productPrice) + '\n')
        file.writelines('\n')

    file.close()





# Пока костыль, потом посмотреть доработать
def createCatalog(path):
    try:
        os.mkdir(path)
    except OSError:
        print("Создать директорию %s не удалось" % path)
    else:
        print("Успешно создана директория %s " % path)