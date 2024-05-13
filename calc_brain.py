equation = ""

# clears the screen
def clear(label):
    global equation
    equation = ""
    label.config(text=equation)

# calculates the given equation on screen
def calculate(label):
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
            label.config(text=equation)
        except:
            result = "error"
            equation = ""
    label.config(text=result)

# show s the given written equation on the calculator screen
def show(label, value):
    global equation
    equation += value
    label.config(text=equation)
