import tkinter as tk
from tkinter import font


class TicTacToeBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("tic-tac-toe")
        self._cells = {}

    def _create_board_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master=display_frame,
            text="Start"
        )
        # incomplete