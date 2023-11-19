import tkinter as tk
import sqlite3
from tkinter import ttk
from tkinter import *
class OKDataViewer:

    def __init__(self, root):
        self.root = root
        self.root.title("Jwewlry Store - DataBase")
        self.root.geometry("1350x1200")
        self.root.config(bg="snow3")
        self.root.resizable(0,0)

        self.create_gui()

    def db_table(self, tbl, sort=0, sortcol=0):
        conn = sqlite3.connect('JewelryStore.db')
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM {tbl}')
        data = cursor.fetchall()
        
        #print(f'Do Load {tbl}, sort={sort}, sortcol={sortcol}')

        if sort != 0:
            data.sort(key=lambda row: row[sortcol], reverse=sort<0)

        #print(f'Load {tbl}, sort={sort}, sortcol={sortcol}')

        conn.close()
        return data

    def update_data(self):
        print("Запрос ", self.entry.get()," выполнен")
        conn = sqlite3.connect('JewelryStore.db')
        cursor = conn.cursor()
        try:
            s = self.entry.get()
            if s == '': s = 'select * from materials'
            cursor.execute(s)
        except Exception as e:
            print(e.__repr__())
        else:
            self.entry.delete(0, 'end')
            self.data = cursor.fetchall()
            conn.close()
            
            self.create_gui()

            tree = self.AnswerTree
            tree.delete(*tree.get_children())
            for row_data in self.data:
                #print(row_data)
                #values = str(row_data)
                values = row_data
                tree.insert("", "end", values=values)

    def widget_tbl(self, tbl, cols, wcols, posx, posy, sort=0, sortcol=0):
        #print(f'{tbl} {cols} sort={sort} sortcol={sortcol}')

        for w in self.root.winfo_children():
            if hasattr(w, 'tag') and w.tag == tbl:
                w.destroy()
        
        lbl = tk.Label(text=f'below is the "{tbl}" table:', width=56)
        lbl.place(x=posx, y=posy)
        lbl.tag = tbl

        w = ttk.Treeview(self.root, columns=cols, show="headings")
        w.tag = tbl;

        if sort > 1: sort = -1

        for i, c in enumerate(cols):
            #print(f'{tbl} {c} sort={sort+1} sortcol={i}')

            #w.heading(c, text=c, command=lambda: self.widget_tbl(tbl, cols, wcols, posx, posy, sort=sort+1, sortcol=i) )

            if i == 0:
                w.heading(c, text=c, command=lambda: self.widget_tbl(tbl, cols, wcols, posx, posy, sort=sort+1, sortcol=0) )
            elif i == 1:
                w.heading(c, text=c, command=lambda: self.widget_tbl(tbl, cols, wcols, posx, posy, sort=sort+1, sortcol=1) )
            elif i == 2:
                w.heading(c, text=c, command=lambda: self.widget_tbl(tbl, cols, wcols, posx, posy, sort=sort+1, sortcol=2) )
            elif i == 3:
                w.heading(c, text=c, command=lambda: self.widget_tbl(tbl, cols, wcols, posx, posy, sort=sort+1, sortcol=3) )

            if wcols[i] < 0:
                w.column(c, anchor='e' if i==0 else 'w')
            else:
                w.column(c, anchor='e' if i==0 else 'w', width=wcols[i])
        
        w.place(x=posx, y=posy+20)

        data = self.db_table(tbl, sort, sortcol)
        for row in data:
            w.insert('', 'end', values=row)

        #print(w.xview(), w.yview())

    def create_gui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.entry = tk.Entry(foreground='black', justify='left', width=145)
        self.entry.place(x=450, y=20)

        tk.Label(text="Введите SQL запрос и нажмите на EXECUTE:", width=124).place(x=450, y=0)
        tk.Button(text='Execute!', command=self.update_data, width=123, height=2, bg="Grey", fg="White").place(x=450, y=40)

        self.widget_tbl('MATERIALS', ('id', 'name', 'sample'),                 (50, 175, 175),      10, 70)
        self.widget_tbl('PRODUCTS',  ('id', 'name', 'id_materials', 'cost'),   (50, -1, 80, 70),    10, 325)
        self.widget_tbl('BASKET',    ('id', 'id_customer', 'id_product'),      (50, 50, 300),      450, 325)
        self.widget_tbl('CUSTOMERS', ('id', 'name', 'INN'),                    (50, 220, 130),      10, 580)
        self.widget_tbl('ORDERS',    ('id', 'date', 'id_customer'),            (50, 300, 50),      450, 580)
        self.widget_tbl('PR_OR',     ('id', 'id_order', 'id_product', 'count'),(50, 130, 130, 90), 930, 580)

        self.AnswerTree = ttk.Treeview(self.root, columns=("Result"), show="headings")
        self.AnswerTree.heading("Result", text="Result")
        self.AnswerTree.column("Result", width=400)
        self.AnswerTree.place(x=450,y=80)


if __name__ == '__main__':
    root = tk.Tk()
    app = OKDataViewer(root)
    root.mainloop()

    #SELECT id FROM materials WHERE sample == 375