import tkinter as tk
import random

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
    display_frame.pack(expand=True, fill="both")  
    profile_frame.pack_forget()
    settings_frame.pack_forget()
    update_display_values()

def update_display_values():
    battery_status_var.set(random.randint(0, 100))
    light_intensity_var.set(random.randint(0, 100))
    buzzer_intensity_var.set(random.randint(0, 100))
    buzzer_hz_var.set(random.randint(0, 100))
    haptic_intensity_var.set(random.randint(0, 100))
    light_on_off_var.set(random.choice(["On", "Off"]))

def show_profile_screen():
    main_frame.pack_forget()
    display_frame.pack_forget()
    profile_frame.pack()
    settings_frame.pack_forget()
    # Display profile information
    display_profile_info()

def display_profile_info():
    entry_name.delete(0, tk.END)
    entry_name.insert(0, "Hannah")
    entry_email.delete(0, tk.END)
    entry_email.insert(0, "Hannah@gmail.com")
    entry_phone.delete(0, tk.END)
    entry_phone.insert(0, "06982883748")

def show_edit_screen():
    profile_frame.pack_forget()
    edit_frame.pack()
    edit_name_entry.insert(0, entry_name.get())
    edit_email_entry.insert(0, entry_email.get())
    edit_phone_entry.insert(0, entry_phone.get())

def save_profile_changes():
    new_name = edit_name_entry.get()
    new_email = edit_email_entry.get()
    new_phone = edit_phone_entry.get()

    # Update profile information
    entry_name.delete(0, tk.END)
    entry_name.insert(0, new_name)
    entry_email.delete(0, tk.END)
    entry_email.insert(0, new_email)
    entry_phone.delete(0, tk.END)
    entry_phone.insert(0, new_phone)

    # Hide the edit frame and show the profile frame
    edit_frame.pack_forget()
    profile_frame.pack()

def show_settings_screen():
    main_frame.pack_forget()
    display_frame.pack_forget()
    profile_frame.pack_forget()
    settings_frame.pack()
    show_settings_options()

def show_settings_options():
    for button in settings_buttons:
        button.pack(pady=5)

def on_settings_button_click(part):
    if part == "Button":
        show_button_settings()
    elif part == "Battery":
        show_battery_settings()
    elif part == "Light":
        show_light_settings()
    elif part == "Properties":
        show_properties_settings()

def show_button_settings():
    hide_all_settings_frames()
    button_settings_frame.pack()

def show_battery_settings():
    hide_all_settings_frames()
    battery_settings_frame.pack()

def show_light_settings():
    hide_all_settings_frames()
    light_settings_frame.pack()

def show_properties_settings():
    hide_all_settings_frames()
    properties_settings_frame.pack()

def hide_all_settings_frames():
    for frame in settings_frames:
        frame.pack_forget()

def go_back():
    show_main_screen()

def close_program():
    root.destroy()

def edit_profile():
    show_edit_screen()

# Create the main window
root = tk.Tk()
root.title("LightUpCane")
root.configure(bg="white")  # Set background color to white

# Set the window to full screen
root.attributes('-fullscreen', True)

# Create toolbar frame
toolbar_frame = tk.Frame(root, bg="black")  # Set background color to black
toolbar_frame.pack(side="top", fill="x")

# Add project name label to a frame with black background
project_name_frame = tk.Frame(toolbar_frame, bg="black")
project_name_frame.pack(padx=10, pady=5)
project_name_label = tk.Label(project_name_frame, text="Light-up Cane", bg="black", fg="white", font=("Arial", 24))  # Set text color to white
project_name_label.pack()

# Create main frame
main_frame = tk.Frame(root, bg="white")

# Create display frame
display_frame = tk.Frame(root, bg="white")
display_label = tk.Label(display_frame, text="Display Screen", bg="white", font=("Arial", 30))  # Adjust font size for display
display_label.pack(pady=(50, 10))  # Adjust padding for centering

battery_status_var = tk.StringVar()
light_intensity_var = tk.StringVar()
buzzer_intensity_var = tk.StringVar()
buzzer_hz_var = tk.StringVar()
haptic_intensity_var = tk.StringVar()
light_on_off_var = tk.StringVar()

battery_status_label = tk.Label(display_frame, text="Battery Status: ", bg="white", font=("Arial", 18))  # Adjust font size for display values
battery_status_label.pack()
battery_status_value = tk.Label(display_frame, textvariable=battery_status_var, bg="white", font=("Arial", 18))  # Adjust font size for display values
battery_status_value.pack()

light_intensity_label = tk.Label(display_frame, text="Light Intensity: ", bg="white", font=("Arial", 18))  # Adjust font size for display values
light_intensity_label.pack()
light_intensity_value = tk.Label(display_frame, textvariable=light_intensity_var, bg="white", font=("Arial", 18))  # Adjust font size for display values
light_intensity_value.pack()

buzzer_intensity_label = tk.Label(display_frame, text="Buzzer Intensity: ", bg="white", font=("Arial", 18))  # Adjust font size for display values
buzzer_intensity_label.pack()
buzzer_intensity_value = tk.Label(display_frame, textvariable=buzzer_intensity_var, bg="white", font=("Arial", 18))  # Adjust font size for display values
buzzer_intensity_value.pack()

buzzer_hz_label = tk.Label(display_frame, text="Buzzer Hz: ", bg="white", font=("Arial", 18))  # Adjust font size for display values
buzzer_hz_label.pack()
buzzer_hz_value = tk.Label(display_frame, textvariable=buzzer_hz_var, bg="white", font=("Arial", 18))  # Adjust font size for display values
buzzer_hz_value.pack()

haptic_intensity_label = tk.Label(display_frame, text="Haptic Intensity: ", bg="white", font=("Arial", 18))  # Adjust font size for display values
haptic_intensity_label.pack()
haptic_intensity_value = tk.Label(display_frame, textvariable=haptic_intensity_var, bg="white", font=("Arial", 18))  # Adjust font size for display values
haptic_intensity_value.pack()

light_on_off_label = tk.Label(display_frame, text="Light On/Off: ", bg="white", font=("Arial", 18))  # Adjust font size for display values
light_on_off_label.pack()
light_on_off_value = tk.Label(display_frame, textvariable=light_on_off_var, bg="white", font=("Arial", 18))  # Adjust font size for display values
light_on_off_value.pack()

# Create a "Go Back" button in display frame
go_back_button_display = tk.Button(display_frame, text="Go Back", command=go_back, bg="black", fg="white", width=50, height=5, font=("Arial", 18))  # Adjust font size for button
go_back_button_display.pack(pady=20)  # Adjust top padding

# Pack the display frame
display_frame.pack(expand=True, fill="both")

# Create profile frame
profile_frame = tk.Frame(root, bg="white")
profile_label = tk.Label(profile_frame, text="Profile Screen", bg="white", font=("Arial", 20))
profile_label.pack(pady=10)

# Profile fields
label_name = tk.Label(profile_frame, text="Name:", bg="white")
label_name.pack(pady=5)
entry_name = tk.Entry(profile_frame)
entry_name.pack(pady=5)

label_email = tk.Label(profile_frame, text="Email:", bg="white")
label_email.pack(pady=5)
entry_email = tk.Entry(profile_frame)
entry_email.pack(pady=5)

label_phone = tk.Label(profile_frame, text="Phone:", bg="white")
label_phone.pack(pady=5)
entry_phone = tk.Entry(profile_frame)
entry_phone.pack(pady=5)

# Edit profile button
edit_button = tk.Button(profile_frame, text="Edit", command=edit_profile, bg="black", fg="white")
edit_button.pack(pady=10)

# Initialize initial values of profile fields
initial_name = ""
initial_email = ""
initial_phone = ""

# Create edit frame
edit_frame = tk.Frame(root, bg="white")

edit_name_label = tk.Label(edit_frame, text="Name:", bg="white")
edit_name_label.pack(pady=5)
edit_name_entry = tk.Entry(edit_frame)
edit_name_entry.pack(pady=5)

edit_email_label = tk.Label(edit_frame, text="Email:", bg="white")
edit_email_label.pack(pady=5)
edit_email_entry = tk.Entry(edit_frame)
edit_email_entry.pack(pady=5)

edit_phone_label = tk.Label(edit_frame, text="Phone:", bg="white")
edit_phone_label.pack(pady=5)
edit_phone_entry = tk.Entry(edit_frame)
edit_phone_entry.pack(pady=5)

save_changes_button = tk.Button(edit_frame, text="Save Changes", command=save_profile_changes, bg="black", fg="white")
save_changes_button.pack(pady=10)

# Create settings frame
settings_frame = tk.Frame(root, bg="white")
settings_label = tk.Label(settings_frame, text="Settings Screen", bg="white", font=("Arial", 20))
settings_label.pack(pady=10)

# Settings frames
button_settings_frame = tk.Frame(root, bg="white")
battery_settings_frame = tk.Frame(root, bg="white")
light_settings_frame = tk.Frame(root, bg="white")
properties_settings_frame = tk.Frame(root, bg="white")

settings_frames = [button_settings_frame, battery_settings_frame, light_settings_frame, properties_settings_frame]

# Create settings buttons
settings_buttons = []
for part in ["Button", "Battery", "Light", "Properties"]:
    button = tk.Button(settings_frame, text=part, command=lambda part=part: on_settings_button_click(part), bg="black", fg="white", width=50, height=5)
    settings_buttons.append(button)

# Button settings
button_hold_time_var = tk.StringVar()
button_hold_time_label = tk.Label(button_settings_frame, text="Hold Time: ", bg="white")
button_hold_time_label.pack()
button_hold_time_entry = tk.Entry(button_settings_frame, textvariable=button_hold_time_var)
button_hold_time_entry.pack()

# Battery settings
battery_life_var = tk.StringVar()
battery_life_label = tk.Label(battery_settings_frame, text="Battery Life (%): ", bg="white")
battery_life_label.pack()
battery_life_entry = tk.Entry(battery_settings_frame, textvariable=battery_life_var)
battery_life_entry.pack()

# Light settings
light_on_off_options = ["On", "Off"]
light_on_off_var = tk.StringVar()
light_on_off_label = tk.Label(light_settings_frame, text="Light On/Off: ", bg="white")
light_on_off_label.pack()
light_on_off_option_menu = tk.OptionMenu(light_settings_frame, light_on_off_var, *light_on_off_options)
light_on_off_option_menu.pack()

# Properties settings
buzzer_intensity_var = tk.StringVar()
buzzer_intensity_label = tk.Label(properties_settings_frame, text="Buzzer Intensity: ", bg="white")
buzzer_intensity_label.pack()
buzzer_intensity_entry = tk.Entry(properties_settings_frame, textvariable=buzzer_intensity_var)
buzzer_intensity_entry.pack()

haptic_intensity_var = tk.StringVar()
haptic_intensity_label = tk.Label(properties_settings_frame, text="Haptic Intensity: ", bg="white")
haptic_intensity_label.pack()
haptic_intensity_entry = tk.Entry(properties_settings_frame, textvariable=haptic_intensity_var)
haptic_intensity_entry.pack()

# Create a "Go Back" button in profile frame
go_back_button_profile = tk.Button(profile_frame, text="Go Back", command=go_back, bg="black", fg="white", width=50, height=5, font=("Arial", 18))  # Adjust font size for button
go_back_button_profile.pack(pady=20)  # Adjust top padding

# Create a "Go Back" button in settings frame
go_back_button_settings = tk.Button(settings_frame, text="Go Back", command=go_back, bg="black", fg="white", width=50, height=5, font=("Arial", 18))  # Adjust font size for button
go_back_button_settings.pack(pady=20)  # Adjust top padding

# Create three bigger buttons with black background in main frame
button2 = tk.Button(main_frame, text="Profile", command=lambda: on_button_click(2), bg="black", fg="white", width=50, height=5, font=("Arial", 18))  # Set button background to black and text color to white
button2.pack(pady=5)

button1 = tk.Button(main_frame, text="Display", command=lambda: on_button_click(1), bg="black", fg="white", width=50, height=5, font=("Arial", 18))  # Set button background to black and text color to white
button1.pack(pady=5)

button3 = tk.Button(main_frame, text="Settings", command=lambda: on_button_click(3), bg="black", fg="white", width=50, height=5, font=("Arial", 18))  # Set button background to black and text color to white
button3.pack(pady=5)

# Create a "Close" button in toolbar frame
close_button = tk.Button(toolbar_frame, text="Close", command=close_program, bg="black", fg="white")
close_button.pack(side="right", padx=10, pady=5)

# Show the main screen initially
show_main_screen()

# Run the GUI
root.mainloop()