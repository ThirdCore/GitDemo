import tkinter

screen = tkinter.Tk()
screen.geometry("500x300")
screen.title("DevOps Login")


labelUsername = tkinter.Label(screen, text = "Enter Username: ")
labelUsername.place(x = 75, y = 20)
inputUsername = tkinter.Entry(screen)
inputUsername.place(x = 185, y = 20)

labelPassword = tkinter.Label(screen, text = "Enter password: ")
labelPassword.place(x = 75, y = 45)
inputPassword = tkinter.Entry(screen, show = "*")
inputPassword.place(x = 185, y = 45)

labelCourse = tkinter.Label(screen, text = "Select Course: ")
labelCourse.place(x = 75, y = 80)
selectedCourse = tkinter.StringVar()
dropdownCourse = tkinter.OptionMenu(screen, selectedCourse, "BCA", "BBA", "B.Tech", "MBA", "MCA", "M.Tech")
dropdownCourse.place(x = 185, y = 80)

labelPhone = tkinter.Label(screen, text="Phone number: ")
labelPhone.place(x = 75, y = 120)
inputPhone = tkinter.Entry(screen)
inputPhone.place(x = 185, y = 120)

labelPhone = tkinter.Label(screen, text="Phone number: ")
labelPhone.place(x = 75, y = 120)
inputPhone = tkinter.Entry(screen)
inputPhone.place(x = 185, y = 120)


labelAddress = tkinter.Label(screen, text="Address: ")
labelAddress.place(x = 75, y = 145)
inputAddress = tkinter.Entry(screen)
inputAddress.place(x = 185, y = 145)

registerButton = tkinter.Button(screen, text="Regsiter")
registerButton.place(x = 200, y = 190)

screen.mainloop()