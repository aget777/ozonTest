from Services import OrderService
from Services import AnalyticsService
from Services import PostsService
from Repositories import FileRepository
from Repositories import ExcelRepository

if __name__ == '__main__':
    dealModels = OrderService.getDealModels()
    analyticsModels = AnalyticsService.getAnalyticsModels()
    postsModels = PostsService.getPostsModels()

    FileRepository.setDealInFile(dealModels)
    FileRepository.setAnalyticsInFile(analyticsModels)
    FileRepository.setPostsInFile(postsModels)

    ExcelRepository.writeDataFramesInExcel(dealModels)
    ExcelRepository.writeAnalyticsDataFramesInExcel(analyticsModels)
    ExcelRepository.writePostsDataFramesInExcel(postsModels)


