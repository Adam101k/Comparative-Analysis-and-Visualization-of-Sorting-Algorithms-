import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

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

# Function to handle category selection
def on_category_select():
    global input_frame
    selected_category = category_var.get()
    print(f"Selected category: {selected_category}")
    
    # If "Bubble Sort" is selected, show an input frame
    if selected_category == "Bubble Sort":
        if input_frame:  # Destroy the previous frame if it exists
            input_frame.destroy()
        # Create a new frame inside graphic_frame for input
        input_frame = tk.Frame(root, bg="lightgreen", width=300, height=200)
        input_frame.place(x=0, rely=0.25, width = 300)
        
        # Add a label and entry field for array input
        label = tk.Label(input_frame, text="Enter Array (comma-separated):", font=("Arial", 12), bg="lightgreen", fg="black")
        label.pack(pady=10)
        
        array_entry = tk.Entry(input_frame, width=30)
        array_entry.pack(pady=10)
        
        submit_button = tk.Button(input_frame, text="Submit", font=("Arial", 12), command=lambda: submit_array(array_entry.get()))
        submit_button.pack(pady=10)

    elif selected_category == "Merge Sort":
        if input_frame:
            input_frame.destroy()
       # Create a new frame inside graphic_frame for input
        input_frame = tk.Frame(root, bg="lightgreen", width=300, height=200)
        input_frame.place(x=0, rely=0.25, width = 300)
        
        # Add a label and entry field for array input
        label = tk.Label(input_frame, text="Enter Array (comma-separated):", font=("Arial", 12), bg="lightgreen", fg="black")
        label.pack(pady=10)
        
        array_entry = tk.Entry(input_frame, width=30)
        array_entry.pack(pady=10)
        
        submit_button = tk.Button(input_frame, text="Submit", font=("Arial", 12), command=lambda: submit_array(array_entry.get()))
        submit_button.pack(pady=10)
    
    elif selected_category == "Quick Sort":
        if input_frame:
            input_frame.destroy()  # Destroy the previous input frame if it exists
    
        input_frame = tk.Frame(root, bg="lightgreen", width=300)  # Create a new input frame
        input_frame.place(x=0, rely=0.25, width=300, relheight=0.45)  # Place the frame at the appropriate position

    # Add a label and entry field for array input
        label = tk.Label(input_frame, text="Enter Array (comma-separated):", font=("Arial", 12), bg="lightgreen", fg="black")
        label.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.1)  # Adjust placement and size to be smaller

        array_entry = tk.Entry(input_frame, width=30)
        array_entry.place(relx=0.05, rely=0.15, relwidth=0.9, relheight=0.1)  # Adjust placement and size

    # Add label and entry for low value
        label2 = tk.Label(input_frame, text="Enter one integer for low", font=("Arial", 12), bg="lightgreen", fg="black")
        label2.place(relx=0.05, rely=0.30, relwidth=0.9, relheight=0.1)  # Adjust placement and size to fit

        low_entry = tk.Entry(input_frame, width=30)
        low_entry.place(relx=0.05, rely=0.40, relwidth=0.9, relheight=0.1)  # Adjust placement and size

    # Add label and entry for high value
        label3 = tk.Label(input_frame, text="Enter one integer for high", font=("Arial", 12), bg="lightgreen", fg="black")
        label3.place(relx=0.05, rely=0.55, relwidth=0.9, relheight=0.1)  # Adjust placement and size

        high_entry = tk.Entry(input_frame, width=30)
        high_entry.place(relx=0.05, rely=0.65, relwidth=0.9, relheight=0.1)  # Adjust placement and size

        quick_sort_button = tk.Button(input_frame, text="Submit", command=lambda: run_quick_sort(array_entry.get(), low_entry.get(), high_entry.get()))
        quick_sort_button.place(relx=0.3, rely=0.80, relwidth=0.4, relheight=0.15)  # Adjust button placement and size

    # Optional: Force a UI update to ensure the frame and its contents are shown immediately
        root.update()


    elif selected_category == "Radix Sort":
        if input_frame:
            input_frame.destroy()
        # Create a new frame inside graphic_frame for input
        input_frame = tk.Frame(root, bg="lightgreen", width=300, height=200)
        input_frame.place(x=0, rely=0.25, width = 300)
        
        # Add a label and entry field for array input
        label = tk.Label(input_frame, text="Enter Array (comma-separated):", font=("Arial", 12), bg="lightgreen", fg="black")
        label.pack(pady=10)
        
        array_entry = tk.Entry(input_frame, width=30)
        array_entry.pack(pady=10)
        
        submit_button = tk.Button(input_frame, text="Submit", font=("Arial", 12), command=lambda: submit_array(array_entry.get()))
        submit_button.pack(pady=10)


    elif selected_category == "Linear Search Algorithm":
        if input_frame:
            input_frame.destroy()

        input_frame = tk.Frame(root, bg="lightgreen", width=300)  # Create a new input frame
        input_frame.place(x=0, rely=0.25, width=300, relheight=0.30 )  # Place the frame at the appropriate position

    # Add a label and entry field for array input
        label = tk.Label(input_frame, text="Enter Array (comma-separated):", font=("Arial", 12), bg="lightgreen", fg="black")
        label.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.1)  # Adjust placement and size to be smaller

        array_entry = tk.Entry(input_frame, width=30)
        array_entry.place(relx=0.05, rely=0.15, relwidth=0.9, relheight=0.1)  # Adjust placement and size

    # Add label and entry for 
        label2 = tk.Label(input_frame, text="Enter one integer for target", font=("Arial", 12), bg="lightgreen", fg="black")
        label2.place(relx=0.05, rely=0.30, relwidth=0.9, relheight=0.1)  # Adjust placement and size to fit

        target_entry = tk.Entry(input_frame, width=30)
        target_entry.place(relx=0.05, rely=0.40, relwidth=0.9, relheight=0.1)  # Adjust placement and size

        submit_button = tk.Button(input_frame, text="Submit", font=("Arial", 12), command=lambda: submit_linear_search(array_entry.get(), target_entry.get()))
        submit_button.place(relx=0.3, rely=0.80, relwidth=0.4, relheight=0.15)


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




graphic_frame = tk.Frame(root, bg="gray")
graphic_frame.place(x=300, rely=0, relwidth=1.0, relheight=1)  # Starts at x=300, occupies remaining space

root.mainloop()
