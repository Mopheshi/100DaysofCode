from tkinter import *


def convert_miles_to_km():
    km = float(miles.get()) * 1.60934
    # km_result["text"] = f"{round(km)} OR
    km_result.config(text=f"{round(km)}")
    miles.delete(0, END)

window = Tk()

window.title("Mile to Km Converter")
window.minsize(width=50, height=30)
window.config(padx=20, pady=20)

miles = Entry(width=10)
miles.grid(column=1, row=0)

mLabel = Label(text="Miles")
mLabel.grid(column=2, row=0)

equalLabel = Label(text="is equal to")
equalLabel.grid(column=0, row=1)

km_result = Label(text="0")
km_result.grid(column=1, row=1)

kmLabel = Label(text="Km")
kmLabel.grid(column=2, row=1)

calculate = Button(text="Calculate", command=convert_miles_to_km)
calculate.grid(column=1, row=2)

window.mainloop()
