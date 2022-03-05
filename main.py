from Services import OrderService
from Repositories import FileRepository
from Repositories import ExcelRepository

if __name__ == '__main__':
    dealModels = OrderService.getDealModels()
    FileRepository.setDealInFile(dealModels)
    ExcelRepository.writeDataFramesInExcel(dealModels)