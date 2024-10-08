import requests

from Login.login import Login
from Search.search import Search

def welcome() -> None:
    print("欢迎使用作业查询系统")
    print("本系统支持通过cookie登录或通过MIS登录")
    print("通过cookie登录：输入1")
    print("通过MIS登录：输入2")
    return

def main():

    # 欢迎界面
    welcome()

    # 登录
    # 1：通过cookie登录
    # 2：通过MIS登录
    login_type = input("请选择登录方式：\n1. 通过cookie登录\n2. 通过MIS登录\n")
    myLogin = Login()
    myLogin.login(int(login_type))

    # 选择查询方式
    # 1：显示全部课程作业
    # 2：显示所有未完成作业

    search_type = input("请选择查询方式：\n1. 显示全部课程作业\n2. 显示所有未完成作业\n")
    mySearch = Search(myLogin.cookie)
    mySearch.search(search_type)
    mySearch.display()

    pass

if __name__ == '__main__':
    main()