import tkinter
from tkinter import messagebox
from board.board_generator import gameBoard


uiFrame = tkinter.Frame()
uiFrame.pack(side='top')


class GUI:
    def __init__(self):
        self.rowNum = tkinter.StringVar()
        self.columnNum = tkinter.StringVar()
        self.bombNum = tkinter.StringVar()

    def check_input(self, event, rows, columns, bombs, g_board=gameBoard):
        i = rows.get()
        j = columns.get()
        b = bombs.get()
        if len(i) != 0 and len(j) != 0 and len(b) != 0:
            i_int = int(i)
            j_int = int(j)
            b_int = int(b)
            if 0 < i_int <= 8 and 0 < j_int <= 8 and b_int < i_int * j_int:
                g_board.generate_grid(i_int, j_int, b_int)
            elif b_int>=i_int*j_int:
                g_board.generate_grid(i_int, j_int, i_int*j_int-1)
            else:
                messagebox.showerror('Incorrect values', 'Values from 1-8 for rows and columns are accepted only')
        else:
            messagebox.showerror('Lacking values', 'Please fill in all the fields')

    def create_interface(self):
        label_rows = tkinter.Label(uiFrame, text='Rows')
        label_rows.pack(side='left')
        entry_rows = tkinter.Entry(uiFrame, width=5, textvariable=self.rowNum)
        entry_rows.pack(side='left')

        label_columns = tkinter.Label(uiFrame, text='Columns')
        label_columns.pack(side='left')
        entry_columns = tkinter.Entry(uiFrame, width=5, textvariable=self.columnNum)
        entry_columns.pack(side='left')

        label_bombs = tkinter.Label(uiFrame, text='Bombs')
        label_bombs.pack(side='left')
        entry_bombs = tkinter.Entry(uiFrame, width=5, textvariable=self.bombNum)
        entry_bombs.pack(side='left')

        start_button = tkinter.Button(uiFrame, text='Start')
        start_button.pack(side='right')
        start_button.bind('<Button-1>',
                          lambda e, i=self.rowNum,
                                 j=self.columnNum,
                                 b=self.bombNum: self.check_input(e, i, j, b))


UI = GUI()
