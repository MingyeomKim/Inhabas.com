from entity import BoardEntity
from datetime import datetime
from ..DB.models import Board
#save, update, delete, read의 기본 로직을 제공하는 Repository.py
class BoardRepository(object):
    # def __init__(self): #생성자?

    def save(self, entity):
        entity.save()

    def delete(self, entity):
        return entity.delete()

    def findOne(self, id):
        board = Board.objects.get(board_no=id)
        return board

    def findAll(self, type_id):
        board_list = []
        for board in Board.objects.filter(board_type_no=type_id).all():
            board_list.append(board)
        return board_list

    def update(self, entity): # update하고자 하는 새 board entity
        board = Board.objects.get(board_no=entity.get_board_no())
        board_type_no = board.board_type_no
        board_title = board.title
        board_cont = board.board_cont
        board_updated = datetime.date.now()
