def bullet_formula(n):
    """

    :param n: 连击数，大于等于1
    :return:
    """
    if n < 1:
        return 0

    def f():
        return min(6, n) * 5
        #return min(6, n - 1) * 5

    #print(f())
    return f()


def avg_damage_percent(n):
    ttl = 0
    for i in range(n):
        ttl += bullet_formula(i + 1)
    avg = round(ttl / n, 2)
    return avg


if __name__ == "__main__":
    bullet_cnt = 6
    weapon = "浮游炮"
    print(f"{weapon}连击数：{bullet_cnt}")
    print(f"平均增伤：{avg_damage_percent(bullet_cnt)}%")

    bullet_cnt = 8
    weapon = "觉醒浮游炮"
    print(f"{weapon}连击数：{bullet_cnt}")
    print(f"平均增伤：{avg_damage_percent(bullet_cnt)}%")

    bullet_cnt = 10
    weapon = "机枪"
    print(f"{weapon}连击数：{bullet_cnt}")
    print(f"平均增伤：{avg_damage_percent(bullet_cnt)}%")

    bullet_cnt = 20
    weapon = "机枪"
    print(f"{weapon}连击数：{bullet_cnt}")
    print(f"平均增伤：{avg_damage_percent(bullet_cnt)}%")

    bullet_cnt = 30
    weapon = "机枪"
    print(f"{weapon}连击数：{bullet_cnt}")
    print(f"平均增伤：{avg_damage_percent(bullet_cnt)}%")

    bullet_cnt = 11
    weapon = "彩机枪"
    print(f"{weapon}连击数：{bullet_cnt}")
    print(f"平均增伤：{avg_damage_percent(bullet_cnt)}%")

    bullet_cnt = 22
    weapon = "彩机枪"
    print(f"{weapon}连击数：{bullet_cnt}")
    print(f"平均增伤：{avg_damage_percent(bullet_cnt)}%")

    bullet_cnt = 33
    weapon = "彩机枪"
    print(f"{weapon}连击数：{bullet_cnt}")
    print(f"平均增伤：{avg_damage_percent(bullet_cnt)}%")

    bullet_cnt = 54
    weapon = "觉醒大招"
    print(f"{weapon}连击数：{bullet_cnt}")
    print(f"平均增伤：{avg_damage_percent(bullet_cnt)}%")


