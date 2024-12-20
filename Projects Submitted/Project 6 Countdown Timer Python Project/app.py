# -*- coding: utf-8 -*-
"""Project 6: Countdown Timer Python Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BdRkkptgTApNlYLmvqZdsFWih9lV1xn9

# Project 6: Countdown Timer Python Project
In this project, you will build a countdown timer that takes a specified amount of time (in seconds) as input and counts down to zero, displaying the remaining time at regular intervals.
"""

import time

def countdown_timer(seconds):
    """
    Countdown Timer

    This function takes a specified amount of time (in seconds) as input and counts down to zero.
    It displays the remaining time at regular intervals.

    This project helps beginners learn:
    - How to use the time module in Python.
    - How to work with while loops.
    - How to handle time-based operations.
    """
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02}:{secs:02}'
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

if __name__ == "__main__":
    # Input time in seconds
    t = input("Enter the time in seconds: ")

    # Check if the input is a valid number
    if t.isdigit():
        countdown_timer(int(t))
    else:
        print("Please enter a valid number.")


