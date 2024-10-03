import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import AlgorithmCollection as algo
root = tk.Tk()  # create root window
root.title("GUI 1.0")
root.config(bg="skyblue")
root.geometry("1200x800")
root.minsize(800, 800)

user_array = []
low = None
high = None
target_num = None


# Fixed size selection_frame (300px wide, 70% of the window's height)
selection_frame = tk.Frame(root, bg="lightcoral")
selection_frame.place(x=0, y=0, width=300, relheight=0.7)  # Fixed width, relative height

# Fixed size button_frame (300px wide, 30% of the window's height)
button_frame = tk.Frame(root, bg="white")
button_frame.place(x=0, rely=0.7, width=300, relheight=0.3)  # Fixed width, relative height

# Timer variables
is_running = False
elapsed_time = 0

# Define a function to update the timer
def update_timer():
    global elapsed_time
    if is_running:
        elapsed_time += 1  # Increment the timer
        print(f"Elapsed Time: {elapsed_time} seconds")
        root.after(1000, update_timer)  # Call this function again after 1 second

# Define a function to be called when the start button is clicked
def on_startbutton_click():
    global is_running
    is_running = True
    pause_button.config(state=tk.NORMAL)
    reset_button.config(state=tk.NORMAL)
    start_button.config(state=tk.DISABLED)
    update_timer()  # Start updating the timer
    perform_sort()
    print("Start button was clicked!")

def on_pausebutton_click():
    global is_running
    is_running = not is_running  # Toggle the running state
    if is_running:
        pause_button.config(text="Pause")
        update_timer()
        print("Resumed timer.")
    else:
        pause_button.config(text="Resume")
        print("Paused timer")

def on_resetbutton_click():
    global is_running, elapsed_time
    is_running = False
    elapsed_time = 0
    pause_button.config(text="Pause")  # Reset the button text
    pause_button.config(state=tk.DISABLED)
    start_button.config(state=tk.NORMAL)
    reset_button.config(state=tk.DISABLED)
    print("Reset button was clicked!")

# Create a variable to store the selected category
category_var = tk.StringVar(value="Bubble Sort")  # Default selection

# Create a frame for array input (hidden initially)
input_frame = None

def perform_sort():
    selected_category = category_var.get()
    
    if selected_category == "Bubble Sort":
        algo.bubble_sort(user_array)
          # Update visualization after sorting
    
    elif selected_category == "Merge Sort":
        algo.merge_sort(user_array)

    
    elif selected_category == "Quick Sort":
        if low is not None and high is not None:
            algo.quick_sort(user_array, low, high)

    elif selected_category == "Radix Sort":
        algo.radix_sort(user_array)

    
    elif selected_category == "Linear Search Algorithm":
        if target_num is not None:
            algo.linear_search_algorithm(user_array, target_num)

# Function to handle category selection
def on_category_select():
    global input_frame
    selected_category = category_var.get()
    print(f"Selected category: {selected_category}")

    # If an input frame already exists, destroy it
    if input_frame:
        input_frame.destroy()

    # Create a new input frame for user input
    input_frame = tk.Frame(root, bg="lightgreen", width=300)
    input_frame.place(x=0, rely=0.25, width=300, relheight=0.4)  # Adjust height as needed

    # Add a label and entry field for array input
    label = tk.Label(input_frame, text="Enter Array (comma-separated):", font=("Arial", 12), bg="lightgreen", fg="black")
    label.pack(pady=10)

    array_entry = tk.Entry(input_frame, width=30)
    array_entry.pack(pady=10)

    # Check which sorting algorithm was selected
    if selected_category in ["Bubble Sort", "Merge Sort", "Radix Sort"]:
        submit_button = tk.Button(input_frame, text="Submit", font=("Arial", 12), command=lambda: submit_array(array_entry.get()))
        submit_button.pack(pady=10)

    elif selected_category == "Quick Sort":
        # Additional fields for Quick Sort
        label2 = tk.Label(input_frame, text="Enter one integer for low:", font=("Arial", 12), bg="lightgreen", fg="black")
        label2.pack(pady=(10, 0))  # Add top padding only

        low_entry = tk.Entry(input_frame, width=30)
        low_entry.pack(pady=10)

        label3 = tk.Label(input_frame, text="Enter one integer for high:", font=("Arial", 12), bg="lightgreen", fg="black")
        label3.pack(pady=(10, 0))  # Add top padding only

        high_entry = tk.Entry(input_frame, width=30)
        high_entry.pack(pady=10)

        quick_sort_button = tk.Button(input_frame, text="Submit", command=lambda: run_quick_sort(array_entry.get(), low_entry.get(), high_entry.get()))
        quick_sort_button.pack(pady=10)

    elif selected_category == "Linear Search Algorithm":
        # Additional input for Linear Search target
        label2 = tk.Label(input_frame, text="Enter one integer for target:", font=("Arial", 12), bg="lightgreen", fg="black")
        label2.pack(pady=(10, 0))  # Add top padding only

        target_entry = tk.Entry(input_frame, width=30)
        target_entry.pack(pady=10)

        submit_button = tk.Button(input_frame, text="Submit", font=("Arial", 12), command=lambda: submit_linear_search(array_entry.get(), target_entry.get()))
        submit_button.pack(pady=10)

    # Optional: Force a UI update to ensure the frame and its contents are shown immediately
    root.update()




# Function to handle the array input submission
def submit_array(array_string):
    try:
        global user_array
        user_array = [int(x.strip()) for x in array_string.split(",")]  # Convert the string to a list of integers
        print(f"Array submitted: {user_array}")
    except ValueError:
        print("Invalid input. Please enter a valid array.")

def run_quick_sort(array_string, low_string, high_string):
    try:
        global user_array, low, high
        user_array = [int(x.strip()) for x in array_string.split(",")]  # Convert the string to a list of integers
        low = int(low_string.strip())
        high = int(high_string.strip())
        print(f"Array submitted: {user_array}")
        print(f"Low: {low}, High: {high}")
    except ValueError:
        print("Invalid input. Please enter a valid array.")

def submit_linear_search(array_string, target_string):
    try:
        global user_array, target_num
        user_array = [int(x.strip()) for x in array_string.split(",")]  # Convert the string to a list of integers
        target_num = int(target_string.strip())
        print(f"Array submitted: {user_array}")
        print(f"Low: {target_num}")
    except ValueError:
        print("Invalid input. Please enter a valid array.")



# Create radio buttons for category selection
categories = ["Bubble Sort", "Merge Sort", "Quick Sort", "Radix Sort", "Linear Search Algorithm"]
for i, category in enumerate(categories):
    radio_button = tk.Radiobutton(selection_frame, text=category, variable=category_var, value=category, bg="lightcoral", command=on_category_select)
    radio_button.pack(anchor="center", padx=10, pady=5)  # Pack the radio buttons

# Create buttons
start_button = tk.Button(button_frame, text="Start", command=on_startbutton_click, bg="lightblue", fg="black", font=("Arial", 16))
start_button.place(relx=0.25, rely=0.05, relwidth=0.5, relheight=0.25)
start_button.config(state=tk.NORMAL)

pause_button = tk.Button(button_frame, text="Pause", command=on_pausebutton_click, bg="lightblue", fg="black", font=("Arial", 16))
pause_button.place(relx=0.25, rely=0.375, relwidth=0.5, relheight=0.25)
pause_button.config(state=tk.DISABLED)

reset_button = tk.Button(button_frame, text="Reset", command=on_resetbutton_click, bg="lightblue", fg="black", font=("Arial", 16))
reset_button.place(relx=0.25, rely=0.70, relwidth=0.5, relheight=0.25)
reset_button.config(state=tk.DISABLED)

# Dynamic graphic_frame that resizes with the window, placed next to the other frames

root.mainloop()
