from tkinter import *
from tkinter import filedialog
sourse=''


def My_open():
    f_sourse=filedialog.askopenfilename(title="Выбор файла", filetypes=[("Текстовые документы","*.txt")])
    global sourse
    if f_sourse:
        text.delete('1.0',END)
        f_open=open(f_sourse).read()
        text.insert('1.0', f_open)
        sourse=f_sourse   
    

def My_save():
    if sourse!='':
        f_save=open(sourse, "w")
        text_out=text.get('1.0', END)
        f_save.write(text_out)
        f_save.close()
    else:
        My_save_as()
    

def My_save_as():
    f_sourse=filedialog.asksaveasfilename( filetypes=[("Текстовые документы","*.txt")])
    f_save=open(f_sourse, "w")
    text_out=text.get('1.0', END)
    f_save.write(text_out)
    f_save.close()


def My_close():
    root.destroy()


root = Tk()
root.title('WordPad')
root.iconbitmap('notepad.ico')
root.geometry('1000x500+300+52')
text=Text(root, wrap=WORD, padx=1, pady=10, spacing3=10)
text.pack(expand=True, fill=BOTH, side=RIGHT)
scrol=Scrollbar(text, command=text.yview)
scrol.pack(fill=Y, side=RIGHT)
text.config(yscrollcommand=scrol.set)
mainmenu=Menu(root)
root.config(menu=mainmenu)

file_menu=Menu(mainmenu, tearoff=0)
file_menu.add_command(label='Открыть', command=My_open)
file_menu.add_command(label='Сохранить', command=My_save)
file_menu.add_command(label='Сохранить как', command=My_save_as)
file_menu.add_command(label='Выхход', command=My_close)
mainmenu.add_cascade(label='Файл', menu=file_menu)






root.mainloop()