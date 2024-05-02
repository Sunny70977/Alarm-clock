import pygame
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0
    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")

    pygame.mixer.init()
    pygame.mixer.music.load("alarm.mp3")  # Make sure "alarm.mp3" is in the same directory as your script
    pygame.mixer.music.play()
    time.sleep(5)  # Wait for 5 seconds before exiting

try:
    minutes = int(input("How many minutes to wait: "))
    seconds = int(input("How many seconds to wait: "))
    total_seconds = minutes * 60 + seconds
    alarm(total_seconds)
except ValueError:
    print("Invalid input. Please enter a valid integer for minutes and seconds.")
