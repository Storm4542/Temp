import requests
import json
import jdCookie
"""
https://wbbny.m.jd.com/babelDiy/Zeus/4SJUHwGdUQYgg94PFzjZZbGZRjDd/index.html#/home

仅领取金币
cron 0 * * * * 
"""


cookies1 = {
    'pt_key': '',
    'pt_pin': '',
}

headers = {
    'User-Agent': 'jdapp;iPhone;9.2.0;14.1;;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'api.m.jd.com',
    'Origin': 'https://wbbny.m.jd.com',
    'Referer': 'https://wbbny.m.jd.com/babelDiy/Zeus/4SJUHwGdUQYgg94PFzjZZbGZRjDd/index.html',
}


def postTemplete(cookies, functionId, body):
    params = (
        ('functionId', functionId),
    )
    data = {
        'functionId': functionId,
        'body': json.dumps(body),
        'client': 'wh5',
        'clientVersion': '1.0.0'
    }

    response = requests.post('https://api.m.jd.com/client.action',
                             headers=headers, params=params, cookies=cookies, data=data)
    return response.json()["data"]["result"]


def get_ss(data, secretp):
    ss = {"extraData": '{}', "businessData": json.dumps(
        data), "secretp": secretp}
    body = {"ss": json.dumps(ss)}
    return body


def collectProduceScore(cookies):
    stall_getHomeData = postTemplete(cookies, "stall_getHomeData", {})
    secretp = stall_getHomeData["homeMainInfo"]["secretp"]
    data = {"taskId": "collectProducedCoin",
            "rnd": "", "inviteId": "-1", "stealId": "-1"}
    body = get_ss(data, secretp)
    coin = postTemplete(
        cookies, "stall_collectProduceScore", body)
    print("收集金币: ", coin)


for cookies in jdCookie.get_cookies():
    print(f"""[ {cookies["pt_pin"]} ]""")
    collectProduceScore(cookies)
    print("\n")
    # exit()
