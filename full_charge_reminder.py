import psutil
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import winsound

# Path to the sound file
SOUND_FILE = r"battery-charge-reminder\charging-sound.wav"  # Or use forward slashes

def convert_time(seconds):
    if seconds == psutil.POWER_TIME_UNLIMITED or seconds == psutil.POWER_TIME_UNKNOWN:
        return "N/A"
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def play_sound():
    winsound.PlaySound(SOUND_FILE, winsound.SND_FILENAME)

def check_battery_status():
    battery = psutil.sensors_battery()
    if battery.percent == 100 and battery.power_plugged:
        messagebox.showwarning("Battery Full", "Unplug the charging cable!")
        play_sound()
    root.after(60000, check_battery_status)

def update_battery_info():
    battery = psutil.sensors_battery()
    percent_label.config(text=f"Battery Percentage: {battery.percent}%")
    plugged_label.config(text=f"Power Plugged: {'Yes' if battery.power_plugged else 'No'}")
    time_left_label.config(text=f"Time Left: {convert_time(battery.secsleft)}" if not battery.power_plugged else "Charging...")
    root.after(1000, update_battery_info)

root = tk.Tk()
root.title("Battery Charge Reminder by Yaffawijaya")
root.geometry("400x200")

style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("Header.TLabel", font=("Helvetica", 16, "bold"))
style.configure("Footer.TLabel", font=("Helvetica", 10, "italic"))

header_label = ttk.Label(root, text="Battery Charge Reminder", style="Header.TLabel")
header_label.pack(pady=10)

percent_label = ttk.Label(root, text="", style="TLabel")
percent_label.pack(pady=5)

plugged_label = ttk.Label(root, text="", style="TLabel")
plugged_label.pack(pady=5)

time_left_label = ttk.Label(root, text="", style="TLabel")
time_left_label.pack(pady=5)

footer_label = ttk.Label(root, text="Developed by Yaffawijaya with love", style="Footer.TLabel")
footer_label.pack(side="bottom", pady=10)

check_battery_status()
update_battery_info()

root.mainloop()
