import tkinter as tk
from tkinter import messagebox, scrolledtext
import numpy as np


def log(text):
    """Logs text to the output box."""
    output_box.insert(tk.END, text + "\n")
    output_box.see(tk.END)
    output_box.update()


def display_matrix(A):
    """Display matrix in formatted form inside GUI box."""
    matrix_str = "\n".join("   " + "  ".join(f"{val:8.3f}" for val in row) for row in A)
    log(matrix_str)
    log("-" * 60)


def gaussian_elimination_verbose(A):
    """Perform Gaussian elimination and log every step."""
    A = A.astype(float)
    n = A.shape[0]

    log("🔹 Initial Augmented Matrix:")
    display_matrix(A)

    for i in range(n):
       
        if i == 0:
            ones = np.where(A[:, 0] == 1)[0]
            if len(ones) > 0 and ones[0] != 0:
                log(f"↔ Bring the row with 1 in column 1 to top (R1 ↔ R{ones[0]+1})")
                A[[0, ones[0]]] = A[[ones[0], 0]]
                display_matrix(A)

       
        max_row = np.argmax(abs(A[i:, i])) + i

        if A[max_row, i] == 0:
            messagebox.showerror("Error", "Matrix is singular or has no unique solution.")
            return

        if max_row != i:
            log(f"↔ Swap R{i+1} ↔ R{max_row+1}")
            A[[i, max_row]] = A[[max_row, i]]
            display_matrix(A)

        
        pivot = A[i, i]
        if pivot != 1:
            log(f"÷ Normalize: R{i+1} = R{i+1} ÷ {pivot:.3f}")
            A[i] = A[i] / pivot
            display_matrix(A)

       
        for j in range(i + 1, n):
            factor = A[j, i]
            if factor != 0:
                log(f"↓ Eliminate: R{j+1} = R{j+1} - ({factor:.3f}) × R{i+1}")
                A[j] -= factor * A[i]
                display_matrix(A)

   
    for i in range(n - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            factor = A[j, i]
            if factor != 0:
                log(f"↑ Eliminate: R{j+1} = R{j+1} - ({factor:.3f}) × R{i+1}")
                A[j] -= factor * A[i]
                display_matrix(A)

    log("✅ Final Reduced Row Echelon Form:")
    display_matrix(A)

   
    solution = A[:, -1]
    log("\n📘 Solution:")
    for i, val in enumerate(solution):
        log(f"x{i+1} = {val:.3f}")


def solve_system():
    try:
        n = int(var_count.get())
        if n <= 0:
            raise ValueError

        A = []
        for i in range(n):
            row = []
            for j in range(n + 1):
                val = entries[i][j].get()
                row.append(float(val))
            A.append(row)

        A = np.array(A)
        output_box.delete(1.0, tk.END)
        gaussian_elimination_verbose(A)

    except ValueError:
        messagebox.showerror("Invalid Input", " Please enter valid numeric values.")


def create_input_fields():
    try:
        n = int(var_count.get())
        if n <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", " Enter a valid number of variables.")
        return

    for widget in input_frame.winfo_children():
        widget.destroy()

    global entries
    entries = []

    for i in range(n):
        row_entries = []
        for j in range(n + 1):
            e = tk.Entry(input_frame, width=6, justify="center")
            e.grid(row=i, column=j, padx=4, pady=4)
            row_entries.append(e)
            if j == n - 1:
                tk.Label(input_frame, text="|").grid(row=i, column=j + 1)
        entries.append(row_entries)

    tk.Button(root, text=" Solve System", command=solve_system,
              bg="#4CAF50", fg="white", font=("Arial", 10, "bold")).pack(pady=10)



root = tk.Tk()
root.title("Gaussian Elimination Solver")
root.geometry("850x600")
root.config(bg="#460000")

tk.Label(root, text=" Gaussian Elimination Step-by-Step",
         font=("Arial", 16, "bold"), bg="#FFFFFF").pack(pady=10)

frame_top = tk.Frame(root, bg="#710000")
frame_top.pack()

tk.Label(frame_top, text="Number of Variables:", bg="#FFFFFF").grid(row=0, column=0, padx=5)
var_count = tk.Entry(frame_top, width=5)
var_count.grid(row=0, column=1, padx=5)
tk.Button(frame_top, text="Create Inputs", command=create_input_fields,
          bg="#06477C", fg="white").grid(row=0, column=2, padx=5)

input_frame = tk.Frame(root, bg="#06002A")
input_frame.pack(pady=10)

output_box = scrolledtext.ScrolledText(root, width=100, height=20, wrap=tk.WORD, font=("Courier", 10))
output_box.pack(pady=10)

root.mainloop()
