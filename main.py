import tkinter as tk
from tkinter import messagebox
import random


def check_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Egalitate!"
    elif (
            (player_choice == "piatră" and computer_choice == "foarfecă")
            or (player_choice == "foarfecă" and computer_choice == "hârtie")
            or (player_choice == "hârtie" and computer_choice == "piatră")
    ):
        return "Ai câștigat!"
    else:
        return "Ai pierdut!"


def play_game(player_choice):
    choices = ["piatră", "foarfecă", "hârtie"]
    computer_choice = random.choice(choices)
    result = check_winner(player_choice, computer_choice)
    messagebox.showinfo("Rezultat", f"Ai ales: {player_choice}\nCalculatorul a ales: {computer_choice}\n{result}")


def create_game_window():
    window = tk.Tk()
    window.title("Piatră, Foarfecă, Hârtie")
    window.geometry("450x70")


    lbl_title = tk.Label(window, text="Alege opțiunea ta:", borderwidth=5, border=10, font=10)
    lbl_title.grid(row=1, column=0)

    btn_rock = tk.Button(window, text="Piatră", command=lambda: play_game("piatră"), borderwidth=5, padx=10, pady=10, border=10, font=10)
    btn_rock.grid(row=1, column=1)

    btn_scissors = tk.Button(window, text="Foarfecă", command=lambda: play_game("foarfecă"), borderwidth=5, padx=10, pady=10, border=10, font=10)
    btn_scissors.grid(row=1, column=2)

    btn_paper = tk.Button(window, text="Hârtie", command=lambda: play_game("hârtie"), borderwidth=5, padx=10, pady=10, border=10, font=10)
    btn_paper.grid(row=1, column=3)

    window.mainloop()


create_game_window()