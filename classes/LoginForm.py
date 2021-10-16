from typing import Text
from classes.AccountCreator import *
from classes.Form import *
from misc_functions import check_in_file, check_password
import tkinter as tk
import getpass
import hashlib

class LoginForm(Form):
    def __init__(self, master):
        self.master = master
        self.login_frame = tk.Frame(master)

        self.failed_logins = 0

        self.login_username_label = tk.Label(self.login_frame, text="Username: ")
        self.login_username_label.grid(column=3, row=2)

        self.login_username = tk.StringVar()
        self.login_username_entry = tk.Entry(self.login_frame, textvariable=self.login_username)
        self.login_username_entry.grid(column=4, row=2)
        
        self.login_password_label = tk.Label(self.login_frame, text="Password: ")
        self.login_password_label.grid(column=3,row=3)

        self.login_password = tk.StringVar()
        self.login_password_entry = tk.Entry(self.login_frame, textvariable=self.login_password)
        self.login_password_entry.grid(column=4, row=3)

        self.login_submit_btn = tk.Button(self.login_frame, text="Login", command=self.check_account)
        self.login_submit_btn.grid(column=3, row=4)

        self.login_forgot_btn = tk.Button(self.login_frame, text="Forgot Password")
        self.login_forgot_btn.grid(column=4, row=4)

        self.login_error_label = tk.Label(self.login_frame)

        self.login_create_btn = tk.Button(self.login_frame, text="Create Account", command=self.create_account)
        self.login_create_btn.grid(column=5, row=4)

        self.login_fail_label = tk.Label(self.login_frame)

        self.login_frame.grid(column=0, row=0)

    def check_account(self):
        username = self.login_password_entry.get()
        if check_in_file("data/passwd.txt", username):
            if self.login(username):
                print(username)
                #return username
                #need to see menu
            else:
                self.login_error_label.configure(text="You did not login successfully.")
                self.login_error_label.grid(column=3, row=5)
        else:
            self.login_error_label.configure(text="User does not exist")
            self.login_error_label.grid(column=3, row=5)


    def create_account(self):
        pass


        
    def login(self, username):
            password = self.login_password_entry.get()
            password_hash = hashlib.md5(str(password).encode('utf-8'))
            password = password_hash.hexdigest()
            if check_password(username, password):
                self.login_error_label.configure(text="You have logged in successfully!")
                self.login_error_label.grid(column=3, row=6)
                #return a True value if login success
                return True
            else:
                self.failed_logins += 1
                self.login_error_label.configure(text="You have failed to login.")
                self.login_error_label.grid(column=3, row=6)
                self.login_fail_label.configure(text=f"There are {3-self.failed_logins} attempts remaining")
                self.login_fail_label.grid(column=4, row=6)
                if self.failed_logins >= 3:
                    self.login_error_label.configure("You have failed too many times. Account has been locked.")
                    self.login_error_label.grid(column=3, row=6)
                    self.login_submit_btn.destroy()
                    #need to create account lock method
                    #return a False value if login failed
                    return False

'''
            self.login_frame.
            account_creator = AccountCreator()
            account_creator.create_account(self.master, username)
            
            else:
                #NEED TO DO THIS - FORGOT PASSWORD METHOD
                email = input("Please enter your email address: ")
                try:
                    email = str(email)
                except TypeError:
                    print("You enter an invalid value")
                if check_in_file("data/player_data.txt", email):
                    print("We are sending a password reset token to your email address")
                    #NEED TO DO: SEND EMAIL RESET CODE - METHODS
                    pass
                else:
                    print("This email isn't registered to an account")
'''