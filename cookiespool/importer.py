import requests

from cookiespool.db import RedisClient

conn = RedisClient('accounts', 'weibo')


def set(website, account, sep='----'):
    username, password = account.split(sep)
    conn = RedisClient('accounts', website)
    result = conn.set(username, password)
    print('账号', username, '密码', password)
    print('录入成功' if result else '录入失败')


def scan():
    website = input('请输入网站名')
    print('请输入账号密码组, 输入exit退出读入')
    while True:
        account = input()
        if account == 'exit':
            break
        set(website, account)


if __name__ == '__main__':
    scan()
