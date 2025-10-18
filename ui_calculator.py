import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.entry = tk.Entry(root, width=16, font=('Arial', 24), bd=4, relief='ridge', justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        tombol = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('c', 4, 2), ('+', 4, 3),
            ('=', 5, 0)
        ]

        for (teks, baris, kolom) in tombol:
            if teks == '=':
                btn = tk.Button(root, text=teks, width=22, height=2, font=('Arial', 14), command=self.calcula)
                btn.grid(row=baris, column=kolom, columnspan=4, pady=5)
            elif teks == 'c':
                btn = tk.Button(root, text=teks, width=5, height=2, font=('Arial', 14), command=self.hapus)
                btn.grid(row=baris, column=kolom, padx=5, pady=5)
            else:
                btn = tk.Button(root, text=teks, width=5, height=2, font=('Arial', 14), command=lambda t=teks: self.tekan(t))
                btn.grid(row=baris, column=kolom, padx=5, pady=5)