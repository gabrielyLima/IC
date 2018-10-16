import matplotlib.pyplot as plt
from mapa import map

max_iterations = 10
weidth = 2500
height = 2500
m = map(weidth, height)
m.fill_map([(6, 6), (250, 250), (1000, 200)], [(3.1, 7.9), (0.4, 1.2)], [(5, 5)])
m.simulate(max_iterations)

maps = m.map_history

for k in range(len(maps)):
    x_robot = []
    y_robot = []

    target_x = []
    target_y = []

    wall_x = []
    wall_y = []

    empty_x = []
    empty_y = []

    visited_x = []
    visited_y = []

    possible_x = []
    possible_y = []

    grid = maps[k]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] is 0:
                empty_x.append(j)
                empty_y.append(i)
            elif grid[i][j] is 1:
                visited_x.append(j)
                visited_y.append(i)
            elif grid[i][j] is 2:
                target_x.append(j)
                target_y.append(i)
            elif grid[i][j] is 3:
                wall_x.append(j)
                wall_y.append(i)
            elif grid[i][j] is 4:
                possible_x.append(j)
                possible_y.append(i)
            elif grid[i][j] is 6:
                x_robot.append(j)
                y_robot.append(i)

    # g, r, b, y, black,
    fig = plt.figure(k)
    #plt.ylim(-1, weidth + 1)
    #plt.xlim(-1, height + 1)
    plt.plot(target_x, target_y, "ro", c='g')
    plt.plot(wall_x, wall_y, "ro", c='r')
    plt.plot(x_robot, y_robot, "ro", c='b')
    #plt.plot(empty_x, empty_y, "ro", c='y')
    plt.plot(visited_x, visited_y, "ro", c='black')
    plt.plot(possible_x, possible_y, "ro", c="grey")

    plt.savefig('test' + str(k) + ".png")
    plt.show()
