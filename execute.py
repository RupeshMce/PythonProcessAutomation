import pyautogui
import time
import pickle
import os
import argparse


parser = argparse.ArgumentParser(description="Automate the Task")
parser.add_argument('-e','--picklefileName',required=True, help='Name of the pickle file which need to execute')

args = parser.parse_args()
filename=args.picklefileName


size=pyautogui.size()
listerner_status=True
flag=1
postions=[0,0]
inital=time.time()
click=1
button_select=1

try:
    with open(filename, 'rb') as handle:
        actions_performed = pickle.load(handle)
except Exception as e:
    print("Oops File Doesn't Exist")
    exit()
else:
    print("Action Begins")



key_flag=[]
button_number=1


def mouse_click(click):
    pyautogui.click(x=click[1],y=click[2],button=click[3])
    
def mouse_scroll(click):
    pyautogui.scroll(click[-1])
    
def mouse_move(click):
    pyautogui.moveTo(click[1], click[2])

def double_click(click):
    pyautogui.click(x=click[1],y=click[2],button=click[3])
    pyautogui.doubleClick(x=click[1],y=click[2],button='left')
    pyautogui.doubleClick(x=click[1],y=click[2],button='left')

    
def key_release(click):
    pyautogui.keyUp(click[1])
    
def mouse_drag(click):
    pyautogui.click(x=(click[1]+click[3])/2,y=(click[2]+click[4])/2)
    pyautogui.click(click[1],click[2])
    pyautogui.dragTo(click[3], click[4], button='left') 
        
def hotkey():
    global key_flag
    for i in key_flag:
        if(i in ['ctrl','shift','alt','ctrl_r','shift_r','alt_r','tab']):
            pyautogui.keyDown(i)
        else:
            pyautogui.press(i)
    for i in key_flag:
        pyautogui.keyUp(i)
    return
        
def key_press(key):

    global key_flag
    if (key in ['ctrl','shift','alt','ctrl_r','shift_r','alt_r','tab']):
        key_flag.append(key)
        if('tab' in key_flag and len(key_flag)>0):
            hotkey()
            key_flag=[]
            
    elif (key=='enter' and len(key_flag)==0):
        pyautogui.press('enter')
        
    elif (len(key_flag)>0 and len(key)>0):
        try:
            key_flag.append(eval(key))
        except Exception as e:
            key_flag.append(key)
            
        hotkey()
        key_flag=[]
        
    elif(len(key_flag)==0 and len(key)>3):
        pyautogui.press(key)
        
    elif(len(key_flag)==0 and len(key)==1):
        pyautogui.press(key)
    
    elif(len(key_flag)==0 and len(key)==3):
        pyautogui.press(eval(key))

    else :
        pyautogui.press(key)
                
    return


    
for j,i in actions_performed.items():
    
    if(i[0]=="mouse_click"):
        mouse_click(i)
        time.sleep(j)
        
    if (i[0]=="mouse_scroll"):
        mouse_scroll(i)
        time.sleep(j)
    if (i[0]=="mouse_move"):
        mouse_move(i)       
        
    if(i[0]=="double_click"):
        double_click(i)
        time.sleep(j)
    
    if(i[0]=="key_press" and i[1]!='esc'):
        key_press(i[1])
        time.sleep(j)
        
    if(i[0]=="key_release"):
        key_release(i)
        time.sleep(j)
        
    if (i[0]=="drag"):
        mouse_drag(i)
        time.sleep(j)
        
    if(i[1]=='esc'):
        break
        
#print("Action Stops ...")
    
    
    