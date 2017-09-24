import math


def coordinates_to_angles(l):
    a = []
    for i in range(1, len(l)):
        r = math.atan2(l[i][1] - l[i-1][1], l[i][0] - l[i-1][0])
        d = math.degrees(r)
        a.append(d)

    print(a)
    return a


def quantize_sample(l, n, step=1):
    """
    quantizes list elements using n levels => 0->n-1
    :param l:
    :param n:
    :return:
    """
    def trim(x2):
        if x2 == -n/2:
            return n/2 + n/2 - 1
        else:
            return x2 + n/2 -1

    noise = 360/n
    l = coordinates_to_angles(l)
    s = l[::step]
    qd = list(map(lambda x: round(x/noise), s))
    qd = list(map(trim, qd))  # now in case of n=8 , 0 represents range(-112.5,157.5)
    print(qd)
    return qd


if __name__ == "__main__":
    l = [[82, 265], [80, 263], [91, 263], [92, 263], [90, 265], [96, 266], [100, 266], [106, 268], [119, 270], [134, 272], [149, 272], [173, 272], [197, 272], [229, 272], [260, 272], [285, 272], [323, 272], [344, 272], [361, 272], [375, 272], [383, 273], [386, 274], [389, 274], [392, 273], [397, 269], [405, 261], [418, 248], [439, 227], [461, 209], [486, 189], [512, 168], [528, 153], [539, 142], [547, 134], [555, 130], [559, 124], [560, 123]]
    quantized = quantize_sample(l, 8)
    # print(quantized)
