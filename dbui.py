import sys
import os
from PySide6.QtWidgets import QApplication, QWidget, QTableView, QDialog, QInputDialog, QMessageBox, QFileDialog
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQueryModel, QSqlQuery
from PySide6.QtCore import Qt, QLibraryInfo, QCoreApplication, QDate, QTime
from ui_form import Ui_DBUI
from ui_queries import Ui_Dialog
from ui_form_1 import Ui_Form as admin_tool
from ui_form_2 import Ui_Form as login_ui
from ui_query_for_admin import Ui_Form as doc_quer
from ui_reg_empl import Ui_Form as reg_empl
from ui_user_reg import Ui_Form as reg_user
from ui_for_users import Ui_Form as user_ui
from ui_reg_type import Ui_RegDialog as reg_type
from ui_mm_user import Ui_Form as log_usr
from ui_mm_doc import Ui_Form as log_doc
from ui_mm_emp import Ui_Form as log_emp
from ui_add_pet import Ui_Dialog as add_pet
from ui_appnt_pet import Ui_Form as appnt_pet
from ui_1word import Ui_Dialog as one_word
from ui_between_2_d import Ui_Dialog as b2d
from ui_word_n_dates import Ui_Dialog as wordndates
from ui_y_n_m import Ui_Dialog as year_n_month
from ui_docs_menu1 import Ui_Form as docMenu1
from ui_docs_menu2 import Ui_Form as docMenu2
from ui_cancel_appoint import Ui_Dialog as app_cans
from ui_sp_menu import Ui_Form as backup_menu
from ui_log_menu import Ui_Form as log_menu
from ui_stress_test import Ui_Form as stress_test
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from argon2.low_level import hash_secret, Type
import subprocess
import datetime


class DBUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.db = QSqlDatabase.addDatabase('QODBC')
        self.db.setDatabaseName(
            'DRIVER={MySQL ODBC 8.0 Unicode Driver};SERVER=localhost;DATABASE=vet_clinic;UID=root;PWD=1111;PORT=3812;'             # у SERVER записати ip локальної мережі, яку ви використали у ODBC Data Sources
        )
        # self.db.setDatabaseName(
        #     'DRIVER={MySQL ODBC 8.0 Unicode Driver};SERVER=25.44.219.6;DATABASE=vet_clinic;UID=ubuntu_root;PWD=1111;PORT=3812;'             # у SERVER записати ip локальної мережі, яку ви використали у ODBC Data Sources
        # )

        if not self.db.open():
            print("Не вдалося підключитися до бази даних")
            print(self.db.lastError().text())
            return

        #self.login = login_ui()
        #self.login.setupUi(self)
        #self.logined = 0
        #self.logined_id = 0

        self.login_window = QWidget()
        self.login = login_ui()
        self.login.setupUi(self.login_window)
        self.login_window.show()

        self.login.pushButton.clicked.connect(self.log_in)
        self.login.pushButton_2.clicked.connect(self.registr)



        #self.admin_menu = log_emp()
        #self.admin_menu.setupUi(QDialog(self))
        #self.admin_menu.pushButton.clicked.connect(self.admins_menu_enter)

        self.ui = Ui_DBUI()
        self.ui.setupUi(QDialog(self))

    def log_in(self):
        phone_num = self.login.textEdit.toPlainText()
        password = self.login.textEdit_2.toPlainText()
        salt = "12345678"
        #ph = PasswordHasher(type=Type.I)
        #hash = ph.hash(password)
        hashed = hash_secret(
            password.encode("utf-8"),
            salt.encode("utf-8"),
            time_cost=2,
            memory_cost=16,
            parallelism=1,
            hash_len=16,
            type=Type.I
        )
        hash = hashed.decode('utf-8')
        checking = QSqlQuery(f"SELECT * FROM `users_login` WHERE `phone_login` = '{phone_num}' and `password_hash` = '{hash}';")
        print(phone_num)
        print(hash)

        if checking.next():
            self.usrid = checking.value(0)
            id = checking.value(4)
            type = checking.value(3)
            print(f"{id}, {type}")
            self.action_log(self.usrid, "Авторизація", f"{self.usrid} увійшов в аккаунт типу {type} з id {id}")
            if type == "adm":
                self.login_window.close()
                #self.login.close()
                self.logined = 1
                self.logined_id = id
                self.empl_login(id)
            elif type == "doc":
                self.login_window.close()
                #self.close()
                self.logined = 2
                self.logined_id = id
                self.doc_login(id)
            elif type == "usr":
                self.login_window.close()
                #self.close()
                self.logined = 3
                self.logined_id = id
                self.user_login(id)
            print(self.logined)
        else:
            QMessageBox.critical(self, "Помилка", "Невірний логін або пароль")
            print("no data")

    def admins_menu_enter(self):
        print("Кнопку натиснуто!")
        self.asm_dialog = QDialog(self)
        #self.ui = Ui_DBUI()
        self.ui.setupUi(self.asm_dialog)


        self.t_index = 'users_login'

        self.arg = ""

        self.ui.comboBox.currentIndexChanged.connect(self.onChanged)

        self.model = QSqlTableModel(self)
        self.model.setTable(self.t_index)
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()

        self.ui.pushButton.clicked.connect(self.addRow)
        self.ui.pushButton_2.clicked.connect(self.delRow)
        self.ui.pushButton_3.clicked.connect(self.asm_dialog.close)
        self.ui.pushButton_4.clicked.connect(self.stress_test_exec)

        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setSelectionBehavior(QTableView.SelectRows)
        self.ui.tableView.setSelectionMode(QTableView.SingleSelection)
        self.ui.tableView.setSortingEnabled(True)
        self.ui.tableView.horizontalHeader().setStretchLastSection(True)

        self.ui.tableView.setEditTriggers(QTableView.DoubleClicked | QTableView.SelectedClicked)
        self.action_log(self.usrid, "Перейдено у меню реагування БД", f"Користувач {self.usrid} перейшов у меню реагування БД")
        self.asm_dialog.exec()


    def stress_test_exec(self):
        st_t_d = QDialog(self)
        self.st_t = stress_test()
        self.st_t.setupUi(st_t_d)
        st_t_d.exec()


    def doctors_menu_enter(self):
        self.docmenu_dialog = QDialog(self)
        self.docmenu = doc_quer()
        self.docmenu.setupUi(self.docmenu_dialog)
        self.query_model1 = QSqlQueryModel(self)
        self.query_text1 = f"""
        SELECT DISTINCT p.patient_id, p.name, p.species, p.breed
        FROM Patients p
        JOIN Treatments t ON p.patient_id = t.patient_id
        WHERE t.doctor_id = '{self.doc_id}'
        """


        self.docmenu.pushButton.clicked.connect(self.doc_menu_query_exec)
        self.docmenu.comboBox.addItems(doctor_queries)
        self.docmenu.comboBox.currentIndexChanged.connect(self.choseQueryDoctor)
        self.docmenu.pushButton_2.clicked.connect(self.save_to_pdf1)
        self.docmenu.pushButton_3.clicked.connect(self.docs_menu1)
        self.docmenu.pushButton_4.clicked.connect(self.docs_menu2)
        self.docmenu.pushButton_5.clicked.connect(self.docmenu_dialog.close)


        self.docmenu_dialog.exec()


    def doc_menu_query_exec(self):

        if self.query_text1:
            self.query_model1.setQuery(self.query_text1)

            if self.query_model1.lastError().isValid():
                print(f"Помилка виконання запиту: {self.query_model1.lastError().text()}")
            else:
                self.docmenu.tableView.setModel(self.query_model1)

        self.action_log(self.usrid, "Відправка запиту (лікар)", f"{self.docmenu.comboBox.currentText()}")



    def docs_menu1(self):
        self.dm1_dialog = QDialog(self)
        self.dm1 = docMenu1()
        self.dm1.setupUi(self.dm1_dialog)
        self.dm1.dateEdit.setMinimumDate(QDate.currentDate())
        self.dm1.comboBox_2.addItems(["Оплачено", "Не оплачено"])
        self.dm1_pets_list_former()

        self.dm1.comboBox.addItems(self.dm1.pet_name)
        self.dm1.comboBox.currentIndexChanged.connect(self.dm1_pets_list_former)
        self.dm1.pushButton.clicked.connect(self.dm1_finish)
        self.dm1.pushButton_2.clicked.connect(self.dm1_dialog.close)


        self.dm1_dialog.exec()

    def dm1_pets_list_former(self):
        query_info1 = f"SELECT * FROM `appointments` WHERE `doctor_id` = '{self.doc_id}' AND `status` = 'очікує'"
        query_exec1 = QSqlQuery()
        query_exec1.exec(query_info1)
        self.dm1.appoint_id = []
        self.dm1.patient_id = []
        self.dm1.app_date = []
        while query_exec1.next():
            self.dm1.appoint_id.append(query_exec1.value(0))
            self.dm1.patient_id.append(query_exec1.value(1))
            self.dm1.app_date.append(query_exec1.value(3))


        self.dm1.pet_name = []
        pet_weight = []
        pet_age = []
        pet_species = []
        pet_breed = []
        query_exec2 = QSqlQuery()
        for i in range(len(self.dm1.patient_id)):
            query_info2 = f"SELECT * FROM `patients` WHERE `patient_id` = '{self.dm1.patient_id[i]}'"
            query_exec2.exec(query_info2)
            if query_exec2.next():
                self.dm1.pet_name.append(query_exec2.value(1))
                pet_weight.append(query_exec2.value(5))
                pet_age.append(query_exec2.value(4))
                pet_breed.append(query_exec2.value(3))
                pet_species.append(query_exec2.value(2))

        if len(self.dm1.pet_name) > 0:
            prenum = self.dm1.comboBox.currentIndex()
            if prenum < 0:
                num = 0
            else:
                num = prenum
            self.dm1.label_6.setText(str(pet_age[num]))
            self.dm1.label_7.setText(str(pet_weight[num]))
            self.dm1.label_8.setText(pet_species[num])
            self.dm1.label_9.setText(pet_breed[num])
            self.dm1.label_15.setText(str(self.dm1.app_date[num].toString("yyyy.MM.dd")))
        else:
            QMessageBox.critical(self, "Помилка", "Для вас немає записів")
            self.dm1_dialog.close


    def dm1_finish(self):
        diagn = self.dm1.lineEdit_3.text()
        treatm = self.dm1.lineEdit.text()
        price = self.dm1.lineEdit_2.text()
        d = self.dm1.dateEdit.date()
        date = d.toString("yyyy.MM.dd")
        p_id = self.dm1.patient_id[self.dm1.comboBox.currentIndex()]
        if self.dm1.comboBox_2.currentIndex() == 1:
            p_status = "Unpaid"
        else:
            p_status = "Paid"


        tr_query = f"INSERT INTO `treatments` (`treatment_id`, `patient_id`, `doctor_id`, `diagnosis`, `prescribed_treatment`, `visit_date`, `service_cost`, `payment_status`) VALUES (NULL, '{p_id}', '{self.doc_id}', '{diagn}', '{treatm}', '{date}', '{price}', '{p_status}')"
        query_exec3 = QSqlQuery()
        #print(tr_query)
        app_qry_upd = f"UPDATE `appointments` SET `status` = 'завершено' WHERE `appointment_id` = '{self.dm1.appoint_id[self.dm1.comboBox.currentIndex()]}'"
        query_exec4 = QSqlQuery()
        #print(app_qry_upd)
        query_exec3.exec(tr_query)
        query_exec4.exec(app_qry_upd)

        self.action_log(self.usrid, "Створення лікування", f"Лікар {self.doc_id} назначив лікування пацієнту {self.dm1.patient_id[self.dm1.comboBox.currentIndex()]}")

        self.dm1_dialog.close()

    def docs_menu2(self):
        self.dm2_dialog = QDialog(self)
        self.dm2 = docMenu2()
        self.dm2.setupUi(self.dm2_dialog)
        self.dm2_pets_list_former()

        self.dm2.comboBox.addItems(self.dm2.pet_name)
        self.dm2.pushButton.clicked.connect(self.dm2_finish)
        self.dm2.pushButton_2.clicked.connect(self.dm2_dialog.close)

        self.dm2_dialog.exec()

    def dm2_pets_list_former(self):
        query_info1 = f"SELECT * FROM `appointments` WHERE `doctor_id` = '{self.doc_id}' AND `status` = 'очікує'"
        query_exec1 = QSqlQuery()
        query_exec1.exec(query_info1)
        self.dm2.appoint_id = []
        self.dm2.patient_id = []
        self.dm2.app_date = []
        while query_exec1.next():
            self.dm2.appoint_id.append(query_exec1.value(0))
            self.dm2.patient_id.append(query_exec1.value(1))
            self.dm2.app_date.append(query_exec1.value(3))

        self.dm2.pet_name = []
        pet_weight = []
        pet_age = []
        pet_species = []
        pet_breed = []
        query_exec2 = QSqlQuery()
        for i in range(len(self.dm2.patient_id)):
            query_info2 = f"SELECT * FROM `patients` WHERE `patient_id` = '{self.dm2.patient_id[i]}'"
            query_exec2.exec(query_info2)
            if query_exec2.next():
                self.dm2.pet_name.append(query_exec2.value(1))
                pet_weight.append(query_exec2.value(5))
                pet_age.append(query_exec2.value(4))
                pet_breed.append(query_exec2.value(3))
                pet_species.append(query_exec2.value(2))


        if len(self.dm2.pet_name) > 0:
            prenum = self.dm2.comboBox.currentIndex()
            if prenum < 0:
                num = 0
            else:
                num = prenum
            self.dm2.label_6.setText(str(pet_age[num]))
            self.dm2.label_7.setText(str(pet_weight[num]))
            self.dm2.label_8.setText(pet_species[num])
            self.dm2.label_9.setText(pet_breed[num])
            self.dm2.label_15.setText(str(self.dm2.app_date[num].toString("yyyy.MM.dd")))
        else:
            QMessageBox.critical(self, "Помилка", "Для вас немає записів")
            self.dm2_dialog.close

    def dm2_finish(self):
        app_qry_upd = f"UPDATE `appointments` SET `status` = 'скасовано' WHERE `appointment_id` = '{self.dm2.appoint_id[self.dm2.comboBox.currentIndex()]}'"
        query_exec4 = QSqlQuery()
        #print(app_qry_upd)
        query_exec4.exec(app_qry_upd)

        self.action_log(self.usrid, "Скасування прийому", f"Лікар {self.doc_id} скасував прийом пацієнта {self.dm1.patient_id[self.dm1.comboBox.currentIndex()]}")

        self.dm2_dialog.close()

    def users_menu_enter(self):
        self.umenu_dialog = QDialog(self)
        self.um_ui = user_ui()
        self.um_ui.setupUi(self.umenu_dialog)
        self.query_model2 = QSqlQueryModel(self)
        self.query_text2 = f"""
        SELECT a.appointment_id, a.patient_id, p.name AS patient_name, a.doctor_id,
               d.last_name AS doctor_last_name, a.appointment_date, a.appointment_time, a.status
        FROM Appointments a
        JOIN Patients p ON a.patient_id = p.patient_id
        JOIN Doctors d ON a.doctor_id = d.doctor_id
        WHERE p.owner_id = '{self.log.user_id}'
        """

        self.um_ui.pushButton.clicked.connect(self.user_query_exec) #запити
        self.um_ui.comboBox.addItems(owner_queries)
        self.um_ui.comboBox.currentIndexChanged.connect(self.choseQueryOwner)
        self.um_ui.pushButton_2.clicked.connect(self.enter_appnt_pet_menu)
        self.um_ui.pushButton_3.clicked.connect(self.umenu_dialog.close)
        self.um_ui.pushButton_4.clicked.connect(self.appoint_cancel)

        self.umenu_dialog.exec()


    def user_query_exec(self):

        if self.query_text2:
            self.query_model2.setQuery(self.query_text2)

            if self.query_model2.lastError().isValid():
                print(f"Помилка виконання запиту: {self.query_model2.lastError().text()}")
            else:
                self.um_ui.tableView.setModel(self.query_model2)

        self.action_log(self.usrid, "Відправка запиту (власник тварини)", f"{self.um_ui.comboBox.currentText()}")


    def enter_appnt_pet_menu(self):
        self.appnt_pet_dlg = QDialog(self)
        self.apet = appnt_pet()
        self.apet.setupUi(self.appnt_pet_dlg)
        self.apet.dateEdit.setMinimumDate(QDate.currentDate())
        self.pets_list_former()

        self.apet.comboBox.addItems(self.pets_list)
        self.apet.comboBox_2.addItems(["Терапевт", "Хірург", "Дерматолог", "Кардіолог", "Офтальмолог", "Ортопед", "Стоматолог", "Репродуктолог", "Лаборант"])

        self.apet.comboBox_2.currentIndexChanged.connect(self.docs_list_former)

            # Викликаємо один раз для початкового заповнення comboBox_3
        self.docs_list_former()

        self.apet.pushButton.clicked.connect(self.add_appnt_pet)
        self.apet.pushButton_2.clicked.connect(self.appnt_pet_dlg.close)

        self.appnt_pet_dlg.exec()


    def pets_list_former(self):
        owner_id = self.log.user_id
        self.pets_list = []
        self.pets_id = []
        self.pet_kinds = []
        searching_proc = QSqlQuery()
        searching_proc.exec(f"SELECT * FROM `patients` WHERE `owner_id` = '{owner_id}'")
        while searching_proc.next():
            self.pets_list.append(searching_proc.value(1))
            self.pets_id.append(searching_proc.value(0))
            self.pet_kinds.append(searching_proc.value(2))
        print(self.pets_list)
        print(self.pets_id)


    def docs_list_former(self):
        docsp = self.apet.comboBox_2.currentText()
        pl_index = self.apet.comboBox.currentIndex()
        pet_kind = self.pet_kinds[pl_index].lower()

        doc_anim_type = [key for key, value_list in pet_families.items() if pet_kind in value_list][0]
        self.doc_list = []
        self.docs_id = []
        searching_proc = QSqlQuery()
        searching_proc.exec(f"SELECT * FROM `doctors` WHERE `specialization` LIKE '%{docsp}%' and `animal_type` = '{doc_anim_type}'")
        while searching_proc.next():
            self.doc_list.append(f"{searching_proc.value(1)} {searching_proc.value(2)} {searching_proc.value(3)}")
            self.docs_id.append(searching_proc.value(0))

        self.apet.comboBox_3.clear()
        self.apet.comboBox_3.addItems(self.doc_list)

    def add_appnt_pet(self):
        my_pet = self.apet.comboBox.currentText()
        spec_in = self.apet.comboBox_2.currentText()
        doctor = self.apet.comboBox_3.currentText()
        date = self.apet.dateEdit.date()
        true_date = date.toString("yyyy.MM.dd")
        time = self.apet.timeEdit.time()
        chosen_pet = self.pets_id[self.apet.comboBox.currentIndex()]
        chosen_doc = self.docs_id[self.apet.comboBox_3.currentIndex()]
        check_query = f"SELECT EXISTS (SELECT 1 FROM appointments WHERE appointment_date = '{true_date}' and appointment_time = '{time.toString()}' and status = 'очікує' and doctor_id = '{chosen_doc}') AS is_exists;"
        cq_exec = QSqlQuery()
        cq_exec.exec(check_query)
        if cq_exec.next():
            ch_result = cq_exec.value(0)
        query1 = f"INSERT INTO `appointments` (`appointment_id`, `patient_id`, `doctor_id`, `appointment_date`, `appointment_time`, `status`) VALUES (NULL, '{chosen_pet}', '{chosen_doc}', '{true_date}', '{time.toString()}', 'очікує')"
        if ch_result == 0:
            appnt_creation = QSqlQuery()
            appnt_creation.exec(query1)
            self.action_log(self.usrid, "Запис на прийом", f"Користувач {self.log.user_id} записав на прийом пацієнта {chosen_pet}")
            self.appnt_pet_dlg.close()
        else:
            QMessageBox.warning(self, "Попередження", f"На жаль, цей час у лікаря {chosen_doc} недоступний. оберіть інший час або інший день")



    def add_pet_menu(self):
        self.pet_dialog = QDialog(self)
        self.apm = add_pet()
        self.apm.setupUi(self.pet_dialog)

        self.apm.pushButton.clicked.connect(self.execute_adding)
        self.apm.pushButton_2.clicked.connect(self.pet_dialog.close)
        self.pet_dialog.exec()


    def execute_adding(self):
        pet_name = self.apm.lineEdit_10.text()
        species = self.apm.lineEdit_8.text()
        breed = self.apm.lineEdit_9.text()
        age = self.apm.lineEdit_11.text()
        weight = self.apm.lineEdit_12.text()
        id = self.log.user_id
        query = f"INSERT INTO `patients` (`patient_id`, `name`, `species`, `breed`, `age`, `weight_kg`, `owner_id`) VALUES (NULL, '{pet_name}', '{species}', '{breed}', '{age}', '{weight}', '{id}')"

        QSqlQuery(query)
        self.action_log(self.usrid, "Додавання тварини", f"Користувач {self.log.user_id} додав собі у список нову тварину")
        #print(query)
        self.pet_dialog.close()

    def appoint_cancel(self):
        self.apcan_d = QDialog(self)
        self.apcan = app_cans()
        self.apcan.setupUi(self.apcan_d)
        self.ac_pets_list_former()
        self.apcan.comboBox.addItems(self.apcan.apname)
        self.apcan.comboBox.currentIndexChanged.connect(self.ac_pets_list_former)

        self.apcan.pushButton.clicked.connect(self.apcan_finish)
        self.apcan.pushButton_2.clicked.connect(self.apcan_d.close)

        self.apcan_d.exec()


    def ac_pets_list_former(self):
        query_info1 = f"""
        SELECT a.appointment_id, a.patient_id, p.name AS patient_name, a.doctor_id,
               d.last_name AS doctor_last_name, a.appointment_date, d.first_name AS doctor_first_name, a.status
        FROM Appointments a
        JOIN Patients p ON a.patient_id = p.patient_id
        JOIN Doctors d ON a.doctor_id = d.doctor_id
        WHERE p.owner_id = '{self.log.user_id}' AND a.status = 'очікує'
        """
        query_exec1 = QSqlQuery()
        query_exec1.exec(query_info1)
        self.apcan.appoint_id = []
        self.apcan.patient_id = []
        self.apcan.app_date = []
        self.apcan.pet_name = []
        self.apcan.doc = []
        self.apcan.apname = []
        apnum = 0
        while query_exec1.next():
            apnum += 1
            self.apcan.appoint_id.append(query_exec1.value(0))
            self.apcan.patient_id.append(query_exec1.value(1))
            self.apcan.app_date.append(query_exec1.value(5))
            self.apcan.pet_name.append(query_exec1.value(2))
            self.apcan.doc.append(f"{query_exec1.value(4)} {query_exec1.value(6)}")
            self.apcan.apname.append(f"{apnum}: {query_exec1.value(5).toString('yyyy.MM.dd')} - {query_exec1.value(2)}")

        if len(self.apcan.appoint_id) > 0:
            prenum = self.apcan.comboBox.currentIndex()
            if prenum < 0:
                num = 0
            else:
                num = prenum
            print(num)
            self.apcan.label_2.setText(self.apcan.pet_name[num])
            self.apcan.label_15.setText(str(self.apcan.app_date[num].toString("yyyy.MM.dd")))
            self.apcan.label_17.setText(self.apcan.doc[num])
        else:
            QMessageBox.critical(self, "Помилка", "Ви ще не створили актуальний запис")


    def apcan_finish(self):
        app_qry_upd = f"UPDATE `appointments` SET `status` = 'скасовано' WHERE `appointment_id` = '{self.apcan.appoint_id[self.apcan.comboBox.currentIndex()]}'"
        query_exec4 = QSqlQuery()
        #print(app_qry_upd)
        query_exec4.exec(app_qry_upd)

        self.action_log(self.usrid, "Скасування прийому (власник)", f"Користувач {self.log.user_id} скасував прийом пацієнта {self.apcan.patient_id[self.apcan.comboBox.currentIndex()]}")

        self.apcan_d.close()



    def user_login(self, id):
        self.user_dialog = QDialog(self)
        self.log = log_usr()
        self.log.setupUi(self.user_dialog)

        user_info = QSqlQuery(f"SELECT * FROM `owners` where `owner_id` = '{int(id)}'")
        if user_info.next():
            self.log.user_id = user_info.value(0)
            lst_name = user_info.value(1)
            frt_name = user_info.value(2)
            mdl_name = user_info.value(3)
            addr = user_info.value(4)
            loc = user_info.value(5)
            ph = user_info.value(6)
            email = user_info.value(7)
            adcon = user_info.value(8)

        self.log.pushButton.clicked.connect(self.add_pet_menu)
        self.log.pushButton_2.clicked.connect(self.user_log_out)
        self.log.pushButton_3.clicked.connect(self.users_menu_enter)

        pet_count = QSqlQuery(f"SELECT COUNT(*) AS total_rows FROM patients where owner_id = {id};")
        if pet_count.next():
            pets = pet_count.value(0)

        self.log.label_ln.setText(lst_name)
        self.log.label_fn.setText(frt_name)
        self.log.label_mn.setText(mdl_name)
        self.log.label_adr.setText(addr)
        self.log.label_phn.setText(ph)
        self.log.label_eml.setText(email)
        self.log.label_14.setText(str(pets))

        self.user_dialog.exec()

    def empl_login(self, id):
        self.adm_dialog = QDialog(self)
        self.log = log_emp()
        self.log.setupUi(self.adm_dialog)

        self.log.pushButton.clicked.connect(self.openQueries)
        self.log.pushButton_2.clicked.connect(self.adm_log_out)
        self.log.pushButton_3.clicked.connect(self.adm_backup_menu)
        self.log.pushButton_4.clicked.connect(self.log_menu_enter)

        user_info = QSqlQuery(f"SELECT * FROM `admins` where `admin_id` = '{int(id)}'")
        if user_info.next():
            self.adm_id = user_info.value(0)
            lst_name = user_info.value(1)
            frt_name = user_info.value(2)
            mdl_name = user_info.value(3)
            spec = user_info.value(4)
            ph = user_info.value(7)

        self.log.label_ln.setText(lst_name)
        self.log.label_fn.setText(frt_name)
        self.log.label_mn.setText(mdl_name)
        self.log.label_spc.setText(spec)
        self.log.label_phn.setText(str(ph))

        self.adm_dialog.exec()

    def log_menu_enter(self):
        self.lm_dialog = QDialog(self)
        self.lm = log_menu()
        self.lm.setupUi(self.lm_dialog)

        self.model1 = QSqlTableModel(self)
        self.model1.setTable("user_actions_log")
        self.model1.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model1.select()

        self.lm.pushButton.clicked.connect(self.dellogRow)
        self.lm.pushButton_2.clicked.connect(self.lm_dialog.close)

        self.lm.tableView.setModel(self.model1)
        self.lm.tableView.setSelectionBehavior(QTableView.SelectRows)
        self.lm.tableView.setSelectionMode(QTableView.SingleSelection)
        self.lm.tableView.setSortingEnabled(True)
        self.lm.tableView.horizontalHeader().setStretchLastSection(True)

        self.lm.tableView.setEditTriggers(QTableView.DoubleClicked | QTableView.SelectedClicked)

        self.lm_dialog.exec()

    def dellogRow(self):
        selected_row = self.lm.tableView.currentIndex().row()
        self.model1.removeRow(selected_row)
        self.model1.submitAll()
        self.model1.select()

    def adm_backup_menu(self):
        self.abm_dialog = QDialog(self)
        self.bm = backup_menu()
        self.bm.setupUi(self.abm_dialog)
        self.backup_type()

        self.bm.radioButton.toggled.connect(self.backup_type)
        self.bm.radioButton_2.toggled.connect(self.backup_type)
        self.bm.checkBox.stateChanged.connect(self.backup_type)
        self.bm.checkBox_2.stateChanged.connect(self.backup_type)
        self.bm.checkBox_3.stateChanged.connect(self.backup_type)
        self.bm.checkBox_4.stateChanged.connect(self.backup_type)
        self.bm.checkBox_5.stateChanged.connect(self.backup_type)
        self.bm.checkBox_6.stateChanged.connect(self.backup_type)
        self.bm.checkBox_7.stateChanged.connect(self.backup_type)
        self.bm.checkBox_8.stateChanged.connect(self.backup_type)

        self.bm.pushButton.clicked.connect(self.backup_database)
        self.bm.pushButton_2.clicked.connect(self.restore_database)
        self.bm.pushButton_3.clicked.connect(self.abm_dialog.close)

        self.abm_dialog.exec()



    def backup_type(self):
        if self.bm.radioButton_2.isChecked():
            if self.bm.checkBox.isChecked():
                table1 = "admins"
            else:
                table1 = ""
            if self.bm.checkBox_2.isChecked():
                table2 = "appointments"
            else:
                table2 = ""
            if self.bm.checkBox_3.isChecked():
                table3 = "doctors"
            else:
                table3 = ""
            if self.bm.checkBox_4.isChecked():
                table4 = "owners"
            else:
                table4 = ""
            if self.bm.checkBox_5.isChecked():
                table5 = "patients"
            else:
                table5 = ""
            if self.bm.checkBox_6.isChecked():
                table6 = "reg_keys"
            else:
                table6 = ""
            if self.bm.checkBox_7.isChecked():
                table7 = "treatments"
            else:
                table7 = ""
            if self.bm.checkBox_8.isChecked():
                table8 = "users_login"
            else:
                table8 = ""
            tables = [table1, table2, table3, table4, table5, table6, table7, table8]
            tables = list(filter(None, tables))
            self.command = [
                "mysqldump",
                "-h", "25.44.219.6",
                "-P", "3812",
                "-u", "ubuntu_root",
                f"-p1111",
                "vet_clinic",
                *tables
            ]

        elif self.bm.radioButton.isChecked():
            self.command = [
                "mysqldump",
                "-h", "25.44.219.6",
                "-P", "3812",
                "-u", "ubuntu_root",
                f"-p1111",
                "vet_clinic"
            ]

    def temp(self):
        print(self.command)

    def doc_login(self, id):
        self.doc_dialog = QDialog(self)
        self.log = log_doc()
        self.log.setupUi(self.doc_dialog)

        self.log.pushButton.clicked.connect(self.doctors_menu_enter)
        self.log.pushButton_2.clicked.connect(self.doc_log_out)

        user_info = QSqlQuery(f"SELECT * FROM `doctors` where `doctor_id` = '{int(id)}'")
        if user_info.next():
            self.doc_id = user_info.value(0)
            lst_name = user_info.value(1)
            frt_name = user_info.value(2)
            mdl_name = user_info.value(3)
            spec = user_info.value(6)
            at = user_info.value(7)
            wf = user_info.value(8)
            ph = user_info.value(9)
            exp = user_info.value(10)

        self.log.label_ln.setText(lst_name)
        self.log.label_fn.setText(frt_name)
        self.log.label_mn.setText(mdl_name)
        self.log.label_spc.setText(spec)
        self.log.label_phn.setText(ph)
        self.log.label_wsk.setText(f"{exp} років")
        self.log.label_wfm.setText(wf)
        self.log.label_aty.setText(at)


        self.doc_dialog.exec()

    def doc_log_out(self):
        self.doc_dialog.close()

        self.login_window = QWidget()
        self.login = login_ui()
        self.login.setupUi(self.login_window)

        self.login.pushButton.clicked.connect(self.log_in)
        self.login.pushButton_2.clicked.connect(self.registr)

        self.action_log(self.usrid, "Вихід з аккаунту (лікар)", f"Користувач {self.usrid} вийшов з аккаунту {self.doc_id}")

        self.login_window.show()

    def user_log_out(self):
        self.user_dialog.close()

        self.login_window = QWidget()
        self.login = login_ui()
        self.login.setupUi(self.login_window)

        self.login.pushButton.clicked.connect(self.log_in)
        self.login.pushButton_2.clicked.connect(self.registr)

        self.action_log(self.usrid, "Вихід з аккаунту (користувач)", f"Користувач {self.usrid} вийшов з аккаунту {self.log.user_id}")

        self.login_window.show()

    def adm_log_out(self):
        self.adm_dialog.close()

        self.login_window = QWidget()
        self.login = login_ui()
        self.login.setupUi(self.login_window)

        self.login.pushButton.clicked.connect(self.log_in)
        self.login.pushButton_2.clicked.connect(self.registr)

        self.action_log(self.usrid, "Вихід з аккаунту (адмін)", f"Користувач {self.usrid} вийшов з аккаунту {self.adm_id}")

        self.login_window.show()


    def registr(self):
        dialog = QDialog(self)
        self.rety = reg_type()
        self.rety.setupUi(dialog)
        dialog.exec()

    def onChanged(self, index):
        text = self.ui.comboBox.currentText()
        self.t_index = text
        self.model.setTable(self.t_index)
        self.model.select()

    def addRow(self):
        self.action_log(self.usrid, "додано новий рядок в бд", f"Користувач {self.usrid} додав новий рядок в бд у меню реагування БД")
        row_count = self.model.rowCount()
        self.model.insertRow(row_count)
        self.model.submitAll()
        self.model.select

    def delRow(self):
        self.action_log(self.usrid, "видалено рядок в бд", f"Користувач {self.usrid} видалив рядок в бд у меню реагування БД")
        selected_row = self.ui.tableView.currentIndex().row()
        self.model.removeRow(selected_row)
        self.model.submitAll()
        self.model.select()

    def ow_exec(self, s):
        self.ow_dialog = QDialog(self)
        self.ow = one_word()
        self.ow.setupUi(self.ow_dialog)

        self.ow.label.setText(s)
        self.ow.pushButton.clicked.connect(self.ow_ok_button)

        self.ow_dialog.exec()

    def ow_ok_button(self):
        self.ow_text = self.ow.lineEdit.text()
        print(self.ow_text)
        self.ow_dialog.close()

    def betw_tw_dat(self, s):
        self.btwd_dialog = QDialog(self)
        self.btwd = b2d()
        self.btwd.setupUi(self.btwd_dialog)

        self.btwd.label.setText(s)
        self.btwd.pushButton.clicked.connect(self.btwd_ok_button)

        self.btwd_dialog.exec()

    def btwd_ok_button(self):
        from_d = self.btwd.dateEdit.date()
        to_d = self.btwd.dateEdit_2.date()

        self.from_date = from_d.toString("yyyy.MM.dd")
        self.to_date = to_d.toString("yyyy.MM.dd")

        self.btwd_dialog.close()

    def word_and_dates(self, s, st):
        self.wnd_dialog = QDialog(self)
        self.wnd = wordndates()
        self.wnd.setupUi(self.wnd_dialog)

        self.wnd.label.setText(s)
        self.wnd.label_2.setText(st)
        self.wnd.pushButton.clicked.connect(self.wnd_ok)

        self.wnd_dialog.exec()

    def wnd_ok(self):
        self.word = self.wnd.lineEdit.text()
        date1 = self.wnd.dateEdit.date()
        date2 = self.wnd.dateEdit_2.date()

        self.date_1 = date1.toString("yyyy.MM.dd")
        self.date_2 = date2.toString("yyyy.MM.dd")

        self.wnd_dialog.close()

    def year_n_month_exec(self, s):
        self.ynm_dialog = QDialog(self)
        self.ynm = year_n_month()
        self.ynm.setupUi(self.ynm_dialog)

        self.ynm.label.setText(s)
        self.ynm.pushButton.clicked.connect(self.ynm_ok)

        self.ynm_dialog.exec()

    def ynm_ok(self):
        self.y = self.ynm.lineEdit_2.text()
        self.m = self.ynm.lineEdit.text()

        self.ynm_dialog.close()

    def openQueries(self):
        self.dialog = QDialog(self)
        self.ui_dialog = Ui_Dialog()
        self.ui_dialog.setupUi(self.dialog)
        self.query_model = QSqlQueryModel(self)
        self.query_text = """
        SELECT p.patient_id, p.name AS patient_name, p.species, p.breed, p.age, p.weight_kg, o.owner_id, o.last_name, o.first_name, o.middle_name
        FROM Patients p
        JOIN Owners o ON p.owner_id = o.owner_id
        """

        self.ui_dialog.pushButton.clicked.connect(self.admins_menu_enter)
        self.ui_dialog.pushButton_2.clicked.connect(self.dialog.close)
        self.ui_dialog.pushButton_4.clicked.connect(self.executeQuery)
        self.ui_dialog.comboBox_2.addItems(admin_queries)
        self.ui_dialog.comboBox_2.currentIndexChanged.connect(self.choseQuery)
        self.ui_dialog.pushButton_5.clicked.connect(self.save_to_pdf)

        self.dialog.exec()

    def executeQuery(self):

        if self.query_text:
            self.query_model.setQuery(self.query_text)

            if self.query_model.lastError().isValid():
                print(f"Помилка виконання запиту: {self.query_model.lastError().text()}")
            else:
                self.ui_dialog.tableView_2.setModel(self.query_model)

        self.action_log(self.usrid, "Відправка запиту (адмін)", f"{self.ui_dialog.comboBox_2.currentText()}")






    def choseQuery(self, index):
        if index == 0:
            self.query_text = """
                SELECT p.patient_id, p.name AS patient_name, p.species, p.breed, p.age, p.weight_kg, 
                       o.owner_id, o.last_name, o.first_name, o.middle_name
                FROM Patients p
                JOIN Owners o ON p.owner_id = o.owner_id
                """
        elif index == 1:
            s = "Введіть кличку"
            self.ow_exec(s)
            p_name = self.ow_text
            self.query_text = f"""
                SELECT * FROM Patients WHERE name = '{p_name}'
                """
        elif index == 2:
            s = "Введіть певний вид"
            self.ow_exec(s)
            sp = self.ow_text
            self.query_text = f"""
                SELECT * FROM Patients WHERE species = '{sp}'
                """
        elif index == 3:
            s = "Введіть id певного власника"
            self.ow_exec(s)
            u_id = self.ow_text
            self.query_text = f"""
                SELECT p.* 
                FROM Patients p
                JOIN Owners o ON p.owner_id = o.owner_id
                WHERE o.owner_id = '{u_id}'
                """
        elif index == 4:
            self.query_text = """
                SELECT COUNT(*) AS total_patients FROM Patients
                """
        elif index == 5:
            s = "Введіть id пацієнта"
            self.ow_exec(s)
            p_id = self.ow_text
            self.query_text = f"""
                SELECT EXISTS (SELECT 1 FROM Patients WHERE patient_id = '{p_id}') AS patient_exists
                """
        elif index == 6:
            s = "Введіть id певного власника"
            self.ow_exec(s)
            u_id = self.ow_text
            self.query_text = f"""
                SELECT a.appointment_id, a.patient_id, a.doctor_id, a.appointment_date, a.appointment_time, a.status
                FROM Appointments a
                JOIN Patients p ON a.patient_id = p.patient_id
                WHERE p.owner_id = '{u_id}'
                """
        elif index == 7:
            s = 'Введить місяць та рік'
            self.year_n_month_exec(s)
            year = self.y
            month = self.m
            self.query_text = f"""
                SELECT d.doctor_id, d.last_name, d.first_name, COUNT(a.appointment_id) AS appointment_count
                FROM Doctors d
                LEFT JOIN Appointments a ON d.doctor_id = a.doctor_id
                WHERE YEAR(a.appointment_date) = '{year}' AND MONTH(a.appointment_date) = '{month}'
                GROUP BY d.doctor_id, d.last_name, d.first_name
                """
        elif index == 8:
            s = "Введіть id певного пацієнта"
            self.ow_exec(s)
            p_id = self.ow_text
            self.query_text = f"""
                SELECT EXISTS (
                    SELECT 1 
                    FROM Appointments 
                    WHERE patient_id = '{p_id}' AND status = 'очікує'
                ) AS has_active_appointments
                """
        elif index == 9:
            s = "Введіть id певного пацієнта"
            self.ow_exec(s)
            p_id = self.ow_text
            self.query_text = f"""
                SELECT t.treatment_id, t.diagnosis, t.prescribed_treatment, t.visit_date, t.service_cost,
                       d.last_name AS doctor_last_name, d.first_name AS doctor_first_name
                FROM Treatments t
                JOIN Doctors d ON t.doctor_id = d.doctor_id
                WHERE t.patient_id = '{p_id}'
                """
        elif index == 10:
            s = "Введіть id певного пацієнта"
            self.ow_exec(s)
            p_id = self.ow_text
            self.query_text = f"""
                SELECT DISTINCT d.doctor_id, d.last_name, d.first_name, d.specialization
                FROM Doctors d
                JOIN Treatments t ON d.doctor_id = t.doctor_id
                WHERE t.patient_id = '{p_id}'
                """
        elif index == 11:
            s = "Введіть певний діагноз"
            self.ow_exec(s)
            diag = self.ow_text
            self.query_text = f"""
                SELECT p.patient_id, p.name, p.species, p.breed
                FROM Patients p
                JOIN Treatments t ON p.patient_id = t.patient_id
                WHERE t.diagnosis = '{diag}'
                """
        elif index == 12:
            s = "Введіть період між датами"
            self.betw_tw_dat(s)
            d1 = self.from_date
            d2 = self.to_date
            self.query_text = f"""
                SELECT SUM(service_cost) AS total_revenue
                FROM Treatments
                WHERE visit_date BETWEEN '{d1}' AND '{d2}'
                """
        elif index == 13:
            s = "Введіть період між датами"
            self.betw_tw_dat(s)
            d1 = self.from_date
            d2 = self.to_date
            self.query_text = f"""
                SELECT d.doctor_id, d.last_name, d.first_name, SUM(t.service_cost) AS total_revenue
                FROM Doctors d
                JOIN Treatments t ON d.doctor_id = t.doctor_id
                WHERE t.visit_date BETWEEN '{d1}' AND '{d2}'
                GROUP BY d.doctor_id, d.last_name, d.first_name
                """
        elif index == 14:
            self.query_text = """
                SELECT AVG(service_cost) AS average_cost
                FROM Treatments
                """
        elif index == 15:
            self.query_text = """
                SELECT prescribed_treatment, SUM(service_cost) AS total_revenue
                FROM Treatments
                GROUP BY prescribed_treatment
                ORDER BY total_revenue DESC
                LIMIT 10
                """
        elif index == 16:
            s = "Введіть id клієнта"
            st = "Введіть певний період"
            self.word_and_dates(s, st)
            u_id = self.word
            d1 = self.date_1
            d2 = self.date_2
            self.query_text = f"""
                SELECT SUM(t.service_cost) AS total_expenses
                FROM Treatments t
                JOIN Patients p ON t.patient_id = p.patient_id
                WHERE p.owner_id = '{u_id}' AND t.visit_date BETWEEN '{d1}' AND '{d2}'
                """
        elif index == 17:
            s = 'Введить місяць та рік'
            self.year_n_month_exec(s)
            year = self.y
            month = self.m
            self.query_text = f"""
                SELECT DATE(visit_date) AS treatment_date, SUM(service_cost) AS daily_revenue
                FROM Treatments
                WHERE YEAR(visit_date) = '{year}' AND MONTH(visit_date) = '{month}'
                GROUP BY DATE(visit_date)
                """
        elif index == 18:
            self.query_text = """
                SELECT SUM(t.service_cost) AS total_debt
                FROM Treatments t
                JOIN Patients p ON t.patient_id = p.patient_id
                WHERE t.payment_status = 'Unpaid'
                """
        elif index == 19:
            self.query_text = """
                SELECT YEAR(visit_date) AS year, MONTH(visit_date) AS month,
                       SUM(service_cost) AS monthly_revenue
                FROM Treatments
                WHERE visit_date >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
                GROUP BY YEAR(visit_date), MONTH(visit_date)
                ORDER BY year, month
                """
        elif index == 20:
            s = 'Введить місяць та рік'
            self.year_n_month_exec(s)
            year = self.y
            month = self.m
            self.query_text = f"""
                SELECT prescribed_treatment, COUNT(*) AS treatment_count
                FROM Treatments
                WHERE YEAR(visit_date) = '{year}' AND MONTH(visit_date) = '{month}'
                GROUP BY prescribed_treatment
                ORDER BY treatment_count DESC
                """
        elif index == 21:
            s = "Введіть рік"
            self.ow_exec(s)
            year = self.ow_text
            self.query_text = f"""
                SELECT diagnosis, COUNT(*) AS diagnosis_count
                FROM Treatments
                WHERE YEAR(visit_date) = '{year}'
                GROUP BY diagnosis
                ORDER BY diagnosis_count DESC
                LIMIT 10
                """
        elif index == 22:
            s = "Введіть певний діагноз"
            self.ow_exec(s)
            diag = self.ow_text
            self.query_text = f"""
                SELECT AVG(p.age) AS average_age
                FROM Patients p
                JOIN Treatments t ON p.patient_id = t.patient_id
                WHERE t.diagnosis = '{diag}'
                """
        elif index == 23:
            s = "Введіть певний діагноз"
            self.ow_exec(s)
            diag = self.ow_text
            self.query_text = f"""
                SELECT p.breed, COUNT(*) AS diagnosis_count
                FROM Patients p
                JOIN Treatments t ON p.patient_id = t.patient_id
                WHERE t.diagnosis = '{diag}'
                GROUP BY p.breed
                ORDER BY diagnosis_count DESC
                """
        elif index == 24:
            s = "Введіть рік"
            self.ow_exec(s)
            p_id = self.ow_text
            self.query_text = f"""
                SELECT YEAR(visit_date) AS year, MONTH(visit_date) AS month,
                       diagnosis, COUNT(*) AS diagnosis_count
                FROM Treatments
                WHERE YEAR(visit_date) = '{year}'
                GROUP BY YEAR(visit_date), MONTH(visit_date), diagnosis
                """
        elif index == 25:
            self.query_text = """
                SELECT p.species, COUNT(t.treatment_id) AS treatment_count
                FROM Patients p
                JOIN Treatments t ON p.patient_id = t.patient_id
                WHERE p.species IN ('Кіт', 'Собака')
                GROUP BY p.species
                """
        elif index == 26:
            self.query_text = """
                SELECT t1.diagnosis AS diagnosis1, t2.diagnosis AS diagnosis2, COUNT(*) AS combo_count
                FROM Treatments t1
                JOIN Treatments t2 ON t1.patient_id = t2.patient_id AND t1.treatment_id < t2.treatment_id
                GROUP BY t1.diagnosis, t2.diagnosis
                ORDER BY combo_count DESC
                LIMIT 10
                """
        elif index == 27:
            s = "Введіть певний діагноз"
            self.ow_exec(s)
            diag = self.ow_text
            self.query_text = f"""
                SELECT d.doctor_id, d.last_name, d.first_name, COUNT(*) AS treatment_count
                FROM Doctors d
                JOIN Treatments t ON d.doctor_id = t.doctor_id
                WHERE t.diagnosis = '{diag}'
                GROUP BY d.doctor_id, d.last_name, d.first_name
                ORDER BY treatment_count DESC
                LIMIT 1
                """
        elif index == 28:
            self.query_text = """
                SELECT p.patient_id, p.name, t.diagnosis
                FROM Patients p
                JOIN Treatments t ON p.patient_id = t.patient_id
                WHERE t.diagnosis IN (
                    SELECT diagnosis 
                    FROM Treatments 
                    GROUP BY diagnosis 
                    HAVING COUNT(*) < 5
                )
                """
        elif index == 29:
            self.query_text = """
                SELECT * FROM Doctors ORDER BY specialization
                """
        elif index == 30:
            s = "Введіть певний вид тварин (Наприклад, Котові)"
            self.ow_exec(s)
            sp = self.ow_text
            self.query_text = f"""
                SELECT * FROM Doctors WHERE animal_type = '{sp}'
                """
        elif index == 31:
            self.query_text = """
                SELECT * FROM Doctors ORDER BY experience_years DESC LIMIT 10
                """
        elif index == 32:
            self.query_text = """
                SELECT d.doctor_id, d.last_name, d.first_name, COUNT(a.appointment_id) AS appointment_count
                FROM Doctors d
                JOIN Appointments a ON d.doctor_id = a.doctor_id
                GROUP BY d.doctor_id, d.last_name, d.first_name
                ORDER BY appointment_count DESC
                """
        elif index == 33:
            self.query_text = """
                SELECT d.doctor_id, d.last_name, d.first_name, a.appointment_date, a.appointment_time
                FROM Doctors d
                LEFT JOIN Appointments a ON d.doctor_id = a.doctor_id
                WHERE a.appointment_date BETWEEN CURDATE() AND DATE_ADD(CURDATE(), INTERVAL 7 DAY)
                ORDER BY d.doctor_id, a.appointment_date, a.appointment_time
                """
        elif index == 34:
            s = "Введіть певний рівень кваліфікації(в роках)"
            self.ow_exec(s)
            sp = self.ow_text
            self.query_text = f"""
                SELECT * FROM Doctors WHERE specialization = '{sp}'
                """
        elif index == 35:
            self.query_text = """
                SELECT * FROM Doctors WHERE work_format IN ('By Appointment', 'Emergency Calls')
                """

    def choseQueryDoctor(self, index):
        if index == 0:
            self.query_text1 = f"""
            SELECT DISTINCT p.patient_id, p.name, p.species, p.breed
            FROM Patients p
            JOIN Treatments t ON p.patient_id = t.patient_id
            WHERE t.doctor_id = '{self.doc_id}'
            """
        elif index == 1:
            s = "Введіть певну дату"
            self.ow_exec(s)
            date = self.ow_text
            self.query_text1 = f"""
            SELECT time_slot
            FROM (
                SELECT '08:00' AS time_slot UNION SELECT '08:30' UNION SELECT '09:00' UNION SELECT '09:30' 
                UNION SELECT '10:00' UNION SELECT '10:30' UNION SELECT '11:00' UNION SELECT '11:30'
            ) AS slots
            WHERE time_slot NOT IN (
                SELECT appointment_time 
                FROM Appointments 
                WHERE doctor_id = '{self.doc_id}' AND appointment_date = '{date}' AND status = 'очікує'
            )
            """
        elif index == 2:
            s = "Введіть id певного пацієнта"
            self.ow_exec(s)
            p_id = self.ow_text
            self.query_text1 = f"""
            SELECT a.appointment_id, a.doctor_id, a.appointment_date, a.appointment_time, a.status
            FROM Appointments a
            WHERE a.patient_id = '{p_id}' AND a.doctor_id = '{self.doc_id}'
            """
        elif index == 3:
            self.query_text1 = f"""
            SELECT t.treatment_id, t.patient_id, t.diagnosis, t.prescribed_treatment, t.visit_date, t.service_cost
            FROM Treatments t
            WHERE t.doctor_id = '{self.doc_id}'
            """
        elif index == 4:
            s = "Введіть певну дату"
            self.ow_exec(s)
            date = self.ow_text
            self.query_text1 = f"""
            SELECT a.appointment_id, a.patient_id, a.doctor_id, a.appointment_date, a.appointment_time, a.status
            FROM Appointments a
            WHERE a.doctor_id = '{self.doc_id}' AND a.appointment_date = '{date}'
            """
        elif index == 5:
            self.query_text1 = f"""
            SELECT a.appointment_id, a.patient_id, a.appointment_date, a.appointment_time
            FROM Appointments a
            WHERE a.doctor_id = '{self.doc_id}' AND a.appointment_date BETWEEN CURDATE() AND DATE_ADD(CURDATE(), INTERVAL 7 DAY)
            ORDER BY a.appointment_date, a.appointment_time
            """
        elif index == 6:
            self.query_text = f"""
            SELECT p.patient_id, p.name AS patient_name, p.species, p.breed, p.age, p.weight_kg,
                    o.owner_id, o.last_name, o.first_name, o.middle_name
            FROM Patients p
            JOIN Owners o ON p.owner_id = o.owner_id
            JOIN Treatments t ON p.patient_id = t.patient_id
            WHERE t.doctor_id = '{self.doc_id}'
            """
        elif index == 7:
            s = "Введіть певну кличку"
            self.ow_exec(s)
            name = self.ow_text
            self.query_text = f"""
            SELECT * FROM Patients WHERE name = '{name}' 
            """
        elif index == 8:
            s = "Введіть певний вид"
            self.ow_exec(s)
            spec = self.ow_text
            self.query_text = f"""
            SELECT * FROM Patients WHERE species = '{spec}'
            """
        elif index == 9:
            s = "Введіть id певного пацієнта"
            self.ow_exec(s)
            p_id = self.ow_text
            self.query_text = f"""
            SELECT EXISTS (SELECT 1 FROM Patients WHERE patient_id = '{p_id}') AS patient_exists
            """
        elif index == 10:
            s = "Введіть певний рік"
            self.ow_exec(s)
            year = self.ow_text
            self.query_text = f"""
                SELECT diagnosis, COUNT(*) AS diagnosis_count
                FROM Treatments
                WHERE YEAR(visit_date) = '{year}' AND doctor_id = '{self.doc_id}'
                GROUP BY diagnosis
                ORDER BY diagnosis_count DESC
                LIMIT 10
                """
        elif index == 11:
            s = "Введіть певний діагноз"
            self.ow_exec(s)
            diag = self.ow_text
            self.query_text = f"""
                SELECT AVG(p.age) AS average_age
                FROM Patients p
                JOIN Treatments t ON p.patient_id = t.patient_id
                WHERE t.diagnosis = '{diag}' AND t.doctor_id = '{self.doc_id}'
                """
        elif index == 12:
            s = "Введіть певний діагноз"
            self.ow_exec(s)
            diag = self.ow_text
            self.query_text = f"""
                SELECT p.breed, COUNT(*) AS diagnosis_count
                FROM Patients p
                JOIN Treatments t ON p.patient_id = t.patient_id
                WHERE t.diagnosis = '{diag}' AND t.doctor_id = '{self.doc_id}'
                GROUP BY p.breed
                ORDER BY diagnosis_count DESC
                """
        elif index == 13:
            s = "Введіть певний рік"
            self.ow_exec(s)
            year = self.ow_text
            self.query_text = f"""
                SELECT YEAR(visit_date) AS year, MONTH(visit_date) AS month, 
                       diagnosis, COUNT(*) AS diagnosis_count
                FROM Treatments
                WHERE YEAR(visit_date) = '{year}' AND doctor_id = '{self.doc_id}'
                GROUP BY YEAR(visit_date), MONTH(visit_date), diagnosis
                """
        elif index == 14:
            self.query_text = f"""
                SELECT p.species, COUNT(t.treatment_id) AS treatment_count
                FROM Patients p
                JOIN Treatments t ON p.patient_id = t.patient_id
                WHERE p.species IN ('Cat', 'Dog') AND t.doctor_id = '{self.doc_id}'
                GROUP BY p.species
                """
        elif index == 15:
            self.query_text = f"""
                SELECT t1.diagnosis AS diagnosis1, t2.diagnosis AS diagnosis2, COUNT(*) AS combo_count
                FROM Treatments t1
                JOIN Treatments t2 ON t1.patient_id = t2.patient_id AND t1.treatment_id < t2.treatment_id
                WHERE t1.doctor_id = '{self.doc_id}' AND t2.doctor_id = '{self.doc_id}'
                GROUP BY t1.diagnosis, t2.diagnosis
                ORDER BY combo_count DESC
                LIMIT 10
                """


    def choseQueryOwner(self, index):
        if index == 0:
            self.query_text2 = f"""
            SELECT a.appointment_id, a.patient_id, p.name AS patient_name, a.doctor_id,
                   d.last_name AS doctor_last_name, a.appointment_date, a.appointment_time, a.status
            FROM Appointments a
            JOIN Patients p ON a.patient_id = p.patient_id
            JOIN Doctors d ON a.doctor_id = d.doctor_id
            WHERE p.owner_id = '{self.log.user_id}'
            """
        elif index == 1:
            s = "Введіть id певного пацієнта"
            self.ow_exec(s)
            p_id = self.ow_text
            self.query_text2 = f"""
            SELECT a.appointment_id, a.appointment_date, a.appointment_time, t.diagnosis, 
                   t.prescribed_treatment, t.service_cost
            FROM Appointments a
            LEFT JOIN Treatments t ON a.patient_id = t.patient_id AND a.appointment_date = t.visit_date
            JOIN Patients p ON a.patient_id = p.patient_id
            WHERE a.patient_id = '{p_id}' AND p.owner_id = '{self.log.user_id}'
            """
        elif index == 2:
            s = "Введіть певний період"
            self.betw_tw_dat(s)
            d1 = self.from_date
            d2 = self.to_date
            self.query_text2 = f"""
            SELECT a.appointment_id, a.patient_id, p.name AS patient_name, a.doctor_id, 
                   d.last_name AS doctor_last_name, a.appointment_date, a.appointment_time, a.status
            FROM Appointments a
            JOIN Patients p ON a.patient_id = p.patient_id
            JOIN Doctors d ON a.doctor_id = d.doctor_id
            WHERE p.owner_id = '{self.log.user_id}' AND a.appointment_date BETWEEN '{d1}' AND '{d2}'
            """
        elif index == 3:
            s = "Введіть певний статус"
            self.ow_exec(s)
            stat = self.ow_text
            print(stat)
            self.query_text2 = f"""
            SELECT a.appointment_id, a.patient_id, p.name AS patient_name, a.doctor_id, 
                   d.last_name AS doctor_last_name, a.appointment_date, a.appointment_time, a.status
            FROM Appointments a
            JOIN Patients p ON a.patient_id = p.patient_id
            JOIN Doctors d ON a.doctor_id = d.doctor_id
            WHERE p.owner_id = '{self.log.user_id}' AND a.status = '{stat}';
            """
        elif index == 4:
            self.query_text2 = f"""
            SELECT p.patient_id, p.name, p.species, p.breed, p.age, p.weight_kg
            FROM Patients p
            WHERE p.owner_id = '{self.log.user_id}'
            """
        elif index == 5:
            s = "Введіть id пацієнта"
            st = "Введіть певний період"
            self.word_and_dates(s, st)
            p_id = self.word
            d1 = self.date_1
            d2 = self.date_2
            self.query_text2 = f"""
            SELECT SUM(t.service_cost) AS total_cost
            FROM Treatments t
            JOIN Patients p ON t.patient_id = p.patient_id
            WHERE t.patient_id = '{p_id}' AND p.owner_id = '{self.log.user_id}' AND t.visit_date BETWEEN '{d1}' AND '{d2}'
            """
        elif index == 6:
            s = "Введіть id певного пацієнта"
            self.ow_exec(s)
            p_id = self.ow_text
            self.query_text2 = f"""
            SELECT DISTINCT t.diagnosis
            FROM Treatments t
            JOIN Patients p ON t.patient_id = p.patient_id
            WHERE t.patient_id = '{p_id}' AND p.owner_id = '{self.log.user_id}'
            """
        elif index == 7:
            s = "Введіть певну кличку"
            self.ow_exec(s)
            name = self.ow_text
            self.query_text = f"""
                SELECT * FROM Patients WHERE name = '{name}' AND owner_id = '{self.log.user_id}'
                """
        elif index == 8:
            s = "Введіть певний вид"
            self.ow_exec(s)
            spec = self.ow_text
            self.query_text = f"""
                SELECT * FROM Patients WHERE species = '{spec}' AND owner_id = '{self.log.user_id}'
                """
        elif index == 9:
            s = "Введіть id певного пацієнта"
            self.ow_exec(s)
            p_id = self.ow_text
            self.query_text = f"""
                SELECT EXISTS (SELECT 1 FROM Patients WHERE patient_id = '{p_id}' AND owner_id = '{self.log.user_id}') AS patient_exists
                """

    def insTD(self):
        text, ok = QInputDialog.getText(self, "Введіть значення", "")

        if ok and text:
            print(text)
            self.arg = text

    def generate_pdf(combo_text, table_data, file_name="report.pdf"):
        pdfmetrics.registerFont(TTFont('DejaVuSansCondensed', 'DejaVuSansCondensed.ttf'))

        doc = SimpleDocTemplate(file_name, pagesize=landscape(letter))
        elements = []

                # Створення заголовка
        styles = getSampleStyleSheet()
        title_style = styles['Title']
        title_style.fontName = 'DejaVuSansCondensed'

        title = Paragraph(combo_text, title_style)
        elements.append(title)

                # Додавання таблиці
        table = Table(table_data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, -1), 'DejaVuSansCondensed'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))

        elements.append(table)
        doc.build(elements)

            # Додайте метод для збереження у PDF у ваш клас
    def save_to_pdf(self):
        combo_text = self.ui_dialog.comboBox_2.currentText()  # Текст з comboBox_2
        if not combo_text:
            print("Помилка: Комбо-бокс порожній")
            return

                # Отримання даних з моделі
        table_data = []
        for row in range(self.query_model.rowCount()):
            row_data = []
            for column in range(self.query_model.columnCount()):
                index = self.query_model.index(row, column)
                row_data.append(self.query_model.data(index))
            table_data.append(row_data)

                # Додавання заголовків колонок
        headers = [self.query_model.headerData(i, Qt.Horizontal) for i in range(self.query_model.columnCount())]
        table_data.insert(0, headers)

                # Формування PDF
        try:
            DBUI.generate_pdf(combo_text, table_data, file_name=f"query_{combo_text}.pdf")
            print("Звіт збережено у файлі query_report.pdf")
        except Exception as e:
            print(f"Помилка при створенні PDF: {e}")

        for row in table_data:
            print(row)


    def save_to_pdf1(self):
        combo_text = self.docmenu.comboBox.currentText()
        if not combo_text:
            print("Помилка: Комбо-бокс порожній")
            return

                        # Отримання даних з моделі
        table_data = []
        for row in range(self.query_model1.rowCount()):
            row_data = []
            for column in range(self.query_model1.columnCount()):
                index = self.query_model1.index(row, column)
                row_data.append(self.query_model1.data(index))
            table_data.append(row_data)

                        # Додавання заголовків колонок
        headers = [self.query_model1.headerData(i, Qt.Horizontal) for i in range(self.query_model1.columnCount())]
        table_data.insert(0, headers)

                        # Формування PDF
        try:
            DBUI.generate_pdf(combo_text, table_data, file_name=f"query_{combo_text}.pdf")
            print("Звіт збережено у файлі query_report.pdf")
        except Exception as e:
            print(f"Помилка при створенні PDF: {e}")

        for row in table_data:
            print(row)




    def backup_database(self):
        save_path, _ = QFileDialog.getSaveFileName(self, "Зберегти резервну копію", "", "SQL файли (*.sql)")
        if not save_path:
            return

        try:
            command = [
                "mysqldump",
                "-h", "25.44.219.6",
                "-P", "3812",
                "-u", "ubuntu_root",
                f"-p1111",
                "vet_clinic"
            ]
            with open(save_path, "w", encoding="utf-8") as outfile:
                subprocess.run(command, stdout=outfile, check=True)
            QMessageBox.information(self, "Успіх", "Резервна копія створена успішно.")
            self.action_log(self.usrid, "Створено бекап бази даних", "")
        except subprocess.CalledProcessError as e:
            QMessageBox.critical(self, "Помилка", f"Не вдалося створити резервну копію:\n{e}")

    def backup_database_tables(self):
        save_path, _ = QFileDialog.getSaveFileName(self, "Зберегти резервну копію", "", "SQL файли (*.sql)")
        if not save_path:
            return

        try:
            command = self.command
            with open(save_path, "w", encoding="utf-8") as outfile:
                subprocess.run(command, stdout=outfile, check=True)
            QMessageBox.information(self, "Успіх", "Резервна копія створена успішно.")
            self.action_log(self.usrid, "Створено бекап деяких таблиць бази даних", "")
        except subprocess.CalledProcessError as e:
            QMessageBox.critical(self, "Помилка", f"Не вдалося створити резервну копію:\n{e}")


    def restore_database(self):
        load_path, _ = QFileDialog.getOpenFileName(self, "Вибрати файл резервної копії", "", "SQL файли (*.sql)")
        if not load_path:
            return

        try:
            command = [
                "mysql",
                "-h", "25.44.219.6",
                "-P", "3812",
                "-u", "ubuntu_root",
                f"-p1111",
                "vet_clinic"
            ]
            with open(load_path, "r", encoding="utf-8") as infile:
                subprocess.run(command, stdin=infile, check=True)
            QMessageBox.information(self, "Успіх", "Базу даних успішно відновлено.")
            self.action_log(self.usrid, "Відновлено бекап бази даних", "")
        except subprocess.CalledProcessError as e:
            QMessageBox.critical(self, "Помилка", f"Не вдалося відновити базу даних:\n{e}")

    def action_log(self, userid, a_type, descr):
        dt = datetime.datetime.now()
        a_date = dt.strftime('%Y.%m.%d')
        a_time = dt.strftime('%H:%M:%S')
        add_log = QSqlQuery()
        add_log.exec(f"""
        INSERT INTO `user_actions_log` (`log_id`, `user_id`, `action_type`, `description`, `action_date`, `action_time`)
        VALUES (NULL, '{userid}', '{a_type}', '{descr}', '{a_date}', '{a_time}')
        """)





owner_queries = [
    "Вивести всі власні записи",
    "Відобразити всі записи конкретної тварини з діагнозом, лікуванням та вартістю",
    "Вивести всі записи за певний період",
    "Вивести записи певного статусу",
    "Відобразити всіх тварин та інформацію про них",
    "Визначити загальну вартість лікування тварини за певний період",
    "Отримати список усіх діагнозів тварини",
    "Знайти свою тварину за кличкою",
    "Отримати список своїх тварин певного виду",
    "Перевірити, чи існує своя тварина із заданим ID"
]


doctor_queries = [
    "Отримати список пацієнтів, які лікувалися у лікаря",
    "Отримати всі записи лікаря на певний день",
    "Визначити вільні часові слоти для запису",
    "Знайти всі записи певного пацієнта та їх статуси",
    "Отримати історію лікувань, проведених лікарем",
    "Вивести графік роботи лікаря на поточний тиждень",
    "Отримати список своїх пацієнтів із зазначенням власників",
    "Знайти пацієнта за кличкою",
    "Отримати список пацієнтів певного виду",
    "Перевірити, чи існує пацієнт із заданим ID",
    "Отримати список найпоширеніших діагнозів лікаря за рік",
    "Визначити середній вік своїх пацієнтів із певним захворюванням",
    "Визначити породи тварин, схильні до певного захворювання (лікар)",
    "Отримати свою статистику захворювань по місяцях",
    "Визначити співвідношення лікувань між котами та собаками (лікар)",
    "Знайти найчастіші комбінації діагнозів у своїх пацієнтів"
]


admin_queries = [
    "Отримати список усіх пацієнтів із зазначенням їхніх власників",
    "Знайти пацієнта за кличкою",
    "Отримати список пацієнтів певного виду",
    "Отримати список пацієнтів певного власника",
    "Порахувати загальну кількість зареєстрованих пацієнтів",
    "Перевірити, чи існує пацієнт із заданим ID",
    "Отримати список записів для певного власника",
    "Отримати кількість прийомів всіх лікарів за місяць",
    "Перевірити, чи є у пацієнта активні записи",
    "Отримати історію лікувань конкретного пацієнта",
    "Визначити лікарів, які лікували конкретного пацієнта",
    "Отримати список усіх пацієнтів по вказаному діагнозу",
    "Отримати загальний дохід клініки за певний період",
    "Визначити дохід по кожному лікарю",
    "Порахувати середню вартість одного прийому",
    "Отримати список найприбутковіших послуг",
    "Визначити суму витрат клієнта за певний період",
    "Отримати фінансовий звіт за місяць із розбивкою по днях",
    "Визначити сумарний борг клієнтів, якщо існує післяплата",
    "Отримати статистику змін доходу за останні 6 місяців",
    "Кількість звернень за місяць за послугами за спадним порядком",
    "Отримати список найпоширеніших діагнозів за рік",
    "Визначити середній вік пацієнтів із певним захворюванням",
    "Визначити породи тварин, схильні до певного захворювання",
    "Отримати статистику захворювань по місяцях",
    "Визначити співвідношення лікувань між котами та собаками",
    "Знайти найчастіші комбінації діагнозів у пацієнтів",
    "Визначити лікаря, який найчастіше лікує певне захворювання",
    "Отримати список пацієнтів із рідкісними діагнозами",
    "Вивести список лікарів, відсортований за спеціалізацією",
    "Знайти всіх лікарів, які працюють із певним видом тварин",
    "Вивести список лікарів із найбільшим досвідом роботи",
    "Визначити лікарів, які найчастіше проводять прийоми",
    "Вивести графік роботи лікарів на поточний тиждень",
    "Знайти лікарів із певним рівнем кваліфікації",
    "Відобразити лікарів, які працюють за попереднім записом або в екстрених викликах"
]

pet_families = {
    # Ссавці
    "Псові": ["собака", "лис", "лисиця"],
    "Котові": ["кіт", "кішка", "каракал", "сервал"],
    "Мишачі": ["хом’як", "миша", "щур"],
    "Свинкові": ["морська свинка"],
    "Шиншилові": ["шиншила"],
    "Зайцеві": ["кролик"],
    "Куницеві": ["фретка"],
    "Вивіркові": ["бурундук"],

    # Птахи
    "Папугові": ["папуга"],
    "В’юркові": ["канарка"],
    "Астрильдові": ["амадина"],

    # Рептилії
    "Черепахові": ["черепаха"],
    "Агамові": ["агама"],
    "Ігуанові": ["ігуана"],
    "Геконові": ["гекон"],
    "Удавові": ["пітон", "удав"],
    "Вужеві": ["королівська змія"],

    # Амфібії
    "Райкові": ["деревна жаба"],
    "Жаб’ячі": ["карликова жаба"],
    "Саламандрові": ["аксолотль"],

    # Риби
    "Коропові": ["золота рибка"],
    "Цихлідові": ["скалярія"],
    "Пецилієві": ["гуппі"],
    "Харацинові": ["неон"],

    "Павукові": ["павук", "скорпіон"]
}


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = DBUI()
    #widget.show()
    sys.exit(app.exec())
