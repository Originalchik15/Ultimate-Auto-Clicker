import tkinter as tk
import random as rng
import pyautogui as pg
import keyboard as kb
import time
import mouse 
import csv

def autoclick_mouse(e): # mouse autoclicking
    while True:
        if kb.is_pressed(stop_button_mouse):
            break
        mouse.click(mouse_type)
        time.sleep(speed_click)

def autoclick_key(e): # key autoclicking
    while True:
        if kb.is_pressed(stop_button_key):
            break
        kb.send(key_click)
        time.sleep(speed_click)
        

k = []
with open("settings.csv", newline='') as csvfile:
    saved = csv.reader(csvfile,delimiter=',')
    for row in saved:
        for key in row:
            k.append(key)

#----------DEFAULT_SETTINGS----------
start_button_mouse = k[0]
stop_button_mouse = k[1]
start_button_key = k[2]
stop_button_key = k[3]
key_click = k[4]
speed_click = k[5]
mouse_type = k[6]

print(start_button_mouse)
def main_menu():
    #----------AUTOCLICKER----------
    def autoclicker_key_mouse():
        #сделать проверку на однотипность и количество букв
        
        def change_button_start():
            global start_button_mouse
            start_button_mouse = entry_for_change.get()
            label_start_stop.config(text = f'Press {start_button_mouse} to start / {stop_button_mouse} to stop', background='lightgrey')

        def change_button_stop():
            global stop_button_mouse
            stop_button_mouse = entry_for_change.get()
            label_start_stop.config(text = f'Press {start_button_mouse} to start / {stop_button_mouse} to stop', background='lightgrey')  

        def change_speed_click():
            global speed_click
            speed_click = int(entry_for_speed_ms.get())//100

        def change_key_button_start():
            global start_button_key
            start_button_key = entry_for_change.get()
            label_key_start_stop.config(text = f'Press {start_button_key} to start / {stop_button_key} to stop', background='lightgrey')
            
        def change_key_button_stop():
            global stop_button_key
            stop_button_key = entry_for_change.get()
            label_key_start_stop.config(text = f'Press {start_button_key} to start / {stop_button_key} to stop', background='lightgrey')
        
        def to_menu():
            root.destroy()
            main_menu()
            
        main_m.destroy()
        root = tk.Tk()
        root.title("UAClicker - Clicker")
        root.geometry(f"400x250+{int(root.winfo_screenwidth()//2)}+{int((root.winfo_screenheight()//2)-150)}")
        root.resizable(False,False)


        kb.on_press_key(start_button_mouse, autoclick_mouse)
        kb.on_press_key(start_button_key,autoclick_key)


        #----------LABEL----------
        label_start_stop = tk.Label(text = f'Press {start_button_mouse} to start / {stop_button_mouse} to stop', background='lightgrey')
        label_change_btn = tk.Label(text='Change button mouse',background='lightgrey')
        label_speed_click = tk.Label(text='Speed (ms)', background='lightgrey')
        label_key_start_stop = tk.Label(text = f'Press {start_button_key} to start / {stop_button_key} to stop', background='lightgrey')
        label_key_change_btn = tk.Label(text='Change button key',background='lightgrey')
        label_new_button1 = tk.Label(text="New button here --->",font=("Arial", 8))
        label_new_button2 = tk.Label(text="<--- New button here",font=("Arial", 8))
        label_mouse_type = tk.Label(text='Mouse type (left/right)',background='lightgrey',font=("Arial", 8))
        label_key_type = tk.Label(text='Key type(a-z...)',background='lightgrey',font=("Arial", 8))

        label_start_stop.place(x=10,y=10)
        label_change_btn.place(x=10,y=60)
        label_speed_click.place(x=10,y=150)
        label_key_start_stop.place(x=250,y=10)
        label_key_change_btn.place(x=250,y=60)
        label_new_button1.place(x=10,y=35)
        label_new_button2.place(x=250,y=35)
        label_mouse_type.place(x=90,y=150)
        label_key_type.place(x=220,y=150)
        #----------BUTTON----------
        change_start_btn = tk.Button(text='Change Start',width=15,height=1,command=change_button_start)
        change_stop_btn = tk.Button(text='Change Stop',width=15,height=1,command=change_button_stop)
        change_speed_clk = tk.Button(text='Set',width=5,height=1,command=change_speed_click)
        change_key_start_btn = tk.Button(text='Change Start',width=15,height=1,command=change_key_button_start)
        change_key_stop_btn = tk.Button(text='Change Stop',width=15,height=1,command=change_key_button_stop)
        to_main_menu = tk.Button(text='Menu',width=5,height=1,command=to_menu)
        change_mouse_type_btn = tk.Button(text='Set',width=5,height=1,)
        change_key_type_btn = tk.Button(text='Set',width=5,height=1,)

        change_start_btn.place(x=10,y=85)
        change_stop_btn.place(x=10,y=115)
        change_speed_clk.place(x=10,y=190)
        change_key_start_btn.place(x=250,y=85)
        change_key_stop_btn.place(x=250,y=115)
        to_main_menu.place(x=320,y=200)
        change_mouse_type_btn.place(x=100,y=190)
        change_key_type_btn.place(x=220,y=190)
        #----------ENTRY----------
        entry_for_change = tk.Entry()
        entry_for_speed_ms = tk.Entry(width=7)
        entry_for_mouse_type = tk.Entry(width=7)
        entry_for_key_type = tk.Entry(width=7)

        entry_for_change.place(x=120,y=35)
        entry_for_speed_ms.place(x=10,y=170)
        entry_for_mouse_type.place(x=100,y=170)
        entry_for_key_type.place(x=220,y=170)
        #------------


        root.mainloop()
    
    #----------MAIN----------
    main_m = tk.Tk()
    main_m.title('UAClicker - Menu')
    main_m.geometry(f"400x250+{int(main_m.winfo_screenwidth()//2)}+{int((main_m.winfo_screenheight()//2)-150)}")
    main_m.resizable(False,False)

    clicker_btn = tk.Button(text='Clicker',width=15,height=1,command=autoclicker_key_mouse)
    
    clicker_btn.place(x=10,y=10) 

    main_m.mainloop()
    
    

main_menu()