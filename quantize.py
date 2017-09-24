import math


def coordinates_to_angles(l):
    a = []
    for i in range(1, len(l)):
        r = math.atan2(l[i][1] - l[i-1][1], l[i][0] - l[i-1][0])
        d = math.degrees(r)
        a.append(d)

    print(a)
    return a


def quantize(l, n):
    """
    quantizes list elements using n levels => 0->n-1
    :param l:
    :param n:
    :return:
    """
    noise = 360/n
    l=coordinates_to_angles(l)

    qd = list(map(lambda x: round(x/noise) , l))
    print(qd)
    return qd


if __name__ == "__main__":
    l = [[89, 265], [90, 265], [91, 265], [92, 265], [94, 265], [96, 266], [100, 266], [106, 268], [119, 270], [134, 272], [149, 272], [173, 272], [197, 272], [229, 272], [260, 272], [285, 272], [323, 272], [344, 272], [361, 272], [375, 272], [383, 273], [386, 274], [389, 274], [392, 273], [397, 269], [405, 261], [418, 248], [439, 227], [461, 209], [486, 189], [512, 168], [528, 153], [539, 142], [547, 134], [555, 130], [559, 124], [560, 123]]
    quantized=quantize(l, 8)
    # print(quantized)
