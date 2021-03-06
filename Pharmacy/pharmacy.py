# Python Packages required
# Python --Version => 3.9
# --------------------------------- ----------
# Package                           Version
# --------------------------------- ----------
# cx-Oracle                         8.3.0

# docx2pdf                          0.1.7
# docxtpl                           0.15.2
# pypng                             0.0.21
# PyQt5                             5.15.4
# pyqt5-tools                       5.15.4.3.2
# PySide2                           5.15.2
# qrcode                            7.3.1
# qt-material                       2.8.15
# wikipedia                         1.4.0
# xlwt                              1.3.0
# ---------------------------------------------
# Syntax : pip install "Package_name"
# ---------------------------------------------
import sys
import os

from PySide2 import *
from PySide2 import QtWidgets

from PyQt5.Qt import Qt
from PySide2.QtWidgets import QMessageBox

from ui_pharmacy import *

import wikipedia as wk
from wikipedia.wikipedia import search

from qt_material import *

from datetime import datetime, timedelta

import pyqrcode

import cx_Oracle

from docxtpl import DocxTemplate, InlineImage
from docx.shared import Cm  # , Inches, Mm, Emu

from docx2pdf import convert

import xlwt
from xlwt import Workbook


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        title = "Pharmacy"
        self.setWindowTitle(title)

        apply_stylesheet(app, theme='dark_cyan.xml')

        #######

        #######
        # logout btn
        self.ui.logout_btn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.login))
        #######

        self.ui.login_btn.clicked.connect(self.login)

        # Nagavation menu
        self.ui.dashboard_btn.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.Dashboard))
        # self.dashboard()

        self.ui.description_btn.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.Description))

        self.ui.inventory_btn.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.Inventory))

        self.ui.customer_btn.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.Customer))

        self.ui.purchase_btn.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.Purchase))

        self.ui.report_btn.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.Report))
        # self.data_insert()
        #######

        #######
        # Inventory menu
        self.ui.insert_btn.clicked.connect(
            lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.Insert))
        # self.data_insert()

        self.ui.view_btn.clicked.connect(
            lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.View))

        self.ui.update_btn.clicked.connect(
            lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.Update))

        # self.data_delete()
        #######

        #######
        # Dash Board
        self.ui.stock_btn.clicked.connect(self.dashboard)
        self.ui.customer_btn_2.clicked.connect(self.dashboard_customer)
        self.ui.dashboard_clear_btn.clicked.connect(self.dashboard_clear)
        self.ui.sale_btn.clicked.connect(self.dashboard_sales)
        self.ui.Download.clicked.connect(self.print_excel)
        #######
        #######
        # Description
        self.ui.Search_btn.clicked.connect(self.description_)
        #######
        #######
        # Insert a value Trigger
        self.ui.m_Add.clicked.connect(self.data_insert)
        self.ui.m_show.clicked.connect(self.data_display)
        #######
        #######
        # view view value trigger
        self.ui.view_search_btn.clicked.connect(self.data_view)
        self.ui.view_clear_btn.clicked.connect(self.view_clear)

        #######
        # Report value trigger
        self.ui.report_show_btn.clicked.connect(self.report_show)

        #######
        # update value trigger
        self.ui.update_search_btn.clicked.connect(self.update_data_view)
        self.ui.confirm_update_btn.clicked.connect(self.update_data)
        ######
        # Customer value trigger
        self.ui.c_new_id_btn.clicked.connect(self.customer_data)
        self.ui.c_add_btn.clicked.connect(self.customer_add_data)
        self.ui.c_show_btn.clicked.connect(self.order_data_display)
        self.ui.pushButton_2.clicked.connect(self.print_recipt)
        ######
        ######
        # Purchase Menu
        self.ui.purchase_historybtn.clicked.connect(
            lambda: self.ui.stackedWidget_4.setCurrentWidget(self.ui.purchase_history))
        self.ui.customer_deletebtn.clicked.connect(
            lambda: self.ui.stackedWidget_4.setCurrentWidget(self.ui.purchase_delete))
        self.ui.Customer_search_btn.clicked.connect(
            lambda: self.ui.stackedWidget_4.setCurrentWidget(self.ui.Customer_search_page))
        ######
        # Purchase value trigger
        self.ui.purchase_history_show_btn.clicked.connect(
            self.purchase_history)
        self.ui.p_serch_btn.clicked.connect(self.search_customer)
        self.ui.customer_search_btn.clicked.connect(self.delete_customer_data)
        self.ui.customer_confirm_delete_btn.clicked.connect(
            self.confirm_delete)

        self.ui.pushButton_3.clicked.connect(self.update_clear)
        self.ui.customer_clear.clicked.connect(self.customerclear)

        ######
        # insert_table size
        self.ui.insert_table.setColumnWidth(0, 200)
        self.ui.insert_table.setColumnWidth(1, 300)
        self.ui.insert_table.setColumnWidth(2, 200)
        self.ui.insert_table.setColumnWidth(3, 200)
        self.ui.insert_table.setColumnWidth(4, 200)
        self.ui.insert_table.setColumnWidth(5, 200)
        self.ui.insert_table.setColumnWidth(6, 200)
        self.ui.insert_table.setColumnWidth(7, 200)

        # dashboard_table size
        self.ui.dashboard_table.setColumnWidth(0, 200)
        self.ui.dashboard_table.setColumnWidth(1, 300)
        self.ui.dashboard_table.setColumnWidth(2, 200)
        self.ui.dashboard_table.setColumnWidth(3, 200)
        self.ui.dashboard_table.setColumnWidth(4, 200)
        self.ui.dashboard_table.setColumnWidth(5, 200)
        self.ui.dashboard_table.setColumnWidth(6, 200)
        self.ui.dashboard_table.setColumnWidth(7, 200)
        # customer_table size
        self.ui.customer_table.setColumnWidth(0, 100)
        self.ui.customer_table.setColumnWidth(1, 300)
        self.ui.customer_table.setColumnWidth(2, 200)
        self.ui.customer_table.setColumnWidth(3, 200)

        # purchase_customer_table size
        self.ui.purchase_customer_table.setColumnWidth(0, 100)
        self.ui.purchase_customer_table.setColumnWidth(1, 300)
        self.ui.purchase_customer_table.setColumnWidth(2, 200)
        self.ui.purchase_customer_table.setColumnWidth(3, 200)

        # purchase_history_table size
        self.ui.Purchase_history_table.setColumnWidth(0, 100)
        self.ui.Purchase_history_table.setColumnWidth(1, 250)
        for i in range(2, 7):
            self.ui.Purchase_history_table.setColumnWidth(i, 200)

        # purchase_history_table size
        self.ui.Purchase_history_table_2.setColumnWidth(0, 100)
        self.ui.Purchase_history_table_2.setColumnWidth(1, 250)
        for i in range(2, 7):
            self.ui.Purchase_history_table_2.setColumnWidth(i, 200)

        # purchase_delete_table size
        self.ui.purchase_delete_table.setColumnWidth(0, 100)
        self.ui.purchase_delete_table.setColumnWidth(1, 250)
        for i in range(2, 7):
            self.ui.purchase_delete_table.setColumnWidth(i, 200)
        #######
        self.show()

    def update_clear(self):
        self.ui.update_search.clear()
        self.ui.uname2.clear()
        self.ui.u_cprice2.clear()
        self.ui.u_sprice2.clear()
        self.ui.u_qty2.clear()

    def login(self):
        user = 'admin'
        passw = 'user123'
        if self.ui.email.text() == user and self.ui.password.text() == passw:
            # login window
            self.ui.login_btn.clicked.connect(
                lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.main))
        #######
        else:
            self.popup("Invalid Credentials")

    def keyPressEvent(self, event):

        # print(event.key())
        if event.key() == (Qt.Key_Control and Qt.Key_F):
            self.view_clear()
            self.update_clear()
            self.customerclear()
            # self.customer_list()
        elif event.key() == 82:
            apply_stylesheet(app, theme='dark_red.xml')
        elif event.key() == 67:
            apply_stylesheet(app, theme='dark_cyan.xml')
        elif event.key() == 89:
            apply_stylesheet(app, theme='dark_yellow.xml')
        elif event.key() == 84:
            apply_stylesheet(app, theme='dark_teal.xml')
        elif event.key() == 76:
            apply_stylesheet(app, theme='light_red.xml')
        elif event.key() == 79:
            self.open_recipt()
        elif event.key() == 88:
            self.open_recipt_excel()
        else:
            apply_stylesheet(app, theme='dark_teal.xml')

    def customer_list(self):
        c_rows = self.SQL_Query_retrive("select c_id , C_PHNO from customer")
        id = []
        phone = []
        for tup in c_rows:
            id.append(tup[0])
            phone.append(tup[1])
        return id, phone

    def medicine_list(self):
        m_rows = self.SQL_Query_retrive("select id from MEDICINE")
        id = []
        for tup in m_rows:
            id.append(tup[0])
        return id

    def delete_customer_data(self, n):
        c_id = self.ui.customer_search.text()
        if c_id.isdigit():
            rows = self.SQL_Query_retrive(
                f"select * from customer where c_id={int(c_id)} ")
            if len(rows) != 0 or n:
                rowcount = len(rows)
                self.ui.purchase_delete_table.setRowCount(rowcount)
                tablerow = 0
                rows.sort(key=lambda lst: lst[0], reverse=False)
                ########
                for tup in rows:
                    i = 0
                    for col in tup:
                        self.ui.purchase_delete_table.setItem(
                            tablerow, i, QtWidgets.QTableWidgetItem(str(tup[i])))
                        i += 1
                    tablerow += 1
            else:
                self.popup(f"{c_id} : Customer Not Found ")
        else:
            self.popup(f"{c_id} : Invalid Input")

    def confirm_delete(self):
        c_id = self.ui.customer_search.text()
        self.SQL_Query_delete(f"delete from customer where c_id = {int(c_id)}")

        self.delete_customer_data(True)

    def search_customer(self):
        item = self.ui.p_item.currentText()
        lst = self.customer_list()
        if item == 'ID':
            value = self.ui.p_search.text()
            if value.isdigit():
                if int(value) in lst[0]:
                    o_rows = self.SQL_Query_retrive(
                        f"select * from orders where c_id = {int(value)}")
                    c_rows = self.SQL_Query_retrive(
                        f"select * from customer where c_id={int(value)} ")
                else:
                    self.popup(f"{value} : Not Found")
            else:
                self.popup(f"{value} : Invalid Input")

        else:
            value = self.ui.p_search.text()
            if value.isdigit():
                if int(value) in lst[1]:
                    c_id = self.SQL_Query_retrive(
                        f"select c_id from customer where c_phno = {int(value)} ")
                    o_rows = self.SQL_Query_retrive(
                        f"select * from orders where c_id = {c_id[0][0]}")
                    c_rows = self.SQL_Query_retrive(
                        f"select * from customer where c_id={c_id[0][0]} ")
                else:
                    self.popup(f"{value} : Not Found")
            else:
                self.popup(f"{value} : Invalid Input")

        self.ui.p_id.setText(str(c_rows[0][0]))
        self.ui.p_name.setText(str(c_rows[0][1]))
        self.ui.p_contact.setText(str(c_rows[0][2]))
        self.ui.p_gender.setText(str(c_rows[0][3]))
        self.ui.p_cost.setText(str(c_rows[0][4]))
        self.ui.p_date.setText(str(c_rows[0][5]))
        self.ui.p_qty.setText(str(c_rows[0][6]))

        rowcount = len(o_rows)
        self.ui.purchase_customer_table.setRowCount(rowcount)
        tablerow = 0
        for tup in o_rows:
            i = 0
            med = self.SQL_Query_retrive(
                f"select name ,s_price from MEDICINE where id = {tup[2]}")
            med_name = med[0][0]
            med_cost = med[0][1]
            self.ui.purchase_customer_table.setItem(
                tablerow, 0, QtWidgets.QTableWidgetItem(str(tup[0])))
            self.ui.purchase_customer_table.setItem(
                tablerow, 1, QtWidgets.QTableWidgetItem(str(med_name)))
            self.ui.purchase_customer_table.setItem(
                tablerow, 2, QtWidgets.QTableWidgetItem(str(med_cost)))
            self.ui.purchase_customer_table.setItem(
                tablerow, 3, QtWidgets.QTableWidgetItem(str(tup[1])))

            tablerow += 1

    def purchase_history(self):
        rows = self.SQL_Query_retrive(f"select * from customer")
        rowcount = len(rows)
        self.ui.Purchase_history_table.setRowCount(rowcount)
        tablerow = 0
        rows.sort(key=lambda lst: lst[0], reverse=False)
        ########
        for tup in rows:
            i = 0
            for col in tup:
                self.ui.Purchase_history_table.setItem(
                    tablerow, i, QtWidgets.QTableWidgetItem(str(tup[i])))
                i += 1
            tablerow += 1

    def dashboard_customer(self):
        cust_rows = self.SQL_Query_retrive(f"select * from customer")
        self.ui.label_17.setText(str(len(cust_rows)))
        self.ui.label_33.setText(str(len(cust_rows)))

    def date_time(self):
        current_time = datetime.now()
        today = f"{current_time.day}-{current_time.month}-{current_time.year}"
        return today

    def popup(self, text):
        QMessageBox.warning(self, "WARNING", f"{text}\t")

    def dashboard(self):

        rows = self.SQL_Query_retrive("select * from MEDICINE")
        sum = 0
        row_count = 0
        for row in rows:
            row_count += 1
            sum = sum + row[6]

        self.ui.d_stock.setText(str(sum))
        self.ui.d_product.setText(str(row_count))

        self.ui.dashboard_table.setRowCount(row_count)
        tablerow = 0
        # used to sort database rows in desinding order

        rows.sort(key=lambda lst: lst[0], reverse=True)

        ########
        for tup in rows:
            i = 0
            for col in tup:
                self.ui.dashboard_table.setItem(
                    tablerow, i, QtWidgets.QTableWidgetItem(str(tup[i])))
                i += 1
            tablerow += 1

    def dashboard_clear(self):
        self.ui.label_17.setText('N/A')
        self.ui.label_20.setText('N/A')
        self.ui.d_stock.setText('N/A')
        # self.ui.dashboard_table.clear()
        self.ui.d_product.setText('N/A')
        self.ui.label_33.setText('N/A')
        self.ui.label_35.setText('N/A')
        self.ui.label_36.setText('N/A')

    def dashboard_sales(self):
        ms_rows = self.SQL_Query_retrive(
            f"select id,s_price,c_price,qty,(c_price * qty) c_price,(s_price * qty) s_price from MEDICINE_DATA")
        o_rows = self.SQL_Query_retrive(f"select sum(t_price) from orders")
        cost_value = 0
        sale_value = 0
        for tup in ms_rows:
            cost_value = cost_value + tup[4]
            sale_value = sale_value + tup[5]
        self.ui.label_36.setText(str(cost_value))
        self.ui.label_35.setText(str(sale_value))
        self.ui.label_20.setText(str(o_rows[0][0]))

    def SQL_Query_insert(self, query):
        try:
            con = cx_Oracle.connect('PHARMACY/user123@localhost')
            print(con.version)
            cursor = con.cursor()
            cursor.execute(query)

            print("inserted successfully")

            con.commit()

        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)

        finally:
            if cursor:
                cursor.close()
            if con:
                con.close()

    def SQL_Query_delete(self, query):
        try:
            con = cx_Oracle.connect('PHARMACY/user123@localhost')
            print(con.version)
            cursor = con.cursor()
            cursor.execute(query)

            print("deleted successfully")

            con.commit()

        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)

        finally:
            if cursor:
                cursor.close()
            if con:
                con.close()

    def SQL_Query_retrive(self, query):
        try:
            con = cx_Oracle.connect('PHARMACY/user123@localhost')
            print(con.version)
            cursor = con.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            print("retrived successfully")
            return rows

        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)

        finally:
            if cursor:
                cursor.close()
            if con:
                con.close()

    def SQL_Query_update(self, query):
        try:
            con = cx_Oracle.connect('PHARMACY/user123@localhost')
            print(con.version)
            cursor = con.cursor()
            cursor.execute(query)
            print("updated successfully")
            con.commit()

        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)

        finally:
            if cursor:
                cursor.close()
            if con:
                con.close()

    def data_display(self):
        rows = self.SQL_Query_retrive("select * from MEDICINE")
        max_id = [1000]
        row_count = 0
        for row in rows:
            ls = list(row)
            max_id.append(ls[0])
            row_count += 1

        self.ui.insert_table.setRowCount(row_count)
        tablerow = 0
        # used to sort database rows in desinding order
        rows.sort(key=lambda lst: lst[0], reverse=True)
        ########
        for tup in rows:
            i = 0
            for col in tup:
                self.ui.insert_table.setItem(
                    tablerow, i, QtWidgets.QTableWidgetItem(str(tup[i])))
                i += 1
            tablerow += 1

    def data_insert(self):

        rows = self.SQL_Query_retrive(
            "select * from medicine ")
        max_id = [1000]
        row_count = 0
        for row in rows:
            ls = list(row)
            max_id.append(ls[0])
            row_count += 1

        self.ui.insert_table.setRowCount(row_count)
        tablerow = 0
        for tup in rows:
            i = 0
            for col in tup:
                self.ui.insert_table.setItem(
                    tablerow, i, QtWidgets.QTableWidgetItem(str(tup[i])))
                i += 1
            tablerow += 1

        count = max(max_id)+1

        name = self.ui.m_name.text()
        cost_price = self.ui.m_cost.text()
        sell_price = self.ui.m_sell.text()
        qty = self.ui.m_Qty.text()
        MFD = self.ui.m_mfd.text()
        b_f = self.ui.best_before.text()
        if cost_price.isdigit() and int(cost_price) > 0 and sell_price.isdigit() and int(sell_price) > 0 and qty.isdigit() and int(qty) > 0 and b_f.isdigit() and int(b_f) > 0:
            mfd = datetime.strptime(MFD, "%d-%m-%Y")
            exd = str(mfd+timedelta(days=int(b_f)*30)).split()[0]
            exd_month = exd[5:7]
            exd_day = exd[8:10]
            exd_year = exd[0:4]
            exd = f"{exd_day}-{exd_month}-{exd_year}"
            self.ui.Id.setText(str(count))
            self.ui.m_Exd.setText(str(exd))
            # list creation
            data = [count, name, cost_price, sell_price, MFD, exd, qty]
            self.SQL_Query_insert(
                f"insert into MEDICINE values({data[0]},'{data[1]}',{data[2]},{data[3]},'{data[4]}','{data[5]}',{data[6]})")
            self.SQL_Query_insert(
                f"insert into MEDICINE_DATA values({data[0]},'{data[1]}',{data[2]},{data[3]},'{data[4]}','{data[5]}',{data[6]})")
            self.data_display()
        else:
            self.popup(f"Invalid values")

    def data_view(self):
        search_text = self.ui.view_search.text()
        m_id = self.medicine_list()
        if int(search_text) in m_id:
            rows = self.SQL_Query_retrive(
                f"select * from MEDICINE where id = {search_text}")
            for tup in rows:
                self.ui.view_id.setText(str(tup[0]))
                self.ui.view_name.setText(str(tup[1]))
                self.ui.view_cost.setText(str(tup[2]))
                self.ui.view_sell.setText(str(tup[3]))
                self.ui.view_mfd.setText(str(tup[4]))
                self.ui.view_exd.setText(str(tup[5]))
                self.ui.view_qty.setText(str(tup[6]))
        else:
            self.popup(f"{search_text} : Not Found")

    def view_clear(self):
        self.ui.view_search.clear()
        self.ui.view_id.clear()
        self.ui.view_name.clear()
        self.ui.view_cost.clear()
        self.ui.view_sell.clear()
        self.ui.view_mfd.clear()
        self.ui.view_exd.clear()
        self.ui.view_qty.clear()

    def update_data_view(self):
        search_text = self.ui.update_search.text()
        m_id = self.medicine_list()
        if int(search_text) in m_id:
            rows = self.SQL_Query_retrive(
                f"select * from MEDICINE where id = {search_text}")

            for tup in rows:
                self.ui.u_id1.setText(str(tup[0]))
                self.ui.u_id2.setText(str(tup[0]))
                self.ui.uname1.setText(str(tup[1]))
                self.ui.u_cprice1.setText(str(tup[2]))
                self.ui.u_sprice1.setText(str(tup[3]))
                self.ui.u_mfd1.setText(str(tup[4]))
                self.ui.u_exd1.setText(str(tup[5]))
                self.ui.u_qty1.setText(str(tup[6]))
        else:
            self.popup(f"{search_text} : Not Found")

    def update_data(self):
        search_text = self.ui.update_search.text()
        u_name = self.ui.uname2.text()
        cost_price = self.ui.u_cprice2.text()
        sell_price = self.ui.u_sprice2.text()
        MFD = self.ui.u_mfd2.text()
        qty = self.ui.u_qty2.text()
        if cost_price.isdigit() and int(cost_price) > 0 and sell_price.isdigit() and int(sell_price) > 0 and qty.isdigit() and int(qty) > 0:
            mfd = datetime.strptime(MFD, "%d-%m-%Y")
            exd = str(mfd+timedelta(days=180)).split()[0]
            exd_month = exd[5:7]
            exd_day = exd[8:10]
            exd_year = exd[0:4]
            exd = f"{exd_day}-{exd_month}-{exd_year}"

            self.SQL_Query_update(
                f"update MEDICINE set name = '{u_name}',c_price = {cost_price},s_price = {sell_price},m_mfd = '{MFD}',m_exd = '{exd}',qty={qty} where id = {search_text}")

            self.SQL_Query_update(
                f"update MEDICINE_DATA set name = '{u_name}',c_price = {cost_price},s_price = {sell_price},m_mfd = '{MFD}',m_exd = '{exd}',qty={qty} where id = {search_text}")

            self.popup(f'{search_text} : Updated successfully')
        else:
            self.popup("Invalid Input")

    def description_(self):
        search_word = self.ui.description_search.text()
        try:
            result = wk.summary(search_word, sentences=5)
        except:
            result = f'{search_word} : Invalid'
        self.ui.description.setText(result)

    def customer_id(self):
        c_rows = self.SQL_Query_retrive("select * from CUSTOMER")
        ls = [100]
        for tup in c_rows:
            ls.append(tup[0])
        max_id = max(ls)+1
        return max_id

    def customer_data(self):
        id = self.customer_id()
        self.ui.c_id.setText(str(id))
        self.ui.c_display_cost.setText('0')
        name = self.ui.c_name.text()
        phone = self.ui.c_phno.text()
        gender = self.ui.c_gender.currentText()
        if len(phone) == 10 and phone.isdigit():
            total = 0
            total_qty = 0
            today = self.date_time()
            self.SQL_Query_insert(
                f"insert into CUSTOMER values({id},'{name}','{phone}','{gender}',{total},'{today}',{total_qty})")
            self.ui.customer_show_id.setText(str(0))
            self.ui.customer_date.setText(str(0))
            self.ui.customer_totalcost.setText(str(0))
            self.ui.custome_data_field.setText('N/A')
            self.ui.customer_qrcode.setText('N/A')
        else:
            self.popup("Invalid Input")

    def customer_add_data(self):
        cid = self.customer_id()
        id = self.medicine_list()
        cid = cid-1
        m_id = self.ui.c_m_id.text()
        m_qty = self.ui.c_m_qty.text()
        cust_name = self.ui.c_name.text()
        cust_phone = self.ui.c_phno.text()
        cust_gender = self.ui.c_gender.currentText()
        cust_rows = self.SQL_Query_retrive(
            f"select * from customer where c_id = {cid}")
        customer_len = len(cust_rows)
        med_rows = self.SQL_Query_retrive(
            f"select * from medicine where  id = {int(m_id)}")
        if customer_len != 0 and cust_rows[0][0] == (cid) and cust_name == cust_rows[0][1] and int(cust_phone) == cust_rows[0][2] and cust_gender == cust_rows[0][3]:
            if int(m_id) in id:
                if int(m_qty) > 0:
                    if int(m_id) == med_rows[0][0]:
                        if int(m_qty) <= med_rows[0][6]:
                            sum = int(m_qty)*med_rows[0][3]
                            new_qty = med_rows[0][6]-int(m_qty)
                            self.SQL_Query_insert(
                                f"insert into orders values({cid},{int(m_qty)},{int(m_id)},{sum})")
                            t_rows = self.SQL_Query_retrive(
                                f"select sum(t_price) from orders where c_id = {cid}")
                            qty_rows = self.SQL_Query_retrive(
                                f"select sum(o_qty) from orders where c_id = {cid}")
                            self.ui.c_display_cost.setText(
                                f"{str(t_rows[0][0])}.Rs")
                            self.SQL_Query_insert(
                                f"update customer set t_price = {int(t_rows[0][0])},t_qty = {qty_rows[0][0]} where c_id = {cid}")
                            self.SQL_Query_insert(
                                f"update Medicine set qty = {new_qty} where id = {int(m_id)}")
                            self.order_table_data(cid)
                        else:
                            self.popup(f"Available Stock : {med_rows[0][6]}")
                    else:
                        self.popup(f"Invalid Medicine ID : {m_id}")
                else:
                    self.popup(f"{m_qty} : Should be greater than 0")
            else:
                self.popup(f"Invalid Medicine ID : {m_id}")
        else:
            self.popup("\tMake a new Customer\t")

    def customerclear(self):
        self.ui.c_id.setText('N/A')
        self.ui.c_display_cost.setText('N/A')
        self.ui.custome_data_field.setText('N/A')
        self.ui.customer_totalcost.setText('N/A')
        self.ui.customer_show_id.setText('N/A')
        self.ui.customer_date.setText('N/A')
        self.ui.customer_qrcode.setText('N/A')
        self.ui.c_m_id.clear()
        self.ui.c_phno.clear()
        self.ui.c_m_qty.clear()
        self.ui.c_name.clear()

    def order_table_data(self, cid):
        order_rows = self.SQL_Query_retrive(
            f"select * from orders where c_id = {cid}")
        row_count = len(order_rows)
        self.ui.customer_table.setRowCount(row_count)
        tablerow = 0

        for tup in order_rows:
            med_rows = self.SQL_Query_retrive(
                f"select * from medicine where id = {tup[2]}")
            self.ui.customer_table.setItem(
                tablerow, 0, QtWidgets.QTableWidgetItem(str(tup[2])))
            self.ui.customer_table.setItem(
                tablerow, 1, QtWidgets.QTableWidgetItem(str(med_rows[0][1])))
            self.ui.customer_table.setItem(
                tablerow, 2, QtWidgets.QTableWidgetItem(str(med_rows[0][3])))
            self.ui.customer_table.setItem(
                tablerow, 3, QtWidgets.QTableWidgetItem(str(tup[1])))
            tablerow += 1

    def order_data_display(self):
        cid = self.customer_id()
        cid = cid-1
        self.ui.customer_show_id.setText(str(cid))
        customer_rows = self.SQL_Query_retrive(
            f"select * from CUSTOMER where c_id={cid}")
        order_rows = self.SQL_Query_retrive(
            f"select * from orders where c_id = {cid}")
        str_list = []

        for tup in order_rows:
            med_rows = self.SQL_Query_retrive(
                f"select name,s_price from medicine where id = {tup[2]}")
            str_list.append((med_rows[0][0], med_rows[0][1], tup[1]))
        lst = []
        i = 0
        for tup in str_list:
            lst.append(f"     {tup[0]}  \t\t{tup[1]}.rs  \t\t  {tup[2]}.qty ")
            i += 1
        str_ = "\n".join(lst)
        t_price = customer_rows[0][4]
        self.ui.customer_totalcost.setText(str(t_price))
        self.ui.customer_date.setText(customer_rows[0][5])
        self.ui.customer_show_id.setText(str(cid))
        self.ui.custome_data_field.setText(str_)
        detail = f"C_id : {cid}\nName : {customer_rows[0][1]}\nPhone : {customer_rows[0][2]}\nTotal Price : {t_price}\ndate : {customer_rows[0][5]}\n\n"
        str_ = (detail+str_+"\n\nTHANK YOU")
        self.generateqr(str_, i)

    def generateqr(self, text, i):

        url = pyqrcode.create(text)
        if i >= 5:
            url.svg('qrcode.svg', scale=2.5)
            url.png('qrcode.png', scale=2.5)
        else:
            url.svg('qrcode.svg', scale=2.5)
            url.png('qrcode.png', scale=2.5)
        self.ui.customer_qrcode.setPixmap(
            QPixmap("qrcode.svg"))
        os.remove('qrcode.svg')

    def print_recipt(self):
        cid = self.customer_id()
        cid = cid-1
        customer_rows = self.SQL_Query_retrive(
            f"select * from CUSTOMER where c_id={cid}")
        order_rows = self.SQL_Query_retrive(
            f"select * from orders where c_id = {cid}")
        str_list = []
        for tup in order_rows:
            med_rows = self.SQL_Query_retrive(
                f"select name,s_price from medicine where id = {tup[2]}")
            str_list.append((med_rows[0][0], med_rows[0][1], tup[1]))
        lst = []
        i = 0
        for tup in str_list:
            lst.append(
                f"     \t{tup[0]}  \t\t\t\t{tup[1]}.rs  \t\t\t {tup[2]}.qty ")
            i += 1
        str1 = '\n**********************************************************\n\tName \t\t\t Qty\t\t\t\t Price\n**********************************************************\n'
        str2 = '\n**********************************************************\n\t\t\t\t\tTHANK YOU'
        str_ = "\n".join(lst)
        new_str = str1+str_+str2
        name = customer_rows[0][1]
        phone = customer_rows[0][2]
        total = customer_rows[0][4]
        date = self.date_time()
        doc = DocxTemplate('template.docx')
        image = InlineImage(doc, 'qrcode.png', Cm(6.5))
        context = {'name': name,
                   'c_id': cid,
                   'contact': phone,
                   'Total': total,
                   'date': date,
                   'qrcode': image,
                   'Product': new_str}

        doc.render(context)
        filename = f"\{cid}.docx"
        filename1 = f"\{cid}.pdf"
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, "Bill")
        os.chdir(path)
        doc.save(path+filename)
        convert(path+filename, path+filename1)  # doc to pdf convetor
        os.remove(path+filename)
        os.chdir('../')
        os.remove('qrcode.png')
        self.popup("Recipt Printed Successfully Press O to Open")

    def open_recipt(self):
        cid = self.customer_id()
        cid = cid-1
        if cid != 100:
            filename = f"\{cid}.pdf"
            parent_dir = os.getcwd()
            path = os.path.join(parent_dir, "Bill")
            os.chdir(path)
            path = path+filename
            os.system(path)
            os.chdir('../')
        else:
            self.popup("file not found")

    def open_recipt_excel(self):
        date = self.date_time()
        filename = f"\{date}_Report.xls"
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, "Report")
        os.chdir(path)
        os.system(path+filename)
        os.chdir('../')

    def report_id(self):
        r_rows = self.SQL_Query_retrive("select * from REPORT_DETAILS")
        ls = [100]
        for tup in r_rows:
            ls.append(tup[0])
        max_id = max(ls)+1
        return max_id

    def print_excel(self):
        date = self.date_time()
        filename = f"\{date}_Report.xls"
        wb = Workbook()
        style = xlwt.easyxf('font: bold 1,height 250')
        Report = wb.add_sheet('Report')
        Medicine = wb.add_sheet('Medicine')
        customer = wb.add_sheet('Customer')
        m_rows = self.SQL_Query_retrive("select * from medicine")
        c_rows = self.SQL_Query_retrive("select * from customer")
        ms_rows = self.SQL_Query_retrive(
            f"select id,s_price,c_price,qty,(c_price * qty) c_price,(s_price * qty) s_price from MEDICINE_DATA")
        o_rows = self.SQL_Query_retrive(f"select sum(t_price) from orders")
        mc_rows = self.SQL_Query_retrive(f"select sum(qty)from MEDICINE")
        med_list = ['Medicine id', 'Name', 'Cost Price', 'Selling Price',
                    'Manufacture Date', 'Expirary Date', 'Quantity']
        cust_list = ['C_id', 'Name', 'Phone',
                     'Gender', 'Total Price', 'Date', 'Quantity']
        cost_value = 0
        sale_value = 0
        for tup in ms_rows:
            cost_value = cost_value + tup[4]
            sale_value = sale_value + tup[5]

        r_rows = self.SQL_Query_retrive(
            f"select * from REPORT_DETAILS where R_DATE = '{date}'")
        print(r_rows)
        c_customer = len(c_rows)
        c_sales = o_rows[0][0]
        c_cost = cost_value
        s_sales = sale_value
        p_product = len(ms_rows)
        s_stock = mc_rows[0][0]
        c_date = date

        if len(r_rows) == 0:
            r_id = self.report_id()
            self.SQL_Query_insert(
                f"insert into REPORT_DETAILS values({r_id},{c_customer},{s_stock},{p_product},{c_cost},{s_sales},'{c_date}',{c_sales})")
        else:
            self.SQL_Query_update(
                f"update REPORT_DETAILS set R_CUSTOMER={c_customer},R_STOCK={s_stock},R_PRODUCT={p_product},R_COST={c_cost},R_SALES={s_sales},R_SALES_CUST={c_sales} where R_DATE = '{date}'")

        first_col = Report.col(0)
        first_col.width = 256 * 18
        Report.write(0, 0, 'Customer', style)
        Report.write(0, 1, len(c_rows))
        Report.write(1, 0, 'Sales', style)
        Report.write(1, 1, f"{o_rows[0][0]}.rs")
        Report.write(2, 0, 'Stock', style)
        Report.write(2, 1, mc_rows[0][0])
        Report.write(3, 0, 'Products', style)
        Report.write(3, 1, len(ms_rows))
        Report.write(4, 0, 'Cost Value', style)
        Report.write(4, 1, f"{cost_value}.rs")
        Report.write(5, 0, 'Sales Value', style)
        Report.write(5, 1, f"{sale_value}.rs")

        i = 0
        for item in med_list:
            first_col = Medicine.col(i)
            first_col.width = 256 * 18
            Medicine.write(0, i, item, style)
            i += 1
        i = 0
        for item in cust_list:
            first_col = customer.col(i)
            first_col.width = 256 * 18
            customer.write(0, i, item, style)
            i += 1

        m_rows.sort(key=lambda lst: lst[0], reverse=False)
        r = 1
        for tup in m_rows:
            c = 0
            for item in tup:
                Medicine.write(r, c, item)
                c += 1
            r += 1

        c_rows.sort(key=lambda lst: lst[0], reverse=False)
        r = 1
        for tup in c_rows:
            c = 0
            for item in tup:
                customer.write(r, c, item)
                c += 1
            r += 1
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, "Report")
        os.chdir(path)
        print(path)
        wb.save(path+filename)
        os.chdir('../')
        self.popup("Report Created Successfully Press X to Open")

    def report_show(self):
        c_date = self.ui.calendarWidget.selectedDate()
        ls = str(c_date)
        date = ls.split('(')[1].split(')')[0].split(' ')
        r_date = f"{date[2]}-{date[1][0]}-{date[0][0:4]}"

        rows = self.SQL_Query_retrive(
            f"select * from customer where C_DATE='{r_date}'")
        r_rows = self.SQL_Query_retrive(
            f"select * from REPORT_DETAILS where R_DATE = '{r_date}'")
        if len(r_rows) == 0:
            self.popup(f"No Daily Report found : {r_date}")
            self.ui.label_8.setText('N/A')
            self.ui.label_10.setText('N/A')
            self.ui.label_34.setText('N/A')
            self.ui.label_87.setText('N/A')
            self.ui.label_88.setText('N/A')
            self.ui.label_89.setText('N/A')
        else:
            self.ui.label_8.setText(str(r_rows[0][1]))
            self.ui.label_10.setText(str(r_rows[0][2]))
            self.ui.label_34.setText(str(r_rows[0][7]))
            self.ui.label_87.setText(str(r_rows[0][3]))
            self.ui.label_88.setText(str(r_rows[0][5]))
            self.ui.label_89.setText(str(r_rows[0][4]))
        rowcount = len(rows)
        self.ui.Purchase_history_table_2.setRowCount(rowcount)
        tablerow = 0
        rows.sort(key=lambda lst: lst[0], reverse=False)
        ########
        for tup in rows:
            i = 0
            for col in tup:
                self.ui.Purchase_history_table_2.setItem(
                    tablerow, i, QtWidgets.QTableWidgetItem(str(tup[i])))
                i += 1
            tablerow += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = MainWindow()
    sys.exit(app.exec_())
