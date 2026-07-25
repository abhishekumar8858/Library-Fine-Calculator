from tkinter import *
from datetime import datetime

root = Tk()
root.title("Library Fine Calculator")
root.geometry("800x900")
root.resizable(False, False)
root.configure(bg="#E3F2FD")


def calculateFine():
    try:
        name = nameValue.get().strip()
        book = bookValue.get().strip()
        issue = issueValue.get().strip()
        return_date = returnValue.get().strip()

        
        if name == "" or book == "" or issue == "" or return_date == "":
            result.config(
                text="Please fill all the fields!",
                fg="red"
            )
            return

        
        issue_date = datetime.strptime(issue, "%d/%m/%Y")
        return_dt = datetime.strptime(return_date, "%d/%m/%Y")

        
        days = (return_dt - issue_date).days

        if days < 0:
            result.config(
                text="Return Date cannot be before Issue Date!",
                fg="red"
            )
            return

        
        if days <= 7:
            fine = 0
            status = "No Fine"

        elif days <= 15:
            fine = (days - 7) * 2
            status = "Fine Due"

        elif days <= 30:
            fine = (8 * 2) + (days - 15) * 5
            status = "Fine Due"

        else:
            fine = (8 * 2) + (15 * 5) + (days - 30) * 10
            status = "Fine Due"

        result.config(
            text=f"Student Name : {name}\n"
                 f"Book Name    : {book}\n"
                 f"Late Days    : {days}\n"
                 f"Fine         : ₹{fine}\n"
                 f"Status       : {status}",
            fg="green"
        )

    except ValueError:
        result.config(
            text="Enter dates in DD/MM/YYYY format!",
            fg="red"
        )


def reset():
    nameValue.set("")
    bookValue.set("")
    issueValue.set("")
    returnValue.set("")
    result.config(text="")
    nameEntry.focus()


def nextBook(event):
    bookEntry.focus()


def nextIssue(event):
    issueEntry.focus()


def nextReturn(event):
    returnEntry.focus()


frame = Frame(
    root,
    bg="white",
    bd=3,
    relief="ridge",
    width=700,
    height=600
)
frame.place(x=50, y=40)


Label(
    frame,
    text="📚 Library Fine Calculator",
    font=("Arial", 24, "bold"),
    bg="white",
    fg="#0D47A1"
).place(x=150, y=20)

nameValue = StringVar()
bookValue = StringVar()
issueValue = StringVar()
returnValue = StringVar()

Label(
    frame,
    text="Student Name",
    font=("Arial", 15, "bold"),
    bg="white",
    fg="#1565C0"
).place(x=80, y=100)

Label(
    frame,
    text="Book Name",
    font=("Arial", 15, "bold"),
    bg="white",
    fg="#1565C0"
).place(x=80, y=170)

Label(
    frame,
    text="Issue Date",
    font=("Arial", 15, "bold"),
    bg="white",
    fg="#1565C0"
).place(x=80, y=240)

Label(
    frame,
    text="Return Date",
    font=("Arial", 15, "bold"),
    bg="white",
    fg="#1565C0"
).place(x=80, y=310)

nameEntry = Entry(
    frame,
    textvariable=nameValue,
    font=("Arial", 15),
    width=25,
    bd=3,
    relief="groove"
)
nameEntry.place(x=280, y=100)

bookEntry = Entry(
    frame,
    textvariable=bookValue,
    font=("Arial", 15),
    width=25,
    bd=3,
    relief="groove"
)
bookEntry.place(x=280, y=170)

issueEntry = Entry(
    frame,
    textvariable=issueValue,
    font=("Arial", 15),
    width=25,
    bd=3,
    relief="groove"
)
issueEntry.place(x=280, y=240)

returnEntry = Entry(
    frame,
    textvariable=returnValue,
    font=("Arial", 15),
    width=25,
    bd=3,
    relief="groove"
)
returnEntry.place(x=280, y=310)


nameEntry.bind("<Return>", nextBook)
bookEntry.bind("<Return>", nextIssue)
issueEntry.bind("<Return>", nextReturn)
returnEntry.bind("<Return>", lambda event: calculateFine())

Button(
    frame,
    text="Calculate Fine",
    font=("Arial", 14, "bold"),
    bg="#1976D2",
    fg="white",
    activebackground="#0D47A1",
    activeforeground="white",
    padx=10,
    pady=5,
    command=calculateFine
).place(x=170, y=390)

Button(
    frame,
    text="Reset",
    font=("Arial", 14, "bold"),
    bg="#D32F2F",
    fg="white",
    activebackground="#B71C1C",
    activeforeground="white",
    padx=20,
    pady=5,
    command=reset
).place(x=430, y=390)

result = Label(
    frame,
    text="",
    font=("Arial", 16, "bold"),
    bg="white",
    fg="green",
    justify=LEFT
)
result.place(x=200, y=450)

nameEntry.focus()

root.mainloop()