from utils.init_room import init_room
from utils.connect_rooms import connect_rooms
from utils.draw_dungeon import draw_dungeon

map_width = 50
map_height = 50


def init_map():
    for y in range(map_height):
        for x in range(map_width):
            map[x,y] = 0

def generate_dungeon():
    init_map()
    init_rooms()
    connect_rooms()
    draw_dungeon()

if __name__=="__main__":
    generate_dungeon()


