import os
import msvcrt

game_data = {
    'width': 5,
    'height': 5,
    'player': {"x": 0, "y": 0, "score": 0},
    'collectibles': [,
        {"x": 2, "y": 1, "collected": False},
        {"x": 4, "y": 3, "collected": False}
    ]
    'obstacles': [,
        {"x": 1, "y": 2},
        {"x": 3, "y": 1}
    ]

    'turtle': "\U0001F422"   # 🐢,
    'rock': "\U0001FAA8 "     # 🪨,
    'leaf': "\U0001F343"     # 🍃,
    'empty': "\u2B1B"        # ⬛,
}

# Draw the board
def draw_board():
    os.system("cls")  # Clear the terminal (Windows)
    for y in range(game_data['height']):
        row = ""
        for x in range(game_data['width']):
            if game_data['player']["x"] == x and game_data['player']["y"] == y:
                row += game_data['turtle']
            elif any(o["x"] == x and o["y"] == y for o in game_data['obstacles']):
                row += ROCK
            elif any(c["x"] == x and c["y"] == y and not c["collected"] for c in game_data['collectibles']):
                row += game_data['leaf']
            else:
                row += game_data['empty']
        print(row)
    print(f"Score: {game_data['player']['score']}")
    print("Move with W/A/S/D, Q to quit")

# Check collectibles
def check_collectibles():
    for c in game_data['collectibles']:
        if not c["collected"] and game_data['player']["x"] == c["x"] and game_data['player']["y"] == c["y"]:
            c["collected"] = True
            game_data['player']["score"] += 1
            print("You collected a leaf!")

# Move player
def move_player(key):
    key = key.lower()
    if key == "w" and player["y"] > 0:
        if not any(o["x"] == game_data['player']["x"] and o["y"] == game_data['player']["y"]-1 for o in game_data['obstacles']):
            game_data['player']["y"] -= 1
    elif key == "s" and game_data['player']["y"] < height-1:
        if not any(o["x"] == game_data['player']["x"] and o["y"] == game_data['player']["y"]+1 for o in game_data['obstacles']):
            game_data['player']["y"] += 1
    elif key == "a" and game_data['player']["x"] > 0:
        if not any(o["x"] == game_data['player']["x"]-1 and o["y"] == game_data['player']["y"] for o in game_data['obstacles']):
            game_data['player']["x"] -= 1
    elif key == "d" and game_data['player']["x"] < width-1:
        if not any(o["x"] == game_data['player']["x"]+1 and o["y"] == game_data['player']["y"] for o in game_data['obstacles']):
            game_data['player']["x"] += 1

# Main game loop
def play_game():
    draw_board()
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch().decode("utf-8")
            if key.lower() == "q":
                print("Thanks for playing!")
                break
            move_player(key)
            check_collectibles()
            draw_board()

play_game()