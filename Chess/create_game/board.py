import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

def draw_board(board, color_map, move_num, images_dir):
    rows = len(board)
    cols = len(board[0]) if rows > 0 else 0
    fig, ax = plt.subplots(figsize=(max(cols, 6), max(rows, 6)))
    for y in range(rows):
        for x in range(cols):
            rect = patches.Rectangle((x, rows - 1 - y), 1, 1, edgecolor='black', facecolor='white')
            ax.add_patch(rect)
            piece = board[y][x]
            if piece:
                piece_color = color_map[y][x]
                ax.text(x + 0.5, rows - 1 - y + 0.5, piece, ha='center', va='center', fontsize=18, color=piece_color)
    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    ax.axis('off')
    filename = f"move_{move_num:02d}.png"
    filepath = os.path.join(images_dir, filename)
    plt.savefig(filepath, dpi=150)
    plt.close()