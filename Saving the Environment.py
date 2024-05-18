

import tkinter as tk
from tkinter import messagebox
import datetime

def register_volunteer():
    event_index = event_options.index(event_dropdown.get())
    event_name = events[event_index][0]
    event_date = events[event_index][1]
    event_time = events[event_index][2]
    event_location = events[event_index][3]
    volunteers_needed = events[event_index][4]

    volunteer_name = name_entry.get()
    trees_to_plant = trees_entry.get()
    choice = choice_var.get()  # Get the choice for volunteering hours or money

    if volunteer_name and trees_to_plant.isdigit() and int(trees_to_plant) > 0:
        if len(volunteers_registered[event_index]) < volunteers_needed:
            volunteers_registered[event_index].append((volunteer_name, int(trees_to_plant), choice))  # Store choice too
            total_trees_planted = sum([trees for _, trees, _ in volunteers_registered[event_index]])  # Calculate total trees planted
            if choice == "Hours":
                total_hours = total_trees_planted * 2  # Assume 2 hours per tree planted
                messagebox.showinfo("Success", f"Thank you, {volunteer_name}! You have successfully registered to plant {trees_to_plant} trees at the {event_name} event. You earned {total_hours} volunteering hours.")
            elif choice == "Money":
                total_money = total_trees_planted * 5  # Assume $5 per tree planted
                messagebox.showinfo("Success", f"Thank you, {volunteer_name}! You have successfully registered to plant {trees_to_plant} trees at the {event_name} event. You earned ${total_money}.")
        else:
            messagebox.showerror("Error", "Sorry, the maximum number of volunteers for this event has been reached.")
    else:
        messagebox.showerror("Error", "Please enter your name and a valid number of trees to plant.")

    display_event_details()

def display_event_details():
    event_index = event_options.index(event_dropdown.get())
    event_name = events[event_index][0]
    event_date = events[event_index][1]
    event_time = events[event_index][2]
    event_location = events[event_index][3]
    volunteers_needed = events[event_index][4]
    registered_volunteers = volunteers_registered[event_index]

    details_text = f"Event Name: {event_name}\nDate: {event_date}\nTime: {event_time}\nLocation: {event_location}\nVolunteers Needed: {volunteers_needed}\n\nRegistered Volunteers:\n"
    if registered_volunteers:
        for volunteer, trees_to_plant, choice in registered_volunteers:
            details_text += f"- {volunteer} (Trees to plant: {trees_to_plant}, Reward: {choice})\n"
    else:
        details_text += "No volunteers registered yet."

    details_label.config(text=details_text)

# Sample events
events = [
    ("Tree Planting Event 1", datetime.date(2024, 6, 1), "10:00 AM", "City Park", 10),
    ("Tree Planting Event 2", datetime.date(2024, 6, 15), "9:00 AM", "Community Garden", 8)
]

# Initialize list to store registered volunteers for each event
volunteers_registered = [[] for _ in range(len(events))]

# Create GUI
root = tk.Tk()
root.title("Tree Planting Event Registration")

# Event dropdown
event_label = tk.Label(root, text="Select Event:")
event_label.grid(row=0, column=0, padx=10, pady=5)

event_options = [event[0] for event in events]
event_dropdown = tk.StringVar(root)
event_dropdown.set(event_options[0])
event_menu = tk.OptionMenu(root, event_dropdown, *event_options, command=display_event_details)
event_menu.grid(row=0, column=1, padx=10, pady=5)

# Volunteer name entry
name_label = tk.Label(root, text="Your Name:")
name_label.grid(row=1, column=0, padx=10, pady=5)

name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1, padx=10, pady=5)

# Number of trees entry
trees_label = tk.Label(root, text="Number of Trees to Plant:")
trees_label.grid(row=2, column=0, padx=10, pady=5)

trees_entry = tk.Entry(root)
trees_entry.grid(row=2, column=1, padx=10, pady=5)

# Choice for volunteering hours or money
choice_label = tk.Label(root, text="Choose Reward:")
choice_label.grid(row=3, column=0, padx=10, pady=5)

choice_var = tk.StringVar(root)
choice_var.set("Hours")  # Default choice
choice_menu = tk.OptionMenu(root, choice_var, "Hours", "Money")
choice_menu.grid(row=3, column=1, padx=10, pady=5)

# Register button
register_button = tk.Button(root, text="Register", command=register_volunteer)
register_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Event details label
details_label = tk.Label(root, text="", justify=tk.LEFT)
details_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Display initial event details
display_event_details()

root.mainloop()
