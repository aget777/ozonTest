import pandas as pd

# Подумать, куда вынести отсюда имена как константы
# В принципе, уже сейчас думать над документацией проекта
def writeDataFramesInExcel(dealModels):
    writer = pd.ExcelWriter('./resultOzon.xlsx', engine='xlsxwriter')

    # Сделать более красивый маппинг
    dealDataFrame = _getDataFrameByDealModels(dealModels)
    dataSheets = {'dealResult': dealDataFrame}

    for sheetName in dataSheets.keys():
        dataSheets[sheetName].to_excel(writer, sheet_name=sheetName, index=False)

    writer.save()

# Уйти потом от этого
# Либо, написать нормальный маппер
def _getDataFrameByDealModels(dealModels):
    dateCreatedList = []
    orderIdList = []
    itemsNameList = []
    itemsSkuList = []
    userStatusList = []
    totalPriceList = []

    # Нужны нормальные мапперы
    # И модели бы развернуть в отдельном проекте
    for dealModel in dealModels:
        dateCreatedList.append(dealModel.dateCreated)
        orderIdList.append(dealModel.orderId)
        itemsNameList.append(dealModel.itemsName)
        itemsSkuList.append(dealModel.itemsSku)
        # userStatusList.append(dealModel.userStatus)
        totalPriceList.append(dealModel.totalPrice)

    # Убрать в константы. Вообще подумать, как лучше все это организовать
    # Пока получается помойка без плана
    # Нужен план развития проекта и план изменений проекта
    # И доска с задачами
    dataFrame = pd.DataFrame({'DateCreated': dateCreatedList,
                 'OrderId': orderIdList,
                 'itemsName': itemsNameList,
                 'itemsSku': itemsSkuList,
                 # 'UserStatus': userStatusList,
                 'TotalPrice': totalPriceList})

    return dataFrame