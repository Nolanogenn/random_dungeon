import random

min_room_size = 6
max_room_size = 20
min_rooms = 3
max_iters = 3

rooms = []

class Room:
    def __init__(self, x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

def __str__(self):
    return f"A room at ({self.x},{self.y})"

def init_rooms():
    total_rooms = random.randrange(min_rooms, max_rooms)

    for i in range(max_iters):
        for r in range(total_rooms):
            if len(rooms) >= max_rooms:
                break
    x = random.randrange(0, map_width)
    y = random.randrange(0, map_height)

    width = random.randrange(min_room_size, max_room_size)
    height = random.randrange(min_room_size, max_room_size)
    room = Room(x,y, width,height)

    if check_for_overlap(room, rooms):
        pass
    else:
        rooms.append(room)
    for room in rooms:
        for y in range(room.y, room.y+room.height):
            for x in range(room.x, room.x+room.width):
                map[x,y] = 1

def check_for_overlap(room, rooms):
    xmin1 = room.x
    xmax2 = xmin1 + room.width

    ymin1 = room.y
    ymax2 = ymin1 + room.height
    for current_room in rooms:
        xmin2 = current_room.x
        xmax2 = xmin2 + current_room.width

        ymin2 = current_room.y
        ymax2 = ymin2 + current_room.height

        if (xmin1 <= xmax2 and xmax1 >= xmin2) and \
                (ymin1 <= ymax2 and ymax2 >= ymin2):
            return True

    return False



