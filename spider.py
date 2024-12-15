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


def download_weapon():
    weapon_url = "https://ma-activity.zlongame.com/common/infodata/mQuery.do?appkey=1616148215678&target=weapon_data&type=detail&query="
    weapon_list = "data/weapon_list.json"
    wp_dir = "data/weapon"
    if not os.path.exists(wp_dir):
        # 如果文件夹不存在，则创建文件夹
        os.makedirs(wp_dir)

    with open(weapon_list, "r", encoding="utf-8") as f:
        weapons = json.load(f)
        for wp in weapons["data"]["data"]:
            name = wp["name"]
            print(f"正在下载{name}")
            save_json(weapon_url + name, os.path.join(wp_dir, name + ".json"))


def download_backpack():
    backpack_url = "https://ma-activity.zlongame.com/common/infodata/mQuery.do?appkey=1616148215678&target=backpack_data&type=detail&query="
    backpack_list = "data/backpack_list.json"
    bp_dir = "data/backpack"
    if not os.path.exists(bp_dir):
        # 如果文件夹不存在，则创建文件夹
        os.makedirs(bp_dir)

    with open(backpack_list, "r", encoding="utf-8") as f:
        backpacks = json.load(f)
        for bp in backpacks["data"]["data"]:
            name = bp["name"]
            print(f"正在下载{name}")
            save_json(backpack_url + bp["ID"], os.path.join(bp_dir, name + "_" + bp["quality"] + ".json"))


def download_module():
    module_url = "https://ma-activity.zlongame.com/common/infodata/mQuery.do?appkey=1616148215678&target=module_props&type=detail&query="
    module_list = "data/module_list.json"
    mdl_dir = "data/module"
    if not os.path.exists(mdl_dir):
        # 如果文件夹不存在，则创建文件夹
        os.makedirs(mdl_dir)

    with open(module_list, "r", encoding="utf-8") as f:
        modules = json.load(f)
        for mdl in modules["data"]["data"]:
            name = mdl["name"]
            print(f"正在下载{name}")
            save_json(module_url + mdl["ID"], os.path.join(mdl_dir, name + ".json"))


def download_component():
    component_url = "https://ma-activity.zlongame.com/common/infodata/mQuery.do?appkey=1616148215678&target=component_props&type=detail&query="
    component_list = "data/component_list.json"
    cmpt_dir = "data/component"
    if not os.path.exists(cmpt_dir):
        # 如果文件夹不存在，则创建文件夹
        os.makedirs(cmpt_dir)

    with open(component_list, "r", encoding="utf-8") as f:
        components = json.load(f)
        for cmpt in components["data"]["data"]:
            name = cmpt["name"]
            print(f"正在下载{name}")
            save_json(component_url + cmpt["ID"], os.path.join(cmpt_dir, name + ".json"))


def download_all_data():
    # 检查文件夹是否存在
    data_dir = "data"
    if not os.path.exists(data_dir):
        # 如果文件夹不存在，则创建文件夹
        os.makedirs(data_dir)

    # 机兵
    aircraft_list_url = "https://ma-activity.zlongame.com/common/infodata/mQuery.do?appkey=1616148215678&target=aircraft_data&type=list"
    save_json(aircraft_list_url, os.path.join(data_dir, "aircraft_list.json"))
    download_aircraft()

    # 机师
    pilot_list_url = "https://ma-activity.zlongame.com/common/infodata/mQuery.do?appkey=1616148215678&target=pilot_data&type=list"
    save_json(pilot_list_url, os.path.join(data_dir, "pilot_list.json"))
    download_pilot()

    # 武器
    weapon_list_url = "https://ma-activity.zlongame.com/common/infodata/mQuery.do?appkey=1616148215678&target=weapon_data&type=list"
    save_json(weapon_list_url, os.path.join(data_dir, "weapon_list.json"))
    download_weapon()

    # 背包
    backpack_list_url = "https://ma-activity.zlongame.com/common/infodata/mQuery.do?appkey=1616148215678&target=backpack_data&type=list"
    save_json(backpack_list_url, os.path.join(data_dir, "backpack_list.json"))
    download_backpack()

    # 模组
    module_list_url = "https://ma-activity.zlongame.com/common/infodata/mQuery.do?appkey=1616148215678&target=module_props&type=list"
    save_json(module_list_url, os.path.join(data_dir, "module_list.json"))
    download_module()

    # 元件
    component_list_url = "https://ma-activity.zlongame.com/common/infodata/mQuery.do?appkey=1616148215678&target=component_props&type=list"
    save_json(component_list_url, os.path.join(data_dir, "component_list.json"))
    download_component()


if __name__ == "__main__":
    download_all_data()
