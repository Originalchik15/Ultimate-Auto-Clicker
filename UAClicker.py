import tkinter as tk
import random as rng
import pyautogui as pg
import keyboard as kb
import time
import mouse 

def autoclick_mouse(e): # mouse autoclicking
    while True:
        if kb.is_pressed(stop_button_mouse):
            break
        mouse.click('left')
        time.sleep(speed_click)

def autoclick_key(e): # key autoclicking
    while True:
        if kb.is_pressed(stop_button_key):
            break
        kb.send(key_click)
        time.sleep(speed_click)
        



#----------DEFAULT_SETTINGS----------
start_button_mouse = 'f8'
stop_button_mouse = 'f7'
start_button_key = 'f6'
stop_button_key = 'f5'
key_click = 'e'
speed_click = 10

def main_menu():
    #----------AUTOCLICKER----------
    def autoclicker_key_mouse():
        #сделать проверку на однотипность и количество букв
        main_m.destroy()
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

        label_start_stop.place(x=10,y=10)
        label_change_btn.place(x=10,y=60)
        label_speed_click.place(x=10,y=150)
        label_key_start_stop.place(x=250,y=10)
        label_key_change_btn.place(x=250,y=60)
        label_new_button1.place(x=10,y=35)
        label_new_button2.place(x=250,y=35)
        #----------BUTTON----------
        change_start_btn = tk.Button(text='Change Start',width=15,height=1,command=change_button_start)
        change_stop_btn = tk.Button(text='Change Stop',width=15,height=1,command=change_button_stop)
        change_speed_clk = tk.Button(text='Set',width=5,height=1,command=change_speed_click)
        change_key_start_btn = tk.Button(text='Change Start',width=15,height=1,command=change_key_button_start)
        change_key_stop_btn = tk.Button(text='Change Stop',width=15,height=1,command=change_key_button_stop)

        change_start_btn.place(x=10,y=85)
        change_stop_btn.place(x=10,y=115)
        change_speed_clk.place(x=10,y=190)
        change_key_start_btn.place(x=250,y=85)
        change_key_stop_btn.place(x=250,y=115)
        #----------ENTRY----------
        entry_for_change = tk.Entry()
        entry_for_speed_ms = tk.Entry(width=7)

        entry_for_change.place(x=120,y=35)
        entry_for_speed_ms.place(x=10,y=170)
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