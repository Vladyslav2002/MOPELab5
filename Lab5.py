import random
from math import sqrt
import scipy.stats
m = 3
for i in range(100):
    def proga(m):
        x1max = 70
        x1min = 20
        x2max = 40
        x2min = -20
        x3max = 80
        x3min = 70
        xcpmax=(x1max + x2max + x3max) / 3
        xcpmin = (x1min + x2min + x3min) / 3
        ymax = 200 + xcpmax
        ymin = 200 + xcpmin
        amatrix = [[-1, -1, -1, 1, 1, 1, -1],
                   [-1, -1, 1, 1, -1, -1, 1],
                   [-1, 1, -1, -1, 1, -1, 1],
                   [-1, 1, 1, -1, -1, 1, -1],
                   [1, -1, -1, -1, -1, 1, 1],
                   [1, -1, 1, -1, 1, -1, -1],
                   [1, 1, -1, 1, -1, -1, -1],
                   [1, 1, 1, 1, 1, 1, 1]]
        for i in range(m):
            for j in range(len(amatrix)):
                amatrix[j].append(random.randint(int(ymin), int(ymax)))
        b0 = 0
        b1 = 0
        b2 = 0
        b3 = 0
        b12 = 0
        b13 = 0
        b23 = 0
        b123 = 0
        for i in range(8):
            yi = 0
            for j in range(len(amatrix[0]) - m, len(amatrix[0])):
                yi = yi + amatrix[i][j] / m
            b0 = b0 + yi / 8
            b1 = b1 + yi * amatrix[i][0] / 8
            b2 = b2 + yi * amatrix[i][1] / 8
            b3 = b3 + yi * amatrix[i][2] / 8
            b12 = b12 + yi * amatrix[i][3] / 8
            b13 = b13 + yi * amatrix[i][4] / 8
            b23 = b23 + yi * amatrix[i][5] / 8
            b123 = b123 + yi * amatrix[i][6] / 8
        blist = [b0, b1, b2, b3, b12, b13, b23, b123]
        text0 = "y  =  " + str('%.3f' % b0) + "  +  " + str('%.3f' % b1) + "*X1  +  " + str('%.3f' % b2) + "*X2  +"+str('%.3f'  %b3)+" * X3 + "+str('%.3f'  %b12)+" * X12 + "+str('%.3f'  %b13)+" * X13 +"+str('%.3f'  %b23)+" * X23 + "+str('%.3f'  %b123)+"* X123"
        for i in range(8):
            print(amatrix[i])
        print('Рівняння регресії:')
        print(text0)
        ynlist = []
        for i in range(8):
            yn = 0
            for j in range(len(amatrix[0]) - m, len(amatrix[0])):
                yn = yn + amatrix[i][j]
            yn = yn / m
            ynlist.append(yn)
        S2ylist = []
        S2ysum = 0
        for i in range(8):
            S2y = 0
            for j in range(len(amatrix) - m, len(amatrix)):
                S2y = S2y + ((amatrix[i][j] - ynlist[i]) ** 2) / m
            S2ylist.append(S2y)
            S2ysum = S2ysum + S2y
        Gp = max(S2ylist) / S2ysum
        print('Gp =', Gp)
        Gt = 0.5157
        print('Gt =', Gt)
        k = 0
        l = 0
        if Gp < Gt:
            print("Gp < Gt, а отже дисперсія  однорідна")
            k = k + 1
        else:
            proga(m + 1)
            l = l + 1
        S2b = S2ysum / 8
        S2B = S2b / (8 * m)
        SB = sqrt(S2B)
        for i in range(8):
            yi = 0
            for j in range(len(amatrix[0]) - m, len(amatrix[0])):
                yi = yi + amatrix[i][j] / m
            b0 = b0 + yi / 8
            b1 = b1 + yi * amatrix[i][0] / 8
            b2 = b2 + yi * amatrix[i][1] / 8
            b3 = b3 + yi * amatrix[i][2] / 8
            b12 = b12 + yi * amatrix[i][3] / 8
            b13 = b13 + yi * amatrix[i][4] / 8
            b23 = b23 + yi * amatrix[i][5] / 8
            b123 = b123 + yi * amatrix[i][6] / 8
        t0 = abs(b0) / SB

        t1 = abs(b1) / SB
        t2 = abs(b2) / SB
        t3 = abs(b3) / SB
        t4 = abs(b12) / SB
        t5 = abs(b13) / SB
        t6 = abs(b23) / SB
        t7 = abs(b123) / SB
        tlist = [t0, t1, t2, t3, t4, t5, t6, t7]
        ttabl = 2.120
        a = []
        d = 0
        for i in range(len(tlist)):
            if tlist[i] > ttabl:
                a.append(1)
                d = d + 1
            else:
                a.append(0)
        yslist = []
        for i in range(len(amatrix)):
            ysn = 0
            if a[0] == 1:
                ysn = tlist[0]
            for z in range(6):
                for j in range(7):
                    if a[z + 1] == 1:
                        ysn = ysn + amatrix[i][j] * blist[z + 1]
            yslist.append(ysn)
        tlist2 = ["  ", "*X1", "*X2", "*X3", "*X12", "*X13", "*X23", "*X123"]
        text3 = "y  =  "
        blist1 = [str('%.3f' % b0), "  +  " + str('%.3f' % b1), "  +  " + str('%.3f' % b2), "  +  " + str('%.3f' % b3),"  +  "
    + str('%.3f' % b12), "  +  " + str('%.3f' % b13), "  +  " + str('%.3f' % b23), "  +"+str('%.3f'  %b123)]
        for i in range(len(tlist2)):
            if a[i] == 1:
                text3 = text3 + (blist1[i]) + tlist2[i]
        print(text3)
        f4 = 8 - d
        f3 = 8 * (m - 1)
        sad = 0
        for i in range(len(yslist)):
            sad = sad + (yslist[i] - ynlist[i]) ** 2
        sad = (sad / f4) * 3
        Fp = sad / S2b
        if m == 3:
            fisher = [4.5, 3.6, 3.2, 3.0, 2.9, 2.7, 2.4]
        if m == 4:
            fisher = [4.5, 3.4, 3.0, 2.8, 2.6, 2.5, 2.2]
        if m == 5:
            fisher = [4.2, 3.3, 2.9, 2.7, 2.5, 2.4, 2.1]
        if m >= 6:
            if m <= 8:
                fisher = [4.1, 3.2, 2.9, 2.6, 2.5, 2.3, 2]
        if m >= 9:
            if m <= 15:
                fisher = [4.0, 3.2, 2.8, 2.5, 2.4, 2.3, 1.9]
        if m >= 16:
            fisher = [3.8, 3, 2.6, 2.4, 2.2, 2.1, 1.8]
        Fg = fisher[f4 - 1]
        print('Fp =', Fp)
        print('Fg =', Fg)
        f = 0
        n = 0
        if Fp > Fg:
            text2 = "Fp > Fg, а отже рівняння  регресії  неадекватне  оригіналу"
            f = f + 1
        else:
            text2 = "Fp < Fg, а отже рівняння  регресії  адекватне  оригіналу"
            n = n + 1
        print(text2)
        zn = 0
        nzn = 0
        zn = zn + k + f
        nzn = nzn + l + n
        print('Кількість значимих коефіцієнтів: ', zn)
        print('Кількість незначимих коефіцієнтів: ', nzn)
    proga(m)
