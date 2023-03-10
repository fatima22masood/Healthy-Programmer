from pygame import mixer
import threading
import datetime
import time
def get_time():
    return datetime.datetime.now()
def water_log(text):
    with open("water.txt", "a") as f:
        a= f.write(f"{get_time()}-{text}")
        return a
def eye_log(text):
    with open ("eye.txt", "a") as f:
        a= f.write(f"{get_time()}- {text}")
        return a
def exercise_log(text):
    with open("exercise.txt","a") as f:
        a= f.write(f"{get_time()}-{text}")
        return a
def read_water_file():
    with open("water.txt", "r") as f:
        a=f.read()
        return print(a)
def read_eye_file():
    with open("eye.txt", "r") as f:
        a= f.read()
        return print(a)
def read_exercise_file():
    with open("exercise.txt","r")as f:
        a=f.read()
        return print(a)
def drink_water():
    while True:
        print('Water drinking counting is running ...')
        time.sleep(2057)

        # Starting the mixer
        mixer.init()

        # Loading the song
        mixer.music.load("pani.mp3")

        # Setting the volume
        mixer.music.set_volume(0.5)

        # # Start playing the song
        mixer.music.play()

        # Start playing the song
        # mixer.music.play()
        print("enter drank to stop")

        user_input = input()
        query = user_input

        if query == 'drank':
            # Stop the mixer
            mixer.music.stop()
            water_log(query)
            print('Thank you. Your water drinking log is updated.\n'
                  '-----------------------\n')
        continue

def eye_exercise():
    while True:
        print("eye exercise is counting")
        time.sleep(1800)
        mixer.init()
        mixer.music.load("exercise.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()
        print("enetr eydone to stop")
        input_by_user = input()
        query=input_by_user
        if query=='eydone':
            mixer.music.stop()
            eye_log(query)
            print('thank you, your eye log is updated\n')
        continue


def body_exercise():
    while True:
        print("body exercise is counting")
        time.sleep(2700)
        mixer.init()
        mixer.music.load("body.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()
        print("enter Exdone to stop")
        input_by_user = input()
        query = input_by_user
        if query == 'Exdone':
            mixer.music.stop()
            exercise_log(query)
            print('thank you, your exercise log is updated\n')
        continue
if __name__ == '__main__':
    print("press 1 if you want to see record and press 2 if you want to run function")
    choice=input()
    if choice=='1':
        read_choice=input("1 for water\n"
                          "2 for eye\n"
                          "3 for body\n")
        if read_choice=='1':
            read_water_file()
        elif read_choice=='2':
            read_eye_file()
        elif read_choice=='3':
            read_exercise_file()
        else:
            print("invalid coice")
    elif choice=='2':
        t1= threading.Thread(target=drink_water)
        t2= threading.Thread(target=eye_exercise)
        t3= threading.Thread(target=body_exercise)
        #starting threads
        t1.start()
        t2.start()
        t3.start()
        #joining threads
        t1.join()
        t2.join()
        t3.join()

