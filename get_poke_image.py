from tkinter import *
from tkinter import ttk
import os
import ctypes
import get_poke_info
import image_lib
#Get the path of the script and its parent directory
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
# Create an inage cache directory
image_cache_dir = os.path.join(script_dir, 'images')
if not os.path.isdir(image_cache_dir):
    os.makedirs(image_cache_dir)

# Create the main window
root = Tk()
root.title("Pokemon Image")
root.columnconfigure(0, weight=1)
root.rowconfigure(0 , weight=1)
root.minsize(500, 600)
# Set the Taskbar and window icon
icon_path = os.path.join(script_dir, 'poo.ico')
app_id = 'COMP593.PokeImageViewer'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
root.iconbitmap('')

# Put the frame on the GUI
frame = ttk.Frame(root)
frame.grid(row=0, column=0, sticky=NSEW)
frame.columnconfigure(0, weight=100)
frame.rowconfigure(0, weight=100)

# Put image into frame
image_path = os.path.join(script_dir, 'LOGO.png')
img_poke = PhotoImage(file=image_path)
lbl_logo = ttk.Label(frame, image=img_poke)
lbl_logo.grid(padx=10, pady=10)

# Put the Pull-down of pokemon names into the frame
pokemon_names_list = sorted(get_poke_info.get_pokemon_name())
cbox_pokemon_names = ttk.Combobox(frame, values=pokemon_names_list, state='readonly')
cbox_pokemon_names.set("Select a Pokemon")
cbox_pokemon_names.grid(padx=10, pady=10)

def handle_pokemon_sel():
   
    sel_pokemon = cbox_pokemon_names.current()
    global image_path
    image_path = get_poke_info.download_pokemon_artwork(sel_pokemon, image_cache_dir)
    img_poke['file'] = image_path
    return
cbox_pokemon_names.bind('<<ComboboxSelected>>', handle_pokemon_sel)

def handle_set_desktop():
    image_lib.set_desktop_background_image(image_path)
btn_set_desktop = ttk.Button(frame, text='Set as Desktop Image', command=handle_pokemon_sel)
btn_set_desktop.grid(padx=10, pady=10)
# Put the set-desktop button into the frame






root.mainloop()