Shutdown Timer by Spaghett21

A simple Python application built with tkinter to shut down your Windows PC immediately or after a specified delay.
Features

    Instant Shutdown: Shut down your PC immediately with a single click.

    Timer Shutdown: Set a shutdown timer in minutes.

    Cancel Shutdown: Cancel any scheduled shutdown.

Requirements

    Python 3.x

    tkinter (usually included with Python)

    Windows OS (uses shutdown command)

How to Use

    Clone or download the repository.

    Run the script:
    bash
    Copy

    python shutdown_timer.py

    Use the GUI to:

        Shut down your PC immediately.

        Set a shutdown timer (enter minutes in the input box).

        Cancel a scheduled shutdown.

![grafik](https://github.com/user-attachments/assets/c76445e8-515d-4872-9210-b9f336d79273)


Code Overview

    Instant Shutdown: Uses os.system("shutdown /s /t 0") to shut down the PC immediately.

    Timer Shutdown: Converts minutes to seconds and schedules a shutdown using os.system(f"shutdown /s /t {seconds}").

    Cancel Shutdown: Cancels the scheduled shutdown with os.system("shutdown /a").

Notes

    This script is designed for Windows only.

    Ensure you save all work before using the shutdown features.

License

This project is open-source and available under the MIT License.

Feel free to customize this README.md further to suit your needs! Let me know if you need help with anything else. 😊
