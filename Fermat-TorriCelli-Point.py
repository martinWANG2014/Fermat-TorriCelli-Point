#!/bin/python
# author: Chenghao WANG
# Contact: chenghaomartin@gmail.com
# institute: Heudiasyc
# 24/05/2018
import numpy as np
import matplotlib.pyplot as plt


# draw teh circumscribing circle to a triangle
def draw_circumscribing_circle(x_1, y_1, x_2, y_2, x_new, y_new):
    ax = plt.gca()
    a1 = 2 * (x_2 - x_1)
    b1 = 2 * (y_2 - y_1)
    c1 = np.power(x_2, 2) + np.power(y_2, 2) - np.power(x_1, 2) - np.power(y_1, 2)
    a2 = 2 * (x_new - x_2)
    b2 = 2 * (y_new - y_2)
    c2 = np.power(x_new, 2) + np.power(y_new, 2) - np.power(x_2, 2) - np.power(y_2, 2)
    center_x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
    center_y = (a1 * c2 - a2 * c1) / (a1 * b2 - a2 * b1)
    radius = np.sqrt(np.power(x_1 - x_2, 2) + np.power(y_1 - y_2, 2)) / np.sqrt(3)
    cir = plt.Circle((center_x, center_y), radius=radius, color='b', fill=False)
    ax.add_patch(cir)


# draw an equilateral triangle with a correct position
def draw_equilateral_triangles(x_1, y_1, x_2, y_2, x_3, y_3, a):
    angle = np.deg2rad(60)
    if a == 1:
        x_new = x_2 + np.cos(angle) * (x_3 - x_2) + np.sin(angle) * (y_3 - y_2)
        y_new = y_2 - np.sin(angle) * (x_3 - x_2) + np.cos(angle) * (y_3 - y_2)
        check = ((y_2 - y_3) * (x_1 - x_2) + (x_3 - x_2) * (y_1 - y_2)) * (
            (y_2 - y_3) * (x_new - x_2) + (x_3 - x_2) * (y_new - y_2))
        # print check
        if not check < 0:
            angle = np.deg2rad(-60)
            x_new = x_2 + np.cos(angle) * (x_3 - x_2) + np.sin(angle) * (y_3 - y_2)
            y_new = y_2 - np.sin(angle) * (x_3 - x_2) + np.cos(angle) * (y_3 - y_2)
        plt.plot([x_3, x_2], [y_3, y_2], color='orange')
        plt.plot([x_3, x_new], [y_3, y_new], color='y')
        plt.plot([x_2, x_new], [y_2, y_new], color='g')
    elif a == 2:
        x_new = x_1 + np.cos(angle) * (x_3 - x_1) + np.sin(angle) * (y_3 - y_1)
        y_new = y_1 - np.sin(angle) * (x_3 - x_1) + np.cos(angle) * (y_3 - y_1)
        check = ((y_3 - y_1) * (x_2 - x_3) + (x_1 - x_3) * (y_2 - y_3)) * (
            (y_3 - y_1) * (x_new - x_3) + (x_1 - x_3) * (y_new - y_3))
        # print check
        if not check < 0:
            angle = np.deg2rad(-60)
            x_new = x_1 + np.cos(angle) * (x_3 - x_1) + np.sin(angle) * (y_3 - y_1)
            y_new = y_1 - np.sin(angle) * (x_3 - x_1) + np.cos(angle) * (y_3 - y_1)
        plt.plot([x_3, x_1], [y_3, y_1], color='red')
        plt.plot([x_3, x_new], [y_3, y_new], color='y')
        plt.plot([x_1, x_new], [y_1, y_new], color='g')
    else:
        x_new = x_2 + np.cos(angle) * (x_1 - x_2) + np.sin(angle) * (y_1 - y_2)
        y_new = y_2 - np.sin(angle) * (x_1 - x_2) + np.cos(angle) * (y_1 - y_2)
        check = ((y_2 - y_1) * (x_3 - x_2) + (x_1 - x_2) * (y_3 - y_2)) * (
            (y_2 - y_1) * (x_new - x_2) + (x_1 - x_2) * (y_new - y_2))
        # print check
        if not check < 0:
            angle = np.deg2rad(-60)
            x_new = x_2 + np.cos(angle) * (x_1 - x_2) + np.sin(angle) * (y_1 - y_2)
            y_new = y_2 - np.sin(angle) * (x_1 - x_2) + np.cos(angle) * (y_1 - y_2)
        plt.plot([x_2, x_1], [y_2, y_1], color='grey')
        plt.plot([x_2, x_new], [y_2, y_new], color='y')
        plt.plot([x_1, x_new], [y_1, y_new], color='g')
    return x_new, y_new


def main(x_1, y_1, x_2, y_2, x_3, y_3):
    x_new, y_new = draw_equilateral_triangles(x_1, y_1, x_2, y_2, x_3, y_3, 1)
    draw_circumscribing_circle(x_2, y_2, x_3, y_3, x_new, y_new)
    x_new, y_new = draw_equilateral_triangles(x_1, y_1, x_2, y_2, x_3, y_3, 2)
    draw_circumscribing_circle(x_1, y_1, x_3, y_3, x_new, y_new)
    x_new, y_new = draw_equilateral_triangles(x_1, y_1, x_2, y_2, x_3, y_3, 3)
    draw_circumscribing_circle(x_2, y_2, x_1, y_1, x_new, y_new)
    plt.axis('scaled')
    plt.title("Fermat-Torricelli Point")
    plt.savefig("res.png")
    plt.show()
    plt.close()


if __name__ == '__main__':
    main(2, 5, 5, 5, 6, 7)
