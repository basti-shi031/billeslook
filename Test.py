import json
import time

from Net import Net

if __name__ == '__main__':

    # 实际index 为1
    current_index = 1
    # 0-2
    time_index = 2
    product_ids = [367, 656]
    sku_ids = ['10321', '14011']

    dest_times = [1572660000000, 1572660000200, 1572660000400]

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
        "token": "user_login_f30f390695110756fb873eeb3d0ef338",
    }
    t = time.time()
    t = int(t)
    cookie = "Hm_lvt_d472e16483828f86781cd857ad2ba196 = 1572580903, 1572580916,1572587444,1572607220;PHPSESSID = 836sjjgrk9d372bhe0ie4lpi93;billeslook_token = user_login_f30f390695110756fb873eeb3d0ef338;Hm_lpvt_d472e16483828f86781cd857ad2ba196 = "
    headers['Cookie'] = cookie + str(t)
    # 设置触发器

    current_time = int(round(time.time() * 1000))
    dest_time = dest_times[time_index]
    delta_time = dest_time - current_time
    delta_time_second = delta_time / 1000
    print(delta_time_second)
    time.sleep(delta_time_second)

    print(time.time())

    response = Net.create_order(product_ids[current_index], sku_ids[current_index], 1, '0', headers)

    if response.status_code == 200:
        order_sn = json.loads(response.text)['data']['order_sn']

        t = time.time()
        t = int(t)
        cookie = "Hm_lvt_d472e16483828f86781cd857ad2ba196 = 1572580903, 1572580916,1572587444,1572607220;PHPSESSID = 836sjjgrk9d372bhe0ie4lpi93;billeslook_token = user_login_f30f390695110756fb873eeb3d0ef338;Hm_lpvt_d472e16483828f86781cd857ad2ba196 = "
        headers['Cookie'] = cookie + str(t)
        print(time.time())
        confirm_response = Net.confirm_order(order_sn, 44210, "", "", 0, "1", "", headers)
        print(time.time())
        print(confirm_response.status_code)
        print(confirm_response.text)
