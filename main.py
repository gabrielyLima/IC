from mapa import map


def main():
    m = map(10, 10)
    m.show_map()
    m.fill_map([(6, 6)], [(3.1, 7.9), (0.4, 1.2)], [(5, 5)])
    m.simulate(10)


if __name__ == "__main__":
    main()