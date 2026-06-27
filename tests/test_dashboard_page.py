import pytest
from playwright.sync_api import expect


from data.url import (
    url_home_page,
    url_admin_page,
    url_boards_page,
    url_dashboard_page,
    url_tasks_page,
)
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@pytest.mark.dash1
def test_open_dashboard(login):
    dashboard = DashboardPage(login)
    dashboard.verify_page_opened()


@pytest.mark.dash2
def test_dashboard_username(login):
    dashboard_user = DashboardPage(login)
    dashboard_user.verify_username("admin")


@pytest.mark.dash3
def test_dashboard_logout(login):
    dashboard_user_logout = DashboardPage(login)
    dashboard_user_logout.logout()

    login_menu = LoginPage(login)
    login_menu.verify_page_opened()


@pytest.mark.dash4
def test_dashboard_boards(login):
    dashboard_boards = DashboardPage(login)
    dashboard_boards.go_to_boards()
    expect(login).to_have_url(url_boards_page)

    dashboard_boards.go_to_home_menu()
    expect(login).to_have_url(url_dashboard_page)


@pytest.mark.dash5
def test_dashboard_tasks(login):
    dashboard_tasks = DashboardPage(login)
    dashboard_tasks.go_to_tasks()
    expect(login).to_have_url(url_tasks_page)

    dashboard_tasks.go_to_home_menu()
    expect(login).to_have_url(url_dashboard_page)


@pytest.mark.dash6
def test_dashboard_admin(login):
    dashboard_admin = DashboardPage(login)
    dashboard_admin.go_to_admin_panel()
    expect(login).to_have_url(url_admin_page)

    dashboard_admin.go_to_home_menu()
    expect(login).to_have_url(url_dashboard_page)


@pytest.mark.dash7
def test_go_back_home_menu(login):
    home_menu = DashboardPage(login)
    home_menu.go_back_home_menu()
    expect(login).to_have_url(url_home_page)


@pytest.mark.dash8
def test_create_board(login):
    create_board = DashboardPage(login)
    create_board.create_board()
    create_board.verify_board_modal_opened()
