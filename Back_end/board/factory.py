from controller import NoticeBoardListController
from dao import BoardDAO
from serviceImpl import GetBoardListServiceImpl


class BoardDaoFactory:

    @staticmethod
    def get():
        return BoardDAO()


class BoardListServiceFactory:

    @staticmethod
    def get():
        dao = BoardDaoFactory.get()
        return GetBoardListServiceImpl(dao)


class NoticeBoardListControllerFactory:

    @staticmethod
    def create():
        service_provider = BoardListServiceFactory.get()
        return NoticeBoardListController(service_provider)