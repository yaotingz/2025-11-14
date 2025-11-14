import requests
import json
import tkinter as tk

api_key = 'Your API'

root = tk.Tk()
root.title ('The Movie DataBase')
root.geometry ('500x500')

label_movie = tk.Label(root, text='Movie ID')
label_movie.pack(pady=(15,5))
entry_movie = tk.Entry(root, width = 25)
entry_movie.pack()

show_variable = tk.StringVar()
show_area = tk.Label(root, 
     textvariable = show_variable,
     font = ('Helvetica', 12),
     bg = 'lightyellow',
     wraplength = 380,
     justify = 'left')
show_area.pack(pady=20, padx=10, fill='both', expand=True)

def print_movie():
    movie_id = entry_movie.get()
    print ('Moive ID = ', movie_id)
    print ('-'*30)

button_print = tk.Button(root, text = 'Print', command = print_movie)
button_print.pack(pady=15)

def print_revenue():
    movie_id = entry_movie.get()
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
    response = requests.get(url)
    data = response.json()
    revenue_value = data.get('revenue')
    print ('Revenu = ', revenue_value)
    print ('-' * 30)

    show_variable.set(revenue_value)

button_revenue = tk.Button(root, text='Revenue', command=print_revenue)
button_revenue.pack(pady=15)

root.mainloop()