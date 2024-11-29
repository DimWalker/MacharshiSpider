import json
import os

import requests


# from bs4 import BeautifulSoup


def save_json(url, json_save_path):
    response = requests.get(url)

    # 检查请求是否成功
    if response.status_code == 200:
        # 解析JSON数据
        data = response.json()

        # 将JSON数据保存到文件
        with open(json_save_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)  # 保存为utf-8编码，美化格式
        print(f'JSON数据已保存到{json_save_path}文件中。')
    else:
        print('请求失败，状态码：', response.status_code)


def download_aircraft():
    aircraft_url = "https://ma-activity.zlongame.com/common/infodata/mQuery.do?appkey=1616148215678&target=aircraft_data&type=detail&query="
    aircraft_list = "data/aircraft_list.json"

    ac_dir = "data/aircraft"
    if not os.path.exists(ac_dir):
        # 如果文件夹不存在，则创建文件夹
        os.makedirs(ac_dir)

    with open(aircraft_list, "r", encoding="utf-8") as f:
        aircrafts = json.load(f)
        for ac in aircrafts["data"]["data"]:
            # if ac["quality"] != "SSR":
            #     continue
            ac_name = ac["name"]
            print(f"正在下载{ac_name}")
            save_json(aircraft_url + ac_name, os.path.join(ac_dir, ac_name + ".json"))


def download_pilot():
    pilot_url = "https://ma-activity.zlongame.com/common/infodata/mQuery.do?appkey=1616148215678&target=pilot_data&type=detail&query="
    pilot_list = "data/pilot_list.json"

    pl_dir = "data/pilot"
    if not os.path.exists(pl_dir):
        # 如果文件夹不存在，则创建文件夹
        os.makedirs(pl_dir)

    with open(pilot_list, "r", encoding="utf-8") as f:
        pilots = json.load(f)
        for pl in pilots["data"]["data"]:
            Nickname = pl["Nickname"]
            print(f"正在下载{Nickname}")
            save_json(pilot_url + pl["ID"], os.path.join(pl_dir, Nickname + ".json"))


def download_all_data():
    # 检查文件夹是否存在
    data_dir = "data"
    if not os.path.exists(data_dir):
        # 如果文件夹不存在，则创建文件夹
        os.makedirs(data_dir)
    aircraft_list_url = "https://ma-activity.zlongame.com/common/infodata/mQuery.do?appkey=1616148215678&target=aircraft_data&type=list"
    save_json(aircraft_list_url, os.path.join(data_dir, "aircraft_list.json"))
    download_aircraft()

    pilot_list_url = "https://ma-activity.zlongame.com/common/infodata/mQuery.do?appkey=1616148215678&target=pilot_data&type=list"
    save_json(pilot_list_url, os.path.join(data_dir, "pilot_list.json"))
    download_pilot()


if __name__ == "__main__":
    download_all_data()
