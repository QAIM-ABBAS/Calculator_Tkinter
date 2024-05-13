equation = ""


def clear(label):
    global equation
    equation = ""
    label.config(text=equation)


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


def show(label, value):
    global equation
    equation += value
    label.config(text=equation)
