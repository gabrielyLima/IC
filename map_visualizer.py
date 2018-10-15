import matplotlib.pyplot as plt
from mapa import map


max_iterations = 5

m = map(10, 10)
m.fill_map([(6, 6)], [(3.1, 7.9), (0.4, 1.2)], [(5, 5)])

target_position = m.pos_target
wall_position = m.pos_wall

target_x = []
target_y = []

wall_x = []
wall_y = []

for pos in target_position:
    x, y = pos
    target_x.append(x)
    target_y.append(y)

for pos in wall_position:
    x, y = pos
    wall_x.append(x)
    wall_y.append(y)

for i in range(max_iterations):
    robot_position = m.pos_robot

    x_robot = []
    y_robot = []

    for pos in robot_position:
        x, y = pos
        x_robot.append(x)
        y_robot.append(y)

    fig = plt.figure(i)

    plt.ylim(-1, m.height + 1)
    plt.xlim(-1, m.width + 1)

    plt.plot(target_x, target_y, "ro")
    plt.plot(wall_x, wall_y, "ro", c='b')
    plt.plot(x_robot, y_robot, "ro", c='g')
    plt.savefig('test' + str(i) + ".png")
    m.move_robots()