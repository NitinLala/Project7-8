import tkinter as tk

def on_button_click(button_number):
    if button_number == 1:
        show_display_screen()
    elif button_number == 2:
        show_profile_screen()
    else:
        show_settings_screen()

def show_main_screen():
    main_frame.pack()
    display_frame.pack_forget()
    profile_frame.pack_forget()
    settings_frame.pack_forget()

def show_display_screen():
    main_frame.pack_forget()
    display_frame.pack()
    profile_frame.pack_forget()
    settings_frame.pack_forget()

def show_profile_screen():
    main_frame.pack_forget()
    display_frame.pack_forget()
    profile_frame.pack()
    settings_frame.pack_forget()

def show_settings_screen():
    main_frame.pack_forget()
    display_frame.pack_forget()
    profile_frame.pack_forget()
    settings_frame.pack()

def go_back():
    show_main_screen()

# Create the main window
root = tk.Tk()
root.title("LightUpCane")
root.configure(bg="white")  # Set background color to white

# Calculate the screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the position for the window to be centered
window_width = 300  # Adjust this value as needed
window_height = 200  # Adjust this value as needed
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Set the geometry of the window to be centered
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create main frame
main_frame = tk.Frame(root, bg="white")

# Create display frame
display_frame = tk.Frame(root, bg="white")
display_label = tk.Label(display_frame, text="Display Screen", bg="white", font=("Arial", 20))
display_label.pack(pady=10)

# Create profile frame
profile_frame = tk.Frame(root, bg="white")
profile_label = tk.Label(profile_frame, text="Profile Screen", bg="white", font=("Arial", 20))
profile_label.pack(pady=10)

# Create settings frame
settings_frame = tk.Frame(root, bg="white")
settings_label = tk.Label(settings_frame, text="Settings Screen", bg="white", font=("Arial", 20))
settings_label.pack(pady=10)

# Create a "Go Back" button in profile frame
go_back_button = tk.Button(display_frame, text="Go Back", command=go_back, bg="black", fg="white", width=50, height=5)
go_back_button.pack(pady=5)

go_back_button = tk.Button(profile_frame, text="Go Back", command=go_back, bg="black", fg="white", width=50, height=5)
go_back_button.pack(pady=5)

go_back_button = tk.Button(settings_frame, text="Go Back", command=go_back, bg="black", fg="white", width=50, height=5)
go_back_button.pack(pady=5)

# Create three bigger buttons with black background in main frame
button1 = tk.Button(main_frame, text="Display", command=lambda: on_button_click(1), bg="black", fg="white", width=50, height=5)  # Set button background to black and text color to white
button1.pack(pady=5)

button2 = tk.Button(main_frame, text="Profile", command=lambda: on_button_click(2), bg="black", fg="white", width=50, height=5)  # Set button background to black and text color to white
button2.pack(pady=5)

button3 = tk.Button(main_frame, text="Settings", command=lambda: on_button_click(3), bg="black", fg="white", width=50, height=5)  # Set button background to black and text color to white
button3.pack(pady=5)

# Show the main screen initially
show_main_screen()

# Run the GUI
root.mainloop()
