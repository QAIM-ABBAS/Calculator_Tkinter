from tkinter import *
from calc_brain import show, clear, calculate

window = Tk()
window.title("Calculator")
window.geometry("555x600+100+200")
window.config(background="#002379")
window.resizable(width=False, height=False)

label_result = Label(window, text="", width=90, height=5)
label_result.pack()


Button(window, width=5, height=1, text="C", fg="#fff", bg="#3697f7", font=("ariel", 30, "bold"), command=lambda: clear(label_result)).place(x=10, y=100)
Button(window, width=5, height=1, text="/", fg="#fff", bg="#322C2B", font=("ariel", 30, "bold"), command=lambda: show(label_result, "/")).place(x=145, y=100)
Button(window, width=5, height=1, text="%", fg="#fff", bg="#322C2B", font=("ariel", 30, "bold"), command=lambda: show(label_result, "%")).place(x=280, y=100)
Button(window, width=5, height=1, text="*", fg="#fff", bg="#322C2B", font=("ariel", 30, "bold"), command=lambda: show(label_result, "*")).place(x=415, y=100)

Button(window, width=5, height=1, text="7", fg="#fff", bg="#002147", font=("ariel", 30, "bold"), command=lambda: show(label_result, "7")).place(x=10, y=200)
Button(window, width=5, height=1, text="8", fg="#fff", bg="#002147", font=("ariel", 30, "bold"), command=lambda: show(label_result, "8")).place(x=145, y=200)
Button(window, width=5, height=1, text="9", fg="#fff", bg="#002147", font=("ariel", 30, "bold"), command=lambda: show(label_result, "9")).place(x=280, y=200)
Button(window, width=5, height=1, text="-", fg="#fff", bg="#322C2B", font=("ariel", 30, "bold"), command=lambda: show(label_result, "-")).place(x=415, y=200)

Button(window, width=5, height=1, text="4", fg="#fff", bg="#002147", font=("ariel", 30, "bold"), command=lambda: show(label_result, "4")).place(x=10, y=300)
Button(window, width=5, height=1, text="5", fg="#fff", bg="#002147", font=("ariel", 30, "bold"), command=lambda: show(label_result, "5")).place(x=145, y=300)
Button(window, width=5, height=1, text="6", fg="#fff", bg="#002147", font=("ariel", 30, "bold"), command=lambda: show(label_result, "6")).place(x=280, y=300)
Button(window, width=5, height=1, text="+", fg="#fff", bg="#322C2B", font=("ariel", 30, "bold"), command=lambda: show(label_result, "+")).place(x=415, y=300)

Button(window, width=5, height=1, text="1", fg="#fff", bg="#002147", font=("ariel", 30, "bold"), command=lambda: show(label_result, "1")).place(x=10, y=400)
Button(window, width=5, height=1, text="2", fg="#fff", bg="#002147", font=("ariel", 30, "bold"), command=lambda: show(label_result, "2")).place(x=145, y=400)
Button(window, width=5, height=1, text="3", fg="#fff", bg="#002147", font=("ariel", 30, "bold"), command=lambda: show(label_result, "3")).place(x=280, y=400)
Button(window, width=5, height=3, text="=", fg="#fff", bg="#FF5F00", font=("ariel", 30, "bold"), command=lambda: calculate(label_result)).place(x=415, y=405)

Button(window, width=10, height=1, text="0", fg="#000", bg="#FFFAE6", font=("ariel", 30, "bold"), command=lambda: show(label_result, "0")).place(x=10, y=500)
Button(window, width=5, height=1, text=".", fg="#fff", bg="#153448", font=("ariel", 30, "bold"), command=lambda: show(label_result, ".")).place(x=272, y=500)

window.mainloop()
