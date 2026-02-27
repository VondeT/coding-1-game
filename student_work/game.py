# The goals for this phase include:
# - Pick out some icons for your game
# - Establish a starting position for each icon
# - Pick a size for your playing space
# - Print your playing space with starting position of each icon

# To make this work, you may have to type this into the terminal --> pip install curses
import curses

game_data = {
    'width': 5,
    'height': 5,
    'player': {"x": 0, "y": 0, "score": 0, "energy": 10, "max_energy": 10},
    'collectibles': [
        {"x": 2, "y": 1, "collected": False},
    ],
    'obstacles': [
        {"x": 1, "y": 2},
        {"x": 3, "y": 1}
    ],

    # ASCII icons
    'mouse': "\U0001F401",
    'cheese': "\U0001F343",
    'empty': "  "
}

def draw_board(stdscr):
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, -1)

    stdscr.clear()
    for y in range(game_data['height']):
        row = ""
        for x in range(game_data['width']):
            # Player
            if x == game_data['player']['x'] and y == game_data['player']['y']:
                row += game_data['mouse']
            # Obstacles
            elif any(o['x'] == x and o['y'] == y for o in game_data['traps']):
                row += game_data['mouse_trap']
            # Collectibles
            elif any(c['x'] == x and c['y'] == y and not c['collected'] for c in game_data['collectibles']):
                row += game_data['cheese']
            else:
                row += game_data['empty']
        stdscr.addstr(y, 0, row, curses.color_pair(1))
def move_player(key):
    x = game_data['player']['x']
    y = game_data['player']['y']

    new_x, new_y = x, y
    key = key.lower()
    if key == "w" and y > 0: 
            new_y -= 1
    elif key == "s" and y < game_data['height'] - 1:
            new_y += 1
    elif key == "a" and x > 0:
             new_x -= 1
    elif key == "d" and x < game_data['width'] - 1:
            new_x += 1
    else:
         return 

if any(o['x'] == new_x and o['y'] == new_y for o in game_data['obstacles']):
        return

game_data['player']['x'] = new_x
game_data['player']['y'] = new_y
game_data['player']['score'] += 1


stdscr.refresh()
stdscr.getkey()  # pause so player can see board

curses.wrapper(draw_board)
