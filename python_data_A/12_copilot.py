import pygame
import sys
import random
import time
import os

# Initialize
pygame.init()
pygame.font.init()
pygame.mixer.init()

# Constants
WINDOW_SIZE = 1000
BOARD_SIZE = 15
CELL_SIZE = WINDOW_SIZE // (BOARD_SIZE + 1)
STONE_SIZE = int(CELL_SIZE * 0.45)
GAME_FONT = pygame.font.SysFont('malgungothic', 80, bold=True)
STATUS_FONT = pygame.font.SysFont('malgungothic', 40)

# Game states and colors
PLAYER = 0  # Black
AI = 1      # White
AI_DELAY = 0.3
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (205, 133, 63)
RED = (255, 0, 0)

# Sound effects
STONE_SOUND = pygame.mixer.Sound(os.path.join('sounds', 'stone.wav'))
WIN_SOUND = pygame.mixer.Sound(os.path.join('sounds', 'win.wav'))

def create_board():
    return [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def draw_board(screen):
    screen.fill(BROWN)
    for i in range(BOARD_SIZE):
        pygame.draw.line(screen, BLACK,
                        (CELL_SIZE * (i + 1), CELL_SIZE),
                        (CELL_SIZE * (i + 1), CELL_SIZE * BOARD_SIZE))
        pygame.draw.line(screen, BLACK,
                        (CELL_SIZE, CELL_SIZE * (i + 1)),
                        (CELL_SIZE * BOARD_SIZE, CELL_SIZE * (i + 1)))
    
    for x, y in [(3,3), (3,11), (11,3), (11,11), (7,7)]:
        center = (CELL_SIZE * (x + 1), CELL_SIZE * (y + 1))
        pygame.draw.circle(screen, BLACK, center, 5)

def draw_stones(screen, board):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] is not None:
                color = BLACK if board[row][col] == PLAYER else WHITE
                center = (CELL_SIZE * (col + 1), CELL_SIZE * (row + 1))
                pygame.draw.circle(screen, color, center, STONE_SIZE)
                if color == WHITE:
                    pygame.draw.circle(screen, BLACK, center, STONE_SIZE, 1)

def draw_status(screen, current_player, game_over, winner=""):
    if game_over:
        text = f"{winner} 승리!"
        color = RED
    else:
        text = "당신 차례" if current_player == PLAYER else "AI 생각중..."
        color = BLACK
    
    status = STATUS_FONT.render(text, True, color)
    text_rect = status.get_rect(center=(WINDOW_SIZE//2, 30))
    screen.blit(status, text_rect)

def evaluate_position(board, row, col, stone):
    directions = [(0,1), (1,0), (1,1), (1,-1)]
    score = 0
    
    for dx, dy in directions:
        count = 1
        block_count = 0
        space_count = 0
        
        for direction in [1, -1]:
            x, y = row + dx * direction, col + dy * direction
            temp_count = 0
            while 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE:
                if board[x][y] == stone:
                    temp_count += 1
                elif board[x][y] is None:
                    space_count += 1
                    break
                else:
                    block_count += 1
                    break
                x, y = x + dx * direction, y + dy * direction
            count += temp_count
        
        if count >= 5:
            score += 100000
        elif count == 4 and block_count == 0:
            score += 10000
        elif count == 4 and block_count == 1:
            score += 1000
        elif count == 3 and block_count == 0:
            score += 500
        elif count == 3 and block_count == 1:
            score += 100
        elif count == 2 and block_count == 0:
            score += 50
    
    return score

def get_valid_moves(board):
    moves = []
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] is None:
                moves.append((row, col))
    return moves

def get_ai_move(board):
    valid_moves = get_valid_moves(board)
    best_score = float('-inf')
    best_move = None
    
    for row, col in valid_moves:
        score = 0
        
        board[row][col] = AI
        if check_win(board, row, col):
            board[row][col] = None
            return row, col
        
        board[row][col] = PLAYER
        if check_win(board, row, col):
            score += 90000
        board[row][col] = None
        
        board[row][col] = AI
        score += evaluate_position(board, row, col, AI)
        score += evaluate_position(board, row, col, PLAYER) * 0.8
        
        center_dist = abs(row - BOARD_SIZE//2) + abs(col - BOARD_SIZE//2)
        score += (BOARD_SIZE - center_dist) * 2
        
        board[row][col] = None
        
        if score > best_score:
            best_score = score
            best_move = (row, col)
    
    return best_move

def check_win(board, row, col):
    directions = [(0,1), (1,0), (1,1), (1,-1)]
    stone = board[row][col]
    
    for dx, dy in directions:
        count = 1
        for direction in [-1, 1]:
            x, y = row, col
            while True:
                x, y = x + dx * direction, y + dy * direction
                if not (0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE) or board[x][y] != stone:
                    break
                count += 1
        if count >= 5:
            return True
    return False

def get_grid_position(pos):
    x, y = pos
    row = round((y - CELL_SIZE) / CELL_SIZE)
    col = round((x - CELL_SIZE) / CELL_SIZE)
    return row, col

def is_valid_move(board, row, col):
    return 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE and board[row][col] is None

def main():
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption('오목 VS AI')
    
    board = create_board()
    current_player = PLAYER
    game_over = False
    winner = ""
    ai_move_time = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if not game_over and current_player == PLAYER and event.type == pygame.MOUSEBUTTONDOWN:
                row, col = get_grid_position(event.pos)
                
                if is_valid_move(board, row, col):
                    board[row][col] = PLAYER
                    STONE_SOUND.play()
                    if check_win(board, row, col):
                        game_over = True
                        winner = "플레이어"
                        WIN_SOUND.play()
                    else:
                        current_player = AI
                        ai_move_time = time.time()
        
        if not game_over and current_player == AI and time.time() - ai_move_time >= AI_DELAY:
            row, col = get_ai_move(board)
            board[row][col] = AI
            STONE_SOUND.play()
            if check_win(board, row, col):
                game_over = True
                winner = "AI"
                WIN_SOUND.play()
            else:
                current_player = PLAYER
        
        draw_board(screen)
        draw_stones(screen, board)
        draw_status(screen, current_player, game_over, winner)
        pygame.display.flip()

if __name__ == "__main__":
    main()