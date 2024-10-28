import tkinter as tk
from tkinter import messagebox
class EmployerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.employee_list = []
        # Create a label for employee name
        self.name_label = tk.Label(root, text="Employee Name:")
        self.name_label.pack(pady=10)
        # Create an entry for employee name
        self.name_entry = tk.Entry(root)
        self.name_entry.pack(pady=10)
        # Create a label for employee role
        self.role_label = tk.Label(root, text="Employee Role:")
        self.role_label.pack(pady=10)
        # Create an entry for employee role
        self.role_entry = tk.Entry(root)
        self.role_entry.pack(pady=10)
        # Button to add employee
        self.add_button = tk.Button(root, text="Add Employee", command=self.add_employee)
        self.add_button.pack(pady=10)
        # Button to show employees
        self.show_button = tk.Button(root, text="Show Employees", command=self.show_employees)
        self.show_button.pack(pady=10)
        # Textbox to display employees
        self.textbox = tk.Text(root, height=10, width=30)
        self.textbox.pack(pady=10)
    def add_employee(self):
        name = self.name_entry.get()
        role = self.role_entry.get()
        if name and role:
            self.employee_list.append((name, role))
            self.name_entry.delete(0, tk.END)
            self.role_entry.delete(0, tk.END)
            messagebox.showinfo("Success", f'Employee {name} added.')
        else:
            messagebox.showwarning("Input Error", "Please enter both name and role.")
    def show_employees(self):
        self.textbox.delete(1.0, tk.END)  # Clear the textbox
        for name, role in self.employee_list:
            self.textbox.insert(tk.END, f'Name: {name}, Role: {role}\n')

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployerApp(root)
    root.mainloop()

    #
    import tkinter as tk
    from tkinter import messagebox
    class RadioButtonApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Radio Button Example")
            self.selected_choice = tk.StringVar(value="")
            # Creating radio buttons
            self.radio1 = tk.Radiobutton(root, text="Apple", variable=self.selected_choice, value="Apple")
            self.radio1.pack(anchor=tk.W)
            self.radio2 = tk.Radiobutton(root, text="Banana", variable=self.selected_choice, value="Banana")
            self.radio2.pack(anchor=tk.W)
            self.radio3 = tk.Radiobutton(root, text="Cherry", variable=self.selected_choice, value="Cherry")
            self.radio3.pack(anchor=tk.W)
            self.radio4 = tk.Radiobutton(root, text="Date", variable=self.selected_choice, value="Date")
            self.radio4.pack(anchor=tk.W)
            # Button to show the selected fruit
            self.button = tk.Button(root, text="Submit", command=self.show_selection)
            self.button.pack(pady=10)
        def show_selection(self):
            selected = self.selected_choice.get()
            if selected:
                messagebox.showinfo("Selected Fruit", f"You selected: {selected}")
            else:
                messagebox.showwarning("Selection Error", "Please select a fruit.")


    if __name__ == "__main__":
        root = tk.Tk()
        app = RadioButtonApp(root)
        root.mainloop()
        #
        from tkinter import *
        window = Tk()
        window.geometry("350x450")
        window.config(bg="orange")
        list_box = Listbox(window, height=10, width=15, bg="green", font="Helvetica", fg="yellow")
        l1 = Label(window, text="SOFTWARE COURSES")
        # INSERT VALUES INTO LIST BOX
        list_box.insert(1, "oracle")
        list_box.insert(2, "SAP")
        list_box.insert(3, "JAVA")
        list_box.insert(4, "React")
        l1.pack()
        list_box.pack(side=LEFT)
        window.mainloop()
        #
        from tkinter import *
        root = Tk()
        root.config(bg="orange")
        root.geometry("350x450")
        root.title("Radio Button demo")
        def sel():
            selection = "u have selected an option:" + str(v.get())
            label.config(text=selection)
        v = IntVar()
        values = {"Ashok": "1", "Pavan": "2", "Naresh": "3", "Suresh": "4"}
        for (key, value) in values.items():
            Radiobutton(root, text=key, variable=v, value=value, command=sel).pack(side=LEFT, ipady=5)
        label = Label(root)
        label.pack()
        root.mainloop()

        #check box
        from tkinter import *

        root = Tk()
        root.config(bg="red")
        root.geometry("350x450")
        root.title("CheckBox demo")
        def check_box_status():
            if var.get() == 1:
                print("check box selected by u\n")
            else:
                print("check box deselected by u\n")
        var = IntVar()
        check_box = Checkbutton(root, text="JAVA", variable=var, onvalue=1, offvalue=0, command=check_box_status)
        check_box.config(bg="green", fg="olive", font=30, selectcolor="red", relief="raised", padx=10, pady=5)
        check_box.pack(padx=40, pady=40)
        check_box.flash()
        root.mainloop()
       #
    from tkinter import *
    from tkinter import messagebox
    parent = Tk()
    parent.title("man")
    parent.config(bg="red")
    parent.geometry("689x569")
    name = Label(parent, text="Name:")
    name.grid(row=0, column=0, pady=10, padx=5)
    e1 = Entry(parent)
    e1.grid(row=0, column=1)
    regno = Label(parent, text="Regd NO:")
    regno.grid(row=1, column=0, pady=10, padx=5)
    e2 = Entry(parent)
    e2.grid(row=1, column=1)
    btm = Label(parent, text="Submit:")
    btm.grid(row=3, column=1)
    parent.mainloop()
    #
    import time
    import datetime
    from tkinter import *
    import tkinter.messagebox
    window = Tk()
    window.title("NTH: Employee Payroll System")
    window.geometry('100x200')
    window.configure(background="Red")
    Tops = Frame(window, width=1350, height=50, bd=8, bg="lavender")
    Tops.pack()

