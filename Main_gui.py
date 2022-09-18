import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
from ttkthemes import ThemedTk
from PIL import ImageGrab
from PIL import Image
from numpy import argmax
# tf.keras.utils.load_img
from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array
from tensorflow.keras.models import load_model

root = ThemedTk(theme="equilux")
s = ttk.Style()
# s.configure('.', font=('Helvetica', 12))
s.configure('clear_btn.TButton', font=('Helvetica', 15))
s.configure('predict_label.TLabel' , font=('Helvetica', 18))
s.configure('predict_number_label.TLabel' , font=('Helvetica', 60) , bordercolor="white")
s.configure('confi_number_label.TLabel' , font=('Helvetica', 40) , bordercolor="white")

root.title("Digit Recognizer -- Srivatsa")

predict_text = StringVar(root,value="Loading....")
confi_text= StringVar(root,value="Loading....")


def get_pred():
    img = get_img()
    model = load_model("final_model.h5")
    pred = model.predict(img)
    digit = argmax(pred)
    predict_text.set(digit)
    confi_text.set(pred[0][digit]*100)
    print(pred[0][digit], digit)


def get_img():
    x=root.winfo_rootx()+root.winfo_x()
    y=root.winfo_rooty()+root.winfo_y()
    x1=x+root.winfo_width()
    y1=y+root.winfo_height()
    im = ImageGrab.grab().crop((x,y,x1-500,y1))
    im.save('temp.png')
    # load the image
    img = load_img('temp.png', color_mode = "grayscale", target_size=(28, 28))
	# convert to array
    img = img_to_array(img)
	# reshape into a single sample with 1 channel
    img = img.reshape(1, 28, 28, 1)
	# prepare pixel data
    img = img.astype('float32')
    img = img / 255.0
    return img
    
def viewer():
    x=root.winfo_rootx()+root.winfo_x()
    y=root.winfo_rooty()+root.winfo_y()
    x1=x+root.winfo_width()
    y1=y+root.winfo_height()
    im = ImageGrab.grab().crop((x,y,x1-500,y1))
    print("Size Information of the Canvas :- ",x,y,x1,y1)
    im.show()
    
def clear_all():
    canvas.delete('all')

def draw_lines( event):
        x = event.x
        y = event.y
        r=20
        canvas.create_oval(x-r,y-r, x + r, y + r, fill='white' , outline = 'white')

leftframe = ttk.Frame(root)
rightframe = ttk.Frame(root)

canvas = tk.Canvas(leftframe, width=700, height=506, cursor="cross"  , bg = 'black')
canvas.grid()


# Right Side (Includes Buttons and dispaly board)
# button for clearing
clear_btn = ttk.Button(rightframe, text="Clear",width = 20 , command=clear_all , style='clear_btn.TButton').grid(column= 0 , row= 6 )
# button for submitting your drawing
submit_btn = ttk.Button(rightframe, text="Submit",width = 20 , command=get_pred , style='clear_btn.TButton').grid(column= 1 , row= 6)
#button for seeing what we have drawn in canvas
view_btn = ttk.Button(rightframe, text="View",width = 20 , command=viewer , style='clear_btn.TButton').grid(column= 0 , row= 7)
#button for getting the help page open up
help_btn = ttk.Button(rightframe, text="Help",width = 20 , command=clear_all , style='clear_btn.TButton').grid(column= 1 , row= 7)

# predicting label
ttk.Label(rightframe , text = "The Predicted digit is :",justify= 'center', style='predict_label.TLabel').grid(columnspan=2 , row= 1,pady=20)
# predicting number label 

ttk.Label(rightframe , textvariable=predict_text,justify= 'center', style='predict_number_label.TLabel', background="blue", foreground="white" , relief="ridge" , padding=(40,0)).grid(columnspan=2 , row= 2, padx=10, pady=50)

ttk.Label(rightframe , text = "With confidence percentage(%) of :",justify= 'center', style='predict_label.TLabel').grid(columnspan=2 , row= 4)

ttk.Label(rightframe , textvariable=confi_text, style='confi_number_label.TLabel', background="blue", foreground="white" ,justify= tk.CENTER, relief="ridge" , padding=(50,0)).grid(columnspan=2 , row= 5, padx=10, pady=41)
#packing my two frames
leftframe.grid(column=0,row=0)
rightframe.grid(column= 1 , row= 0 )

#binding function to draw on canvas
canvas.bind('<B1-Motion>', draw_lines)





root.configure(bg='gray')
root.mainloop()