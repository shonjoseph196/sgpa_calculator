from tkinter import *
from trial import grade_convertor
from tkinter import ttk


def calculate():
    m1 = (m1_input.get().lower())
    m2 = (m2_input.get().lower())
    m3 = (m3_input.get().lower())
    m4 = (m4_input.get().lower())
    m5 = (m5_input.get().lower())
    m6 = (m6_input.get().lower())
    m7 = (m7_input.get().lower())
    grades = [m1, m2, m3, m4, m5, m6, m7]
    gp = []
    a = grade_convertor(*grades)
    result = f" SGPA IS {a}"
    result_label.config(text=result)


root = Tk()
root.configure(bg="#4682B4")
root.title("SGPA Calculator")
root.geometry("1500x1200")

label = Label(root, text="WELCOME TO KTU S1 SGPA CALCULATOR",
              font=("Arial", 25, "bold"), bg="#4682B4", fg="white")
label.pack(pady=20)
entry_label = Label(root, text="Enter Your Details",
                    font=("Arial", 18, "bold"), bg="#4682B4", fg="white")
entry_label.pack(pady=20)

frame = Frame(root, width=800, height=450, padx=30,
              pady=30, bd=10, relief="groove")
frame.pack(pady=20)
frame.pack_propagate(False)
frame.config(bg="#C0C8D2")

grades = ["S", "A+", "A", "B+", "B", "C+", "C", "D", "P", "F"]
m1 = Label(frame, text="Select grade for mathemaics for information science -1",
           font=("Arial", 10, "bold"))
m1.grid(row=0, column=0, sticky="w")

m1_input = ttk.Combobox(
    frame,
    values=grades,
    state="readonly",
    width=15
)
m1_input.grid(row=0, column=1, padx=10, pady=5)

m2 = Label(frame, text="Select grade for Chemistry/physics for information science",
           font=("Arial", 10, "bold"))
m2.grid(row=1, column=0, sticky="w")

m2_input = ttk.Combobox(
    frame,
    values=grades,
    state="readonly",
    width=15
)
m2_input.grid(row=1, column=1, padx=10, pady=5)

m3 = Label(
    frame, text="Select grade for engineering graphic and Computer Aided Drawing", font=("Arial", 10, "bold"))
m3.grid(row=2, column=0, sticky="w")

m3_input = ttk.Combobox(
    frame,
    values=grades,
    state="readonly",
    width=15
)
m3_input.grid(row=2, column=1, padx=10, pady=5)

m4 = Label(
    frame, text="Select grade for Introduction to Electrical and Electronics Engineering", font=("Arial", 10, "bold"))
m4.grid(row=3, column=0, sticky="w")

m4_input = ttk.Combobox(
    frame,
    values=grades,
    state="readonly",
    width=15
)
m4_input.grid(row=3, column=1, padx=10, pady=5)

m5 = Label(frame, text="Select grade for Algorithmic Thinking with Python (ATP)",
           font=("Arial", 10, "bold"))
m5.grid(row=4, column=0, sticky="w")

m5_input = ttk.Combobox(
    frame,
    values=grades,
    state="readonly",
    width=15
)
m5_input.grid(row=4, column=1, padx=10, pady=5)

m6 = Label(
    frame, text="Select grade for Basic Electrical/Civil and Electronics/Mechanical Engineering Workshop", font=("Arial", 10, "bold"))
m6.grid(row=5, column=0, sticky="w")

m6_input = ttk.Combobox(
    frame,
    values=grades,
    state="readonly",
    width=15
)
m6_input.grid(row=5, column=1, padx=10, pady=5)

m7 = Label(frame, text="Select grade for Life Skills and Professional Communication",
           font=("Arial", 10, "bold"))
m7.grid(row=6, column=0, sticky="w")

m7_input = ttk.Combobox(
    frame,
    values=grades,
    state="readonly",
    width=15
)
m7_input.grid(row=6, column=1, padx=10, pady=5)

button = Button(root, text="Get SGPA", bg="#2563EB", fg="white", activebackground="#1D4ED8",
                activeforeground="white", width=10, height=2, command=calculate)
button.pack(pady=10)

result_label = Label(root, text="", font=(
    "Arial", 22, "bold"), bg="#4682B4", fg="white")
result_label.pack(pady=10)

root.mainloop()
