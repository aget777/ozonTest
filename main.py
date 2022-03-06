from Services import OrderService
from Services import AnalyticsService
from Repositories import FileRepository
from Repositories import ExcelRepository

if __name__ == '__main__':
    dealModels = OrderService.getDealModels()
    analyticsModels = AnalyticsService.getAnalyticsModels()
    FileRepository.setDealInFile(dealModels)
    FileRepository.setAnalyticsInFile(analyticsModels)

    ExcelRepository.writeDataFramesInExcel(dealModels)
    ExcelRepository.writeAnalyticsDataFramesInExcel(analyticsModels)