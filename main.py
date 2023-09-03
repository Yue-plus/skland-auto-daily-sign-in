import requests

CRED = '________________________________'
COOKIE = 'acw_tc=________________________________________________________________'

##########################################################################################

HEADER = {
    'User-Agent': 'Skland/1.0.1 (com.hypergryph.skland; build:100001014; Android 33; ) Okhttp/4.11.0',
    'Content-Type': 'application/json',
    'cred': CRED,
    'Cookie': COOKIE
}

UID_LIST = []


def user_auth_generate_cred_by_code():
    response = requests.post(
        url='https://zonai.skland.com/api/v1/user/auth/generate_cred_by_code',
        headers=HEADER,
        json={
            'kind': 1,
            'code': '长 176 的字符串，生成原理不明。'
        }
    )

    print(response.status_code, response.text)


def game_player_binding():
    response = requests.get('https://zonai.skland.com/api/v1/game/player/binding', headers=HEADER)

    if response.status_code != 200:
        print(response.status_code, response.text)
        exit(1)

    data_list = response.json().get('data').get('list')

    for item in data_list:
        if item.get('appCode') == 'arknights':
            for bind_item in item.get('bindingList'):
                UID_LIST.append(bind_item.get('uid'))

    print(response.status_code, UID_LIST)


def game_attendance(uid: str):
    response = requests.post(
        url='https://zonai.skland.com/api/v1/game/attendance',
        headers=HEADER,
        json={'uid': uid, 'gameId': 1},
    )

    print(response.status_code, response.text)


if __name__ == '__main__':
    game_player_binding()
    for uid in UID_LIST:
        game_attendance(uid)
