# Import Module
from tkinter import *
from tkhtmlview import HTMLLabel
 
# Create Object
root = Tk()
 
# Set Geometry
root.geometry("400x400")
 
# Add label
my_label = HTMLLabel(root, html="""
    <ul>
        <li><a href='https://www.geeksforgeeks.org/python-programming-language/'>Python</a></li>
        <li><a href='https://www.geeksforgeeks.org/c-plus-plus/'>C++</a></li>
        <li><a href='https://www.geeksforgeeks.org/java/'>Java</a></li>
    </ul>
    """)
 
# Adjust label
my_label.pack(pady=20, padx=20)
 
# Execute Tkinter
root.mainloop()