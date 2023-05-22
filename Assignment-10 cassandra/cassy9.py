from tkinter import *
from cassandra.cluster import Cluster

# Connect to Cassandra
cluster = Cluster(['localhost']) # Change to your Cassandra node's IP address
session = cluster.connect('demo') # Change to your keyspace name

# Define a function to execute a query
def execute_query(query):
    rows = session.execute(query)
    return rows

# Define a function to display the query result in a listbox
def display_result(result):
    listbox.delete(0, END)
    for row in result:
        listbox.insert(END, row)

# Define a function to handle button click event
def handle_click():
    query = query_entry.get()
    result = execute_query(query)
    display_result(result)

# Create a window
window = Tk()
window.title('Cassandra GUI')
window.geometry('900x900')
# Create a label
label = Label(window, text='Enter a CQL query:',font=('Arial', 24))
label.pack()

# Create an entry field
query_entry = Entry(window)
query_entry.pack()

# Create a button
button = Button(window, text='Execute', command=handle_click)
button.pack()

# Create a listbox to display the query result
listbox = Listbox(window)
listbox.pack()

# Start the GUI main loop
window.mainloop()
