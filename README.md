# Full Charge Reminder

A Python application that provides a notification when your laptop's battery is fully charged. This app uses `psutil` to monitor battery status and `winsound` to play a sound notification when the battery reaches 100% while plugged in.

## Features

- Monitors battery percentage.
- Checks if the laptop is plugged in.
- Displays time left until the battery is fully charged.
- Plays a sound notification when the battery reaches 100% and is still plugged in.
- Provides a graphical user interface using `tkinter`.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/full_charge_reminder.git
Navigate to the project directory:

bash
Copy code
cd full_charge_reminder
Install the required Python packages:

bash
Copy code
pip install psutil
(Optional) If you don't have winsound, it is included with Python on Windows, so no additional installation is required.

Configuration
Place your sound file in the battery-charge-reminder directory.

Update the SOUND_FILE path in full_charge_reminder.py to point to your sound file:

python
Copy code
SOUND_FILE = r"battery-charge-reminder\charging-sound.wav"
or use forward slashes:

python
Copy code
SOUND_FILE = "battery-charge-reminder/charging-sound.wav"
Usage
Run the application using Python:

bash
Copy code
python full_charge_reminder.py
The application will start and check the battery status every minute. It will display a warning and play a sound when the battery is fully charged and plugged in.

Contributing
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
psutil - A cross-platform library for retrieving battery information.
tkinter - The standard Python interface to the Tk GUI toolkit.
winsound - A module for playing sounds on Windows.
css
Copy code

Feel free to adjust the sections or content based on your needs!