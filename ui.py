from tkinter import * 
import pyautogui 

try:
    count = 3
    for i in range(4):
        pwd = pyautogui.password('enter the password')

        if  pwd:
                
            if pwd != 'adam':
                count -= 1
                if count == 1:
                    pyautogui.alert(f"password is not correct ({count} more attempt)  ")
                elif count == 0:
                    exit()
                else:
                    pyautogui.alert(f"password is not correct ({count} more attempts)  ")
            else:
                root = Tk()




                root.mainloop()
        else:
            exit()

except:
    print("there was an err")
