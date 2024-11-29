class Aircraft:
    """
    机兵部件
    """

    def __init__(self, ID=None, name=None, position=None, type=None, quality=None,
                 aircraftWeight=None, durable=None, Armor=None, fire=None, output=None,
                 Antiriot=None, Hit=None, Dodge=None
                 , **kwargs):  # 字典比类字段多时报错，需要
        self.ID = ID  # ID
        self.name = name  # 名称
        self.position = position  # 部位
        self.type = type  # 甲种类
        self.quality = quality  # 品质
        self.aircraftWeight = aircraftWeight  # 重量
        self.durable = durable  # 耐久
        self.Armor = Armor  # 护甲
        self.fire = fire  # 火力
        self.output = output  # 出力
        self.Antiriot = Antiriot  # 抗暴
        self.Hit = Hit  # 命中
        self.Dodge = Dodge  # 闪避

    @classmethod
    def from_dict(cls, data):
        # 检查data是否为字典
        if not isinstance(data, dict):
            raise ValueError("Data must be a dictionary")

        if "manji" in data:
            data.update(data["manji"])

        # 使用字典的键值对设置属性
        return cls(**data)


class AircraftUnit:
    """
    机兵整机
    """

    def __init__(self, name=None, type=None, quality=None,
                 output=None, aircraftWeight=None, netWeight=None,
                 durableTop=None, durableRight=None, durableLeft=None, durableBottom=None,
                 ArmorTop=None, ArmorRight=None, ArmorLeft=None, ArmorBottom=None,
                 fireTop=None, fireRight=None, fireLeft=None, fireBottom=None,
                 Antiriot=None, Dodge=None,
                 fire=None, HitRight=None, HitLeft=None
                 , **kwargs):
        self.name = name  # 名称
        self.type = type  # 甲种类
        self.quality = quality  # 品质

        self.output = output  # 出力
        self.aircraftWeight = aircraftWeight  # 重量
        self.netWeight = netWeight  # 净出力

        self.durableTop = durableTop  # 躯干耐久
        self.durableRight = durableRight  # 右手耐久
        self.durableLeft = durableLeft  # 左手耐久
        self.durableBottom = durableBottom  # 腿部耐久

        self.ArmorTop = ArmorTop  # 躯干护甲
        self.ArmorRight = ArmorRight  # 右手护甲
        self.ArmorLeft = ArmorLeft  # 左手护甲
        self.ArmorBottom = ArmorBottom  # 腿部护甲

        self.fireTop = fireTop  # 躯干火力
        self.fireRight = fireRight  # 右手火力
        self.fireLeft = fireLeft  # 左手火力
        self.fireBottom = fireBottom  # 腿部火力

        self.Antiriot = Antiriot  # 抗暴
        self.Dodge = Dodge  # 闪避

        self.fire = fire  # 火力

        self.HitRight = HitRight  # 右手命中
        self.HitLeft = HitLeft  # 左手命中

    def combine_part(self, part: Aircraft):
        if self.fire is None:
            self.fire = 0
        if self.aircraftWeight is None:
            self.aircraftWeight = 0

        if part.position == "躯干":
            self.name = part.name  # 名称
            self.type = part.type  # 甲种类
            self.quality = part.quality  # 品质
            self.output = int(part.output)  # 出力

            self.durableTop = part.durable  # 耐久
            self.ArmorTop = part.Armor  # 护甲
            self.fireTop = part.fire  # 火力
            self.Antiriot = part.Antiriot  # 抗暴

            self.aircraftWeight += int(part.aircraftWeight)  # 重量
            self.fire += int(part.fire)  # 火力
        elif part.position == "右臂":
            self.durableRight = part.durable  # 耐久
            self.ArmorRight = part.Armor  # 护甲
            self.fireRight = part.fire  # 火力
            self.HitRight = part.Hit  # 命中

            self.aircraftWeight += int(part.aircraftWeight)  # 重量
            self.fire += int(part.fire)  # 火力
        elif part.position == "左臂":
            self.durableLeft = part.durable  # 耐久
            self.ArmorLeft = part.Armor  # 护甲
            self.fireLeft = part.fire  # 火力
            self.HitLeft = part.Hit  # 命中

            self.aircraftWeight += int(part.aircraftWeight)  # 重量
            self.fire += int(part.fire)  # 火力
        elif part.position == "腿部":
            self.durableBottom = part.durable  # 耐久
            self.ArmorBottom = part.Armor  # 护甲
            self.fireBottom = part.fire  # 火力
            self.Dodge = part.Dodge  # 命中

            self.aircraftWeight += int(part.aircraftWeight)  # 重量
            self.fire += int(part.fire)  # 火力

        self.netWeight = self.output - self.aircraftWeight  # 净出力
