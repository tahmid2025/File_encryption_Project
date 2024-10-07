# All the libaries that will be used
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import os
import random
import string

# This is a function to generate my Encryption key
def encryption_key(length=6):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))



