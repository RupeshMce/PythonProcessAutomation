import os
from pynput import keyboard,mouse
import pynput
from threading import *
import pyautogui
from collections import OrderedDict
import time 
import pickle
import argparse

parser = argparse.ArgumentParser(description="Automate the Task")
parser.add_argument('-n','--picklefileName',required=True, help='Name of the pickle file where cmds are saved')

args = parser.parse_args()
filename=args.picklefileName

if (".pickle" in filename):
    print("Actions are Stored in FileName is {}".format(filename))
else:
    filename=filename+".pickle"
    print("The Output is an Pickle File")
    print("Actions are Stored in  FileName is {}".format(filename))



# Golbal Variable Declartion
size=pyautogui.size()
listerner_status=True
flag=1
postions=[0,0]
events_list=OrderedDict()
inital=time.time()


class keyboard_event(Thread):
    def run(self):
        def on_press(key):
            global events_list,listerner_status
            # print(key)
            events_list[time.time()]=['key_press',key]
            if (key==keyboard.Key.esc):
                listerner_status=False
                pyautogui.click()
                return listerner_status
                
        def on_release(key):
            # print(key)
            global events_list
            events_list[time.time()]=['key_release',key]
                    
        with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
            listener.join()
            print("Keyboard Recording Ends")

            
class mouse_click(Thread):

    def run(self):
        def on_click(x, y, button, pressed):
            global events_list,listerner_status,postions
            print(x, y, button.name,pressed)
            if listerner_status:
                if pressed :
                    if(postions==[x,y]):
                        events_list[time.time()]=['double_click',x,y,button.name]
                        postions=[0,0]
                    else:
                        postions=[x,y]
                elif (not pressed and postions==[x,y]):
                    events_list[time.time()]=['mouse_click',x,y,button.name]
                    postions=[0,0]


                else:
                    events_list[time.time()]=["drag",postions[0],postions[1],x,y]
                    postions=[0,0]

                  
            else:
                return listerner_status 
                
                
        
        def on_move(x, y):
            if listerner_status:
                events_list[time.time()]=['mouse_move',x,y]
            else:
                return listerner_status 
        
        def on_scroll(x, y, dx, dy):  
            if listerner_status:
                events_list[time.time()]=['mouse_scroll',x,y,dx,dy]
            else:
                return listerner_status 
            
        with mouse.Listener(on_click=on_click,on_scroll=on_scroll,on_move=on_move) as listener:
            listener.join()
            print("Mouse Recording Ends")

time.sleep(0.5)
key_actions=keyboard_event()
time.sleep(0.5)
click_actions=mouse_click()
key_actions.start()
time.sleep(0.5)
print("Key log Starts")
click_actions.start()
time.sleep(1)
print("Mouse Action Starts")
time.sleep(1)
print("Recording Starts ...")

key_actions.join()
click_actions.join()
time.sleep(0.5)
print("Record Stops ...")
    
    


key=list(events_list.keys())
key=[0]+[key[x+1]-key[x] for x in range(0,len(key)-1)]
actions_performed=OrderedDict()
value=list(events_list.values())

for index in range(len(key)):
    actions_performed[key[index]]=value[index]



for key,value in actions_performed.items():
    if (value[0]=="key_press" or value[0]=="key_release"):
        # print(value[1])
        if(len(str(value[1])))>3:
            value[1]=str(value[1])[4:]
            if value[1]=="56>":
                value[1]="tab"
            # print(value[1])
        else:
            value[1]=str(value[1])


with open(filename, 'wb') as handle:
    pickle.dump(actions_performed, handle, protocol=pickle.HIGHEST_PROTOCOL)
