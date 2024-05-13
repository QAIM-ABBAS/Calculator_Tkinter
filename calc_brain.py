equation = ""

# clears the calculator screen
def clear(label):
    global equation
    equation = ""
    label.config(text=equation)

# calculates the given equation on the screen
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

# shows the written equation on the calculator screen
def show(label, value):
    global equation
    equation += value
    label.config(text=equation)
