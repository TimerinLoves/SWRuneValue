import tkinter as tk
from tkinter import ttk

def calculate_score(substats):
    score = 0
    for stat, value in substats.items():
        min_value = min_values.get(stat, 0)
        max_value = max_values.get(stat, 0)
        if min_value == max_value:
            continue  # Skip if min and max values are the same (e.g., for non-numeric stats)
        score += (value - min_value) / (max_value - min_value) * 100
    return score / len(substats)  # Average score


def apply_debuff(main_stat, slot, substats):
    if slot in (2, 4, 6):
        if main_stat in ('Attack', 'Defense', 'HP'):
            substats_score = calculate_score(substats)
            substats_score *= 0.8  # Applying the 20% reduction
            return substats_score
    return calculate_score(substats)


def calculate_rune_score():
    main_stat = main_stat_var.get()
    slot = int(slot_var.get())

    substats = {
        substat_comboboxes[i].get(): int(substat_values[i].get())
        for i in range(len(substat_comboboxes))
    }

    score = apply_debuff(main_stat, slot, substats)
    result_label.config(text=f"Final Rune Score: {score:.2f}")


def update_main_stat_options(event):
    slot = int(slot_var.get())
    if slot == 1:
        main_stat_combobox['values'] = ['Attack']
    elif slot == 3:
        main_stat_combobox['values'] = ['Defense']
    elif slot == 5:
        main_stat_combobox['values'] = ['HP']
    elif slot == 2:
        main_stat_combobox['values'] = ['Speed', 'Attack', 'Attack%', 'Defense', 'Defense%', 'HP', 'HP%']
    elif slot == 4:
        main_stat_combobox['values'] = ['Attack', 'Attack%', 'Defense', 'Defense%', 'HP', 'HP%', 'Crit Rate', 'Crit Damage']
    elif slot == 6:
        main_stat_combobox['values'] = ['Attack', 'Attack%', 'Defense', 'Defense%', 'HP', 'HP%', 'Accuracy', 'Resistance']


# GUI Setup
root = tk.Tk()
root.title("Rune Judging Program")

slot_label = ttk.Label(root, text="Slot:")
slot_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
slot_var = tk.StringVar()
slot_combobox = ttk.Combobox(root, textvariable=slot_var, values=[1, 2, 3, 4, 5, 6])
slot_combobox.grid(row=0, column=1, padx=5, pady=5)
slot_combobox.bind("<<ComboboxSelected>>", update_main_stat_options)

main_stat_label = ttk.Label(root, text="Main Stat:")
main_stat_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
main_stat_var = tk.StringVar()
main_stat_combobox = ttk.Combobox(root, textvariable=main_stat_var, values=['Attack'])
main_stat_combobox.grid(row=1, column=1, padx=5, pady=5)

substat_labels = []
substat_comboboxes = []
substat_values = []
for i, stat in enumerate(['Substat 1', 'Substat 2', 'Substat 3', 'Substat 4']):
    label = ttk.Label(root, text=stat)
    label.grid(row=i + 2, column=0, padx=5, pady=2, sticky="e")
    substat_labels.append(label)

    substat_var = tk.StringVar()
    substat_combobox = ttk.Combobox(root, textvariable=substat_var)
    substat_combobox.grid(row=i + 2, column=1, padx=5, pady=2)
    substat_combobox['values'] = ['-', 'Attack', 'Attack%', 'Defense', 'Defense%', 'HP', 'HP%', 'Speed', 'Crit Rate', 'Crit Damage', 'Resistance', 'Accuracy']
    substat_comboboxes.append(substat_combobox)

    value_var = tk.StringVar()
    value_entry = ttk.Entry(root, textvariable=value_var)
    value_entry.grid(row=i + 2, column=2, padx=5, pady=2)
    substat_values.append(value_var)

calculate_button = ttk.Button(root, text="Calculate Score", command=calculate_rune_score)
calculate_button.grid(row=10, column=0, columnspan=3, pady=10)

result_label = ttk.Label(root, text="")
result_label.grid(row=11, column=0, columnspan=3)

min_values = {
    'Attack': 10,
    'Attack%': 5,
    'Defense': 10,
    'Defense%': 5,
    'HP': 135,
    'HP%': 5,
    'Speed': 4,
    'Crit Rate': 4,
    'Crit Damage': 4,
    'Resistance': 4,
    'Accuracy': 4
}

max_values = {
    'Attack': 20,
    'Attack%': 8,
    'Defense': 20,
    'Defense%': 8,
    'HP': 375,
    'HP%': 8,
    'Speed': 6,
    'Crit Rate': 6,
    'Crit Damage': 7,
    'Resistance': 8,
    'Accuracy': 8
}

root.mainloop()
