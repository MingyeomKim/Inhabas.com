from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework.decorators import api_view
from factory import NoticeBoardListControllerFactory
from controller import NoticeBoardListController
from dao import BoardDAO
from serviceImpl import GetBoardListServiceImpl
from ..DB.models import Board


@api_view(['GET'])
@login_required
def notice_board_list_view():
    # body, status = NoticeBoardListController(GetBoardListServiceImpl(BoardDAO())).get()
    body, status = NoticeBoardListControllerFactory.create()  # 위와 같이 작성해야하는걸 factory 로 해결

    return JsonResponse(data=body, status=status, safe=False)


# /board/notice
class NoticeBoardListView(View):
    controller_factory = None

    # @method_decorator(permission_required('board.list_notice_board', raise_exception=True), name='dispatch')
    def get(self, request, *args, **kwargs):
        body, status =
        # board_id = request.post_id
        # board = Board.objects.get(board_no = board_id)
        # body = {
        #     # body에 board 객체 값들을 가져온다...!
        #     board_type_no = board.board_type_no,
        #     board_title = board.board_title,
        #     board_cont = board.board_cont,
        #     board_writer = board.board_writer,
        #     board_created = board.board_created,
        #     board_fixdate = board.board_fixdate
        # }
        body, status = self.controller_factory.create().execute()

        return JsonResponse(data=body, status=status, safe=False)

    # @method_decorator(permission_required('board.create_notice_board', raise_exception=True), name='dispatch')
    def post(self):
        pass
