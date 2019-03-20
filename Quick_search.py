import webbrowser
from tkinter import *
from PyQt4 import QtGui

google_search = True
stackoverflow_search = True

def set_text(entry, text):
    entry.delete(0, END)
    entry.insert(0, text)

def center(toplevel):
    toplevel.update_idletasks()

    app = QtGui.QApplication([])
    screen_width = app.desktop().screenGeometry().width()
    screen_height = app.desktop().screenGeometry().height()

    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = screen_width/2 - size[0]/2
    y = screen_height/2 - size[1]/2

    toplevel.geometry("+%d+%d" % (x, y))
    
    search.after(150, show_window, None)

def select_all(widget):
    widget.select_range(0, 'end')
    widget.icursor('end')

def callback(event):
    window.after(50, select_all, event.widget)

def search_func(widget):
    print('Google search: ' + str(google_search) + ' So search: ' + str(stackoverflow_search))
    if(not google_search):
        webbrowser.open_new_tab('https://stackoverflow.com/search?q=' + widget.get())
    elif(stackoverflow_search):
        webbrowser.open_new_tab('https://www.google.com/search?q=' + widget.get() + ' site:stackoverflow.com')
    else:
        webbrowser.open_new_tab('https://www.google.com/search?q=' + widget.get())
    exit()

def search_callback(event):
    window.after(50, search_func, event.widget)

def show_window(arg):
    window.lift()
    pass

def quit_code(event):
    exit()

def steal_focus():
    window.focus_force()
    search.focus()

def change_search(event):
    global google_search
    if(not google_search):
        google_search = True
        if(not stackoverflow_search):
            set_text(event.widget, 'Google search')
        else:
            set_text(event.widget, 'Google search (on stackoverflow)')
    else:
        google_search = False
        set_text(event.widget, 'Stackoverflow search')

def enable_so_google(event):
    global stackoverflow_search
    if(google_search and not stackoverflow_search):
        set_text(event.widget, 'Google search (on stackoverflow)')
        select_all(event.widget)
        stackoverflow_search = True
    elif(google_search):
        set_text(event.widget, 'Google search')
        select_all(event.widget)
        stackoverflow_search = False

window = Tk()
frame = Frame(window)

window.lower()
window.title(' ')

search = Entry(width=30)
search.pack()
center(window)
search.insert(END, 'Google search (on stackoverflow)')
search.bind('<Return>', search_callback)
search.bind('<Control-a>', callback)
search.bind('<Alt-j>', enable_so_google)
search.bind('<Escape>', quit_code)
search.bind('<Tab>', change_search)
search.bind('<FocusOut>', quit_code)

window.wm_attributes('-type', 'splash')

window.after(50, select_all, search)
window.after(50, steal_focus)

window.mainloop()