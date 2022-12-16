

def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "body":
                body = Body()
                parse_star_parameters(line, body)
                objects.append(body)
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, body):
    """Считывает данные о тела из строки.
    Входная строка должна иметь слеюущий формат:
    Body <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты тела, (Vx, Vy) — скорость.
    Пример строки:
    Body 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описанием тела.
    **body** — объект тела.
    """
    data = line.split()
    body.R = float(data[1])
    body.color = data[2]
    body.m = float(data[3])
    body.x = float(data[4])
    body.y = float(data[5])
    body.Vx = float(data[6])
    body.Vy = float(data[7])
