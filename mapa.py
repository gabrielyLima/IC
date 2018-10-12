import math
import random


class map():
    def __init__(self, width, height):
        # O valor do raio de alcance de cada robô é por padrão 1
        self.robot_radious = 1
        self.width = width
        self.height = height
        self.grid = []
        self.pos_robot = []
        self.pos_target = []
        self.pos_wall = []
        self.min_step = 1
        self.max_step = 3

        # Preenche todas as posições do mapa com 0
        self.__initialize_map()

    def fill_map(self, posi_robot, posi_target, posi_wall):
        for pos in posi_robot:
            x, y = pos

            x = math.floor(x)
            y = math.floor(y)

            self.grid[y][x] = 6
            self.pos_robot.append((x, y))

        for pos in posi_target:
            x, y = pos

            x = math.floor(x)
            y = math.floor(y)

            self.grid[y][x] = 2
            self.pos_target.append((x, y))

        for pos in posi_wall:
            x, y = pos

            x = math.floor(x)
            y = math.floor(y)

            self.grid[y][x] = 3
            self.pos_wall.append((x, y))

    def set_robot_radious(self, radious):
        self.robot_radious = radious

    def move_robots(self):
        for i in range(len(self.pos_robot)):
            x, y = self.pos_robot[i]
            self.marking_map(x, y)

            x_new = x + self.random_step()
            y_new = y + self.random_step()

            # Encontra uma posição válida para x, y que respeite os limites da matriz e que não esteja ocupada
            while self.__is_position_valid_robot((x_new, y_new)) is not True:
                x_new = x + self.random_step()
                y_new = y + self.random_step()

            x_new = math.floor(x_new)
            y_new = math.floor(y_new)

            self.pos_robot[i] = (x_new, y_new)
            self.grid[y][x] = 1
            self.grid[y_new][x_new] = 6

    def marking_map(self, x_pos_robot, y_pos_robot):
        # Gerando posições que serão visitadas de acordo com o raio
        pos_up = (x_pos_robot, y_pos_robot - 1)
        pos_down = (x_pos_robot, y_pos_robot + 1)

        pos_left = (x_pos_robot - 1, y_pos_robot)
        pos_rigth = (x_pos_robot + 1, y_pos_robot)

        pos_left_up = (x_pos_robot - 1, y_pos_robot - 1)
        pos_right_up = (x_pos_robot + 1, y_pos_robot - 1)

        pos_left_down = (x_pos_robot - 1, y_pos_robot + 1)
        pos_right_down = (x_pos_robot + 1, y_pos_robot + 1)

        positions_on_radius = [pos_up, pos_down, pos_left, pos_rigth, pos_left_up, pos_right_up, pos_left_down,
                               pos_right_down]

        # Posições que estão dentro do mapa
        posible_position = []

        # Verificando se as posições estão dentro da matriz
        for pos in positions_on_radius:
            if self.__is_on_matrix(pos):
                posible_position.append(pos)

        for pos in posible_position:
            x_pos_robot, y_pos_robot = pos

            # Se a célula estiver vazia siginifica que eu possa acessa-la
            if self.grid[y_pos_robot][x_pos_robot] is 0:
                self.grid[y_pos_robot][x_pos_robot] = 4
            if self.grid[y_pos_robot][x_pos_robot] is 2:
                pass
            if self.grid[y_pos_robot][x_pos_robot] is 3:
                pass

    def show_map(self):
        for elem in self.grid:
            for e in elem:
                print(str(e) + " ", end="")
            print()
        print()

    def random_step(self):
        setp1 = random.uniform(self.min_step, self.max_step)
        setp2 = random.uniform(-self.max_step, -self.min_step)

        signal = random.uniform(-1, 1)
        if (signal >= 0):
            return setp1
        else:
            return setp2

    def __initialize_map(self):
        for i in range(self.height):
            self.grid.append([])
            for j in range(self.width):
                self.grid[i].append(0)

    def __is_position_valid_robot(self, posi):
        answer = False
        x, y = posi

        x = math.floor(x)
        y = math.floor(y)

        if x >= 0 and y >= 0:
            if self.__is_on_matrix(posi):
                if self.grid[y][x] is 0 or self.grid[y][x] is 1 or self.grid[y][x] is 4:
                    answer = True
        return answer

    def __is_on_matrix(self, posi):
        x, y = posi
        return 0 <= x < self.width and 0 <= y < self.height