import tkinter as tk
import webbrowser
import os, fnmatch
import subprocess

DAYS = ["S:/Claims EOB/Testfolder/39C5318831-4.pdf", "S:\Claims EOB\Testfolder\\39C5442119-2.pdf"]
MODES = [tk.SINGLE, tk.BROWSE, tk.MULTIPLE, tk.EXTENDED]


class ListApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.list = tk.Listbox(self)
        self.list.insert(0, *DAYS)
        self.print_btn = tk.Button(self, text="Print selection",
                                   command=self.print_selection)
        self.btns = [self.create_btn(m) for m in MODES]

        self.list.pack()
        self.print_btn.pack(fill=tk.BOTH)
        for btn in self.btns:
            btn.pack(side=tk.LEFT)

    def create_btn(self, mode):
        cmd = lambda: self.list.config(selectmode=mode)
        return tk.Button(self, command=cmd,
                         text=mode.capitalize())

    def print_selection(self):
        selection = self.list.curselection()
        selection1 = list(selection)
        print([self.list.get(i) for i in selection])
        str = ''
        for i in selection:
            str = str + self.list.get(i)
            # webbrowser.open_new(str)
            subprocess.Popen(str, shell=True)
        # webbrowser.open_new((self.list.get(i)) for i in selection)
        # webbrowser.open_new(str(self.list.get(i)) for i in selection)


if __name__ == "__main__":
    app = ListApp()
    app.mainloop()