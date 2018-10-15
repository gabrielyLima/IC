class ComunicationPackageType():
    def __init__(self, pos_robot, pos_target = None, pos_wall = None):
        self.pos_robot = pos_robot
        self.pos_wall = pos_wall
        self.pos_target = pos_target

    def save_package(self, path):
        #salvando as informações no pacote tipo 1
        if self.pos_target is None and self.pos_wall is None:
            package_type = "1\n"

            x_pos_robot, y_pos_robot = self.pos_robot
            robot = str(x_pos_robot) + " " + str(y_pos_robot) + "\n"

            pacote = package_type + robot

            file = open(path, "w")
            file.write(pacote)

        elif self.pos_wall is not None and self.pos_target is None:
            package_type = "1\n"

            x_pos_robot, y_pos_robot = self.pos_robot
            robot = str(x_pos_robot) + " " + str(y_pos_robot) + "\n"

            x_pos_wall, y_pos_wall = self.pos_wall
            wall = str(x_pos_wall) + " " + str(y_pos_wall) + "\n"

            pacote = package_type + robot + wall

            file = open(path, "w")
            file.write(pacote)

        #salvando as informações no pacote tipo 2
        elif self.pos_wall is None and self.pos_target is not None:
            package_type = "2\n"

            x_pos_robot, y_pos_robot = self.pos_robot
            robot = str(x_pos_robot) + " " + str(y_pos_robot) + "\n"

            x_pos_target, y_pos_target = self.pos_target
            target = str(x_pos_target) + " " + str(y_pos_target) + "\n"

            pacote = package_type + robot + target

            file = open(path, "w")
            file.write(pacote)

        elif self.pos_wall is not None and self.pos_target is not None:
            package_type = "2\n"

            x_pos_robot, y_pos_robot = self.pos_robot
            robot = str(x_pos_robot) + " " + str(y_pos_robot) + "\n"

            x_pos_wall, y_pos_wall = self.pos_wall
            wall = str(x_pos_wall) + " " + str(y_pos_wall) + "\n"

            x_pos_target, y_pos_target = self.pos_target
            target = str(x_pos_target) + " " + str(y_pos_target) + "\n"

            pacote = package_type + robot + wall + target

            file = open(path, "w")
            file.write(pacote)





















