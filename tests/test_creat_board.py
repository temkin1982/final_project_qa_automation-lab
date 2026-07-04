from pages.create_board_page import CreateBoardModal


def test_close_create_board(open_create_board):
    create_board = CreateBoardModal(open_create_board)
    create_board.close_model()
    create_board.verify_close_model()


def test_cancel_create_board(open_create_board):
    create_board = CreateBoardModal(open_create_board)
    create_board.cancel()
    create_board.verify_close_model()


def test_create_board(open_create_board):
    create_board = CreateBoardModal(open_create_board)
    create_board.fill_title("Test board")
    create_board.submit()
    create_board.verify_board_created()


def test_create_board_with_description(open_create_board):
    create_board = CreateBoardModal(open_create_board)
    create_board.fill_title("My board")
    create_board.fill_description_title("Dima test board")
    create_board.submit()
    create_board.verify_board_created()


def test_create_board_with_minimum(open_create_board):
    create_board = CreateBoardModal(open_create_board)
    create_board.fill_title("abc")
    create_board.submit()
    create_board.verify_board_created()


def test_create_board_with_under_minimum(open_create_board):
    create_board = CreateBoardModal(open_create_board)
    create_board.fill_title("ab")
    create_board.submit()
    create_board.verify_board_modal_opened()


def test_checkbox(open_create_board):
    create_board = CreateBoardModal(open_create_board)
    create_board.check_checkbox()
    create_board.verify_checkbox()
    create_board.uncheck_checkbox()
    create_board.verify_uncheck_checkbox()
