import csv
import json
import os

from models.aircraft import Aircraft, AircraftUnit
from models.polit import Pilot


def list_dir(folder_path):
    files = []
    # 遍历文件夹
    for filename in os.listdir(folder_path):
        # 检查文件扩展名是否为.json
        if filename.endswith('.json'):
            # 构建完整的文件路径
            file_path = os.path.join(folder_path, filename)
            files.append(file_path)
    return files


def load_aircraft(json_file):
    parts = []
    with open(json_file, "r", encoding="utf-8") as f:
        ac = json.load(f)
        for part in ac["data"]["data"]:
            parts.append(Aircraft.from_dict(part))
        return parts


def load_ac_list():
    print("正在读取json")
    ac_list = list_dir("data/aircraft")
    t_list = []
    for ac_path in ac_list:
        t_list += load_aircraft(ac_path)
    return t_list


def aircraft_to_csv():
    t_list = load_ac_list()
    # 指定CSV文件的名称
    if not os.path.exists("csv"):
        # 如果文件夹不存在，则创建文件夹
        os.makedirs("csv")
    csv_file_name = 'csv/aircraft_parts.csv'
    # 打开文件，准备写入
    print("正在写入csv")
    with open(csv_file_name, 'w', newline='', encoding='utf-8') as csvfile:
        # 创建一个csv.writer对象
        writer = csv.writer(csvfile)
        # 写入标题行
        writer.writerow(['ID', 'name', 'position', 'type', 'quality'
                            , 'aircraftWeight', 'durable', 'Armor', 'fire', 'output'
                            , 'Antiriot', 'Hit', 'Dodge'])
        # 遍历实例列表，写入每行数据
        for t in t_list:
            writer.writerow([t.ID, t.name, t.position, t.type, t.quality
                                , t.aircraftWeight, t.durable, t.Armor, t.fire, t.output
                                , t.Antiriot, t.Hit, t.Dodge])


def aircraft_to_csv_2():
    t_list = load_ac_list()
    # 指定CSV文件的名称
    if not os.path.exists("csv"):
        # 如果文件夹不存在，则创建文件夹
        os.makedirs("csv")
    csv_file_name = 'csv/aircraft_unit.csv'

    u_list = []
    for t in t_list:
        acu = [u for u in u_list if u.name == t.name]
        if len(acu) == 0:
            acu = AircraftUnit()
            u_list.append(acu)
        else:
            acu = acu[0]
        acu.combine_part(t)

    # 打开文件，准备写入
    print("正在写入csv")
    with open(csv_file_name, 'w', newline='', encoding='utf-8') as csvfile:
        # 创建一个csv.writer对象
        writer = csv.writer(csvfile)

        # 写入标题行
        writer.writerow(['name', 'type', 'quality'
                            , "output", "aircraftWeight", "netWeight"
                            , 'durableTop', 'durableRight', 'durableLeft', 'durableBottom'
                            , 'ArmorTop', 'ArmorRight', 'ArmorLeft', 'ArmorBottom'
                            , 'fireTop', 'fireRight', 'fireLeft', 'fireBottom'
                            , 'Antiriot', 'Dodge'
                            , 'fire', 'HitRight', 'HitLeft'
                         ])

        # 遍历实例列表，写入每行数据
        for u in u_list:
            writer.writerow([u.name, u.type, u.quality
                                , u.output, u.aircraftWeight, u.netWeight
                                , u.durableTop, u.durableRight, u.durableLeft, u.durableBottom
                                , u.ArmorTop, u.ArmorRight, u.ArmorLeft, u.ArmorBottom
                                , u.fireTop, u.fireRight, u.fireLeft, u.fireBottom
                                , u.Antiriot, u.Dodge
                                , u.fire, u.HitRight, u.HitLeft])


def load_pilot(json_file):
    with open(json_file, "r", encoding="utf-8") as f:
        pl = json.load(f)
        return Pilot.from_dict(pl["data"]["data"])


def pilot_to_csv():
    print("正在读取json")
    pl_list = list_dir("data/pilot")
    t_list = []
    for pl_path in pl_list:
        t_list.append(load_pilot(pl_path))

    # 指定CSV文件的名称
    if not os.path.exists("csv"):
        # 如果文件夹不存在，则创建文件夹
        os.makedirs("csv")
    csv_file_name = 'csv/pilot.csv'

    # 打开文件，准备写入
    print("正在写入csv")
    with open(csv_file_name, 'w', newline='', encoding='utf-8') as csvfile:
        # 创建一个csv.writer对象
        writer = csv.writer(csvfile)

        # 写入标题行
        writer.writerow(['name', 'quality', "Occupation"
                            , "Combat", "Assault", "Shooting"
                            , 'Tactics', 'Defense', 'Engineering'
                         ])

        # 遍历实例列表，写入每行数据
        for t in t_list:
            writer.writerow([t.name, t.quality, t.Occupation
                                , t.Combat, t.Assault, t.Shooting
                                , t.Tactics, t.Defense, t.Engineering])


if __name__ == "__main__":
    aircraft_to_csv()
    aircraft_to_csv_2()
    pilot_to_csv()
