import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import csv


def calculate_score():
    values_team_one = []
    values_team_two = []
    for entry_one, entry_two in zip(entries_team_one, entries_team_two):
        try:
            value_one = float(entry_one.get())
            value_two = float(entry_two.get())
            values_team_one.append(value_one)
            values_team_two.append(value_two)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")
            return

    score_team_one = sum(values_team_one)
    score_team_two = sum(values_team_two)

    score_label_team_one.config(text=f"Score Team 1: {score_team_one:.2f}")
    score_label_team_two.config(text=f"Score Team 2: {score_team_two:.2f}")

    if score_team_one > score_team_two:
        first_place = "Team 1"
        second_place = "Team 2"
    elif score_team_two > score_team_one:
        first_place = "Team 2"
        second_place = "Team 1"
    else:
        first_place = "Tie"
        second_place = "Tie"

    first_place_label.config(text=f"1st Place: {first_place}")
    second_place_label.config(text=f"2nd Place: {second_place}")


def clear_entries():
    for entry_one, entry_two in zip(entries_team_one, entries_team_two):
        entry_one.delete(0, tk.END)
        entry_two.delete(0, tk.END)


def reset_scores():
    for entry_one, entry_two in zip(entries_team_one, entries_team_two):
        entry_one.delete(0, tk.END)
        entry_two.delete(0, tk.END)
    score_label_team_one.config(text="Score Team 1: ")
    score_label_team_two.config(text="Score Team 2: ")
    first_place_label.config(text="1st Place: ")
    second_place_label.config(text="2nd Place: ")


def create_tooltip(widget, text):
    tooltip = tk.Toplevel(widget)
    tooltip.wm_overrideredirect(True)
    tooltip.wm_geometry("+0+0")
    tooltip_label = ttk.Label(
        tooltip, text=text, background="yellow", relief="solid", borderwidth=1
    )
    tooltip_label.pack()

    def show_tooltip(event):
        tooltip.wm_geometry(f"+{event.x_root+10}+{event.y_root+10}")
        tooltip.deiconify()

    def hide_tooltip(event):
        tooltip.withdraw()

    widget.bind("<Enter>", show_tooltip)
    widget.bind("<Leave>", hide_tooltip)
    tooltip.withdraw()


def export_scores():
    try:
        with filedialog.asksaveasfile(mode="w", defaultextension=".csv") as file:
            writer = csv.writer(file)
            writer.writerow(["Event", "Team 1", "Team 2"])
            for i, (entry_one, entry_two) in enumerate(
                zip(entries_team_one, entries_team_two)
            ):
                writer.writerow([criteria[i], entry_one.get(), entry_two.get()])
            writer.writerow(
                [
                    "Total",
                    sum(float(entry.get() or 0) for entry in entries_team_one),
                    sum(float(entry.get() or 0) for entry in entries_team_two),
                ]
            )
            messagebox.showinfo("Success", "Scores exported successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to export scores: {e}")


root = tk.Tk()
root.title("Scoring System")
root.geometry("800x550")
root.configure(bg="#ffffff")

style = ttk.Style()
style.theme_use("clam")

style.configure("TFrame", background="#ffffff")
style.configure(
    "TLabel", background="#ffffff", foreground="#333333", font=("Helvetica", 12)
)
style.configure(
    "TButton",
    background="#4CAF50",
    foreground="#ffffff",
    font=("Helvetica", 12, "bold"),
    padding=6,
)
style.map("TButton", background=[("active", "#45a049")])

title_label = ttk.Label(
    root,
    text="Scoring System",
    font=("Helvetica", 20, "bold"),
    background="#ffffff",
    foreground="#333333",
)
title_label.grid(row=0, column=0, columnspan=2, pady=20)

team_one_frame = ttk.Frame(root, borderwidth=2, relief="solid", padding=(20, 10))
team_one_frame.grid(row=1, column=0, padx=20, pady=20, sticky="n")

team_one_label = ttk.Label(
    team_one_frame,
    text="Team 1",
    font=("Helvetica", 16, "bold"),
    background="#ffffff",
    foreground="#333333",
)
team_one_label.pack()

criteria_frame_team_one = ttk.Frame(
    team_one_frame, borderwidth=2, relief="solid", padding=(20, 10)
)
criteria_frame_team_one.pack(pady=20)

criteria = ["Event 1", "Event 2", "Event 3", "Event 4", "Event 5"]
entries_team_one = []
for i in range(len(criteria)):
    label = ttk.Label(
        criteria_frame_team_one,
        text=criteria[i],
        background="#ffffff",
        foreground="#333333",
        font=("Helvetica", 12, "bold"),
    )
    label.grid(row=i, column=0, padx=10, pady=10, sticky="w")
    entry = ttk.Entry(criteria_frame_team_one)
    entry.grid(row=i, column=1, padx=10, pady=10)
    entries_team_one.append(entry)

score_label_team_one = ttk.Label(
    team_one_frame,
    text="Score Team 1: ",
    font=("Helvetica", 16),
    background="#ffffff",
    foreground="#333333",
)
score_label_team_one.pack()

team_two_frame = ttk.Frame(root, borderwidth=2, relief="solid", padding=(20, 10))
team_two_frame.grid(row=1, column=1, padx=20, pady=20, sticky="n")

team_two_label = ttk.Label(
    team_two_frame,
    text="Team 2",
    font=("Helvetica", 16, "bold"),
    background="#ffffff",
    foreground="#333333",
)
team_two_label.pack()

criteria_frame_team_two = ttk.Frame(
    team_two_frame, borderwidth=2, relief="solid", padding=(20, 10)
)
criteria_frame_team_two.pack(pady=20)

entries_team_two = []
for i in range(len(criteria)):
    label = ttk.Label(
        criteria_frame_team_two,
        text=criteria[i],
        background="#ffffff",
        foreground="#333333",
        font=("Helvetica", 12, "bold"),
    )
    label.grid(row=i, column=0, padx=10, pady=10, sticky="w")
    entry = ttk.Entry(criteria_frame_team_two)
    entry.grid(row=i, column=1, padx=10, pady=10)
    entries_team_two.append(entry)

score_label_team_two = ttk.Label(
    team_two_frame,
    text="Score Team 2: ",
    font=("Helvetica", 16),
    background="#ffffff",
    foreground="#333333",
)
score_label_team_two.pack()

buttons_frame = ttk.Frame(root)
buttons_frame.grid(row=2, column=0, columnspan=2, pady=20)

calculate_button = ttk.Button(buttons_frame, text="Calculate", command=calculate_score)
calculate_button.pack(side=tk.LEFT, padx=10)
create_tooltip(calculate_button, "Calculate the scores based on the entered values")

clear_button = ttk.Button(buttons_frame, text="Clear", command=clear_entries)
clear_button.pack(side=tk.LEFT, padx=10)
create_tooltip(clear_button, "Clear all the entries")

reset_button = ttk.Button(buttons_frame, text="Reset", command=reset_scores)
reset_button.pack(side=tk.LEFT, padx=10)
create_tooltip(reset_button, "Reset all the scores")

export_button = ttk.Button(buttons_frame, text="Export", command=export_scores)
export_button.pack(side=tk.LEFT, padx=10)
create_tooltip(export_button, "Export the scores to a CSV file")

rank_frame = ttk.Frame(root, borderwidth=2, relief="solid", padding=(20, 10))
rank_frame.grid(row=3, column=0, columnspan=2, pady=20)

first_place_label = ttk.Label(
    rank_frame,
    text="1st Place: ",
    font=("Helvetica", 16),
    background="#ffffff",
    foreground="#333333",
)
first_place_label.pack()
second_place_label = ttk.Label(
    rank_frame,
    text="2nd Place: ",
    font=("Helvetica", 16),
    background="#ffffff",
    foreground="#333333",
)
second_place_label.pack()

root.mainloop()
