import os

# Добавить нормальные проверки и нормальное отслеживание состояния файлов в каталоге
# Возможно, свои эксепшены. Логировать.
def setDealInFile(dealModels) -> None:
    # path = 'E:\\Wildberries\\API\\WildbberiesData\\DataTest'
    path = r'C:\Users\Lenovo\Downloads\01_Текущие'
    if not os.path.exists(path):
        createCatalog(path)

    file = open(path + '\\dealTestResult', 'w', encoding='utf-8')

    for dealModel in dealModels:
        file.writelines('dateCreated: ' + str(dealModel.dateCreated) + '\n')
        file.writelines('orderId: ' + str(dealModel.orderId) + '\n')
        file.writelines('itemsName: ' + str(dealModel.itemsName) + '\n')
        file.writelines('itemsSku: ' + str(dealModel.itemsSku) + '\n')
        # file.writelines('status: ' + str(dealModel.status) + '\n')
        file.writelines('totalPrice: ' + str(dealModel.totalPrice) + '\n')
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