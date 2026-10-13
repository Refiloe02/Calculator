import tkinter

button_values = [
    ["AC", "+/-", "%", "/"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["/", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values)
column_count = len(button_values[0])

colour_light_gray = "#D4D4D2"
colour_black = "#1C1C1C"
colour_dark_gray = "#505050"
colour_orange = "#FF9500"
colour_white = "white"

window = tkinter.Tk()
window.title("Calculator")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0", font=("Ariel", 45), background=colour_black,
                      foreground=colour_white, anchor="e")

label.grid(row=0,column=0, columnspan=column_count, sticky="we")

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 30), width=column_count-1,
                                height=1, command=lambda value=value: button_clicked(value))

        if value in top_symbols:
            button.config(foreground=colour_black, background=colour_light_gray)
        elif value in right_symbols:
            button.config(foreground=colour_white, background=colour_orange)
        else:
            button.config(foreground=colour_white, background=colour_dark_gray)

        button.grid(row = row+1, column=column)
        

frame.pack()

#A+B, A-B, A*B, A/B
A = "0"
operator = None
B = None

def button_clicked(value):
    global right_symbols, top_symbols, label, A, B, operator

    if value in right_symbols:
        pass
    elif value in top_symbols:
        pass
    else: #digits or .
        if value == ".":
            pass
        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value #replace 0
            else:
                label["text"] += value #append digit

window.update() #update window with the new size dimensions
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenwidth()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()