import tkinter
from tkinter import messagebox
from random import randint
from math import ceil


buttonFrame = tkinter.Frame()
buttonFrame.pack(side='bottom')


class GameBoard:
    def __init__(self):
        self.questionMarkImage = tkinter.PhotoImage(file='questionmark.png')
        self.bombImage = tkinter.PhotoImage(file='bomb.png')
        self.coinImage = tkinter.PhotoImage(file='gold.png')
        self.coinFoundCounter = 0
        self.requiredCoins = 0
        self.gameBoard = []
        self.buttonList = []

    def generate_grid(self, rows, columns, bombs):
        self.gameBoard = []
        for button in self.buttonList:
            button.grid_forget()
        self.buttonList = []
        for i in range(rows):
            self.gameBoard.append([])
            for j in range(columns):
                self.gameBoard[i].append(1)
                self.generate_button(i, j)
        self.requiredCoins = ceil((rows*columns-bombs)/3)
        self.place_bombs(rows, columns, bombs)
        print(self.gameBoard)

    def place_bombs(self, rows, columns, bombs):
        bomb_indexes = set()
        while len(bomb_indexes) != bombs:
            bomb_indexes.add((randint(0, rows-1), randint(0, columns-1)))
        bomb_indexes_list = list(bomb_indexes)
        counter = 0
        for index in range(bombs):
            i = bomb_indexes_list[counter][0]
            j = bomb_indexes_list[counter][1]
            self.gameBoard[i][j] = 0
            counter += 1

    def generate_button(self, rows, columns):
        button = tkinter.Button(buttonFrame)
        button.config(image=self.questionMarkImage, width=100, height=100,
                      command=lambda b=button, i=rows, j=columns:
                      self.check_cell(b, i, j))
        button.grid(row=rows, column=columns)
        self.buttonList.append(button)

    def check_cell(self, button, row, column, msg_box=messagebox):
        if self.gameBoard[row][column] == 0:
            button.config(image=self.bombImage)
            msg_box.showinfo('Game Over', 'You found a bomb!')
            self.end_game()
        else:
            button.config(image=self.coinImage)
            self.coin_counter()

    def coin_counter(self, msg_box=messagebox):
        self.coinFoundCounter += 1
        if self.coinFoundCounter == self.requiredCoins:
            msg_box.showinfo('Victory', 'You won!')
            self.end_game()

    def end_game(self):
        for button in self.buttonList:
            button.config(state='disabled')
        self.coinFoundCounter = 0


gameBoard = GameBoard()
