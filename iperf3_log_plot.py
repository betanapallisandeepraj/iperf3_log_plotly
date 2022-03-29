import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objs as go
from tkinter import *
from tkinter import filedialog

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                        title = "Select a File",
                        filetypes = (("Text files",
                        "*.txt*"),
                        ("all files",
                        "*.*")))

    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)
    df = pd.read_fwf(filename)
    df=df.drop(labels=[0,1],axis=0)
    df = df.reset_index(drop=True)
    df.columns = ['Bitrate_Mbps']
    for index, row in df.iterrows():
        val=row['Bitrate_Mbps']
        val=val.split("Bytes  ",1)
        if len(val)>1 :
            val=val[1]
            val=val.split(" ",1)[0]
        else:
            val=0
        df.iloc[index]=val

    df['Bitrate_Mbps']=pd.to_numeric(df.Bitrate_Mbps, errors='coerce').fillna(-1, downcast='infer')
    fig = px.area(df, x=df.index, y="Bitrate_Mbps")
    fig.write_html("file.html")
    fig.show()

# Create the root window
window = Tk()
# Set window title
window.title('File Explorer')
# Set window size
window.geometry("500x500")
#Set window background color
window.config(background = "white")

# Create a File Explorer label
label_file_explorer = Label(window,
                            text = "File Explorer using Tkinter",
                            width = 100, height = 4,
                            fg = "blue")
button_explore = Button(window,
                            text = "Browse Files",
                            command = browseFiles)

# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column = 1, row = 1)
button_explore.grid(column = 1, row = 2)
# Let the window wait for any events
window.mainloop()
