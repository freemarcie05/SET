import pickle
import tkinter as tk
from tkinter import filedialog

class SaveLoad:
    @staticmethod
    def save_game(currentcards, total_sets, computer_sets, set_this_round, save_dir):
        root = tk.Tk()
        root.withdraw()

        file_path = filedialog.asksaveasfilename(initialdir=save_dir, title="Save game", defaultextension=".set", filetypes=[("SET Save Files", "*.set")])

        #If the saving is canceled
        if not file_path:
            return

        data = {"currentcards": currentcards, "total_sets": total_sets, "computer_sets": computer_sets, "set_this_round": set_this_round,}

        with open(file_path, "wb") as f:
            pickle.dump(data, f)

    @staticmethod
    def load_game(save_dir):
        root = tk.Tk()
        root.withdraw()

        file_path = filedialog.askopenfilename(initialdir=save_dir, title="Load game", filetypes=[("SET Save Files", "*.set")])

        #If the loading is canceled
        if not file_path:
            return None

        with open(file_path, "rb") as f:
            data = pickle.load(f)

        return data