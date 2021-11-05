class BoardEntity(object):
    def __init__(self, board_no, board_type_no, board_title, board_cont, board_writer, board_created, board_fixdate):
        self.board_no = board_no
        self.board_type_no = board_type_no
        self.board_title = board_title
        self.board_cont = board_cont
        self.board_writer = board_writer
        self.board_created = board_created
        self.board_fixdate = board_fixdate

    @property
    def get_board_no(self):
        return self.board_no

    @property
    def get_board_type_no(self):
        return self.board_type_no
