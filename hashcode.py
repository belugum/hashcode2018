#!/usr/bin/python3

from sys import argv

"""def add_ride(cars, id_car, ride):
    x1 = int(ride.split(' ')[0])
    y1 = int(ride.split(' ')[1])
    x2 = int(ride.split(' ')[2])
    y2 = int(ride.split(' ')[3])
    start = int(ride.split(' ')[4])
    end = int(ride.split(' ')[5])
    if cars[id_car][start] != cars[id_car][start + 1]:
        return False
    x_cur, y_cur = cars[id_car][start]
    x_tmp, y_tmp = cars[id_car][start]
    cars[id_car][start] = x1, x2
    i = start
    while x_tmp != x_cur:
        i -= 1
        if (i < 0):
            return False
        x_tmp += 1 if x_cur > x_tmp else -1
        cars[id_car][i] = x_tmp, y_tmp
    while y_tmp != y_cur:
        i -= 1
        if (i < 0):
            return False
        y_tmp += 1 if y_cur > y_tmp else -1
        cars[id_car][i] = x_tmp, y_tmp
    i = start
    while x_tmp != x_cur:
        i += 1
        x_tmp += 1 if x_cur > x_tmp else -1
        cars[id_car][i] = x_tmp, y_tmp
    while y_tmp != y_cur:
        i += 1
        y_tmp += 1 if y_cur > y_tmp else -1
        cars[id_car][i] = x_tmp, y_tmp
    i += 1
    x_cur, y_cur = cars[id_car][i]
    while cars[id_car][i] != (x_cur, y_cur):
        cars[id_car][i] = x_tmp, y_tmp
        i += 1
    return True
"""        

def get_disp(car, start, end_, x, y, dist):
    i = start
    while car[i][2]:
        i += 1
    end = i + dist + abs(car[i][0] - x)  + abs(car[i][1] - y)
    if end > end_ or end > len(car):
        return -1
    j = i
    while j < end:
        if car[j][2]:
            return -1
        j += 1
    return i

def add_ride(cars, id_car, ride):
    x1 = int(ride.split(' ')[0])
    y1 = int(ride.split(' ')[1])
    x2 = int(ride.split(' ')[2])
    y2 = int(ride.split(' ')[3])
    start = int(ride.split(' ')[4])
    end = int(ride.split(' ')[5])
    real_start = get_disp(cars[id_car], start, end, x1, y1, abs(y1 - y2) + abs(x1 - x2))
    if real_start == -1:
        return False
    x_tmp , y_tmp, busy = cars[id_car][real_start]
    real_start -= 1
    while real_start < 0 or cars[id_car][real_start][0] != x1:
        real_start += 1
        x_tmp += 1 if x_tmp < x1 else -1
        cars[id_car][real_start][0] = x_tmp
        cars[id_car][real_start][1] = y_tmp
        cars[id_car][real_start][2] = True
    while cars[id_car][real_start][1] != y1:
        real_start += 1
        y_tmp += 1 if y_tmp < y1 else -1
        cars[id_car][real_start][0] = x_tmp
        cars[id_car][real_start][1] = y_tmp
        cars[id_car][real_start][2] = True
    while cars[id_car][real_start][0] != x2:
        real_start += 1
        x_tmp += 1 if x_tmp < x2 else -1
        cars[id_car][real_start][0] = x_tmp
        cars[id_car][real_start][1] = y_tmp
        cars[id_car][real_start][2] = True
    while cars[id_car][real_start][1] != y2:
        real_start += 1
        y_tmp += 1 if y_tmp < y2 else -1
        cars[id_car][real_start][0] = x_tmp
        cars[id_car][real_start][1] = y_tmp
        cars[id_car][real_start][2] = True
    return True


def main(name):
    f = open(name, 'r')
    line = f.readline()
    rows = int(line.split(' ')[0])
    cols = int(line.split(' ')[1])
    nb_vehi = int(line.split(' ')[2])
    nb_rides = int(line.split(' ')[3])
    bonus = int(line.split(' ')[4])
    steps = int(line.split(' ')[5])
    rides = list()
    for line in f:
        rides.append(line)
    cars = list()
    car_rides = list()
    for i in range(0, nb_vehi):
        cars.append(list())
        car_rides.append(list())
        for j in range(0, steps):
            cars[-1].append([0,0, False])
    i = 0
    for ride in rides:
        j = 0
        while j < len(cars):
            if add_ride(cars, j, ride):
                car_rides[j].append(i)
                break
            j += 1
        i += 1
    i = 0
    while i < len(car_rides):
        out = "%i" % len(car_rides[i])
        for ride in car_rides[i]:
            out += " %i" % ride
        print(out)
        i += 1
    

if __name__ == "__main__":
    main(argv[1])
