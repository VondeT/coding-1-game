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
    'obstacle': "\U0001FAA8 ",
    'cheese': "\U0001F9C0",
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
            elif any(o['x'] == x and o['y'] == y for o in game_data['obstacles']):
                row += game_data['obstacle']
            # Collectibles
            elif any(c['x'] == x and c['y'] == y and not c['collected'] for c in game_data['collectibles']):
                row += game_data['cheese']
            else:
                row += game_data['empty']
        stdscr.addstr(y, 0, row, curses.color_pair(1))

    stdscr.addstr(game_data['height'] + 1, 0,
                  f"Moves Survived: {game_data['player']['score']}",
                  curses.color_pair(1))
    stdscr.addstr(game_data['height'] + 2, 0,
                  "Move with W/A/S/D, Q to quit",
                  curses.color_pair(1))
    stdscr.refresh()

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
        return  # Invalid key or move off board
    for cheese in game_data['collectibles']:
        if cheese['x'] == new_x and cheese['y'] == new_y and not cheese['collected']:
            cheese['collected'] = True
            game_data['player']['score'] + 1

    # Check for obstacles
    if any(o['x'] == new_x and o['y']
     == new_y for o in game_data['obstacles']):
        return

    # Update position and increment score
    game_data['player']['x'] = new_x
    game_data['player']['y'] = new_y
    game_data['player']['score'] + 1

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)

    draw_board(stdscr)

    while True:
        try:
            key = stdscr.getkey()
        except:
            key = None

        if key:
            if key.lower() == "q":
                break

            move_player(key)
            draw_board(stdscr)

def spawn_cheese():
    # Limit number of leaves on board
    active_cheese = [c for c in game_data['collectibles'] if not c["collected"]]
    if len(active_cheese) >= 4:
        return

def spawn_cheese():
    # Limit number of cheese on board
    active_cheese = [c for c in game_data['collectibles'] if not c["collected"]]
    if len(active_cheese) >= 4:
        return
import random
    # Find a random free spot that is not on the player and not on another cheese
    while True:
        x = random.randint(0, game_data['width'] - 1)
        y = random.randint(0, game_data['height'] - 1)
       

        # Avoid player's current position
        if x == game_data["player_x"] and y == game_data["player_y"]:
            continue

        # Avoid overlapping other active cheese
        occupied = any(
            c["x"] == x and c["y"] == y and not c["collected"]
            for c in game_data["collectibles"]
        )
        if not occupied:
            break

    game_data["collectibles"].append({
        "x": x,
        "y": y,
        "collected": False
    })

# at start
for _ in range(3):
    spawn_cheese()

# inside your game loop, after moves or on a timer
spawn_cheese()


curses.wrapper(main)
