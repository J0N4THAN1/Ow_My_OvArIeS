from tkinter import*

root = Tk()
root.geometry("600x600")


list_name = ["Abbakeio","Naranchuh","Meestah","Jornoh"]
dict_student = {"name" : "Jonathan",
                "age" : "12"}

try:
    print(list_name[5])
    
    print(dict_student["mom"])
    
    

except IndexError :
    messagebox.showinfo("LiL bIg BoB","Ow My OvArIeS")
except KeyError :
    messagebox.showinfo("LiL bIg BoB","Ow My OvArIeS")