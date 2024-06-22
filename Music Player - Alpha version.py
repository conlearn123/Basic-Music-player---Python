import os
import time
import msvcrt
import glob
import vlc
import sys

def play_music(player):
    print("started")
    player.play()
    print("Music playing")

def wait_for_exit(player):
    print("Press q to exit program, press x to end song and press space to pause song")
    is_paused = False
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8').lower()
            if key == 'q':
                print("Program closed by keyboard input")
                os._exit(0)
                break
            elif key == "x":
                player.stop()
                print("Music stopped by keyboard input")
                break
            elif key == " ":
                if is_paused:
                    player.play()
                    print("Music unpaused")
                    is_paused = False
                else:
                    player.pause()
                    print("Music paused")
                    is_paused = True      
        time.sleep(0.1)

def main():
    while True:
        x = input("Do you want to play your own music file(o) or one in the current directory(c)? ")
        if x == 'o':
            song = input("File name here: ")
        elif x =='c':
            if getattr(sys, "frozen", False):
                current_dir = os.path.dirname(sys.executable)
            else:
                current_dir = os.path.dirname(os.path.abspath(__file__))
            
            mp3_files = glob.glob(os.path.join(current_dir, "*.mp3"))
            i = 1
            for file in mp3_files:
                print(f"{i}. {os.path.basename(file)}")
                i+=1
            index = int(input("Which number song do you want? ")) - 1
            song = mp3_files[index]
        elif x == "q":
            print("Program closed by keyboard input")
            os._exit(0)
        else:
            print("Unknown input")
            continue

        player = vlc.MediaPlayer(song)

        play_music(player)
    
        wait_for_exit(player)

main()