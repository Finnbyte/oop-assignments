from users import *
from custom_types import Gender, UserExistsException
import tkinter as tk
from tkinter import messagebox

class Sorter:
    NAME = { "title": "Nimi", "method": lambda d: d["name"], "should_reverse": False }
    WEALTH = { "title": "Varat", "method": lambda d: int(d["wealth"]), "should_reverse": True }

class MyDialog:
    def __init__(self, parent, labels, placeholders=None, title=None):
        top = self.top = tk.Toplevel(parent)
        top.geometry("400x200")

        if title is not None:
            top.title(title)

        self.entries = []
        self.exited_succesfully = False
        self.answers = []
        for i, label in enumerate(labels):
            label = tk.Label(top, text=label)
            label.pack()

            entry = tk.Entry(top)
            if placeholders is not None and len(placeholders) >= i:
                entry.insert(0, placeholders[i])
            self.entries.append(entry)
            entry.pack()

        self.mySubmitButton = tk.Button(top, text='Submit', command=self._send)
        self.mySubmitButton.pack()

    def _send(self):
        self.exited_succesfully = True
        self.answers = [entry.get().strip() for entry in self.entries]
        self.top.destroy()

class UserManagementPanel:
    def __init__(self, root):
        self.root = root
        self.root.title("Pankkikäyttäjät GUI")

        self.user_manager = UserManager()
        self.users = self.user_manager.fetch_users()

        self.sort_by = Sorter.NAME

        self.create_widgets()

    def on_select(self, event):
        selected_idx = self.user_list.curselection()
        if selected_idx:
            userlist_user = self.user_list.get(selected_idx)

            self.display_user_data([user for user in self.users if user.name == userlist_user][0])

    def create_widgets(self):
        # User list
        self.user_list = tk.Listbox(self.root, width=30)
        self.user_list.pack(side=tk.LEFT, padx=10, pady=10)
        self.user_list.bind("<<ListboxSelect>>", self.on_select)

        # Populate user list
        for user in self.users:
            self.user_list.insert(tk.END, user.name)

        # User details display
        self.details_frame = tk.Frame(self.root, padx=10, pady=10)
        self.details_frame.pack(side=tk.LEFT)

        self.name_label = tk.Label(self.details_frame, text="Nimi:")
        self.name_label.pack(anchor=tk.W)

        self.gender_label = tk.Label(self.details_frame, text="Sukupuoli:")
        self.gender_label.pack(anchor=tk.W)

        self.age_label = tk.Label(self.details_frame, text="Ikä:")
        self.age_label.pack(anchor=tk.W)

        self.wealth_label = tk.Label(self.details_frame, text="Varat:")
        self.wealth_label.pack(anchor=tk.W)

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=5)

        self.sort_button = tk.Button(button_frame, text=f"Sort by: {self.sort_by['title']}", command=self.swap_sorter_and_apply_sorting)
        self.sort_button.grid(row=0, column=0, padx=10)

        add_button = tk.Button(button_frame, text="Add User", command=self.add_user)
        add_button.grid(row=0, column=1, padx=5)

        modify_button = tk.Button(button_frame, text="Modify User", command=self.modify_user)
        modify_button.grid(row=0, column=2, padx=5)

        delete_button = tk.Button(button_frame, text="Delete User", command=self.delete_user)
        delete_button.grid(row=0, column=3, padx=5)

    def display_user_data(self, user):
        self.name_label.config(text=f"Nimi: {user.name or ''}")
        self.gender_label.config(text=f"Sukupuoli: {user.gender or ''}")
        self.age_label.config(text=f"Ikä: {user.age or ''}")
        self.wealth_label.config(text=f"Varat: {user.wealth or 'Ei varallisuutta'}")

    def swap_sorter_and_apply_sorting(self):
        self.sort_by = Sorter.NAME if self.sort_by == Sorter.WEALTH else Sorter.WEALTH
        self.sort_button.config(text=f"Sort by: {self.sort_by['title']}")

        # Apply sorting
        self.apply_sorting(self.sort_by["method"], do_reverse=self.sort_by["should_reverse"])


    def apply_sorting(self, method, do_reverse: bool):
        names_and_wealths = [{ "name": user.name, "wealth": user.wealth } for user in self.users]
        sorted_users = sorted(names_and_wealths, key=method, reverse=do_reverse)

        self.user_list.delete(0, tk.END)
        for user in sorted_users:
            self.user_list.insert(tk.END, user["name"])
        self.user_list.selection_set(0)

       
    def add_user(self):
        inputDialog = MyDialog(root, labels=("Nimi:", "Sukupuoli:", "Ikä:", "Varat:"), title="Lisää käyttäjä")
        root.wait_window(inputDialog.top)
        if inputDialog.exited_succesfully:
            data = inputDialog.answers
            user = User(data[0], data[1], data[2], data[3])
            if self.user_manager.add_user(user) is not UserExistsException:
                self.users.append(user)
                self.user_list.insert(tk.END, user.name)

    def modify_user(self):
        selected_index = self.user_list.curselection()
        user = self.users[selected_index[0]]

        inputDialog = MyDialog(root, 
                                placeholders=(user.name, user.gender, user.age, user.wealth), 
                                labels=("Uusi nimi:", "Uusi sukupuoli:", "Uusi ikä:", "Uudet varat:"), 
                                title=f"Muokkaa käyttäjää {user.name}")
        root.wait_window(inputDialog.top)
        if inputDialog.exited_succesfully:
            data = inputDialog.answers                                                                              
            try:
                self.user_manager.modify_user(user, data)

                updated_info_user = User(data[0], data[1], data[2], data[3])

                # Get index of name
                idx = self.user_list.get(0, tk.END).index(user.name)

                self.users[idx] = updated_info_user

                self.user_list.delete(idx)
                self.user_list.insert(idx, updated_info_user.name)
            except Exception as e: 
                print("Error occured:", e)

    def delete_user(self):
        selected_index = self.user_list.curselection()
        user = self.users[selected_index[0]]
        confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete {user.name}?")
        if confirm:
            try:
                self.user_manager.remove_user(user)
                self.users.remove(user)

                # Get index of name
                idx = self.user_list.get(0, tk.END).index(user.name)

                # Delete from user_list
                self.user_list.delete(idx)
            except Exception as e:
                # Handle errors here
                print("Error occured:", e)

# Entry point of program
if __name__ == "__main__":
    UserManager().ensure_table()

    root = tk.Tk()
    app = UserManagementPanel(root)
    root.mainloop()
