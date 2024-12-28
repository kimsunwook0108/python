import pygame
import sys

# Initialize
pygame.init()
pygame.font.init()

# Constants
WINDOW_SIZE = 800
BOARD_SIZE = 8
SQUARE_SIZE = WINDOW_SIZE // BOARD_SIZE
PIECE_FONT = pygame.font.SysFont('segoe ui symbol', 72)
STATUS_FONT = pygame.font.SysFont('arial', 24)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HIGHLIGHT = (255, 255, 0)
LIGHT_SQUARE = (240, 217, 181)
DARK_SQUARE = (181, 136, 99)
TEXT_COLOR = (50, 50, 50)

# Unicode chess pieces
PIECES = {
    'white_king': '♕', 'white_queen': '♔', 'white_rook': '♖',
    'white_bishop': '♗', 'white_knight': '♘', 'white_pawn': '♙',
    'black_king': '♛', 'black_queen': '♚', 'black_rook': '♜',
    'black_bishop': '♝', 'black_knight': '♞', 'black_pawn': '♟'
}

class Piece:
    def __init__(self, color, piece_type):
        self.color = color
        self.type = piece_type
        self.has_moved = False
        self.symbol = PIECES[f"{color}_{piece_type}"]
    
    def get_valid_moves(self, board, start_pos):
        row, col = start_pos
        moves = []
        
        # Pawn movement
        if self.type == 'pawn':
            direction = -1 if self.color == 'white' else 1
            # Forward move
            if 0 <= row + direction < BOARD_SIZE and not board[row + direction][col]:
                moves.append((row + direction, col))
                # Initial two-square move
                if not self.has_moved and not board[row + 2*direction][col]:
                    moves.append((row + 2*direction, col))
            # Captures
            for dcol in [-1, 1]:
                if 0 <= col + dcol < BOARD_SIZE:
                    if (board[row + direction][col + dcol] and 
                        board[row + direction][col + dcol].color != self.color):
                        moves.append((row + direction, col + dcol))
        
        # Rook movement
        elif self.type == 'rook':
            for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                x, y = row + dx, col + dy
                while 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE:
                    if board[x][y]:
                        if board[x][y].color != self.color:
                            moves.append((x, y))
                        break
                    moves.append((x, y))
                    x, y = x + dx, y + dy
        
        # Knight movement
        elif self.type == 'knight':
            for dx, dy in [(-2,-1), (-2,1), (-1,-2), (-1,2),
                          (1,-2), (1,2), (2,-1), (2,1)]:
                x, y = row + dx, col + dy
                if 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE:
                    if not board[x][y] or board[x][y].color != self.color:
                        moves.append((x, y))
        
        # Bishop movement
        elif self.type == 'bishop':
            for dx, dy in [(1,1), (1,-1), (-1,1), (-1,-1)]:
                x, y = row + dx, col + dy
                while 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE:
                    if board[x][y]:
                        if board[x][y].color != self.color:
                            moves.append((x, y))
                        break
                    moves.append((x, y))
                    x, y = x + dx, y + dy
        
        # Queen movement (combination of rook and bishop)
        elif self.type == 'queen':
            for dx, dy in [(0,1), (0,-1), (1,0), (-1,0),
                          (1,1), (1,-1), (-1,1), (-1,-1)]:
                x, y = row + dx, col + dy
                while 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE:
                    if board[x][y]:
                        if board[x][y].color != self.color:
                            moves.append((x, y))
                        break
                    moves.append((x, y))
                    x, y = x + dx, y + dy
        
        # King movement
        elif self.type == 'king':
            for dx, dy in [(0,1), (0,-1), (1,0), (-1,0),
                          (1,1), (1,-1), (-1,1), (-1,-1)]:
                x, y = row + dx, col + dy
                if 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE:
                    if not board[x][y] or board[x][y].color != self.color:
                        moves.append((x, y))
        
        return moves

def create_board():
    board = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']
    
    for col in range(BOARD_SIZE):
        board[1][col] = Piece('black', 'pawn')
        board[6][col] = Piece('white', 'pawn')
        board[0][col] = Piece('black', pieces[col])
        board[7][col] = Piece('white', pieces[col])
    
    return board

def draw_board(screen):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            color = LIGHT_SQUARE if (row + col) % 2 == 0 else DARK_SQUARE
            pygame.draw.rect(screen, color,
                           (col * SQUARE_SIZE, row * SQUARE_SIZE,
                            SQUARE_SIZE, SQUARE_SIZE))

def draw_pieces(screen, board):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            piece = board[row][col]
            if piece:
                text = PIECE_FONT.render(piece.symbol, True,
                                       WHITE if piece.color == 'white' else BLACK)
                text_rect = text.get_rect(center=(col * SQUARE_SIZE + SQUARE_SIZE//2,
                                                row * SQUARE_SIZE + SQUARE_SIZE//2))
                screen.blit(text, text_rect)

def draw_game_over(screen, winner):
    overlay = pygame.Surface((WINDOW_SIZE, WINDOW_SIZE))
    overlay.set_alpha(128)
    overlay.fill(BLACK)
    screen.blit(overlay, (0,0))
    
    text = PIECE_FONT.render(f"{winner} 승리!", True, WHITE)
    restart_text = STATUS_FONT.render("R 키를 눌러서 재시작", True, WHITE)
    
    text_rect = text.get_rect(center=(WINDOW_SIZE//2, WINDOW_SIZE//2))
    restart_rect = restart_text.get_rect(center=(WINDOW_SIZE//2, WINDOW_SIZE//2 + 50))
    
    screen.blit(text, text_rect)
    screen.blit(restart_text, restart_rect)

def get_square_at_pixel(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def is_valid_move(board, start_pos, end_pos, turn):
    start_row, start_col = start_pos
    end_row, end_col = end_pos
    piece = board[start_row][start_col]
    
    if not piece or piece.color != turn:
        return False
    
    valid_moves = piece.get_valid_moves(board, start_pos)
    return (end_row, end_col) in valid_moves

def is_king_captured(captured_pieces):
    return any(piece.type == 'king' for piece in captured_pieces)

def reset_game():
    return (create_board(), 'white', [], [], False, None, None)

def main():
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption('Chess')
    
    board, turn, captured_white, captured_black, game_over, selected_piece, selected_pos = reset_game()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r and game_over:
                board, turn, captured_white, captured_black, game_over, selected_piece, selected_pos = reset_game()
            
            if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_square_at_pixel(pos)
                
                if selected_piece:
                    if is_valid_move(board, selected_pos, (row, col), turn):
                        if board[row][col]:
                            captured_piece = board[row][col]
                            if turn == 'white':
                                captured_white.append(captured_piece)
                                if captured_piece.type == 'king':
                                    game_over = True
                            else:
                                captured_black.append(captured_piece)
                                if captured_piece.type == 'king':
                                    game_over = True
                        
                        board[row][col] = selected_piece
                        board[selected_pos[0]][selected_pos[1]] = None
                        selected_piece.has_moved = True
                        turn = 'black' if turn == 'white' else 'white'
                    selected_piece = None
                    selected_pos = None
                else:
                    if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
                        piece = board[row][col]
                        if piece and piece.color == turn:
                            selected_piece = piece
                            selected_pos = (row, col)
        
        screen.fill(WHITE)
        draw_board(screen)
        if selected_pos and not game_over:
            pygame.draw.rect(screen, HIGHLIGHT,
                           (selected_pos[1] * SQUARE_SIZE,
                            selected_pos[0] * SQUARE_SIZE,
                            SQUARE_SIZE, SQUARE_SIZE), 3)
        draw_pieces(screen, board)
        
        if game_over:
            winner = "White" if turn == "black" else "Black"
            draw_game_over(screen, winner)
        
        pygame.display.flip()

if __name__ == "__main__":
    main()