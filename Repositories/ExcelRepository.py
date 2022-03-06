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
    totalPriceList = []
    totalCommissionList = []
    orderDateList = []
    warehouseIdList = []

    # Нужны нормальные мапперы
    # И модели бы развернуть в отдельном проекте
    for dealModel in dealModels:
        dateCreatedList.append(dealModel.dateCreated)
        orderIdList.append(dealModel.orderId)
        itemsNameList.append(dealModel.itemsName)
        itemsSkuList.append(dealModel.itemsSku)
        totalPriceList.append(dealModel.totalPrice)
        totalCommissionList.append(dealModel.totalCommission)
        orderDateList.append(dealModel.orderDate)
        warehouseIdList.append(dealModel.warehouseId)

    # Убрать в константы. Вообще подумать, как лучше все это организовать
    # Пока получается помойка без плана
    # Нужен план развития проекта и план изменений проекта
    # И доска с задачами
    dataFrame = pd.DataFrame({'DateCreated': dateCreatedList,
                 'OrderId': orderIdList,
                 'itemsName': itemsNameList,
                 'itemsSku': itemsSkuList,
                 'TotalPrice': totalPriceList,
                 'totalCommission': totalCommissionList,
                 'orderDate': orderDateList,
                 'warehouseId': warehouseIdList})


    return dataFrame


def writeAnalyticsDataFramesInExcel(analyticsModels):
    writer = pd.ExcelWriter('./analyticsOzon.xlsx', engine='xlsxwriter')

    # Сделать более красивый маппинг
    analyticsDataFrame = _getDataFrameByAnalyticsModels(analyticsModels)
    dataSheets = {'analyticsResult': analyticsDataFrame}

    for sheetName in dataSheets.keys():
        dataSheets[sheetName].to_excel(writer, sheet_name=sheetName, index=False)

    writer.save()

def _getDataFrameByAnalyticsModels(analyticsModels):
    skuIdList = []
    skuNameList = []
    orderDayList = []
    brandIdList = []
    brandNameList = []
    modelIdList = []
    modelNameList = []
    hitsViewList = []
    sessionViewList = []
    hitsToCartList = []
    convToCartList = []
    revenueList = []
    returnsList = []
    cancellationsList = []
    orderedUnitsList = []

    # Нужны нормальные мапперы
    # И модели бы развернуть в отдельном проекте
    for analyticsModel in analyticsModels:
        skuIdList.append(analyticsModel.skuId)
        skuNameList.append(analyticsModel.skuName)
        orderDayList.append(analyticsModel.orderDay)
        brandIdList.append(analyticsModel.brandId)
        brandNameList.append(analyticsModel.brandName)
        modelIdList.append(analyticsModel.modelId)
        modelNameList.append(analyticsModel.modelName)
        hitsViewList.append(analyticsModel.hitsView)
        sessionViewList.append(analyticsModel.sessionView)
        hitsToCartList.append(analyticsModel.hitsToCart)
        convToCartList.append(analyticsModel.convToCart)
        revenueList.append(analyticsModel.revenue)
        returnsList.append(analyticsModel.returns)
        cancellationsList.append(analyticsModel.cancellations)
        orderedUnitsList.append(analyticsModel.orderedUnits)

    # Убрать в константы. Вообще подумать, как лучше все это организовать
    # Пока получается помойка без плана
    # Нужен план развития проекта и план изменений проекта
    # И доска с задачами
    dataFrame = pd.DataFrame({'skuId': skuIdList,
                 'skuName': skuNameList,
                 'orderDay': orderDayList,
                 'brandId': brandIdList,
                 'brandName': brandNameList,
                 'modelId': modelIdList,
                 'modelName': modelNameList,
                 'hitsView': hitsViewList,
                 'sessionView': sessionViewList,
                 'hitsToCart': hitsToCartList,
                 'convToCart': convToCartList,
                 'revenue': revenueList,
                 'returns': returnsList,
                 'cancellations': cancellationsList,
                 'orderedUnits': orderedUnitsList})


    return dataFrame

def writePostsDataFramesInExcel(postsModels):
    writer = pd.ExcelWriter('./postsOzon.xlsx', engine='xlsxwriter')

    # Сделать более красивый маппинг
    postsDataFrame = _getDataFrameByPostsModels(postsModels)
    dataSheets = {'postsResult': postsDataFrame}

    for sheetName in dataSheets.keys():
        dataSheets[sheetName].to_excel(writer, sheet_name=sheetName, index=False)

    writer.save()

def _getDataFrameByPostsModels(postsModels):
    orderIdList = []
    orderNumberList = []
    inProcessAtList = []
    priceList = []
    nameList = []
    skuList = []
    quantityList = []
    regionList = []
    cityList = []
    deliveryDateEndList = []
    commissionAmountList = []
    commissionPercentList = []
    payoutList = []
    productIdList = []
    productPriceList = []

    # Нужны нормальные мапперы
    # И модели бы развернуть в отдельном проекте
    for postsModel in postsModels:
        orderIdList.append(postsModel.orderId)
        orderNumberList.append(postsModel.orderNumber)
        inProcessAtList.append(postsModel.inProcessAt)
        priceList.append(postsModel.price)
        nameList.append(postsModel.name)
        skuList.append(postsModel.sku)
        quantityList.append(postsModel.quantity)
        regionList.append(postsModel.region)
        cityList.append(postsModel.city)
        deliveryDateEndList.append(postsModel.deliveryDateEnd)
        commissionAmountList.append(postsModel.commissionAmount)
        commissionPercentList.append(postsModel.commissionPercent)
        payoutList.append(postsModel.payout)
        productIdList.append(postsModel.productId)
        productPriceList.append(postsModel.productPrice)

    # Убрать в константы. Вообще подумать, как лучше все это организовать
    # Пока получается помойка без плана
    # Нужен план развития проекта и план изменений проекта
    # И доска с задачами
    dataFrame = pd.DataFrame({'orderId': orderIdList,
                 'orderNumber': orderNumberList,
                 'inProcessAt': inProcessAtList,
                 'price': priceList,
                 'name': nameList,
                 'sku': skuList,
                 'quantity': quantityList,
                 'region': regionList,
                 'city': cityList,
                 'deliveryDateEnd': deliveryDateEndList,
                 'commissionAmount': commissionAmountList,
                 'commissionPercent': commissionPercentList,
                 'payout': payoutList,
                 'productId': productIdList,
                 'productPrice': productPriceList})


    return dataFrame