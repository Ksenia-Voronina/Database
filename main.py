from tkinter import *
from tkinter.ttk import *
import mysql.connector
from threading import Timer


# подключение базы данных
db = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="root",
  password="Ksu12345!",
  database="dm"
)

window = Tk()
window.geometry('800x500')
window['background'] = "lightblue"
window.title("Приемная комиссия")

# # создание объекта стилей
style = Style()

style.configure('TButton', 
                font = ('calibri', 15, 'bold'),
                foreground = 'darkblue')


############################################# Добавление абитуриента #########################################################

def add_entr():
    global window
    window.destroy()
    window=Tk()
    window.geometry('800x500')
    window['background'] = "lightblue"
    window.title("Добавление абитуриента в базу данных")

    style = Style()
 
    style.configure('TButton', 
                    font = ('calibri', 14, 'bold'),
                    foreground = 'darkblue')
    
    lbl_name = Label(window, text="Введите имя абитуриента")  
    lbl_name.place(relx=0.5, rely=0.05, anchor='center', width=400, height=20) 
    txt_name = Entry(window,width=20)  
    txt_name.place(relx=0.5, rely=0.10, anchor='center', width=400, height=20) 

    lbl_lname = Label(window, text="Введите фамилию абитуриента")  
    lbl_lname.place(relx=0.5, rely=0.20, anchor='center', width=400, height=20)  
    txt_lname = Entry(window,width=20)  
    txt_lname.place(relx=0.5, rely=0.25, anchor='center', width=400, height=20) 

    lbl_patr = Label(window, text="Введите отчество абитуриента")
    lbl_patr.place(relx=0.5, rely=0.35, anchor='center', width=400, height=20)   
    txt_patr = Entry(window,width=20)  
    txt_patr.place(relx=0.5, rely=0.40, anchor='center', width=400, height=20)

    lbl_num_ex = Label(window, text="Введите номер экзаменационного листа")
    lbl_num_ex.place(relx=0.5, rely=0.50, anchor='center', width=400, height=20)   
    txt_num_ex = Entry(window,width=20)  
    txt_num_ex.place(relx=0.5, rely=0.55, anchor='center', width=400, height=20)

    lbl_fac = Label(window, text="Введите факультет абитуриента")
    lbl_fac.place(relx=0.5, rely=0.65, anchor='center', width=400, height=20)   
    txt_fac = Entry(window,width=20)  
    txt_fac.place(relx=0.5, rely=0.70, anchor='center', width=400, height=20)
    
    lbl_dep = Label(window, text="Введите кафедру абитуриента")
    lbl_dep.place(relx=0.5, rely=0.80, anchor='center', width=400, height=20)   
    txt_dep = Entry(window,width=20)  
    txt_dep.place(relx=0.5, rely=0.85, anchor='center', width=400, height=20)

    def save_to_db():
        a = txt_name.get()
        b = txt_lname.get()
        c = txt_patr.get()
        d = txt_num_ex.get()
        e = txt_fac.get()
        f = txt_dep.get()

        mycursor = db.cursor()

        sql = """INSERT INTO entrant (name, lastname, patronymic, certificate_number, faculty, department, num_group, num_flow) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        val = (a, b, c, d, e, f, 1, 1)

        mycursor.execute(sql, val)
        
        db.commit()

        def close_window():
            window.destroy()

        window = Tk()
        window.title("Уведомление")
        window.geometry("300x100")

        label = Label(window, text="Данные успешно добавлены")
        label.pack(pady=20)

        timer = Timer(3.0, close_window)
        timer.start()

        clicked_adm()       

        window.mainloop()


    btn_add = Button(window, text="Добавить", command=save_to_db)  
    btn_add.place(relx=0.5, rely=0.95, anchor='center', width=200, height=40) 

############################################# Удаление абитуриента #########################################################

def del_entr():
    global window
    window.destroy()
    window=Tk()
    window.geometry('800x500')
    window['background'] = "lightblue"
    window.title("Удаление абитуриента из базы данных")

    style = Style()
 
    style.configure('TButton', 
                    font = ('calibri', 14, 'bold'),
                    foreground = 'darkblue')
    
    lbl_name = Label(window, text="Введите имя абитуриента")  
    lbl_name.place(relx=0.5, rely=0.2, anchor='center', width=400, height=20) 
    txt_name = Entry(window,width=20)  
    txt_name.place(relx=0.5, rely=0.25, anchor='center', width=400, height=20)  
    lbl_lname = Label(window, text="Введите фамилию абитуриента")  
    lbl_lname.place(relx=0.5, rely=0.35, anchor='center', width=400, height=20)  
    txt_lname = Entry(window,width=20)  
    txt_lname.place(relx=0.5, rely=0.4, anchor='center', width=400, height=20) 
    lbl_patr = Label(window, text="Введите отчество абитуриента")
    lbl_patr.place(relx=0.5, rely=0.50, anchor='center', width=400, height=20)   
    txt_patr = Entry(window,width=20)  
    txt_patr.place(relx=0.5, rely=0.55, anchor='center', width=400, height=20)
    
    def del_from_db():
        a = txt_name.get()
        b = txt_lname.get()
        c = txt_patr.get()

        mycursor = db.cursor()

        sql = "DELETE FROM entrant WHERE name = %s and lastname = %s and patronymic = %s"
        val = (a, b, c)
        
        mycursor.execute(sql, val)

        db.commit()

        def close_window():
            window.destroy()

        window = Tk()
        window.title("Уведомление")
        window.geometry("300x100")

        label = Label(window, text="Данные успешно удалены")
        label.pack(pady=20)

        timer = Timer(3.0, close_window)
        timer.start()

        clicked_adm()       

        window.mainloop()

    btn_del = Button(window, text="Удалить", command=del_from_db)  
    btn_del.place(relx=0.5, rely=0.7, anchor='center', width=200, height=40)
 

############################################# Изменение оценки #########################################################

def change_mark():
    global window
    window.destroy()
    window=Tk()
    window.geometry('800x500')
    window['background'] = "lightblue"
    window.title("Изменение оценки по предмету у абитуриента")

    style = Style()
 
    style.configure('TButton', 
                    font = ('calibri', 14, 'bold'),
                    foreground = 'darkblue')
    
    lbl_name = Label(window, text="Введите имя абитуриента")  
    lbl_name.place(relx=0.5, rely=0.1, anchor='center', width=400, height=20) 
    txt_name = Entry(window,width=20)  
    txt_name.place(relx=0.5, rely=0.15, anchor='center', width=400, height=20)  
    lbl_lname = Label(window, text="Введите фамилию абитуриента")  
    lbl_lname.place(relx=0.5, rely=0.25, anchor='center', width=400, height=20)  
    txt_lname = Entry(window,width=20)  
    txt_lname.place(relx=0.5, rely=0.3, anchor='center', width=400, height=20) 
    lbl_patr = Label(window, text="Введите отчество абитуриента")
    lbl_patr.place(relx=0.5, rely=0.4, anchor='center', width=400, height=20)   
    txt_patr = Entry(window,width=20)  
    txt_patr.place(relx=0.5, rely=0.45, anchor='center', width=400, height=20)
    lbl_sub = Label(window, text="Выберете предмет, по которому нужно изменить оценку у абитуриента")
    lbl_sub.place(relx=0.5, rely=0.55, anchor='center', width=400, height=20)   
    combo_sub = Combobox(window)  
    combo_sub['values'] = ("Математика", "Информатика", "Физика")  
    combo_sub.place(relx=0.5, rely=0.6, anchor='center', width=400, height=20)
    lbl_mark = Label(window, text="Выберете оценку, которую получил абитуриент")
    lbl_mark.place(relx=0.5, rely=0.7, anchor='center', width=400, height=20)   
    combo_mark = Combobox(window)  
    combo_mark['values'] = ("2", "3", "4", "5")  
    combo_mark.place(relx=0.5, rely=0.75, anchor='center', width=400, height=20) 

    def change_db():
        a = txt_name.get()
        b = txt_lname.get()
        c = txt_patr.get()
        d = combo_sub.get()
        e = combo_mark.get()

        mycursor = db.cursor()

        if d == "Математика":
            d = "maths"
        elif d == "Информатика":
            d = "informatics"
        elif d == "Физика":
            d = "physics"

        sql = f"UPDATE entrant SET {d} = %s WHERE name = %s and lastname = %s and patronymic = %s"
        val = (e, a, b, c)

        mycursor.execute(sql, val)
        
        db.commit()

        def close_window():
            window.destroy()

        window = Tk()
        window.title("Уведомление")
        window.geometry("300x100")

        label = Label(window, text="Данные успешно изменены")
        label.pack(pady=20)

        timer = Timer(3.0, close_window)
        timer.start()

        clicked_adm()       

        window.mainloop()  
    
    btn_change = Button(window, text="Изменить оценку", command=change_db)  
    btn_change.place(relx=0.5, rely=0.9, anchor='center', width=200, height=40) 

############################################# Возвращение в главное меню #########################################################

def menu():
    global window
    window.destroy()
    window=Tk()
    window.geometry('800x500')
    window['background'] = "lightblue"

    style = Style()
 
    style.configure('TButton', 
                    font = ('calibri', 14, 'bold'),
                    foreground = 'darkblue')


    # кнопка для входа администратора
    btn_adm = Button(window, text="Войти как администратор", command=clicked_adm)
    btn_adm.place(relx=0.5, rely=0.4, anchor='center', width=400, height=40)

    # кнопка для входа сотрудника
    btn_user = Button(window, text="Войти как сотрудник приемной комиссии", command=clicked_user)
    btn_user.place(relx=0.5, rely=0.5, anchor='center', width=400, height=40)

############################################# Администратор #########################################################

def clicked_adm():
    global window
    window.destroy()
    window=Tk()
    window.geometry('800x500')
    window['background'] = "lightblue"
    window.title("Администратор")

    style = Style()
 
    style.configure('TButton', 
                    font = ('calibri', 14, 'bold'),
                    foreground = 'darkblue')

    # кнопка добавления абитуриента
    btn_add_entr = Button(window, text="Добавить нового абитуриента", command=add_entr)
    btn_add_entr.place(relx=0.5, rely=0.3, anchor='center', width=400, height=40)

    # кнопка удаления абитуриента
    btn_del_entr = Button(window, text="Удалить нового абитуриента", command=del_entr)
    btn_del_entr.place(relx=0.5, rely=0.4, anchor='center', width=400, height=40)

    # кнопка для изменения оценки абитуриента
    btn_change_mark = Button(window, text="Изменение оценки абитуриента по предмету", command=change_mark)
    btn_change_mark.place(relx=0.5, rely=0.5, anchor='center', width=400, height=40)

    # кнопка возврата в главное меню
    btn_menu = Button(window, text="Назад", command=menu)
    btn_menu.place(relx=0.5, rely=0.7, anchor='center', width=200, height=40)

############################################# Вывод списка абитуриентов #########################################################

def list_entr():
    global window
    window.destroy()
    window=Tk()
    window.geometry('800x500')
    window['background'] = "lightblue"
    window.title("Список абитуриентов")

    style = Style()
 
    style.configure('TButton', 
                    font = ('calibri', 14, 'bold'),
                    foreground = 'darkblue')

    lbl_fac = Label(window, text="Введите нужный факультет")  
    lbl_fac.place(relx=0.5, rely=0.35, anchor='center', width=400, height=20)
    txt_fac = Entry(window,width=20)  
    txt_fac.place(relx=0.5, rely=0.4, anchor='center', width=400, height=20)

    def print_list_fac():
        a = txt_fac.get()

        mycursor = db.cursor()

        sql = """SELECT name, lastname, patronymic, department 
                FROM entrant WHERE faculty = %s"""
        val = (a,)

        mycursor.execute(sql, val)

        columns = [desc[0] for desc in mycursor.description]
        rows = mycursor.fetchall()

        db.commit()

        new_window = Tk()
        new_window.title("Список абитуриентов")
        new_window.geometry("800x500")

        tree = Treeview(new_window)
        tree.pack(side=LEFT, fill=BOTH, expand=True)

        tree["columns"] = columns
        tree["show"] = "headings"
    
        for col in columns:
            tree.column(col, anchor='center', width=len(col)*15)
            tree.heading(col, text=col, anchor='center')
        
        for row in rows:
            tree.insert("", "end", values=row)

        scrollbar = Scrollbar(new_window, orient="horizontal", command=tree.xview)
        tree.configure(xscrollcommand=scrollbar.set)

        new_window.mainloop()
    
    btn_list = Button(window, text="Назад", command=clicked_user)  
    btn_list.place(relx=0.35, rely=0.6, anchor='center', width=200, height=40)    
    btn_list = Button(window, text="Вывести список", command=print_list_fac)  
    btn_list.place(relx=0.65, rely=0.6, anchor='center', width=200, height=40)

############################################# Вывод оценки абитуриента #########################################################

def mark_entr():
    global window
    window.destroy()
    window=Tk()
    window.geometry('800x500')
    window['background'] = "lightblue"
    window.title("Оценки абитуриента")

    style = Style()
 
    style.configure('TButton', 
                    font = ('calibri', 14, 'bold'),
                    foreground = 'darkblue')
    
    lbl_name = Label(window, text="Введите имя абитуриента")  
    lbl_name.place(relx=0.5, rely=0.2, anchor='center', width=400, height=20)
    txt_name = Entry(window,width=20)  
    txt_name.place(relx=0.5, rely=0.25, anchor='center', width=400, height=20)

    lbl_lname = Label(window, text="Введите фамилию абитуриента")  
    lbl_lname.place(relx=0.5, rely=0.35, anchor='center', width=400, height=20)  
    txt_lname = Entry(window,width=20)  
    txt_lname.place(relx=0.5, rely=0.4, anchor='center', width=400, height=20)

    lbl_patr = Label(window, text="Введите отчество абитуриента")
    lbl_patr.place(relx=0.5, rely=0.5, anchor='center', width=400, height=20)   
    txt_patr = Entry(window,width=20)  
    txt_patr.place(relx=0.5, rely=0.55, anchor='center', width=400, height=20)

    def print_mark():
        a = txt_name.get()
        b = txt_lname.get()
        c = txt_patr.get()

        mycursor = db.cursor()

        sql = """SELECT name, lastname, patronymic, department, maths, informatics, physics 
                FROM entrant 
                WHERE name = %s and lastname = %s and patronymic = %s"""
        val = (a, b, c)

        mycursor.execute(sql, val)

        columns = [desc[0] for desc in mycursor.description]
        rows = mycursor.fetchall()

        db.commit()

        new_window = Tk()
        new_window.title("Список оценок")
        new_window.geometry("800x500")

        tree = Treeview(new_window)
        tree.pack(side=LEFT, fill=BOTH, expand=True)

        tree["columns"] = columns
        tree["show"] = "headings"
    
        for col in columns:
            tree.column(col, anchor='center', width=len(col)*10)
            tree.heading(col, text=col, anchor='center')
        
        for row in rows:
            tree.insert("", "end", values=row)

        scrollbar = Scrollbar(new_window, orient="horizontal", command=tree.xview)
        tree.configure(xscrollcommand=scrollbar.set)

        new_window.mainloop()


    btn_list = Button(window, text="Назад", command=clicked_user)  
    btn_list.place(relx=0.35, rely=0.75, anchor='center', width=200, height=40)    
    btn_list = Button(window, text="Вывести список", command=print_mark)  
    btn_list.place(relx=0.65, rely=0.75, anchor='center', width=200, height=40)

############################################# Вывод даты консультации и экзамена для абитуриента #########################################################

def cons_exam():
    global window
    window.destroy()
    window=Tk()
    window.geometry('800x500')
    window['background'] = "lightblue"
    window.title("Даты консультаций и экзаменов абитуриента")

    style = Style()
 
    style.configure('TButton', 
                    font = ('calibri', 14, 'bold'),
                    foreground = 'darkblue')
    
    lbl_name = Label(window, text="Введите имя абитуриента")  
    lbl_name.place(relx=0.5, rely=0.1, anchor='center', width=400, height=20)
    txt_name = Entry(window,width=20)  
    txt_name.place(relx=0.5, rely=0.15, anchor='center', width=400, height=20)

    lbl_lname = Label(window, text="Введите фамилию абитуриента")  
    lbl_lname.place(relx=0.5, rely=0.25, anchor='center', width=400, height=20)  
    txt_lname = Entry(window,width=20)  
    txt_lname.place(relx=0.5, rely=0.3, anchor='center', width=400, height=20) 

    lbl_patr = Label(window, text="Введите отчество абитуриента")
    lbl_patr.place(relx=0.5, rely=0.4, anchor='center', width=400, height=20)   
    txt_patr = Entry(window,width=20)  
    txt_patr.place(relx=0.5, rely=0.45, anchor='center', width=400, height=20)

    lbl_sub = Label(window, text="Выберете предмет")  
    lbl_sub.place(relx=0.5, rely=0.55, anchor='center', width=400, height=20)
    combo_sub = Combobox(window)  
    combo_sub['values'] = ("Математика", "Информатика", "Физика")  
    combo_sub.place(relx=0.5, rely=0.6, anchor='center', width=400, height=20)


    def print_exam():
        a = txt_name.get()
        b = txt_lname.get()
        c = txt_patr.get()
        d = combo_sub.get()

        if d == "Математика":
            d = "maths"
        elif d == "Информатика":
            d = "informatics"
        elif d == "Физика":
            d = "physics"

        mycursor = db.cursor()

        sql = """SELECT entrant.name, entrant.lastname, entrant.patronymic, exam.name_exam, exam.date_cons, exam.date_exam 
                FROM entrant 
                JOIN exam ON entrant.num_flow = exam.num_flow 
                WHERE entrant.name = %s and exam.name_exam = %s"""
        val = (a, b)

        mycursor.execute(sql, val)

        columns = [desc[0] for desc in mycursor.description]
        rows = mycursor.fetchall()

        db.commit()

        new_window = Tk()
        new_window.title("Список консультаций и экзаменов у абитуриентов")
        new_window.geometry("800x500")

        tree = Treeview(new_window)
        tree.pack(side=LEFT, fill=BOTH, expand=True)

        tree["columns"] = columns
        tree["show"] = "headings"
    
        for col in columns:
            tree.column(col, anchor='center', width=len(col)*10)
            tree.heading(col, text=col, anchor='center')
        
        for row in rows:
            tree.insert("", "end", values=row)

        scrollbar = Scrollbar(new_window, orient="horizontal", command=tree.xview)
        tree.configure(xscrollcommand=scrollbar.set)

        new_window.mainloop()


    btn_list = Button(window, text="Назад", command=clicked_user)  
    btn_list.place(relx=0.35, rely=0.75, anchor='center', width=200, height=40)    
    btn_list = Button(window, text="Вывести список", command=print_exam)  
    btn_list.place(relx=0.65, rely=0.75, anchor='center', width=200, height=40)

############################################# Вывод номеров аудиторий для экзаменов у группы #########################################################

def num_audit():
    global window
    window.destroy()
    window=Tk()
    window.geometry('800x500')
    window['background'] = "lightblue"
    window.title("Номера аудиторий для экзаменов")

    style = Style()
 
    style.configure('TButton', 
                    font = ('calibri', 14, 'bold'),
                    foreground = 'darkblue')
    
    lbl_group = Label(window, text="Введите номер группы")  
    lbl_group.place(relx=0.5, rely=0.3, anchor='center', width=400, height=20)
    txt_group = Entry(window,width=20)  
    txt_group.place(relx=0.5, rely=0.35, anchor='center', width=400, height=20)

    def print_aud():
        a = txt_group.get()

        mycursor = db.cursor()

        sql = """SELECT DISTINCT entrant.num_group, exam.name_exam, exam.auditorium 
                FROM exam 
                JOIN entrant ON entrant.num_flow = exam.num_flow 
                WHERE entrant.num_group = %s"""
        val = (a,)

        mycursor.execute(sql, val)

        columns = [desc[0] for desc in mycursor.description]
        rows = mycursor.fetchall()

        db.commit()

        new_window = Tk()
        new_window.title("Список номеров аудиторий")
        new_window.geometry("800x500")

        tree = Treeview(new_window)
        tree.pack(side=LEFT, fill=BOTH, expand=True)

        tree["columns"] = columns
        tree["show"] = "headings"
    
        for col in columns:
            tree.column(col, anchor='center', width=len(col)*10)
            tree.heading(col, text=col, anchor='center')
        
        for row in rows:
            tree.insert("", "end", values=row)

        scrollbar = Scrollbar(new_window, orient="horizontal", command=tree.xview)
        tree.configure(xscrollcommand=scrollbar.set)

        new_window.mainloop()


    btn_list = Button(window, text="Назад", command=clicked_user)  
    btn_list.place(relx=0.35, rely=0.55, anchor='center', width=200, height=40)    
    btn_list = Button(window, text="Вывести список", command=print_aud)  
    btn_list.place(relx=0.65, rely=0.55, anchor='center', width=200, height=40)

############################################# Вывод списка групп в аудитории #########################################################

def list_audit():
    global window
    window.destroy()
    window=Tk()
    window.geometry('800x500')
    window['background'] = "lightblue"
    window.title("Cписок групп в аудитории")

    style = Style()
 
    style.configure('TButton', 
                    font = ('calibri', 14, 'bold'),
                    foreground = 'darkblue')
    
    lbl_audit = Label(window, text="Введите номер аудитории")
    lbl_audit.place(relx=0.5, rely=0.3, anchor='center', width=400, height=20)
    txt_audit = Entry(window,width=20)  
    txt_audit.place(relx=0.5, rely=0.35, anchor='center', width=400, height=20)

    lbl_time = Label(window, text="Введите дату и время")
    lbl_time.place(relx=0.5, rely=0.45, anchor='center', width=400, height=20)
    txt_time = Entry(window,width=20)  
    txt_time.place(relx=0.5, rely=0.5, anchor='center', width=400, height=20)

    def print_group():
        a = txt_audit.get()
        b = txt_time.get()

        mycursor = db.cursor()

        sql = """SELECT DISTINCT entrant.num_group, exam.num_flow, exam.auditorium 
                FROM exam 
                JOIN entrant ON entrant.num_flow = exam.num_flow 
                WHERE exam.auditorium = %s and (exam.date_cons = %s or exam.date_exam = %s)"""
        val = (a, b, b)

        mycursor.execute(sql, val)

        columns = [desc[0] for desc in mycursor.description]
        rows = mycursor.fetchall()

        db.commit()

        new_window = Tk()
        new_window.title("Список групп в аудитории")
        new_window.geometry("800x500")

        tree = Treeview(new_window)
        tree.pack(side=LEFT, fill=BOTH, expand=True)

        tree["columns"] = columns
        tree["show"] = "headings"
    
        for col in columns:
            tree.column(col, anchor='center', width=len(col)*10)
            tree.heading(col, text=col, anchor='center')
        
        for row in rows:
            tree.insert("", "end", values=row)

        scrollbar = Scrollbar(new_window, orient="horizontal", command=tree.xview)
        tree.configure(xscrollcommand=scrollbar.set)

        new_window.mainloop()


    btn_list = Button(window, text="Назад", command=clicked_user)  
    btn_list.place(relx=0.35, rely=0.7, anchor='center', width=200, height=40)    
    btn_list = Button(window, text="Вывести список", command=print_group)  
    btn_list.place(relx=0.65, rely=0.7, anchor='center', width=200, height=40)

############################################# Сотрудник #########################################################

def clicked_user():

    global window
    window.destroy()
    window=Tk()
    window.geometry('800x500')
    window['background'] = "lightblue"
    window.title("Сотрудник")

    style = Style()
 
    style.configure('TButton', 
                    font = ('calibri', 14, 'bold'),
                    foreground = 'darkblue')
    
    # кнопка для списка абитуриентов
    btn_list_entr = Button(window, text="Вывести список абитуриентов", command=list_entr)
    btn_list_entr.place(relx=0.5, rely=0.2, anchor='center', width=400, height=40)

    # кнопка для оценок абитуриента
    btn_mark_entr = Button(window, text="Вывести оценки абитуриента", command=mark_entr)
    btn_mark_entr.place(relx=0.5, rely=0.3, anchor='center', width=400, height=40)

    # кнопка для даты консультации и экзамена для абитуриента по данному предмету
    btn_cons_exam = Button(window, text="Вывести даты консультации и экзамена для абитуриента", command=cons_exam)
    btn_cons_exam.place(relx=0.5, rely=0.4, anchor='center', width=400, height=40)

    # кнопка для номера аудиторий, где будут экзамены у заданной группы
    btn_num_audit = Button(window, text="Вывести номера аудиторий для экзаменов у группы", command=num_audit)
    btn_num_audit.place(relx=0.5, rely=0.5, anchor='center', width=400, height=40)

    # кнопка для списка групп в аудитории
    btn_list_audit = Button(window, text="Вывести список групп в аудитории", command=list_audit)
    btn_list_audit.place(relx=0.5, rely=0.6, anchor='center', width=400, height=40)

    # кнопка возврата в главное меню
    btn_menu = Button(window, text="Назад", command=menu)
    btn_menu.place(relx=0.5, rely=0.8, anchor='center', width=200, height=40)

############################################# Главное меню #########################################################

# кнопка для входа администратора
btn_adm = Button(window, text="Войти как администратор", command=clicked_adm)
btn_adm.place(relx=0.5, rely=0.4, anchor='center', width=400, height=40)


# кнопка для входа сотрудника
btn_user = Button(window, text="Войти как сотрудник приемной комиссии", command=clicked_user)
btn_user.place(relx=0.5, rely=0.5, anchor='center', width=400, height=40)

window.mainloop()
