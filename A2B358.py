def calculate_points_1d(a, b):
    """
    计算一维线段上的1/3点、中点和4/5点

    参数:
        a: 起点坐标 (数值)
        b: 终点坐标 (数值)

    返回:
        dict: 包含三个关键点的坐标
    """
    length = b - a

    # 计算1/3点
    one_third = a + length / 3

    # 计算中点
    midpoint = (a + b) / 2

    # 计算4/5点
    four_fifth = a + length * 4 / 5

    return {
        '1/3_point': round(one_third, 2),
        'midpoint': round(midpoint, 2),
        '4/5_point': round(four_fifth, 2)
    }


# 示例使用
if __name__ == "__main__":
    while True:
        # 输入线段端点
        a = float(input("\n请输入起点坐标: "))
        b = float(input("请输入终点坐标: "))

        # 计算关键点
        points = calculate_points_1d(a, b)

        # 输出结果
        print(f"\n1/3点坐标: {points['1/3_point']}")
        print(f"中点坐标: {points['midpoint']}")
        print(f"4/5点坐标: {points['4/5_point']}")
