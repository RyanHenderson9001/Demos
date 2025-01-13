import pygame
import random

# Initialize pygame
pygame.init()

# Define constants
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
GRID_SIZE = 30
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (128, 0, 128)
TAN = (210, 180, 140)

# Tetrimino shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
]

SHAPE_COLORS = [CYAN, YELLOW, PURPLE, ORANGE, RED, GREEN, TAN]

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Game variables
clock = pygame.time.Clock()
game_over = False
current_piece = None
piece_x, piece_y = 0, 0
board = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]

def draw_grid():
    """Draw the grid lines on the screen."""
    for x in range(0, SCREEN_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (SCREEN_WIDTH, y))

def draw_board():
    """Draw the current state of the game board."""
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if board[y][x]:
                pygame.draw.rect(screen, board[y][x], (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, WHITE, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)

def draw_piece(piece, color, offset_x, offset_y):
    """Draw the current piece on the board."""
    for y, row in enumerate(piece):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, color, ((offset_x + x) * GRID_SIZE, (offset_y + y) * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def check_collision(piece, offset_x, offset_y):
    """Check if the piece collides with the walls or other pieces."""
    for y, row in enumerate(piece):
        for x, cell in enumerate(row):
            if cell:
                px, py = offset_x + x, offset_y + y
                if px < 0 or px >= GRID_WIDTH or py >= GRID_HEIGHT or board[py][px]:
                    #print("Hello")
                    return True
    return False

def clear_lines():
    """Clear any completed lines."""
    global board
    new_board = [row for row in board if any(cell == 0 for cell in row)]  # Keep non-full rows
    lines_cleared = GRID_HEIGHT - len(new_board)
    new_board = [[0] * GRID_WIDTH for _ in range(lines_cleared)] + new_board
    board = new_board
    print("did I clear anything1")
    return lines_cleared

def rotate_piece(piece):
    """Rotate the piece 90 degrees."""
    return [list(row) for row in zip(*piece[::-1])]

def drop_piece():
    """Move the current piece down by one row."""
    global piece_y
    if not check_collision(current_piece, piece_x, piece_y + 1):
        piece_y += 1
        print("the piece has dropped")
    else:
        place_piece()
        print("I am starting to drop")
        return True
    return False

def place_piece():
    """Place the piece on the board and create a new piece."""
    global piece_x, piece_y, current_piece
    for y, row in enumerate(current_piece):
        for x, cell in enumerate(row):
            if cell:
                board[piece_y + y][piece_x + x] = SHAPE_COLORS[SHAPES.index(current_piece)]
    current_piece = random.choice(SHAPES)
    piece_x = GRID_WIDTH // 2 - len(current_piece[0]) // 2
    piece_y = 0
    if check_collision(current_piece, piece_x, piece_y):
        print("I reached this line of code gameover")
        return True  # Game over if the new piece collides immediately
    print("game did not end once")
    return False

def handle_input():
    """Handle user input for moving and rotating the piece."""
    global piece_x, piece_y, current_piece
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if not check_collision(current_piece, piece_x - 1, piece_y):
            piece_x -= 1
    if keys[pygame.K_RIGHT]:
        if not check_collision(current_piece, piece_x + 1, piece_y):
            piece_x += 1
    if keys[pygame.K_DOWN]:
        drop_piece()
    if keys[pygame.K_UP]:
        rotated = rotate_piece(current_piece)
        if not check_collision(rotated, piece_x, piece_y):
            current_piece = rotated

def main():
    """Main game loop."""
    global game_over, current_piece, piece_x, piece_y

    current_piece = random.choice(SHAPES)
    piece_x = GRID_WIDTH // 2 - len(current_piece[0]) // 2
    piece_y = 0

    while not game_over:
        print("the game isnt over yet")
        screen.fill((0, 0, 0))  # Clear screen

        handle_input()  # Handle user inputs

        # Try to drop the piece automatically
        if not drop_piece():
            print("piece did not drop down")
            game_over = place_piece()

        clear_lines()  # Clear any full lines

        draw_board()  # Draw the game board
        draw_piece(current_piece, SHAPE_COLORS[SHAPES.index(current_piece)], piece_x, piece_y)
        print("123")
        draw_grid()  # Draw the grid

        pygame.display.flip()  # Update the screen
        clock.tick(60)  # Control game speed

    # Game over screen
    font = pygame.font.SysFont('Arial', 30)
    text = font.render("Game Over", True, (255, 0, 0))
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(60000)  # Wait for 2 seconds before closing
    pygame.quit()

if __name__ == "__main__":
    main()
