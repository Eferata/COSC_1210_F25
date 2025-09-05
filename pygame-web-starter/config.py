# Grid and Room Settings
GRID_ROWS = 3
GRID_COLS = 3
ROOM_WIDTH = 200
ROOM_HEIGHT = 200
WALL_THICK = 4
DOOR_SIZE = 40

# Player Settings
PLAYER_SPEED = 100
PLAYER_IMAGE_PATH = "assets/goose.png"   # relative to project root
PLAYER_IMAGE_SIZE = (48, 48)             # w, h in pixels
PLAYER_RADIUS = 24                       # collision/visual radius

# Screen Size
WIDTH = ROOM_WIDTH * GRID_COLS
HEIGHT = ROOM_HEIGHT * GRID_ROWS

# Colors (R, G, B)
BG_COLOR = (34, 139, 34) # 34,139,34 forest green
WALL_COLOR = (200, 200, 200)
PLAYER_COLOR = (100, 200, 255)
BOX_COLOR = (225, 153, 100)

# Frames Per Second
FPS = 60
