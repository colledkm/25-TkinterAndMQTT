"""
Using a fake robot as the receiver of messages.
"""

# DONE: 1. In mqtt_remote_method_calls, set LEGO_NUMBER at line 131
# to YOUR robot's number.

# TODO: 2. Copy your Tkinter/ttk ROBOT gui code from the previous session (m6).
# Then modify it so that pressing a button sends a message to a teammate
# of the form:
#   (for Forward)
#        ["forward", X, y]
#   where X and Y are from the entry box.
#
# Implement and test.

import tkinter
from tkinter import ttk
import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
import time

class DelegateThatReceives(object):
    def Forward(self,left_speed,right_speed):
        print("Forward",left_speed,right_speed)

    def Left(self,left_speed,right_speed):
        print("Left",left_speed,right_speed)

    def Right(self,left_speed,right_speed):
        print("Right",left_speed,right_speed)

    def Stop(self,left_speed,right_speed):
        print("Stop",left_speed,right_speed)


    def say_it(self, message):
        print("Message received!", message)

def main():
    name1 = input("Enter one name (subscriber): ")
    name2 = input("Enter another name (publisher): ")
    my_delegate = DelegateThatReceives()
    mqtt_client = com.MqttClient(my_delegate)
    mqtt_client.connect(name1, name2)
    time.sleep(1)  # Time to allow the MQTT setup.
    print()

    def send(name,mqtt_client,left_speed,right_speed):
        mqtt_client.send_message(str(name), [left_speed,right_speed])

    """ Constructs a GUI that will be used MUCH later to control EV3. """
    # -------------------------------------------------------------------------
    # DONE: 2. Follow along with the video to make a remote control GUI
    # For every grid() method call you will add a row and a column argument
    # -------------------------------------------------------------------------

    root = tkinter.Tk()
    root.title("MQTT Remote")

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()  # only grid call that does NOT need a row and column

    left_speed_label = ttk.Label(main_frame, text="Left")
    left_speed_label.grid(row=0,column=0)
    left_speed_entry = ttk.Entry(main_frame, width=8)
    left_speed_entry.insert(0, "600")
    left_speed_entry.grid(row=1,column=0)

    right_speed_label = ttk.Label(main_frame, text="Right")
    right_speed_label.grid(row=0,column=2)
    right_speed_entry = ttk.Entry(main_frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "600")
    right_speed_entry.grid(row=1,column=2)

    forward_button = ttk.Button(main_frame, text="Forward")
    forward_button.grid(row=2,column=1)
    forward_button['command'] = lambda: send('Forward',mqtt_client,left_speed_entry,right_speed_entry)
    root.bind('<Up>', lambda event: send("Forward key"))

    left_button = ttk.Button(main_frame, text="Left")
    left_button.grid(row=3,column=0)
    left_button['command'] = lambda: print("Left",mqtt_client,left_speed_entry,0)
    root.bind('<Left>', lambda event: send("Left key"))

    stop_button = ttk.Button(main_frame, text="Stop")
    stop_button.grid(row=3,column=1)
    stop_button['command'] = lambda: print("Stop",mqtt_client,0,0)
    root.bind('<space>', lambda event: print("Stop key"))

    right_button = ttk.Button(main_frame, text="Right")
    right_button.grid(row=3,column=2)
    right_button['command'] = lambda: print("Right",mqtt_client,0,right_speed_entry)
    root.bind('<Right>', lambda event: print("Right key"))

    back_button = ttk.Button(main_frame, text="Back")
    back_button.grid(row=4,column=1)
    back_button['command'] = lambda: print("Back button")
    root.bind('<Down>', lambda event: print("Back key"))

    up_button = ttk.Button(main_frame, text="Up")
    up_button.grid(row=5,column=0)
    up_button['command'] = lambda: print("Up button")
    root.bind('<u>', lambda event: print("Up key"))

    down_button = ttk.Button(main_frame, text="Down")
    down_button.grid(row=6,column=0)
    down_button['command'] = lambda: print("Down button")
    root.bind('<j>', lambda event: print("Down key"))

    # Buttons for quit and exit
    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=5,column=2)
    q_button['command'] = lambda: print("Quit button")

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid(row=6,column=2)
    e_button['command'] = lambda: exit()

    root.mainloop()


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()