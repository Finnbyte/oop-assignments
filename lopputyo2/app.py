from users import *
from custom_types import Gender, UserExistsException
import tkinter as tk
from tkinter import messagebox

class UserManagementPanel:
    def __init__(self, root):
        self.root = root
        self.root.title("Pankkikäyttäjät GUI")

        self.user_manager = UserManager()
        self.users = self.user_manager.fetch_users()

        self.create_widgets()

    def on_select(self, event):
        selected_index = self.user_list.curselection()
        if selected_index:
            user = self.users[selected_index[0]]
            self.display_user_data(user)

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

        self.name_label = tk.Label(self.details_frame, text="Name:")
        self.name_label.pack(anchor=tk.W)

        self.gender_label = tk.Label(self.details_frame, text="Gender:")
        self.gender_label.pack(anchor=tk.W)

        self.age_label = tk.Label(self.details_frame, text="Age:")
        self.age_label.pack(anchor=tk.W)

        self.wealth_label = tk.Label(self.details_frame, text="Wealth:")
        self.wealth_label.pack(anchor=tk.W)
        # Add user entry
        self.add_entry = tk.Entry(self.root, width=30)

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=5)

        add_button = tk.Button(button_frame, text="Add User", command=self.add_user)
        add_button.grid(row=0, column=0, padx=5)

        modify_button = tk.Button(button_frame, text="Modify User", command=self.modify_user)
        modify_button.grid(row=0, column=1, padx=5)

        delete_button = tk.Button(button_frame, text="Delete User", command=self.delete_user)
        delete_button.grid(row=0, column=2, padx=5)

    def display_user_data(self, user):
        self.name_label.config(text=f"Name: {user.name or ''}")
        self.gender_label.config(text=f"Gender: {user.gender or ''}")
        self.age_label.config(text=f"Age: {user.age or ''}")
        self.wealth_label.config(text=f"Wealth: {user.wealth or ''}")
       
    def add_user(self):
        user = User("John Smith", Gender.MALE, 18, 20)
        if self.user_manager.add_user(user) is not UserExistsException:
            self.users.append(user)
            self.user_list.insert(tk.END, user.name)
        return

        username = self.add_entry.get().strip()
        if username:
            self.add_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a username.")

    def modify_user(self):
        selected_index = self.user_list.curselection()
        if selected_index:
            username = self.add_entry.get().strip()
            if username:
                self.user_list.delete(selected_index)
                self.user_list.insert(selected_index, username)
                self.add_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Please enter a username.")
        else:
            messagebox.showerror("Error", "Please select a user.")

    def delete_user(self):
        selected_index = self.user_list.curselection()
        if selected_index:
            username = self.user_list.get(selected_index)
            confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete {username}?")
            if confirm:
                self.user_list.delete(selected_index)
                del self.users[selected_index]
                self.add_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please select a user.")


if __name__ == "__main__":
    um = UserManager()
    um.ensure_table()

    root = tk.Tk()
    app = UserManagementPanel(root)
    root.mainloop()
