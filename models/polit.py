class Pilot:
    """
    机兵部件
    """

    def __init__(self, ID=None, name=None, RealName=None, Gender=None, Profession=None,
                 quality=None, Occupation=None, MechaDriveLevel=None, Combat=None, Assault=None,
                 Shooting=None, Tactics=None, Defense=None, Engineering=None
                 , **kwargs):  # 字典比类字段多时报错，需要
        self.ID = ID
        self.name = name
        self.RealName = RealName
        self.Gender = Gender
        self.Profession = Profession
        self.quality = quality
        self.Occupation = Occupation
        self.MechaDriveLevel = MechaDriveLevel
        self.Combat = Combat
        self.Assault = Assault
        self.Shooting = Shooting
        self.Tactics = Tactics
        self.Defense = Defense
        self.Engineering = Engineering

    @classmethod
    def from_dict(cls, data):
        # 检查data是否为字典
        if not isinstance(data, dict):
            raise ValueError("Data must be a dictionary")

        if "manji" in data:
            data.update(data["manji"])

        # 使用字典的键值对设置属性
        return cls(**data)
