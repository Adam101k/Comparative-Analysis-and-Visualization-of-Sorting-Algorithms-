import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from AlgorithmCollection import bubble_sort, merge_sort, quick_sort, radix_sort
import time

class SortingSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Algorithms & Linear Search Visualization v1.0")
        self.root.config(bg="skyblue")
        self.root.geometry("1200x800")
        self.root.minsize(800, 800)
        self.num = 0
        self.place_time = 0
        # Frame for the canvas and plot
        self.frame_plot = tk.Frame(self.root)
        self.frame_plot.grid(row=10, column=10, padx=50, pady=0)

        # Create Matplotlib figure and axis
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self.arr = np.random.randint(1, 100, 0)  # Start with 20 random numbers
        self.bars = self.ax.bar(range(len(self.arr)), self.arr, align='center', color='darkblue')  # Default color blue
        self.ax.set_title('Sorting Algorithms (20 Random Numbers)')

        # Canvas for embedding the Matplotlib figure in Tkinter
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame_plot)
        self.canvas.get_tk_widget().pack()

        # Fixed size selection_frame (300px wide, 70% of the window's height)
        self.selection_frame = tk.Frame(self.root, bg="lightcoral")
        self.selection_frame.place(x=0, y=0, width=300, relheight=0.5)  # Fixed width, relative height

        # Fixed size button_frame (300px wide, 30% of the window's height)
        self.button_frame = tk.Frame(self.root)
        self.button_frame.place(x=0, rely=0.5, width=300, relheight=0.5)  # Fixed width, relative height

        # Radio buttons for selecting sorting or searching
        self.selected_action = tk.StringVar(value="null")
        self.radio_frame = tk.Frame(self.root, bg="lightcoral")
        self.radio_frame.grid(row=2, column=5, padx=80, pady=10)
        tk.Label(self.radio_frame, text="Select an Algorithm:", bg="lightcoral").pack(anchor=tk.W)
        
        # Buttons for generating random numbers and starting the action
        actions = ['Bubble Sort', 'Merge Sort', 'Quick Sort', 'Radix Sort', 'Linear Search']
        for action in actions:
            tk.Radiobutton(self.radio_frame, text=action, variable=self.selected_action, value=action, bg="lightcoral").pack(anchor=tk.W)

        self.generate_label = tk.Label(self.button_frame, text="Generate Random Numbers", bg="red", font=("Arial", 16))
        self.generate_label.pack(side=tk.TOP, pady=5)

        self.generate_entry = tk.Entry(self.button_frame)
        self.generate_entry.pack(side=tk.TOP, pady=5)

        self.generate_button = tk.Button(self.button_frame, text="Generate Random Numbers", command=self.generate_random_numbers, bg="red", fg="black", font=("Arial", 16))
        self.generate_button.pack(side=tk.TOP, pady=5)

        self.start_button = tk.Button(self.button_frame, text="Start", command=self.start_action, bg="lightblue", fg="black", font=("Arial", 16), width=10)
        self.start_button.place(relx=0.25, rely=0.05, relwidth=0.5, relheight=0.25)
        self.start_button.pack(side=tk.TOP, pady=5)

        self.pause_button = tk.Button(self.button_frame, text="Pause", command=self.toggle_pause, bg="lightblue", fg="black", font=("Arial", 16), width=10)
        self.pause_button.place(relx=0.25, rely=0.375, relwidth=0.5, relheight=0.25)
        self.pause_button.pack(side=tk.TOP, pady=5)
        self.pause_button.config(state=tk.DISABLED)

        self.reset_button = tk.Button(self.button_frame, text="Reset", command=self.reset_action, bg="lightblue", fg="black", font=("Arial", 16), width=10)
        self.reset_button.place(relx=0.25, rely=0.70, relwidth=0.5, relheight=0.25,anchor = "center")
        self.reset_button.pack(side=tk.BOTTOM, pady=5)
        self.reset_button.config(state=tk.DISABLED)  
        #Text label for time
        self.time_var = tk.StringVar(value="Time: 0.000000 seconds")
        self.time_label = tk.Label(self.button_frame, textvariable=self.time_var, bg="lightcoral", font=("Arial", 16))
        self.time_label.pack(side=tk.TOP, pady=5)
    def update_bars(self, arr):
        """Update the heights of the bars in the bar chart."""
        for bar, val in zip(self.bars, arr):
            bar.set_height(val)
        self.canvas.draw()  # Redraw the canvas

    def generate_random_numbers(self):
        self.num = int(self.generate_entry.get())
        self.arr = np.random.randint(1, 100, self.num)
        self.bars = self.ax.bar(range(len(self.arr)), self.arr, align='center', color='darkblue')  # Default color blue
        self.update_bars(self.arr)
        print(f"Generated new array: {self.arr}")

    def start_action(self):
        """Run the selected sorting algorithm or search when the Start button is clicked."""
        self.place_time = 0  # Reset place_time
        self.is_paused = False
        self.sorting_running = True
        self.pause_button.config(state=tk.NORMAL, text="Pause")  # Enable pause button
        self.reset_button.config(state=tk.NORMAL)
        selected_action = self.selected_action.get()
        print(f"Starting {selected_action}...")

        if selected_action in ['Bubble Sort', 'Merge Sort', 'Quick Sort', 'Radix Sort']:
            self.run_sorting(selected_action)

    def reset_action(self):
        """Reset the visualization to its default state."""
    # Reset variables
        self.place_time = 0
        self.is_paused = False
        self.sorting_running = False
        self.pause_button.config(state=tk.DISABLED, text="Pause")  # Disable pause button

    # Generate a new random array or reset the original array
        self.ax.cla()
        self.arr = np.random.randint(1, 100, self.num)  # New array of 20 random numbers
        self.update_bars(self.arr)  # Reset the bars to the new array
    
    # Reset any other states as needed
    print("Visualization reset to default.")

    def toggle_pause(self):
        """Pause or resume the sorting."""
        self.is_paused = not self.is_paused
        if self.is_paused:
            self.pause_button.config(text="Resume")
        else:
            self.pause_button.config(text="Pause")
            self.root.after(50, self.sort_step)  # Resume sorting

    def run_sorting(self, action):
        """Run the selected sorting algorithm."""
        self.arr = list(self.arr)  # Convert to list to avoid NumPy issues

        # Assign the sorting method generator based on selection
        if action == 'Bubble Sort':
            self.generator = bubble_sort(self.arr)  # bubble_sort should return a generator
        elif action == 'Merge Sort':
            self.generator = merge_sort(self.arr)  # merge_sort should return a generator
        elif action == 'Quick Sort':
            self.generator = quick_sort(self.arr, 0, len(self.arr) - 1)  # Needs to be a generator
        elif action == 'Radix Sort':
            self.generator = radix_sort(self.arr)  # Needs to be a generator

        # Check if the generator was properly assigned
        if self.generator is not None:
            self.sort_step()  # Start the sorting steps
        else:
            print(f"No generator found for {action}")

    def sort_step(self):
        """Perform one step of the sorting and pause if requested."""
        if self.is_paused or not self.sorting_running:
            return  # If paused or sorting is stopped, don't proceed

        try:
            start_iteration_time = time.time()
            step = next(self.generator)
            end_iteration_time = time.time() - start_iteration_time
            self.place_time += end_iteration_time
            self.update_bars(step)
            self.root.after(50, self.sort_step)  # Schedule the next step after 50 ms
        except StopIteration:
            print(f"Sorting completed in {self.place_time:.8f} seconds.")
            self.time_var.set(f"Time: {self.place_time:.8f} seconds")
            self.pause_button.config(state=tk.DISABLED)  # Disable pause when sorting is done
            self.sorting_running = False


if __name__ == "__main__":
    root = tk.Tk()
    app = SortingSearchApp(root)
    root.mainloop()
