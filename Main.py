from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sqlite3
import sys
from datetime import datetime
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import binascii
import os
from hashlib import pbkdf2_hmac

def hash_password(password, salt=None):
    """Hash a password with a salt using PBKDF2-HMAC-SHA256"""
    if salt is None:
        salt = binascii.hexlify(os.urandom(16)).decode('utf-8')
    iterations = 100000
    dk = pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), iterations)
    password_hash = binascii.hexlify(dk).decode('utf-8')
    return password_hash, salt


# Create a connection to the SQLite database
def get_db_connection():
    conn = sqlite3.connect("Database/database.db")
    conn.row_factory = sqlite3.Row  # Optional: for dict-like row access
    return conn

def generate_years(format_type="range", start_year= 2020, num_years=10):
    """
    Generate a list of years in either 'YYYY-YYYY' (range) or 'YYYY' (single) format.

    :param format_type: "range" for '2025-2026', "single" for '2025'
    :param start_year: The starting year (defaults to current year)
    :param num_years: How many years to generate (default 10)
    :return: List of year strings
    """
    if start_year is None:
        start_year = datetime.now().year 
    years = []
    for i in range(num_years):
        y = start_year + i
        if format_type == "range":
            years.append(f"{y}-{y+1}")
        else:
            years.append(str(y))
    return years

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pinnacle Non-Profit v1.0")
        self.setStyleSheet("Background-color:White;")
        # Set Window structure and Design
        Layout = QHBoxLayout()
        Layout.setContentsMargins(0, 0, 0, 0)
        Layout.setSpacing(0)
        # Create the sidebar and main body
        # Sidebar
        Sidebar = QWidget()
        Sidebar.setMaximumWidth(225)
        Sidebar.setMinimumWidth(180)
        Sidebar.setStyleSheet("""
                              background-color: #1B263B;
                               color: white;
                               padding-left: 5px;
                              font-family: Lato-Regular;
                              """)
        SidebarLayout = QVBoxLayout()
        LogoIconFrame = QFrame()
        LogoFrameLayout = QVBoxLayout()
        LogoName = QLabel("Pinnacle Non-Profit")
        LogoName.setAlignment(Qt.AlignCenter)
        LogoName.setStyleSheet("font-size: 20px; font-weight: bold;color: white;")
        LogoIconFrame.setFixedHeight(70)
        LogoIconFrame.setStyleSheet("background-color: #1B263B;")
        LogoFrameLayout.addWidget(LogoName, alignment=Qt.AlignCenter)
        LogoIconFrame.setLayout(LogoFrameLayout)
        SidebarLayout.addWidget(LogoIconFrame, alignment=Qt.AlignTop)
        # Add a spacer and a white line between LogoIconFrame and DashboardButton
        SeparatorLine = QFrame()
        SeparatorLine.setFrameShape(QFrame.HLine)
        SeparatorLine.setFrameShadow(QFrame.Sunken)
        SeparatorLine.setStyleSheet("background-color: white;")
        SidebarLayout.addWidget(SeparatorLine)
        SidebarLayout.addSpacing(10)
        # Create sidebar buttons as variables
        self.DashboardButton = Links("Dashboard")
        self.DonorButton = Links("Donor")
        self.FundButton = Links("Fund")
        self.BudgetButton = Links("Budget")
        self.TransactionButton = Links("Transaction")
        self.CategoriesButton = Links("Categories && Subcategories")
        self.ProgramsButton = Links("Programs && Administration")
        self.ProjectsButton = Links("Projects && Activities")
        self.ReportButton = Links("Report")

        # Add buttons to sidebar layout
        SidebarLayout.addWidget(self.DashboardButton)
        SidebarLayout.addWidget(self.DonorButton)
        SidebarLayout.addWidget(self.FundButton)
        SidebarLayout.addWidget(self.BudgetButton)
        SidebarLayout.addWidget(self.TransactionButton)
        SidebarLayout.addWidget(self.CategoriesButton)
        SidebarLayout.addWidget(self.ProgramsButton)
        SidebarLayout.addWidget(self.ProjectsButton)
        SidebarLayout.addWidget(self.ReportButton)
        SidebarLayout.addStretch()
        SidebarLayout.setContentsMargins(0, 0, 0, 0)
        SidebarLayout.setSpacing(0)
        Sidebar.setLayout(SidebarLayout)
        Layout.addWidget(Sidebar, alignment=Qt.AlignLeft)
        # Main Body
        MainBody = QWidget()
        MainBodyLayout = QVBoxLayout()
        MainBodyHeader = QWidget()
        MainBodyHeader.setFixedHeight(70)
        MainBodyHeaderLayout = QHBoxLayout()
        Todaydate = QLabel("Today: " + QDate.currentDate().toString())
        Todaydate.setStyleSheet("""
            Background-color: #1E90FF;
            font-family: 'Lato', sans-serif;
            font-weight: 600;
            font-size: 18px;
            color: White;
            letter-spacing: 0.5px;
        """)
        Morebutton = QPushButton()
        Morebutton.setFlat(True)
        Morebutton.setIcon(QIcon("Icons/More.svg"))  # Put your icon in Icons/More.svg
        Morebutton.setIconSize(QSize(32, 32))  # Increased size
        Morebutton.setToolTip("More")
        Morebutton.setStyleSheet("""
            QPushButton {
            background: transparent;
            border-radius: 8px;
            padding: 6px;
            }
            QPushButton:hover {
            background: #e0e0e0;
            border-color: #1B263B;  /* Slightly lighter navy on hover */
            }
        """)
        AccountButton = QPushButton()
        AccountButton.setFlat(True)
        AccountButton.setIcon(QIcon("Icons/account.svg"))  # Put your icon in Icons/account_icon.png
        AccountButton.setIconSize(QSize(32, 32))  # Increased size
        AccountButton.setToolTip("Account")
        AccountButton.setStyleSheet("""
            QPushButton {
            background: transparent;
            border-radius: 8px;
            padding: 8px;
            }
            QPushButton:hover {
            background: #e0e0e0;
            }
        """)
        MainBodyHeaderLayout.addWidget(Todaydate, alignment=Qt.AlignLeft)
        MainBodyHeaderLayout.addStretch()
        MainBodyHeaderLayout.addWidget(AccountButton, alignment=Qt.AlignRight)
        MainBodyHeaderLayout.addWidget(Morebutton, alignment=Qt.AlignRight)
        MainBodyHeader.setLayout(MainBodyHeaderLayout)
        MainBodyHeader.setObjectName("MainBodyHeader")
        MainBodyHeader.setStyleSheet("""
            #MainBodyHeader {
               
                Background-color: #1E90FF;
                color: #20c997;                  
                border-radius: 10px;              
                padding: 20px;
                border: 2px solid #006666; 
                }
            
        """)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setXOffset(0)
        shadow.setYOffset(2)
        shadow.setColor(QColor(0, 0, 0, 100))
        MainBodyHeader.setGraphicsEffect(shadow)
        MainBodyLayout.addWidget(MainBodyHeader, alignment=Qt.AlignTop)
        # content area
        ContentArea = QStackedWidget()
        ContentArea.setStyleSheet("Background-color:White;")
        # Create the content area widgets
        DashboardWidget = DashboardPage()
        DonorsWidget = DonorsPage()
        FundsWidget = FundPage()
        BudgetsWidget = BudgetsPage()
        TransactionsWidget = TransactionsPage()
        CategoriesWidget = Categories_SubCategories()
        ProgramsWidget = Program_Admnistration()
        ProjectsWidget = Projects_Activities()
        ReportsWidget = ReportPage()
        ContentArea.addWidget(DashboardWidget)
        ContentArea.addWidget(DonorsWidget)
        ContentArea.addWidget(FundsWidget)
        ContentArea.addWidget(BudgetsWidget)
        ContentArea.addWidget(TransactionsWidget)
        ContentArea.addWidget(CategoriesWidget)
        ContentArea.addWidget(ProgramsWidget)
        ContentArea.addWidget(ProjectsWidget)
        ContentArea.addWidget(ReportsWidget)
        MainBodyLayout.addWidget(ContentArea)
        MainBody.setLayout(MainBodyLayout)
        Layout.addWidget(MainBody)
        # Set the main layout for the window
        self.setLayout(Layout)
        # Connect sidebar buttons to change content area
        self.DashboardButton.clicked.connect(lambda: ContentArea.setCurrentIndex(0))
        self.DonorButton.clicked.connect(lambda: ContentArea.setCurrentIndex(1))
        self.FundButton.clicked.connect(lambda: ContentArea.setCurrentIndex(2))
        self.BudgetButton.clicked.connect(lambda: ContentArea.setCurrentIndex(3))
        self.TransactionButton.clicked.connect(lambda: ContentArea.setCurrentIndex(4))
        self.CategoriesButton.clicked.connect(lambda: ContentArea.setCurrentIndex(5))
        self.ProgramsButton.clicked.connect(lambda: ContentArea.setCurrentIndex(6))
        self.ProjectsButton.clicked.connect(lambda: ContentArea.setCurrentIndex(7))
        self.ReportButton.clicked.connect(lambda: ContentArea.setCurrentIndex(8))

class DonorsPage(QWidget):
    def __init__(self):
        super().__init__()
        Layout = QVBoxLayout()
        self.setLayout(Layout)
        # Content header Area
        ContentAreaHeader = QWidget()
        ContentAreaHeaderLayout = QHBoxLayout()
        self.Title = Title("Donors")
        self.AddButton = button("Add", "primary", "md", icon_path="Icons/add.svg", icon_toolTip="Add New Donor")
        self.AddButton.clicked.connect(self.DonorForm)
        self.ExportButton = button("Export", "success", "md", icon_path="Icons/print.svg", icon_toolTip="Export as Pdf")
        ContentAreaHeaderLayout.addWidget(self.Title, alignment=Qt.AlignLeft)
        ContentAreaHeaderLayout.addStretch()
        ContentAreaHeaderLayout.addWidget(self.AddButton, alignment=Qt.AlignRight)
        ContentAreaHeaderLayout.addWidget(self.ExportButton, alignment=Qt.AlignRight)
        ContentAreaHeader.setLayout(ContentAreaHeaderLayout)
        Layout.addWidget(ContentAreaHeader, alignment=Qt.AlignTop)
        # Table header
        DonorTableTitle = TableTitle("Donor's List")
        TableHeader = QWidget()
        TableHeaderLayout = QHBoxLayout()
        self.SearchBar = QLineEdit()
        self.SearchBar.setClearButtonEnabled(True)
        self.SearchBar.setMinimumWidth(200)
        self.SearchBar.setPlaceholderText("Search")
        self.SearchBar.setStyleSheet(FormStyles())
        self.cancelButton = QPushButton()
        self.cancelButton.setFlat(True)
        self.cancelButton.setIcon(QIcon("Icons/cancel.svg"))
        self.cancelButton.setIconSize(QSize(16, 16))
        self.cancelButton.setToolTip("Cancel")
        self.cancelButton.setVisible(False)
        Filter = QLabel("Filter:")
        Filter.setStyleSheet("""
            color: #1B263B;
            font-size: 12px;
            font-family: Lato-light;
        """)
        self.type_filter = QComboBox()
        self.type_filter.addItem("All")
        self.type_filter.addItems(["Individual", "Government", "Organization", "Events Contribution", "Other"])
        self.type_filter.setStyleSheet(FormStyles())
        self.category_filter = QComboBox()
        self.category_filter.addItem("All")
        self.category_filter.addItems(["Regular", "Permanent", "Partnership", "Occasional", "Other"])
        self.category_filter.setStyleSheet(FormStyles())
        TableHeaderLayout.addWidget(DonorTableTitle)
        TableHeaderLayout.addStretch()
        TableHeaderLayout.addWidget(self.SearchBar, alignment=Qt.AlignRight)
        TableHeaderLayout.addWidget(self.cancelButton)
        TableHeaderLayout.addWidget(Filter)
        TableHeaderLayout.addWidget(QLabel("Type:"))
        TableHeaderLayout.addWidget(self.type_filter)
        TableHeaderLayout.addWidget(QLabel("Category:"))
        TableHeaderLayout.addWidget(self.category_filter)
        TableHeader.setLayout(TableHeaderLayout)
        Layout.addWidget(TableHeader, alignment=Qt.AlignTop)
        # Table of Donors
        self.TableofDonors = QTableWidget()
        self.TableofDonors.setStyleSheet(TableStyles())
        self.TableofDonors.setColumnCount(7)
        self.TableofDonors.setHorizontalHeaderLabels(["Name", "Address", "Contact", "Type", "Category", "Date Joined", "Actions"])
        self.TableofDonors.horizontalHeader().setStretchLastSection(True)
        self.TableofDonors.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        Layout.addWidget(self.TableofDonors)

        # Connect search and filter
        self.SearchBar.textChanged.connect(self.refresh_donor_table)
        self.type_filter.currentIndexChanged.connect(self.refresh_donor_table)
        self.category_filter.currentIndexChanged.connect(self.refresh_donor_table)

        # Initial load
        self.refresh_donor_table()

    def DonorForm(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Register New Donor")
        dialog.setStyleSheet(DialogStyles())
        layout = QVBoxLayout(dialog)
        # Title
        title = QLabel("Register New Donor")
        title.setStyleSheet("font-size: 22px; font-weight: bold; color: #1B263B; margin-bottom: 12px;")
        layout.addWidget(title, alignment=Qt.AlignHCenter)

        form = QFormLayout()
        form.setLabelAlignment(Qt.AlignRight)
        form.setFormAlignment(Qt.AlignHCenter | Qt.AlignTop)
        form.setHorizontalSpacing(20)
        form.setVerticalSpacing(12)

        # Name (single field)
        name_input = QLineEdit()
        name_input.setPlaceholderText("Enter Full Name")
        form.addRow("Name:", name_input)

        # Address
        address_input = QLineEdit()
        address_input.setPlaceholderText("Enter Address")
        form.addRow("Address:", address_input)

        # Contact
        contact_input = QLineEdit()
        contact_input.setPlaceholderText("Enter Contact")
        form.addRow("Contact:", contact_input)

        # Donor Type ComboBox
        type_combo = QComboBox()
        type_combo.addItems([
            "Individual", "Government", "Organization", "Events Contribution", "Other"
        ])
        form.addRow("Type:", type_combo)

        # Category ComboBox
        category_combo = QComboBox()
        category_combo.addItems([
            "Regular", "Permanent", "Partnership", "Occasional", "Other"
        ])
        form.addRow("Category:", category_combo)

        # Date Joined
        date_joined = QDateEdit()
        date_joined.setCalendarPopup(True)
        date_joined.setDate(QDate.currentDate())
        form.addRow("Date Joined:", date_joined)

        layout.addLayout(form)

        # Buttons
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        save_btn = button("Save", "primary", "md", icon_toolTip="Save Donor")
        cancel_btn = button("Cancel", "secondary", "md", icon_toolTip="Cancel")
        btn_layout.addWidget(save_btn)
        btn_layout.addWidget(cancel_btn)
        layout.addLayout(btn_layout)

        def save():
            name = name_input.text().strip()
            address = address_input.text().strip()
            contact = contact_input.text().strip()
            donor_type = type_combo.currentText()
            category = category_combo.currentText()
            date = date_joined.date().toString("yyyy-MM-dd")

            # Validation: not null
            if not name or not address or not contact or not donor_type or not category:
                QMessageBox.warning(dialog, "Validation Error", "All fields are required.")
                return

            # Validation: unique contact
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                cur.execute("SELECT 1 FROM Donors WHERE contact = ?", (contact,))
                if cur.fetchone():
                    QMessageBox.warning(dialog, "Validation Error", "Contact must be unique. This contact already exists.")
                    return
                # Insert into Donors (Name, address, contact, Donor_Type, Donor_Category, Date_Joined)
                cur.execute("""
                    INSERT INTO Donors (Name, address, contact, Donor_Type, Donor_Category, Date_Joined)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (name, address, contact, donor_type, category, date))
                conn.commit()
            finally:
                conn.close()
            QMessageBox.information(self, "Success", "Donor added successfully!")
            dialog.accept()
            self.refresh_donor_table()

        cancel_btn.clicked.connect(dialog.reject)
        save_btn.clicked.connect(save)

        dialog.setLayout(layout)
        dialog.exec_()

    def edit_donor(self, donor_id):
        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Donors WHERE DonorID = ?", (donor_id,))
            donor = cur.fetchone()
        finally:
            conn.close()
        if not donor:
            QMessageBox.warning(self, "Error", "Donor not found.")
            return

        dialog = QDialog(self)
        dialog.setWindowTitle("Edit Donor")
        dialog.setStyleSheet(DialogStyles())
        layout = QVBoxLayout(dialog)
        title = QLabel("Edit Donor")
        title.setStyleSheet("font-size: 22px; font-weight: bold; color: #1B263B; margin-bottom: 12px;")
        layout.addWidget(title, alignment=Qt.AlignHCenter)

        form = QFormLayout()
        form.setLabelAlignment(Qt.AlignRight)
        form.setFormAlignment(Qt.AlignHCenter | Qt.AlignTop)
        form.setHorizontalSpacing(20)
        form.setVerticalSpacing(12)

        name_input = QLineEdit(donor["Name"])
        form.addRow("Name:", name_input)
        address_input = QLineEdit(donor["address"])
        form.addRow("Address:", address_input)
        contact_input = QLineEdit(donor["contact"])
        form.addRow("Contact:", contact_input)

        type_combo = QComboBox()
        type_combo.addItems([
            "Individual", "Government", "Organization", "Events Contribution", "Other"
        ])
        idx = type_combo.findText(donor["Donor_Type"])
        if idx >= 0:
            type_combo.setCurrentIndex(idx)
        form.addRow("Type:", type_combo)

        category_combo = QComboBox()
        category_combo.addItems([
            "Regular", "Permanent", "Partnership", "Occasional", "Other"
        ])
        idx = category_combo.findText(donor["Donor_Category"])
        if idx >= 0:
            category_combo.setCurrentIndex(idx)
        form.addRow("Category:", category_combo)

        date_joined = QDateEdit()
        date_joined.setCalendarPopup(True)
        try:
            date = QDate.fromString(donor["Date_Joined"], "yyyy-MM-dd")
            if date.isValid():
                date_joined.setDate(date)
            else:
                date_joined.setDate(QDate.currentDate())
        except Exception:
            date_joined.setDate(QDate.currentDate())
        form.addRow("Date Joined:", date_joined)

        layout.addLayout(form)

        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        save_btn = button("Save", "primary", "md", icon_toolTip="Save Donor")
        cancel_btn = button("Cancel", "secondary", "md", icon_toolTip="Cancel")
        btn_layout.addWidget(save_btn)
        btn_layout.addWidget(cancel_btn)
        layout.addLayout(btn_layout)

        cancel_btn.clicked.connect(dialog.reject)
        def save_edit():
            conn2 = get_db_connection()
            try:
                cur2 = conn2.cursor()
                cur2.execute("""
                    UPDATE Donors SET Name=?, address=?, contact=?, Donor_Type=?, Donor_Category=?, Date_Joined=?
                    WHERE DonorID=?
                """, (
                    name_input.text(),
                    address_input.text(),
                    contact_input.text(),
                    type_combo.currentText(),
                    category_combo.currentText(),
                    date_joined.date().toString("yyyy-MM-dd"),
                    donor_id
                ))
                conn2.commit()
            finally:
                conn2.close()
            QMessageBox.information(self, "Success", "Donor updated successfully!")
            dialog.accept()
            self.refresh_donor_table()
        save_btn.clicked.connect(save_edit)

        dialog.setLayout(layout)
        dialog.exec_()

    def delete_donor(self, donor_id):
        reply = QMessageBox.question(
            self, "Confirm Delete",
            "Are you sure you want to delete this donor?",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                cur.execute("DELETE FROM Donors WHERE DonorID = ?", (donor_id,))
                conn.commit()
            finally:
                conn.close()
            QMessageBox.information(self, "Deleted", "Donor deleted successfully!")
            self.refresh_donor_table()

    def refresh_donor_table(self):
        # Get filter values
        search_text = self.SearchBar.text().strip().lower()
        type_filter = self.type_filter.currentText()
        category_filter = self.category_filter.currentText()

        # Build SQL query dynamically
        query = "SELECT DonorID, Name, address, contact, Donor_Type, Donor_Category, Date_Joined FROM Donors WHERE 1=1"
        params = []

        if type_filter != "All":
            query += " AND Donor_Type = ?"
            params.append(type_filter)
        if category_filter != "All":
            query += " AND Donor_Category = ?"
            params.append(category_filter)
        if search_text:
            query += " AND (LOWER(Name) LIKE ? OR LOWER(address) LIKE ? OR LOWER(contact) LIKE ?)"
            params.extend([f"%{search_text}%"] * 3)

        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute(query, params)
            donors = cur.fetchall()
        finally:
            conn.close()

        table = self.TableofDonors
        table.setRowCount(0)
        for row_idx, donor in enumerate(donors):
            table.insertRow(row_idx)
            table.setRowHeight(row_idx, 45)
            name = donor['Name']
            table.setItem(row_idx, 0, QTableWidgetItem(name))
            table.setItem(row_idx, 1, QTableWidgetItem(donor['address']))
            table.setItem(row_idx, 2, QTableWidgetItem(donor['contact']))
            table.setItem(row_idx, 3, QTableWidgetItem(donor['Donor_Type']))
            table.setItem(row_idx, 4, QTableWidgetItem(donor['Donor_Category']))
            table.setItem(row_idx, 5, QTableWidgetItem(donor['Date_Joined']))

            action_widget = QWidget()
            action_layout = QHBoxLayout()
            edit_btn = TableButton("Edit")
            delete_btn = TableButton("Delete")
            action_layout.addWidget(edit_btn)
            action_layout.addWidget(delete_btn)
            action_layout.setContentsMargins(0, 0, 0, 0)
            action_widget.setLayout(action_layout)
            table.setCellWidget(row_idx, 6, action_widget)

            edit_btn.clicked.connect(lambda _, did=donor['DonorID']: self.edit_donor(did))
            delete_btn.clicked.connect(lambda _, did=donor['DonorID']: self.delete_donor(did))

class Categoriesvalues():
    def __init__(self):
        self.refresh()

    def refresh(self):
        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT CategoryID, Name FROM Categories")
            self.values = [{"CategoryID": row["CategoryID"], "Name": row["Name"]} for row in cur.fetchall()]
        finally:
            conn.close()

    def get_list(self):
        return self.values

    def get_names(self):
        return [cat["Name"] for cat in self.values]

    def get_ids(self):
        return [cat["CategoryID"] for cat in self.values]

    def get_by_id(self, cat_id):
        for cat in self.values:
            if cat["CategoryID"] == cat_id:
                return cat
        return None

    def get_by_name(self, name):
        for cat in self.values:
            if cat["Name"] == name:
                return cat
        return None
    
class Categories_SubCategories(QWidget):
    def __init__(self):
        super().__init__()
        Layout = QVBoxLayout()
        self.setLayout(Layout)
        # Content header Area
        self.ContentAreaHeader = QWidget()
        self.ContentAreaHeaderLayout = QHBoxLayout()
        self.Title = Title("Categories & Subcategories")
        self.AddButton = button("Add", "primary", "md", icon_path="Icons/add.svg", icon_toolTip="Add New SubCategory")
        self.ExportButton = button("Export", "success", "md", icon_path="Icons/print.svg", icon_toolTip="Export as Pdf")
        self.ContentAreaHeaderLayout.addWidget(self.Title, alignment=Qt.AlignLeft)
        self.ContentAreaHeaderLayout.addStretch()
        self.ContentAreaHeaderLayout.addWidget(self.AddButton, alignment=Qt.AlignRight)
        self.ContentAreaHeaderLayout.addWidget(self.ExportButton, alignment=Qt.AlignRight)
        self.ContentAreaHeader.setLayout(self.ContentAreaHeaderLayout)
        Layout.addWidget(self.ContentAreaHeader, alignment=Qt.AlignTop)

        # Table header
        TableTitleLabel = TableTitle("Categories & Subcategories List")
        TableHeader = QWidget()
        TableHeaderLayout = QHBoxLayout()
        self.SearchBar = QLineEdit()
        self.SearchBar.setClearButtonEnabled(True)
        self.SearchBar.setMinimumWidth(200)
        self.SearchBar.setPlaceholderText("Search")
        self.SearchBar.setStyleSheet(FormStyles())
        self.cancelButton = QPushButton()
        self.cancelButton.setFlat(True)
        self.cancelButton.setIcon(QIcon("Icons/cancel.svg"))
        self.cancelButton.setIconSize(QSize(16, 16))
        self.cancelButton.setToolTip("Cancel")
        self.cancelButton.setVisible(False)
        Filter = QLabel("Filter:")
        Filter.setStyleSheet("""
            color: #1B263B;
            font-size: 12px;
            font-family: Lato-light;
            """
        )
        self.category_filter = QComboBox()
        self.category_filter.setStyleSheet(FormStyles())
        self.category_filter.addItem("All", None)
        # Populate category_filter with categories from the database
        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT CategoryID, Name FROM Categories")
            categories = cur.fetchall()
        finally:
            conn.close()
        for cat in categories:
            self.category_filter.addItem(cat["Name"], cat["CategoryID"])
        self.category_manage = outline_button("Manage Category", "info", "sm")
        self.category_manage.clicked.connect(self.Category)
        TableHeaderLayout.addWidget(TableTitleLabel)
        TableHeaderLayout.addStretch()
        TableHeaderLayout.addWidget(self.SearchBar, alignment=Qt.AlignRight)
        TableHeaderLayout.addWidget(self.cancelButton)
        TableHeaderLayout.addWidget(Filter)
        TableHeaderLayout.addWidget(QLabel("Category:"))
        TableHeaderLayout.addWidget(self.category_filter)
        TableHeaderLayout.addWidget(self.category_manage)
        TableHeader.setLayout(TableHeaderLayout)
        Layout.addWidget(TableHeader, alignment=Qt.AlignTop)

        # Table of Categories & Subcategories
        self.TableofCategories = QTableWidget()
        self.TableofCategories.setStyleSheet(TableStyles())
        self.TableofCategories.setColumnCount(4)
        self.TableofCategories.setHorizontalHeaderLabels(["Category", "Subcategory", "Description", "Actions"])
        self.TableofCategories.horizontalHeader().setStretchLastSection(True)
        self.TableofCategories.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        Layout.addWidget(self.TableofCategories)

        # Connect AddButton to add_subcategory
        self.AddButton.clicked.connect(self.add_subcategory)

        # Connect search and filter
        self.category_filter.currentIndexChanged.connect(self._on_filter_changed)
        self.SearchBar.textChanged.connect(self._on_filter_changed)

        # Initial load
        self.load_subcategories()
   
    def _on_filter_changed(self):
        filter_text = self.SearchBar.text()
        cat_id = self.category_filter.currentData()
        self.load_subcategories(filter_text, cat_id)

    def Category(self):
        self.Dialog = QDialog(self)
        self.Dialog.setWindowTitle("Manage Category")
        self.Dialog.setMinimumWidth(500)
        main_layout = QVBoxLayout(self.Dialog)

        # Title
        title = QLabel("Category management")
        title.setAlignment(Qt.AlignHCenter)
        title.setStyleSheet("font-size: 22px; font-weight: bold; color: #1B263B; margin-bottom: 8px;")
        main_layout.addWidget(title)

        # Subtitle row: Subtitle (left), SearchBar + Add (right)
        subtitle_row = QHBoxLayout()
        subtitle = QLabel("Category List")
        subtitle.setStyleSheet("font-size: 15px; font-weight: 600; color: #1B263B;")
        subtitle_row.addWidget(subtitle, alignment=Qt.AlignLeft)

        subtitle_row.addStretch()

        searchbar = QLineEdit()
        searchbar.setPlaceholderText("Search category...")
        searchbar.setMinimumWidth(180)
        searchbar.setStyleSheet(FormStyles())
        subtitle_row.addWidget(searchbar)

        add_btn = button("Add", "primary", "sm", icon_path="Icons/add.svg", icon_toolTip="Add Category")
        subtitle_row.addWidget(add_btn)

        main_layout.addLayout(subtitle_row)

        # Table row
        table = QTableWidget()
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["Name", "Description", "Actions"])
        table.horizontalHeader().setStretchLastSection(True)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setStyleSheet(TableStyles())
        main_layout.addWidget(table)

        # --- CRUD logic for categories ---
        def load_categories(filter_text=""):
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                if filter_text:
                    cur.execute("SELECT CategoryID, Name, Description FROM Categories WHERE Name LIKE ? OR Description LIKE ?", (f"%{filter_text}%", f"%{filter_text}%"))
                else:
                    cur.execute("SELECT CategoryID, Name, Description FROM Categories")
                rows = cur.fetchall()
            finally:
                conn.close()
            table.setRowCount(0)
            for row_idx, cat in enumerate(rows):
                table.insertRow(row_idx)
                table.setRowHeight(row_idx, 45)
                table.setItem(row_idx, 0, QTableWidgetItem(cat["Name"]))
                table.setItem(row_idx, 1, QTableWidgetItem(cat["Description"]))
                # Actions
                action_widget = QWidget()
                action_layout = QHBoxLayout()
                edit_btn = TableButton("Edit")
                delete_btn = TableButton("Delete")
                action_layout.addWidget(edit_btn)
                action_layout.addWidget(delete_btn)
                action_layout.setContentsMargins(0, 0, 0, 0)
                action_widget.setLayout(action_layout)
                table.setCellWidget(row_idx, 2, action_widget)
                edit_btn.clicked.connect(lambda _, cid=cat["CategoryID"]: edit_category(cid))
                delete_btn.clicked.connect(lambda _, cid=cat["CategoryID"]: delete_category(cid))

        def add_category():
            dlg = QDialog(self.Dialog)
            dlg.setWindowTitle("Add Category")
            dlg.setStyleSheet(DialogStyles())
            lyt = QVBoxLayout(dlg)
            form = QFormLayout()
            name_input = QLineEdit()
            desc_input = QLineEdit()
            form.addRow("Name:", name_input)
            form.addRow("Description:", desc_input)
            lyt.addLayout(form)
            btns = QHBoxLayout()
            save_btn = button("Save", "primary", "sm")
            cancel_btn = button("Cancel", "secondary", "sm")
            btns.addStretch()
            btns.addWidget(save_btn)
            btns.addWidget(cancel_btn)
            lyt.addLayout(btns)
            cancel_btn.clicked.connect(dlg.reject)
            def save():
                name = name_input.text().strip()
                desc = desc_input.text().strip()
                if not name:
                    QMessageBox.warning(dlg, "Error", "Name is required.")
                    return
                # Validate uniqueness of category name
                conn = get_db_connection()
                try:
                    cur = conn.cursor()
                    cur.execute("SELECT 1 FROM Categories WHERE Name = ?", (name,))
                    if cur.fetchone():
                        QMessageBox.warning(dlg, "Error", "Category name must be unique. This name already exists.")
                        return
                    cur.execute("INSERT INTO Categories (Name, Description) VALUES (?, ?)", (name, desc))
                    conn.commit()
                except sqlite3.IntegrityError as e:
                    # Handle unique constraint error (sqlite_autoindex_Categories_1)
                    QMessageBox.warning(dlg, "Error", "Category name must be unique. This name already exists.")
                    return
                finally:
                    conn.close()
                    dlg.accept()
                    load_categories(searchbar.text())
            save_btn.clicked.connect(save)
            dlg.exec_()

        def edit_category(cat_id):
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                cur.execute("SELECT * FROM Categories WHERE CategoryID=?", (cat_id,))
                cat = cur.fetchone()
            finally:
                conn.close()
            if not cat:
                QMessageBox.warning(self.Dialog, "Error", "Category not found.")
                return
            dlg = QDialog(self.Dialog)
            dlg.setWindowTitle("Edit Category")
            dlg.setStyleSheet(DialogStyles())
            lyt = QVBoxLayout(dlg)
            form = QFormLayout()
            name_input = QLineEdit(cat["Name"])
            desc_input = QLineEdit(cat["Description"])
            form.addRow("Name:", name_input)
            form.addRow("Description:", desc_input)
            lyt.addLayout(form)
            btns = QHBoxLayout()
            save_btn = button("Save", "primary", "sm")
            cancel_btn = button("Cancel", "secondary", "sm")
            btns.addStretch()
            btns.addWidget(save_btn)
            btns.addWidget(cancel_btn)
            lyt.addLayout(btns)
            cancel_btn.clicked.connect(dlg.reject)
            def save():
                name = name_input.text().strip()
                desc = desc_input.text().strip()
                if not name:
                    QMessageBox.warning(dlg, "Error", "Name is required.")
                    return
                # Validate uniqueness of category name (excluding current)
                conn2 = get_db_connection()
                try:
                    cur2 = conn2.cursor()
                    cur2.execute("SELECT 1 FROM Categories WHERE Name = ? AND CategoryID != ?", (name, cat_id))
                    if cur2.fetchone():
                        QMessageBox.warning(dlg, "Error", "Category name must be unique. This name already exists.")
                        return
                    cur2.execute("UPDATE Categories SET Name=?, Description=? WHERE CategoryID=?", (name, desc, cat_id))
                    conn2.commit()
                except sqlite3.IntegrityError:
                    QMessageBox.warning(dlg, "Error", "Category name must be unique. This name already exists.")
                    return
                finally:
                    conn2.close()
                dlg.accept()
                load_categories(searchbar.text())
            save_btn.clicked.connect(save)
            dlg.exec_()

        def delete_category(cat_id):
            reply = QMessageBox.question(self.Dialog, "Delete", "Delete this category?", QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                conn = get_db_connection()
                try:
                    cur = conn.cursor()
                    cur.execute("DELETE FROM Categories WHERE CategoryID=?", (cat_id,))
                    conn.commit()
                finally:
                    conn.close()
                load_categories(searchbar.text())

        # Connect signals
        add_btn.clicked.connect(add_category)
        searchbar.textChanged.connect(lambda: load_categories(searchbar.text()))

        # Initial load
        load_categories()

        self.Dialog.setLayout(main_layout)
        self.Dialog.exec_()

    def load_subcategories(self, filter_text="", category_id=None):
        # category_id can be None or an integer
        conn = get_db_connection()
        try:
            cur = conn.cursor()
            query = """
                SELECT s.SubCategoryID, s.Name, s.Description, c.Name as CategoryName, s.category_id
                FROM Subcategories s
                JOIN Categories c ON s.category_id = c.CategoryID
                WHERE 1=1
            """
            params = []
            if category_id and category_id is not None:
                query += " AND s.category_id = ?"
                params.append(category_id)
            if filter_text:
                query += " AND (LOWER(s.Name) LIKE ? OR LOWER(s.Description) LIKE ? OR LOWER(c.Name) LIKE ?)"
                filter_text_l = f"%{filter_text.lower()}%"
                params.extend([filter_text_l, filter_text_l, filter_text_l])
            cur.execute(query, params)
            rows = cur.fetchall()
        finally:
            conn.close()
        self.TableofCategories.setRowCount(0)
        for row_idx, sub in enumerate(rows):
            self.TableofCategories.insertRow(row_idx)
            self.TableofCategories.setRowHeight(row_idx, 45)
            self.TableofCategories.setItem(row_idx, 0, QTableWidgetItem(sub["CategoryName"]))
            self.TableofCategories.setItem(row_idx, 1, QTableWidgetItem(sub["Name"]))
            self.TableofCategories.setItem(row_idx, 2, QTableWidgetItem(sub["Description"]))
            # Actions
            action_widget = QWidget()
            action_layout = QHBoxLayout()
            edit_btn = TableButton("Edit")
            delete_btn = TableButton("Delete")
            action_layout.addWidget(edit_btn)
            action_layout.addWidget(delete_btn)
            action_layout.setContentsMargins(0, 0, 0, 0)
            action_widget.setLayout(action_layout)
            self.TableofCategories.setCellWidget(row_idx, 3, action_widget)
            edit_btn.clicked.connect(lambda _, sid=sub["SubCategoryID"]: self.edit_subcategory(sid))
            delete_btn.clicked.connect(lambda _, sid=sub["SubCategoryID"]: self.delete_subcategory(sid))

    def add_subcategory(self):
        dlg = QDialog(self)
        dlg.setWindowTitle("Add Subcategory")
        dlg.setStyleSheet(DialogStyles())
        lyt = QVBoxLayout(dlg)
        form = QFormLayout()
        categories = Categoriesvalues()
        cat_combo = QComboBox()
        cat_combo.addItems(categories.get_names())
        name_input = QLineEdit()
        desc_input = QLineEdit()
        form.addRow("Category:", cat_combo)
        form.addRow("Name:", name_input)
        form.addRow("Description:", desc_input)
        lyt.addLayout(form)
        btns = QHBoxLayout()
        save_btn = button("Save", "primary", "sm")
        cancel_btn = button("Cancel", "secondary", "sm")
        btns.addStretch()
        btns.addWidget(save_btn)
        btns.addWidget(cancel_btn)
        lyt.addLayout(btns)
        cancel_btn.clicked.connect(dlg.reject)
        def save():
            cat_name = cat_combo.currentText()
            cat_id = categories.get_by_name(cat_name)["CategoryID"]
            name = name_input.text().strip()
            desc = desc_input.text().strip()
            if not name:
                QMessageBox.warning(dlg, "Error", "Name is required.")
                return
            # Validation: unique subcategory name within the same category
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                cur.execute("SELECT 1 FROM Subcategories WHERE Name = ? AND category_id = ?", (name, cat_id))
                if cur.fetchone():
                    QMessageBox.warning(dlg, "Error", "This subcategory already exists in the selected category.")
                    return
                cur.execute("INSERT INTO Subcategories (Name, Description, category_id) VALUES (?, ?, ?)", (name, desc, cat_id))
                conn.commit()
            except sqlite3.IntegrityError:
                QMessageBox.warning(dlg, "Error", "This subcategory already exists in the selected category.")
                return
            finally:
                conn.close()
            dlg.accept()
            # Refresh table
            filter_text = self.SearchBar.text()
            cat_id = self.category_filter.currentData()
            self.load_subcategories(filter_text, cat_id)
        save_btn.clicked.connect(save)
        dlg.exec_()

    def edit_subcategory(self, subcat_id):
        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Subcategories WHERE SubCategoryID=?", (subcat_id,))
            sub = cur.fetchone()
        finally:
            conn.close()
        if not sub:
            QMessageBox.warning(self, "Error", "Subcategory not found.")
            return
        dlg = QDialog(self)
        dlg.setWindowTitle("Edit Subcategory")
        dlg.setStyleSheet(DialogStyles())
        lyt = QVBoxLayout(dlg)
        form = QFormLayout()
        categories = Categoriesvalues()
        cat_combo = QComboBox()
        cat_combo.addItems(categories.get_names())
        idx = cat_combo.findText(categories.get_by_id(sub["category_id"])["Name"])
        if idx >= 0:
            cat_combo.setCurrentIndex(idx)
        name_input = QLineEdit(sub["Name"])
        desc_input = QLineEdit(sub["Description"])
        form.addRow("Category:", cat_combo)
        form.addRow("Name:", name_input)
        form.addRow("Description:", desc_input)
        lyt.addLayout(form)
        btns = QHBoxLayout()
        save_btn = button("Save", "primary", "sm")
        cancel_btn = button("Cancel", "secondary", "sm")
        btns.addStretch()
        btns.addWidget(save_btn)
        btns.addWidget(cancel_btn)
        lyt.addLayout(btns)
        cancel_btn.clicked.connect(dlg.reject)
        def save():
            cat_name = cat_combo.currentText()
            cat_id = categories.get_by_name(cat_name)["CategoryID"]
            name = name_input.text().strip()
            desc = desc_input.text().strip()
            if not name:
                QMessageBox.warning(dlg, "Error", "Name is required.")
                return
            # Validation: unique subcategory name within the same category, excluding current subcategory
            conn2 = get_db_connection()
            try:
                cur2 = conn2.cursor()
                cur2.execute(
                    "SELECT 1 FROM Subcategories WHERE Name = ? AND category_id = ? AND SubCategoryID != ?",
                    (name, cat_id, subcat_id)
                )
                if cur2.fetchone():
                    QMessageBox.warning(dlg, "Error", "This subcategory already exists in the selected category.")
                    return
                cur2.execute("UPDATE Subcategories SET category_id=?, Name=?, Description=? WHERE SubCategoryID=?", (cat_id, name, desc, subcat_id))
                conn2.commit()
            except sqlite3.IntegrityError:
                QMessageBox.warning(dlg, "Error", "This subcategory already exists in the selected category.")
                return
            finally:
                conn2.close()
            dlg.accept()
            filter_text = self.SearchBar.text()
            cat_id = self.category_filter.currentData()
            self.load_subcategories(filter_text, cat_id)
        save_btn.clicked.connect(save)
        dlg.exec_()

    def delete_subcategory(self, subcat_id):
        reply = QMessageBox.question(self, "Delete", "Delete this subcategory?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                cur.execute("DELETE FROM Subcategories WHERE SubCategoryID=?", (subcat_id,))
                conn.commit()
            finally:
                conn.close()
            filter_text = self.SearchBar.text()
            cat_id = self.category_filter.currentData()
            self.load_subcategories(filter_text, cat_id)

class Program_Admnistration(QWidget):
    def __init__(self):
        super().__init__()
        Layout = QVBoxLayout()
        self.setLayout(Layout)
        # Content header Area
        self.ContentAreaHeader = QWidget()
        self.ContentAreaHeaderLayout = QHBoxLayout()
        self.Title = Title("Programs & Administration")
        self.AddButton = button("Add", "primary", "md", icon_path="Icons/add.svg", icon_toolTip="Add New Program/Admin")
        self.ExportButton = button("Export", "success", "md", icon_path="Icons/print.svg", icon_toolTip="Export as Pdf")
        self.ContentAreaHeaderLayout.addWidget(self.Title, alignment=Qt.AlignLeft)
        self.ContentAreaHeaderLayout.addStretch()
        self.ContentAreaHeaderLayout.addWidget(self.AddButton, alignment=Qt.AlignRight)
        self.ContentAreaHeaderLayout.addWidget(self.ExportButton, alignment=Qt.AlignRight)
        self.ContentAreaHeader.setLayout(self.ContentAreaHeaderLayout)
        Layout.addWidget(self.ContentAreaHeader, alignment=Qt.AlignTop)

        # Table header
        TableTitleLabel = TableTitle("Programs & Administration List")
        TableHeader = QWidget()
        TableHeaderLayout = QHBoxLayout()
        self.SearchBar = QLineEdit()
        self.SearchBar.setClearButtonEnabled(True)
        self.SearchBar.setMinimumWidth(200)
        self.SearchBar.setPlaceholderText("Search")
        self.SearchBar.setStyleSheet(FormStyles())
        self.cancelButton = QPushButton()
        self.cancelButton.setFlat(True)
        self.cancelButton.setIcon(QIcon("Icons/cancel.svg"))
        self.cancelButton.setIconSize(QSize(16, 16))
        self.cancelButton.setToolTip("Cancel")
        self.cancelButton.setVisible(False)
        Filter = QLabel("Filter:")
        Filter.setStyleSheet("""
            color: #1B263B;
            font-size: 12px;
            font-family: Lato-light;
            """
        )
        TableHeaderLayout.addWidget(TableTitleLabel)
        TableHeaderLayout.addStretch()
        TableHeaderLayout.addWidget(self.SearchBar, alignment=Qt.AlignRight)
        TableHeaderLayout.addWidget(self.cancelButton)
        TableHeader.setLayout(TableHeaderLayout)
        Layout.addWidget(TableHeader, alignment=Qt.AlignTop)

        # Table of Programs & Administration
        TableofPrograms = QTableWidget()
        TableofPrograms.setStyleSheet(TableStyles())
        TableofPrograms.setColumnCount(4)
        TableofPrograms.setHorizontalHeaderLabels(["Program/Admin", "Description", "Manager", "Actions"])
        TableofPrograms.horizontalHeader().setStretchLastSection(True)
        TableofPrograms.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        Layout.addWidget(TableofPrograms)
        # Store table and filters for later use
        self.TableofPrograms = TableofPrograms

        # Connect Add button
        self.AddButton.clicked.connect(self.add_program)

        # Connect search and filter
        self.SearchBar.textChanged.connect(self.refresh_program_table)

        # Initial load
        self.refresh_program_table()

    def refresh_program_table(self):
        search_text = self.SearchBar.text().strip().lower()

        query = "SELECT PA_Id, PA_Name, PA_Description, Manager FROM Program_administrations WHERE 1=1"
        params = []
        if search_text:
            query += " AND (LOWER(PA_Name) LIKE ? OR LOWER(PA_Description) LIKE ? OR LOWER(Manager) LIKE ?)"
            params.extend([f"%{search_text}%"] * 3)

        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute(query, params)
            rows = cur.fetchall()
        finally:
            conn.close()

        table = self.TableofPrograms
        table.setRowCount(0)
        for row_idx, prog in enumerate(rows):
            table.insertRow(row_idx)
            table.setRowHeight(row_idx, 45)
            table.setItem(row_idx, 0, QTableWidgetItem(prog["PA_Name"]))
            table.setItem(row_idx, 1, QTableWidgetItem(prog["PA_Description"]))
            table.setItem(row_idx, 2, QTableWidgetItem(prog["Manager"]))
            action_widget = QWidget()
            action_layout = QHBoxLayout()
            edit_btn = TableButton("Edit")
            delete_btn = TableButton("Delete")
            action_layout.addWidget(edit_btn)
            action_layout.addWidget(delete_btn)
            action_layout.setContentsMargins(0, 0, 0, 0)
            action_widget.setLayout(action_layout)
            table.setCellWidget(row_idx, 3, action_widget)
            edit_btn.clicked.connect(lambda _, pid=prog["PA_Id"]: self.edit_program(pid))
            delete_btn.clicked.connect(lambda _, pid=prog["PA_Id"]: self.delete_program(pid))

    def add_program(self):
        dlg = QDialog(self)
        dlg.setWindowTitle("Add Program/Admin")
        dlg.setStyleSheet(DialogStyles())
        lyt = QVBoxLayout(dlg)
        form = QFormLayout()
        name_input = QLineEdit()
        desc_input = QLineEdit()
        manager_input = QLineEdit()
        form.addRow("Name:", name_input)
        form.addRow("Description:", desc_input)
        form.addRow("Manager:", manager_input)
        lyt.addLayout(form)
        btns = QHBoxLayout()
        save_btn = button("Save", "primary", "sm")
        cancel_btn = button("Cancel", "secondary", "sm")
        btns.addStretch()
        btns.addWidget(save_btn)
        btns.addWidget(cancel_btn)
        lyt.addLayout(btns)
        cancel_btn.clicked.connect(dlg.reject)

        def save():
            name = name_input.text().strip()
            desc = desc_input.text().strip()
            manager = manager_input.text().strip()
            if not name:
                QMessageBox.warning(dlg, "Error", "Name is required.")
                return
            # Unique validation for PA_Name
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                cur.execute("SELECT 1 FROM Program_administrations WHERE PA_Name = ?", (name,))
                if cur.fetchone():
                    QMessageBox.warning(dlg, "Error", "A Program/Admin with this name already exists.")
                    return
                cur.execute(
                    "INSERT INTO Program_administrations (PA_Name, PA_Description, Manager) VALUES (?, ?, ?)",
                    (name, desc, manager)
                )
                conn.commit()
            finally:
                conn.close()
            dlg.accept()
            self.refresh_program_table()
        save_btn.clicked.connect(save)
        dlg.exec_()

    def edit_program(self, prog_id):
        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Program_administrations WHERE PA_Id=?", (prog_id,))
            prog = cur.fetchone()
        finally:
            conn.close()
        if not prog:
            QMessageBox.warning(self, "Error", "Program/Admin not found.")
            return
        dlg = QDialog(self)
        dlg.setWindowTitle("Edit Program/Admin")
        dlg.setStyleSheet(DialogStyles())
        lyt = QVBoxLayout(dlg)
        form = QFormLayout()
        name_input = QLineEdit(prog["PA_Name"])
        desc_input = QLineEdit(prog["PA_Description"])
        manager_input = QLineEdit(prog["Manager"])
        form.addRow("Name:", name_input)
        form.addRow("Description:", desc_input)
        form.addRow("Manager:", manager_input)
        lyt.addLayout(form)
        btns = QHBoxLayout()
        save_btn = button("Save", "primary", "sm")
        cancel_btn = button("Cancel", "secondary", "sm")
        btns.addStretch()
        btns.addWidget(save_btn)
        btns.addWidget(cancel_btn)
        lyt.addLayout(btns)
        cancel_btn.clicked.connect(dlg.reject)

        def save():
            name = name_input.text().strip()
            desc = desc_input.text().strip()
            manager = manager_input.text().strip()
            if not name:
                QMessageBox.warning(dlg, "Error", "Name is required.")
                return
            # Unique validation for PA_Name (excluding current record)
            conn2 = get_db_connection()
            try:
                cur2 = conn2.cursor()
                cur2.execute(
                    "SELECT 1 FROM Program_administrations WHERE PA_Name = ? AND PA_Id != ?",
                    (name, prog_id)
                )
                if cur2.fetchone():
                    QMessageBox.warning(dlg, "Error", "A Program/Admin with this name already exists.")
                    return
                cur2.execute(
                    "UPDATE Program_administrations SET PA_Name=?, PA_Description=?, Manager=? WHERE PA_Id=?",
                    (name, desc, manager, prog_id)
                )
                conn2.commit()
            finally:
                conn2.close()
            dlg.accept()
            self.refresh_program_table()
        save_btn.clicked.connect(save)
        dlg.exec_()

    def delete_program(self, prog_id):
        reply = QMessageBox.question(self, "Delete", "Delete this program/admin?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                cur.execute("DELETE FROM Program_administrations WHERE PA_Id=?", (prog_id,))
                conn.commit()
            finally:
                conn.close()
            self.refresh_program_table()

class Projects_Activities(QWidget):
    def __init__(self):
        super().__init__()
        Layout = QVBoxLayout()
        self.setLayout(Layout)
        # Content header Area
        self.ContentAreaHeader = QWidget()
        self.ContentAreaHeaderLayout = QHBoxLayout()
        self.Title = Title("Projects & Activities")
        self.AddButton = button("Add", "primary", "md", icon_path="Icons/add.svg", icon_toolTip="Add New Project/Activity")
        self.ExportButton = button("Export", "success", "md", icon_path="Icons/print.svg", icon_toolTip="Export as Pdf")
        self.ContentAreaHeaderLayout.addWidget(self.Title, alignment=Qt.AlignLeft)
        self.ContentAreaHeaderLayout.addStretch()
        self.ContentAreaHeaderLayout.addWidget(self.AddButton, alignment=Qt.AlignRight)
        self.ContentAreaHeaderLayout.addWidget(self.ExportButton, alignment=Qt.AlignRight)
        self.ContentAreaHeader.setLayout(self.ContentAreaHeaderLayout)
        Layout.addWidget(self.ContentAreaHeader, alignment=Qt.AlignTop)

        # Table header
        TableTitleLabel = TableTitle("Projects & Activities List")
        TableHeader = QWidget()
        TableHeaderLayout = QHBoxLayout()
        self.SearchBar = QLineEdit()
        self.SearchBar.setClearButtonEnabled(True)
        self.SearchBar.setMinimumWidth(200)
        self.SearchBar.setPlaceholderText("Search")
        self.SearchBar.setStyleSheet(FormStyles())
        self.cancelButton = QPushButton()
        self.cancelButton.setFlat(True)
        self.cancelButton.setIcon(QIcon("Icons/cancel.svg"))
        self.cancelButton.setIconSize(QSize(16, 16))
        self.cancelButton.setToolTip("Cancel")
        self.cancelButton.setVisible(False)
        Filter = QLabel("Filter:")
        Filter.setStyleSheet("""
            color: #1B263B;
            font-size: 12px;
            font-family: Lato-light;
            """
        )
        Program_adminstrator_filter = QComboBox()
        # Populate Program_adminstrator_filter with Program Administrations (PA_Id, PA_Name)
        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT PA_Id, PA_Name FROM Program_administrations")
            programs = cur.fetchall()
        finally:
            conn.close()
        Program_adminstrator_filter.addItem("All", None)
        for prog in programs:
            Program_adminstrator_filter.addItem(prog["PA_Name"], prog["PA_Id"])
        Program_adminstrator_filter.setStyleSheet(FormStyles())
        Projects_filter = QComboBox()
        # Populate Projects_filter with Projects (ProjectID, ProjectName)
        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT ProjectID, ProjectName FROM Projects")
            projects = cur.fetchall()
        finally:
            conn.close()
        Projects_filter.addItem("All", None)
        for proj in projects:
            Projects_filter.addItem(proj["ProjectName"], proj["ProjectID"])
        Projects_filter.setStyleSheet(FormStyles())
        self.project_manage = outline_button("Manage Project", "info", "sm")
        self.project_manage.clicked.connect(self.Project)
        TableHeaderLayout.addWidget(TableTitleLabel)
        TableHeaderLayout.addStretch()
        TableHeaderLayout.addWidget(self.SearchBar, alignment=Qt.AlignRight)
        TableHeaderLayout.addWidget(self.cancelButton)
        TableHeaderLayout.addWidget(Filter)
        TableHeaderLayout.addWidget(QLabel("Program:"))
        TableHeaderLayout.addWidget(Program_adminstrator_filter)
        TableHeaderLayout.addWidget(QLabel("Project:"))
        TableHeaderLayout.addWidget(Projects_filter)
        TableHeaderLayout.addWidget(self.project_manage)

        TableHeader.setLayout(TableHeaderLayout)
        Layout.addWidget(TableHeader, alignment=Qt.AlignTop)

        # --- Activities CRUD Management (like Project management) ---
        self.TableofActivities = QTableWidget()
        self.TableofActivities.setStyleSheet(TableStyles())
        self.TableofActivities.setColumnCount(6)
        self.TableofActivities.setHorizontalHeaderLabels(["Activity", "Start Date", "End Date", "Project", "Program", "Actions"])
        self.TableofActivities.horizontalHeader().setStretchLastSection(True)
        self.TableofActivities.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)      
        Layout.addWidget(self.TableofActivities)

        def refresh_activities_table():
            # Get filter values
            search_text = self.SearchBar.text().strip().lower()
            # Find the two QComboBox filters for Program and Project
            combo_boxes = self.findChildren(QComboBox)
            program_filter = None
            project_filter = None
            # The first QComboBox is Program, the second is Project (after SearchBar/cancelButton)
            # Find by label text in TableHeaderLayout if needed, but here we assume order
            if len(combo_boxes) >= 2:
                # Use the named widgets directly
                program_filter = Program_adminstrator_filter
                project_filter = Projects_filter
                program_id = program_filter.currentData() if program_filter else None
                project_id = project_filter.currentData() if project_filter else None

            query = """
            SELECT a.ActivityID, a.ActivityName, a.ActivityStartDate, a.ActivityEndDate,
                   p.ProjectName, pa.PA_Name, a.ProjectID
            FROM Project_Activities a
            LEFT JOIN Projects p ON a.ProjectID = p.ProjectID
            LEFT JOIN Program_administrations pa ON p.ProgramID = pa.PA_Id
            WHERE 1=1
            """
            params = []
            if program_id:
                query += " AND pa.PA_Id = ?"
                params.append(program_id)
            if project_id:
                query += " AND p.ProjectID = ?"
                params.append(project_id)
            if search_text:
                query += " AND (LOWER(a.ActivityName) LIKE ? OR LOWER(a.ActivityDescription) LIKE ? OR LOWER(p.ProjectName) LIKE ? OR LOWER(pa.PA_Name) LIKE ?)"
                params.extend([f"%{search_text}%"] * 4)

            conn = get_db_connection()
            try:
                cur = conn.cursor()
                cur.execute(query, params)
                rows = cur.fetchall()
            finally:
                conn.close()
            table = self.TableofActivities
            table.setRowCount(0)
            for row_idx, act in enumerate(rows):
                table.insertRow(row_idx)
                table.setRowHeight(row_idx, 45)
                table.setItem(row_idx, 0, QTableWidgetItem(act["ActivityName"]))
                table.setItem(row_idx, 1, QTableWidgetItem(act["ActivityStartDate"] or ""))
                table.setItem(row_idx, 2, QTableWidgetItem(act["ActivityEndDate"] or ""))
                table.setItem(row_idx, 3, QTableWidgetItem(act["ProjectName"] or ""))
                table.setItem(row_idx, 4, QTableWidgetItem(act["PA_Name"] or ""))
                action_widget = QWidget()
                action_layout = QHBoxLayout()
                edit_btn = TableButton("Edit")
                delete_btn = TableButton("Delete")
                action_layout.addWidget(edit_btn)
                action_layout.addWidget(delete_btn)
                action_layout.setContentsMargins(0, 0, 0, 0)
                action_widget.setLayout(action_layout)
                table.setCellWidget(row_idx, 5, action_widget)
                edit_btn.clicked.connect(lambda _, aid=act["ActivityID"]: edit_activity(aid))
                delete_btn.clicked.connect(lambda _, aid=act["ActivityID"]: delete_activity(aid))

            # Connect signals for live update if not already connected
            try:
                self.SearchBar.textChanged.disconnect()
            except Exception:
                pass
            self.SearchBar.textChanged.connect(refresh_activities_table)
            if program_filter:
                try:
                    program_filter.currentIndexChanged.disconnect()
                except Exception:
                    pass
                program_filter.currentIndexChanged.connect(refresh_activities_table)
            if project_filter:
                try:
                    project_filter.currentIndexChanged.disconnect()
                except Exception:
                    pass
                project_filter.currentIndexChanged.connect(refresh_activities_table)
                project_filter.currentIndexChanged.disconnect()
                
            project_filter.currentIndexChanged.connect(refresh_activities_table)

        def add_activity():
            dlg = QDialog(self)
            dlg.setWindowTitle("Add Activity")
            dlg.setStyleSheet(DialogStyles())
            lyt = QVBoxLayout(dlg)
            form = QFormLayout()
            name_input = QLineEdit()
            desc_input = QLineEdit()
            start_input = QDateEdit()
            start_input.setCalendarPopup(True)
            start_input.setDate(QDate.currentDate())
            end_input = QDateEdit()
            end_input.setCalendarPopup(True)
            end_input.setDate(QDate.currentDate())
            # Project ComboBox
            project_combo = QComboBox()
            project_list = []
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                cur.execute("SELECT ProjectID, ProjectName FROM Projects")
                project_list = cur.fetchall()
            finally:
                conn.close()
            project_combo.addItem("None", None)
            for proj in project_list:
                project_combo.addItem(proj["ProjectName"], proj["ProjectID"])
            form.addRow("Name:", name_input)
            form.addRow("Description:", desc_input)
            form.addRow("Start Date:", start_input)
            form.addRow("End Date:", end_input)
            form.addRow("Project:", project_combo)
            lyt.addLayout(form)
            btns = QHBoxLayout()
            save_btn = button("Save", "primary", "sm")
            cancel_btn = button("Cancel", "secondary", "sm")
            btns.addStretch()
            btns.addWidget(save_btn)
            btns.addWidget(cancel_btn)
            lyt.addLayout(btns)
            cancel_btn.clicked.connect(dlg.reject)
            def save():
                name = name_input.text().strip()
                desc = desc_input.text().strip()
                start = start_input.date().toString("yyyy-MM-dd")
                end = end_input.date().toString("yyyy-MM-dd")
                proj_id = project_combo.currentData()
                if not name or not proj_id:
                    QMessageBox.warning(dlg, "Error", "Name and Project are required.")
                    return
                # Unique validation: ActivityName must be unique within the same ProjectID
                conn = get_db_connection()
                try:
                    cur = conn.cursor()
                    cur.execute(
                        "SELECT 1 FROM Project_Activities WHERE ActivityName = ? AND ProjectID = ?",
                        (name, proj_id)
                    )
                    if cur.fetchone():
                        QMessageBox.warning(dlg, "Error", "This activity already exists in the selected project.")
                        return
                    cur.execute(
                        "INSERT INTO Project_Activities (ActivityName, ActivityDescription, ActivityStartDate, ActivityEndDate, ProjectID) VALUES (?, ?, ?, ?, ?)",
                        (name, desc, start, end, proj_id)
                    )
                    conn.commit()
                except sqlite3.IntegrityError:
                    QMessageBox.warning(dlg, "Error", "This activity already exists in the selected project.")
                    return
                finally:
                    conn.close()
                dlg.accept()
                refresh_activities_table()
            save_btn.clicked.connect(save)
            dlg.exec_()

        def edit_activity(act_id):
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                cur.execute("SELECT * FROM Project_Activities WHERE ActivityID=?", (act_id,))
                act = cur.fetchone()
            finally:
                conn.close()
            if not act:
                QMessageBox.warning(self, "Error", "Activity not found.")
                return
            dlg = QDialog(self)
            dlg.setWindowTitle("Edit Activity")
            dlg.setStyleSheet(DialogStyles())
            lyt = QVBoxLayout(dlg)
            form = QFormLayout()
            name_input = QLineEdit(act["ActivityName"])
            desc_input = QLineEdit(act["ActivityDescription"] or "")
            start_input = QDateEdit()
            start_input.setCalendarPopup(True)
            if act["ActivityStartDate"]:
                start_input.setDate(QDate.fromString(act["ActivityStartDate"], "yyyy-MM-dd"))
            else:
                start_input.setDate(QDate.currentDate())
            end_input = QDateEdit()
            end_input.setCalendarPopup(True)
            if act["ActivityEndDate"]:
                end_input.setDate(QDate.fromString(act["ActivityEndDate"], "yyyy-MM-dd"))
            else:
                end_input.setDate(QDate.currentDate())
            # Project ComboBox
            project_combo = QComboBox()
            project_list = []
            conn2 = get_db_connection()
            try:
                cur2 = conn2.cursor()
                cur2.execute("SELECT ProjectID, ProjectName FROM Projects")
                project_list = cur2.fetchall()
            finally:
                conn2.close()
            project_combo.addItem("None", None)
            idx = 0
            for i, proj in enumerate(project_list):
                project_combo.addItem(proj["ProjectName"], proj["ProjectID"])
                if act["ProjectID"] == proj["ProjectID"]:
                    idx = i + 1  # +1 because of "None"
            project_combo.setCurrentIndex(idx)
            form.addRow("Name:", name_input)
            form.addRow("Description:", desc_input)
            form.addRow("Start Date:", start_input)
            form.addRow("End Date:", end_input)
            form.addRow("Project:", project_combo)
            lyt.addLayout(form)
            btns = QHBoxLayout()
            save_btn = button("Save", "primary", "sm")
            cancel_btn = button("Cancel", "secondary", "sm")
            btns.addStretch()
            btns.addWidget(save_btn)
            btns.addWidget(cancel_btn)
            lyt.addLayout(btns)
            cancel_btn.clicked.connect(dlg.reject)
            def save():
                name = name_input.text().strip()
                desc = desc_input.text().strip()
                start = start_input.date().toString("yyyy-MM-dd")
                end = end_input.date().toString("yyyy-MM-dd")
                proj_id = project_combo.currentData()
                if not name or not proj_id:
                    QMessageBox.warning(dlg, "Error", "Name and Project are required.")
                    return
                # Unique validation: ActivityName must be unique within the same ProjectID, excluding current activity
                conn3 = get_db_connection()
                try:
                    cur3 = conn3.cursor()
                    cur3.execute(
                        "SELECT 1 FROM Project_Activities WHERE ActivityName = ? AND ProjectID = ? AND ActivityID != ?",
                        (name, proj_id, act_id)
                    )
                    if cur3.fetchone():
                        QMessageBox.warning(dlg, "Error", "This activity already exists in the selected project.")
                        return
                    cur3.execute(
                        "UPDATE Project_Activities SET ActivityName=?, ActivityDescription=?, ActivityStartDate=?, ActivityEndDate=?, ProjectID=? WHERE ActivityID=?",
                        (name, desc, start, end, proj_id, act_id)
                    )
                    conn3.commit()
                except sqlite3.IntegrityError:
                    QMessageBox.warning(dlg, "Error", "This activity already exists in the selected project.")
                    return
                finally:
                    conn3.close()
                dlg.accept()
                refresh_activities_table()
            save_btn.clicked.connect(save)
            dlg.exec_()

        def delete_activity(act_id):
            reply = QMessageBox.question(self, "Delete", "Delete this activity?", QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                conn = get_db_connection()
                try:
                    cur = conn.cursor()
                    cur.execute("DELETE FROM Project_Activities WHERE ActivityID=?", (act_id,))
                    conn.commit()
                finally:
                    conn.close()
                refresh_activities_table()

        # Add button for activities
        self.AddButton.clicked.connect(add_activity)
        refresh_activities_table()

    # --- Projects CRUD Management ---
    def Project(self):
        self.ProjectDialog = QDialog(self)
        self.ProjectDialog.setWindowTitle("Manage Projects")
        self.ProjectDialog.setMinimumWidth(600)
        main_layout = QVBoxLayout(self.ProjectDialog)

        # Title
        title = QLabel("Project Management")
        title.setAlignment(Qt.AlignHCenter)
        title.setStyleSheet("font-size: 22px; font-weight: bold; color: #1B263B; margin-bottom: 8px;")
        main_layout.addWidget(title)

        # Subtitle row: Subtitle (left), SearchBar + Add (right)
        subtitle_row = QHBoxLayout()
        subtitle = QLabel("Project List")
        subtitle.setStyleSheet("font-size: 15px; font-weight: 600; color: #1B263B;")
        subtitle_row.addWidget(subtitle, alignment=Qt.AlignLeft)
        subtitle_row.addStretch()

        searchbar = QLineEdit()
        searchbar.setPlaceholderText("Search project...")
        searchbar.setMinimumWidth(180)
        searchbar.setStyleSheet(FormStyles())
        subtitle_row.addWidget(searchbar)

        add_btn = button("Add", "primary", "sm", icon_path="Icons/add.svg", icon_toolTip="Add Project")
        subtitle_row.addWidget(add_btn)

        main_layout.addLayout(subtitle_row)

        # Table row
        table = QTableWidget()
        table.setColumnCount(6)
        table.setHorizontalHeaderLabels(["Name", "Description", "Start Date", "End Date", "Program", "Actions"])
        table.horizontalHeader().setStretchLastSection(True)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setStyleSheet(TableStyles())
        main_layout.addWidget(table)

        # --- CRUD logic for projects ---
        def load_projects(filter_text=""):
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                if filter_text:
                    cur.execute("""
                        SELECT p.ProjectID, p.ProjectName, p.ProjectDescription, p.ProjectStartDate, p.ProjectEndDate, pa.PA_Name
                        FROM Projects p
                        LEFT JOIN Program_administrations pa ON p.ProgramID = pa.PA_Id
                        WHERE p.ProjectName LIKE ? OR p.ProjectDescription LIKE ? OR pa.PA_Name LIKE ?
                    """, (f"%{filter_text}%", f"%{filter_text}%", f"%{filter_text}%"))
                else:
                    cur.execute("""
                        SELECT p.ProjectID, p.ProjectName, p.ProjectDescription, p.ProjectStartDate, p.ProjectEndDate, pa.PA_Name
                        FROM Projects p
                        LEFT JOIN Program_administrations pa ON p.ProgramID = pa.PA_Id
                    """)
                rows = cur.fetchall()
            finally:
                conn.close()
            table.setRowCount(0)
            for row_idx, proj in enumerate(rows):
                table.insertRow(row_idx)
                table.setRowHeight(row_idx, 45)
                table.setItem(row_idx, 0, QTableWidgetItem(proj["ProjectName"]))
                table.setItem(row_idx, 1, QTableWidgetItem(proj["ProjectDescription"] or ""))
                table.setItem(row_idx, 2, QTableWidgetItem(proj["ProjectStartDate"] or ""))
                table.setItem(row_idx, 3, QTableWidgetItem(proj["ProjectEndDate"] or ""))
                table.setItem(row_idx, 4, QTableWidgetItem(proj["PA_Name"] or ""))
                # Actions
                action_widget = QWidget()
                action_layout = QHBoxLayout()
                edit_btn = TableButton("Edit")
                delete_btn = TableButton("Delete")
                action_layout.addWidget(edit_btn)
                action_layout.addWidget(delete_btn)
                action_layout.setContentsMargins(0, 0, 0, 0)
                action_widget.setLayout(action_layout)
                table.setCellWidget(row_idx, 5, action_widget)
                edit_btn.clicked.connect(lambda _, pid=proj["ProjectID"]: edit_project(pid))
                delete_btn.clicked.connect(lambda _, pid=proj["ProjectID"]: delete_project(pid))

        def add_project():
            dlg = QDialog(self.ProjectDialog)
            dlg.setWindowTitle("Add Project")
            dlg.setStyleSheet(DialogStyles())
            lyt = QVBoxLayout(dlg)
            form = QFormLayout()
            name_input = QLineEdit()
            desc_input = QLineEdit()
            start_input = QDateEdit()
            start_input.setCalendarPopup(True)
            start_input.setDate(QDate.currentDate())
            end_input = QDateEdit()
            end_input.setCalendarPopup(True)
            end_input.setDate(QDate.currentDate())
            # Program ComboBox
            program_combo = QComboBox()
            program_list = []
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                cur.execute("SELECT PA_Id, PA_Name FROM Program_administrations")
                program_list = cur.fetchall()
            finally:
                conn.close()
            program_combo.addItem("None", None)
            for prog in program_list:
                program_combo.addItem(prog["PA_Name"], prog["PA_Id"])
            form.addRow("Name:", name_input)
            form.addRow("Description:", desc_input)
            form.addRow("Start Date:", start_input)
            form.addRow("End Date:", end_input)
            form.addRow("Program:", program_combo)
            lyt.addLayout(form)
            btns = QHBoxLayout()
            save_btn = button("Save", "primary", "sm")
            cancel_btn = button("Cancel", "secondary", "sm")
            btns.addStretch()
            btns.addWidget(save_btn)
            btns.addWidget(cancel_btn)
            lyt.addLayout(btns)
            cancel_btn.clicked.connect(dlg.reject)
            def save():
                name = name_input.text().strip()
                desc = desc_input.text().strip()
                start = start_input.date().toString("yyyy-MM-dd")
                end = end_input.date().toString("yyyy-MM-dd")
                prog_id = program_combo.currentData()
                if not name:
                    QMessageBox.warning(dlg, "Error", "Name is required.")
                    return
                if not prog_id:
                    QMessageBox.warning(dlg, "Error", "Program is required.")
                    return
                # Validate uniqueness of ProjectName within the selected ProgramID
                conn = get_db_connection()
                try:
                    cur = conn.cursor()
                    cur.execute(
                        "SELECT 1 FROM Projects WHERE ProjectName = ? AND ProgramID = ?",
                        (name, prog_id)
                    )
                    if cur.fetchone():
                        QMessageBox.warning(dlg, "Error", "A project with this name already exists in the selected program.")
                        return
                    cur.execute(
                        "INSERT INTO Projects (ProjectName, ProjectDescription, ProjectStartDate, ProjectEndDate, ProgramID) VALUES (?, ?, ?, ?, ?)",
                        (name, desc, start, end, prog_id)
                    )
                    conn.commit()
                except sqlite3.IntegrityError:
                    QMessageBox.warning(dlg, "Error", "A project with this name already exists in the selected program.")
                    return
                finally:
                    conn.close()
                dlg.accept()
                load_projects(searchbar.text())
            save_btn.clicked.connect(save)
            dlg.exec_()

        def edit_project(proj_id):
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                cur.execute("SELECT * FROM Projects WHERE ProjectID=?", (proj_id,))
                proj = cur.fetchone()
            finally:
                conn.close()
            if not proj:
                QMessageBox.warning(self.ProjectDialog, "Error", "Project not found.")
                return
            dlg = QDialog(self.ProjectDialog)
            dlg.setWindowTitle("Edit Project")
            dlg.setStyleSheet(DialogStyles())
            lyt = QVBoxLayout(dlg)
            form = QFormLayout()
            name_input = QLineEdit(proj["ProjectName"])
            desc_input = QLineEdit(proj["ProjectDescription"] or "")
            start_input = QDateEdit()
            start_input.setCalendarPopup(True)
            if proj["ProjectStartDate"]:
                start_input.setDate(QDate.fromString(proj["ProjectStartDate"], "yyyy-MM-dd"))
            else:
                start_input.setDate(QDate.currentDate())
            end_input = QDateEdit()
            end_input.setCalendarPopup(True)
            if proj["ProjectEndDate"]:
                end_input.setDate(QDate.fromString(proj["ProjectEndDate"], "yyyy-MM-dd"))
            else:
                end_input.setDate(QDate.currentDate())
            # Program ComboBox
            program_combo = QComboBox()
            program_list = []
            conn2 = get_db_connection()
            try:
                cur2 = conn2.cursor()
                cur2.execute("SELECT PA_Id, PA_Name FROM Program_administrations")
                program_list = cur2.fetchall()
            finally:
                conn2.close()
            program_combo.addItem("None", None)
            idx = 0
            for i, prog in enumerate(program_list):
                program_combo.addItem(prog["PA_Name"], prog["PA_Id"])
                if proj["ProgramID"] == prog["PA_Id"]:
                    idx = i + 1  # +1 because of "None"
            program_combo.setCurrentIndex(idx)
            form.addRow("Name:", name_input)
            form.addRow("Description:", desc_input)
            form.addRow("Start Date:", start_input)
            form.addRow("End Date:", end_input)
            form.addRow("Program:", program_combo)
            lyt.addLayout(form)
            btns = QHBoxLayout()
            save_btn = button("Save", "primary", "sm")
            cancel_btn = button("Cancel", "secondary", "sm")
            btns.addStretch()
            btns.addWidget(save_btn)
            btns.addWidget(cancel_btn)
            lyt.addLayout(btns)
            cancel_btn.clicked.connect(dlg.reject)
            def save():
                name = name_input.text().strip()
                desc = desc_input.text().strip()
                start = start_input.date().toString("yyyy-MM-dd")
                end = end_input.date().toString("yyyy-MM-dd")
                prog_id = program_combo.currentData()
                if not name:
                    QMessageBox.warning(dlg, "Error", "Name is required.")
                    return
                if not prog_id:
                    QMessageBox.warning(dlg, "Error", "Program is required.")
                    return
                # Validate uniqueness of ProjectName within the selected ProgramID, excluding current project
                conn3 = get_db_connection()
                try:
                    cur3 = conn3.cursor()
                    cur3.execute(
                        "SELECT 1 FROM Projects WHERE ProjectName = ? AND ProgramID = ? AND ProjectID != ?",
                        (name, prog_id, proj_id)
                    )
                    if cur3.fetchone():
                        QMessageBox.warning(dlg, "Error", "A project with this name already exists in the selected program.")
                        return
                    cur3.execute(
                        "UPDATE Projects SET ProjectName=?, ProjectDescription=?, ProjectStartDate=?, ProjectEndDate=?, ProgramID=? WHERE ProjectID=?",
                        (name, desc, start, end, prog_id, proj_id)
                    )
                    conn3.commit()
                except sqlite3.IntegrityError:
                    QMessageBox.warning(dlg, "Error", "A project with this name already exists in the selected program.")
                    return
                finally:
                    conn3.close()
                dlg.accept()
                load_projects(searchbar.text())
            save_btn.clicked.connect(save)
            dlg.exec_()

        def delete_project(proj_id):
            reply = QMessageBox.question(self.ProjectDialog, "Delete", "Delete this project?", QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                conn = get_db_connection()
                try:
                    cur = conn.cursor()
                    cur.execute("DELETE FROM Projects WHERE ProjectID=?", (proj_id,))
                    conn.commit()
                finally:
                    conn.close()
                load_projects(searchbar.text())

        # Connect signals
        add_btn.clicked.connect(add_project)
        searchbar.textChanged.connect(lambda: load_projects(searchbar.text()))

        # Initial load
        load_projects()

        self.ProjectDialog.setLayout(main_layout)
        self.ProjectDialog.exec_()
    
class TransactionsPage(QWidget):
    def __init__(self):
        super().__init__()
        Layout = QVBoxLayout()
        self.setLayout(Layout)
        # Content header Area
        ContentAreaHeader = QWidget()
        ContentAreaHeaderLayout = QHBoxLayout()
        self.Title = Title("Transactions")
        self.AddButton = button("Transaction", "primary", "md", icon_path="Icons/add.svg", icon_toolTip="Add New Expenses Transaction")
        self.AddButton.clicked.connect(self.add_transaction)
        self.addFund = button("Add Fund", "info", "md", icon_path="Icons/add.svg", icon_toolTip="Add New Fund")
        # Connect to the add_fund method of the FundPage instance in the main window
        self.addFund.clicked.connect(lambda: self.parent().parent().parent().findChild(FundPage).add_fund())
        self.ExportButton = button("Export", "success", "md", icon_path="Icons/print.svg", icon_toolTip="Export as Pdf")
        ContentAreaHeaderLayout.addWidget(self.Title, alignment=Qt.AlignLeft)
        ContentAreaHeaderLayout.addStretch()
        ContentAreaHeaderLayout.addWidget(self.AddButton, alignment=Qt.AlignRight)
        ContentAreaHeaderLayout.addWidget(self.addFund, alignment=Qt.AlignRight)
        ContentAreaHeaderLayout.addWidget(self.ExportButton, alignment=Qt.AlignRight)
        ContentAreaHeader.setLayout(ContentAreaHeaderLayout)
        Layout.addWidget(ContentAreaHeader, alignment=Qt.AlignTop)

        # Table header
        TableTitleLabel = TableTitle("Transactions List")
        TableHeader = QWidget()
        TableHeaderLayout = QHBoxLayout()
        self.SearchBar = QLineEdit()
        self.SearchBar.setClearButtonEnabled(True)
        self.SearchBar.setMinimumWidth(200)
        self.SearchBar.setPlaceholderText("Search")
        self.SearchBar.setStyleSheet(FormStyles())
        self.cancelButton = QPushButton()
        self.cancelButton.setFlat(True)
        self.cancelButton.setIcon(QIcon("Icons/cancel.svg"))
        self.cancelButton.setIconSize(QSize(16, 16))
        self.cancelButton.setToolTip("Cancel")
        self.cancelButton.setVisible(False)
        Filter = QLabel("Filter:")
        Filter.setStyleSheet("""
            color: #1B263B;
            font-size: 12px;
            font-family: Lato-light;
        """)

        # Filters
        self.type_filter = QComboBox()
        self.type_filter.addItems(["All", "Funds", "Expense"])
        self.type_filter.setStyleSheet(FormStyles())

        self.program_filter = QComboBox()
        self.program_filter.setStyleSheet(FormStyles())
        self.program_filter.addItem("All", None)
        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT PA_Id, PA_Name FROM Program_administrations")
            programs = cur.fetchall()
        finally:
            conn.close()
        for prog in programs:
            self.program_filter.addItem(prog["PA_Name"], prog["PA_Id"])

        self.project_filter = QComboBox()
        self.project_filter.setStyleSheet(FormStyles())
        self.project_filter.addItem("All", None)

        def update_project_filter():
            self.project_filter.blockSignals(True)
            self.project_filter.clear()
            self.project_filter.addItem("All", None)
            program_id = self.program_filter.currentData()
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                if program_id:
                    cur.execute("SELECT ProjectID, ProjectName FROM Projects WHERE ProgramID = ?", (program_id,))
                else:
                    cur.execute("SELECT ProjectID, ProjectName FROM Projects")
                projects = cur.fetchall()
            finally:
                conn.close()
            for proj in projects:
                self.project_filter.addItem(proj["ProjectName"], proj["ProjectID"])
            self.project_filter.blockSignals(False)

        # Initial population
        update_project_filter()
        # Update projects when program changes
        self.program_filter.currentIndexChanged.connect(update_project_filter)

        self.category_filter = QComboBox()
        self.category_filter.setStyleSheet(FormStyles())
        self.category_filter.addItem("All", None)
        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT CategoryID, Name FROM Categories")
            categories = cur.fetchall()
        finally:
            conn.close()
        for cat in categories:
            self.category_filter.addItem(cat["Name"], cat["CategoryID"])

        TableHeaderLayout.addWidget(TableTitleLabel)
        TableHeaderLayout.addStretch()
        TableHeaderLayout.addWidget(self.SearchBar, alignment=Qt.AlignRight)
        TableHeaderLayout.addWidget(self.cancelButton)
        TableHeaderLayout.addWidget(Filter)
        TableHeaderLayout.addWidget(QLabel("Type:"))
        TableHeaderLayout.addWidget(self.type_filter)
        TableHeaderLayout.addWidget(QLabel("Program:"))
        TableHeaderLayout.addWidget(self.program_filter)
        TableHeaderLayout.addWidget(QLabel("Project:"))
        TableHeaderLayout.addWidget(self.project_filter)
        TableHeaderLayout.addWidget(QLabel("Category:"))
        TableHeaderLayout.addWidget(self.category_filter)
        TableHeader.setLayout(TableHeaderLayout)
        Layout.addWidget(TableHeader, alignment=Qt.AlignTop)

        # Table of Transactions
        self.TableofTransactions = QTableWidget()
        self.TableofTransactions.setStyleSheet(TableStyles())
        self.TableofTransactions.setColumnCount(10)
        self.TableofTransactions.setHorizontalHeaderLabels([
            "Date", "Budget Year", "Type", "Amount", "Program", "Project", "Activity", "Reference", "Subcategories"
        ,"Actions"])
        self.TableofTransactions.horizontalHeader().setStretchLastSection(True)
        self.TableofTransactions.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        Layout.addWidget(self.TableofTransactions)

        # Connect search and filters
        self.SearchBar.textChanged.connect(self.refresh_transaction_table)
        self.type_filter.currentIndexChanged.connect(self.refresh_transaction_table)
        self.program_filter.currentIndexChanged.connect(self.refresh_transaction_table)
        self.project_filter.currentIndexChanged.connect(self.refresh_transaction_table)
        self.category_filter.currentIndexChanged.connect(self.refresh_transaction_table)

        # Initial load
        self.refresh_transaction_table()
    
    def refresh_transaction_table(self):
        search_text = self.SearchBar.text().strip().lower()
        type_val = self.type_filter.currentText()
        program_id = self.program_filter.currentData()
        project_id = self.project_filter.currentData()
        category_id = self.category_filter.currentData()

        query = """
            SELECT t.TransactionID, t.TransactionDate, t.BudgetYear, TransactionType , t.Amount,
                    pa.PA_Name, p.ProjectName, a.ActivityName, t.Reference, s.Name as SubcategoryName
            FROM Transactions t
            LEFT JOIN Projects p ON t.ProjectID = p.ProjectID
            LEFT JOIN Program_administrations pa ON t.ProgramID = pa.PA_Id
            LEFT JOIN Project_Activities a ON t.ActivityID = a.ActivityID
            LEFT JOIN Subcategories s ON SubCategories  = s.SubCategoryID
            WHERE 1=1
        """
        params = []
        if type_val != "All":
            query += " AND TransactionType  = ?"
            params.append(type_val)
        if program_id:
            query += " AND t.ProgramID = ?"
            params.append(program_id)
        if project_id:
            query += " AND t.ProjectID = ?"
            params.append(project_id)
        if category_id:
            query += " AND s.CategoryID = ?"
            params.append(category_id)
        if search_text:
            query += """ AND (
                LOWER(t.Reference) LIKE ? OR
                LOWER(pa.PA_Name) LIKE ? OR
                LOWER(p.ProjectName) LIKE ? OR
                LOWER(a.ActivityName) LIKE ? OR
                LOWER(s.Name) LIKE ?
            )"""
            params.extend([f"%{search_text}%"] * 5)

        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute(query, params)
            rows = cur.fetchall()
        finally:
            conn.close()

        table = self.TableofTransactions
        table.setRowCount(0)
        for row_idx, tx in enumerate(rows):
            table.insertRow(row_idx)
            table.setRowHeight(row_idx, 45)
            table.setItem(row_idx, 0, QTableWidgetItem(tx["TransactionDate"] or ""))
            table.setItem(row_idx, 1, QTableWidgetItem(str(tx["BudgetYear"]) if tx["BudgetYear"] else ""))
            table.setItem(row_idx, 2, QTableWidgetItem(tx["TransactionType"] or ""))
            table.setItem(row_idx, 3, QTableWidgetItem(str(tx["Amount"]) if tx["Amount"] else ""))
            table.setItem(row_idx, 4, QTableWidgetItem(tx["PA_Name"] or ""))
            table.setItem(row_idx, 5, QTableWidgetItem(tx["ProjectName"] or ""))
            table.setItem(row_idx, 6, QTableWidgetItem(tx["ActivityName"] or ""))
            table.setItem(row_idx, 7, QTableWidgetItem(tx["Reference"] or ""))
            table.setItem(row_idx, 8, QTableWidgetItem(tx["SubcategoryName"] or ""))
            # Actions
            action_widget = QWidget()
            action_layout = QHBoxLayout()
            edit_btn = TableButton("Edit")
            delete_btn = TableButton("Delete")
            action_layout.addWidget(edit_btn)
            action_layout.addWidget(delete_btn)
            action_layout.setContentsMargins(0, 0, 0, 0)
            action_widget.setLayout(action_layout)
            table.setCellWidget(row_idx, 9, action_widget)
            # Connect edit/delete actions (implement edit_transaction/delete_transaction as needed)
            edit_btn.clicked.connect(lambda _, tid=tx["TransactionID"]: self.edit_transaction(tid))
            delete_btn.clicked.connect(lambda _, tid=tx["TransactionID"]: self.delete_transaction(tid))
    
    def add_transaction(self):
        """
        Show a dialog to add a new transaction (Funds or Expense).
        Fund selection now auto-selects Program and Project based on Fund.
        """
        dlg = QDialog(self)
        dlg.setWindowTitle("Add Transaction")
        dlg.setStyleSheet(DialogStyles())
        lyt = QVBoxLayout(dlg)
        form = QFormLayout()

        # Transaction Date
        date_input = QDateEdit()
        date_input.setCalendarPopup(True)
        date_input.setDate(QDate.currentDate())

        # Transaction Type
        type_input = QComboBox()
        type_input.addItems(["Funds", "Expense"])

        # Fund ComboBox (moved up, only for Funds type)
        fund_input = QComboBox()
        fund_input.addItem("Choose the Fund Name", None)
        def update_funds():
            fund_input.blockSignals(True)
            fund_input.clear()
            fund_input.addItem("Choose the Fund Name", None)
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                cur.execute("SELECT FundID, FundName FROM Fund")
                funds = cur.fetchall()
            finally:
                conn.close()
            for fund in funds:
                fund_input.addItem(fund["FundName"], fund["FundID"])
            fund_input.blockSignals(False)
        update_funds()
        fund_input.setVisible(False)  # Only show for Funds type

        # Budget Year (range format)
        year_input = QComboBox()
        years = generate_years(format_type="range", start_year=datetime.now().year, num_years=10)
        year_input.addItems(years)
        year_input.setCurrentText(str(datetime.now().year))

        # Amount
        amount_input = QLineEdit()
        amount_input.setValidator(QDoubleValidator(0, 1e12, 2))

        # Program ComboBox
        program_input = QComboBox()
        program_input.addItem("None", None)
        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT PA_Id, PA_Name FROM Program_administrations")
            programs = cur.fetchall()
        finally:
            conn.close()
        for prog in programs:
            program_input.addItem(prog["PA_Name"], prog["PA_Id"])

        # Project ComboBox (filtered by program)
        project_input = QComboBox()
        project_input.addItem("None", None)
        def update_projects():
            project_input.blockSignals(True)
            project_input.clear()
            project_input.addItem("None", None)
            prog_id = program_input.currentData()
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                if prog_id:
                    cur.execute("SELECT ProjectID, ProjectName FROM Projects WHERE ProgramID=?", (prog_id,))
                else:
                    cur.execute("SELECT ProjectID, ProjectName FROM Projects")
                projects = cur.fetchall()
            finally:
                conn.close()
            for proj in projects:
                project_input.addItem(proj["ProjectName"], proj["ProjectID"])
            project_input.blockSignals(False)
        update_projects()
        program_input.currentIndexChanged.connect(update_projects)

        # Activity ComboBox (filtered by project)
        activity_input = QComboBox()
        activity_input.addItem("None", None)
        def update_activities():
            activity_input.blockSignals(True)
            activity_input.clear()
            activity_input.addItem("None", None)
            proj_id = project_input.currentData()
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                if proj_id:
                    cur.execute("SELECT ActivityID, ActivityName FROM Project_Activities WHERE ProjectID=?", (proj_id,))
                else:
                    cur.execute("SELECT ActivityID, ActivityName FROM Project_Activities")
                acts = cur.fetchall()
            finally:
                conn.close()
            for act in acts:
                activity_input.addItem(act["ActivityName"], act["ActivityID"])
            activity_input.blockSignals(False)
        update_activities()
        project_input.currentIndexChanged.connect(update_activities)

        # Category ComboBox (for filtering subcategories)
        category_input = QComboBox()
        category_input.addItem("None", None)
        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT CategoryID, Name FROM Categories")
            categories = cur.fetchall()
        finally:
            conn.close()
        for cat in categories:
            category_input.addItem(cat["Name"], cat["CategoryID"])

        # Subcategory ComboBox (filtered by category)
        subcat_input = QComboBox()
        subcat_input.addItem("None", None)
        def update_subcategories():
            subcat_input.blockSignals(True)
            subcat_input.clear()
            subcat_input.addItem("None", None)
            cat_id = category_input.currentData()
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                if cat_id:
                    cur.execute("SELECT SubCategoryID, Name FROM Subcategories WHERE category_id = ?", (cat_id,))
                else:
                    cur.execute("SELECT SubCategoryID, Name FROM Subcategories")
                subcats = cur.fetchall()
            finally:
                conn.close()
            for sub in subcats:
                subcat_input.addItem(sub["Name"], sub["SubCategoryID"])
            subcat_input.blockSignals(False)
        update_subcategories()
        category_input.currentIndexChanged.connect(update_subcategories)

        # Description and Reference
        description_input = QLineEdit()
        reference_input = QLineEdit()

        # Add widgets to form (Fund comes after Type)
        form.addRow("Transaction Date:", date_input)
        form.addRow("Transaction Type:", type_input)
        form.addRow("Fund:", fund_input)
        form.addRow("Budget Year:", year_input)
        form.addRow("Amount:", amount_input)
        form.addRow("Program:", program_input)
        form.addRow("Project:", project_input)
        form.addRow("Activity:", activity_input)
        form.addRow("Category:", category_input)
        form.addRow("Subcategory:", subcat_input)
        form.addRow("Description:", description_input)
        form.addRow("Reference:", reference_input)
        lyt.addLayout(form)

        # Buttons
        btns = QHBoxLayout()
        save_btn = button("Save", "primary", "sm")
        cancel_btn = button("Cancel", "secondary", "sm")
        btns.addStretch()
        btns.addWidget(save_btn)
        btns.addWidget(cancel_btn)
        lyt.addLayout(btns)
        cancel_btn.clicked.connect(dlg.reject)

        # Enable/disable fields based on transaction type
        def on_type_changed(idx):
            ttype = type_input.currentText()
            if ttype == "Funds":
                fund_input.setVisible(True)
                activity_input.setEnabled(False)
                subcat_input.setEnabled(False)
            else:
                fund_input.setEnabled(False)
                activity_input.setEnabled(True)
                subcat_input.setEnabled(True)
        
        type_input.currentIndexChanged.connect(on_type_changed)
        on_type_changed(type_input.currentIndex())

        # When Fund is selected, auto-select Program and Project
        def on_fund_changed(idx):
            fund_id = fund_input.currentData()
            if fund_id:
                conn = get_db_connection()
                try:
                    cur = conn.cursor()
                    cur.execute("SELECT ProgramID, ProjectID, BudgetYear FROM Fund WHERE FundID=?", (fund_id,))
                    fund = cur.fetchone()
                finally:
                    conn.close()
                # Set Program
                if fund and fund["ProgramID"]:
                    prog_idx = program_input.findData(fund["ProgramID"])
                    if prog_idx >= 0:
                        program_input.setCurrentIndex(prog_idx)
                    program_input.setEnabled(False)
                else:
                    program_input.setEnabled(True) 
                # Set Project
                if fund and fund["ProjectID"]:
                    def set_project():
                        proj_idx = project_input.findData(fund["ProjectID"])
                        if proj_idx >= 0:
                            project_input.setCurrentIndex(proj_idx)
                    QTimer.singleShot(0, set_project)
                    project_input.setEnabled(False)
                else:
                    project_input.setEnabled(True)
                # Set BudgetYear and disable
                if fund and fund["BudgetYear"]:
                    year_idx = year_input.findText(str(fund["BudgetYear"]))
                    if year_idx >= 0:
                        year_input.setCurrentIndex(year_idx)
                    year_input.setEnabled(False)
                else:
                    year_input.setEnabled(True)
        fund_input.currentIndexChanged.connect(on_fund_changed)

        # Save logic
        def save():
            tdate = date_input.date().toString("yyyy-MM-dd")
            year = year_input.currentText()
            ttype = type_input.currentText()
            try:
                amount = float(amount_input.text())
            except Exception:
                QMessageBox.warning(dlg, "Error", "Amount is required and must be a number.")
                return
            program_id = program_input.currentData()
            project_id = project_input.currentData()
            activity_id = activity_input.currentData() if activity_input.isEnabled() else None
            category_id = category_input.currentData()
            subcat_id = subcat_input.currentData() if subcat_input.isEnabled() else None
            fund_id = fund_input.currentData() if fund_input.isVisible() else None
            description = description_input.text().strip()
            reference = reference_input.text().strip()

            # Validation
            if not tdate or not year or not ttype or not amount or not program_id or not project_id:
                QMessageBox.warning(dlg, "Error", "Date, Year, Type, Amount, Program, and Project are required.")
                return
            if ttype == "Funds":
                if not fund_id:
                    QMessageBox.warning(dlg, "Error", "Fund is required for Funds transaction.")
                    return
            else:
                if not activity_id or not subcat_id:
                    QMessageBox.warning(dlg, "Error", "Activity and Subcategory are required for Expense transaction.")
                    return
            # If Expense, validate against Budget
            if ttype == "Expense":
                # Check for matching budget
                conn2 = get_db_connection()
                try:
                    cur2 = conn2.cursor()
                    cur2.execute("""
                        SELECT BudgetAmount
                        FROM Budget
                        WHERE BudgetYear=? AND ProgramID=? AND ProjectID=? AND ActivityID=?
                    """, (year, program_id, project_id, activity_id))
                    budget_row = cur2.fetchone()
                    if not budget_row:
                        QMessageBox.warning(dlg, "Error", "No budget allocated for the selected Year, Program, Project, and Activity. Please allocate a budget first.")
                        return
                    budget_amount = budget_row["BudgetAmount"]
                    # Sum all expenses for this budget
                    cur2.execute("""
                        SELECT IFNULL(SUM(Amount),0) as total_expense
                        FROM Transactions
                        WHERE TransactionType='Expense'
                          AND BudgetYear=? AND ProgramID=? AND ProjectID=? AND ActivityID=?
                    """, (year, program_id, project_id, activity_id))
                    total_expense = cur2.fetchone()["total_expense"]
                    # Check if new expense would exceed budget
                    if total_expense + amount > budget_amount:
                        QMessageBox.warning(
                            dlg, "Warning",
                            f"Expense exceeds allocated budget.\n"
                            f"Budget: {budget_amount:.2f}, Already Spent: {total_expense:.2f}, Requested: {amount:.2f}\n"
                            "This transaction will still be saved."
                        )
                        # Do not return; allow transaction to proceed
                finally:
                    conn2.close()
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                # Insert into Transactions
                cur.execute("""
                    INSERT INTO Transactions
                    (TransactionDate, BudgetYear, TransactionType, Amount, ProgramID, ProjectID, ActivityID, Description, Reference, SubCategories)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    tdate, year, ttype, amount, program_id, project_id,
                    activity_id if activity_id else None,
                    description, reference,
                    subcat_id if subcat_id else None
                ))
                transaction_id = cur.lastrowid
                # If Funds, insert into FundTransaction
                if ttype == "Funds":
                    cur.execute("""
                        INSERT INTO FundTransactions (fund_id, Transaction_id)
                        VALUES (?, ?)
                    """, (fund_id, transaction_id))
                conn.commit()
            except Exception as e:
                QMessageBox.warning(dlg, "Error", f"Failed to save transaction: {e}")
                return
            finally:
                conn.close()
            dlg.accept()
            self.refresh_transaction_table()

        save_btn.clicked.connect(save)
        dlg.exec_()
    
    def edit_transaction(self, transaction_id):
        """
        Show a dialog to edit an existing transaction (Funds or Expense).
        """
        # Fetch transaction data
        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute("""
                SELECT t.*, ft.fund_id
                FROM Transactions t
                LEFT JOIN FundTransactions ft ON t.TransactionID = ft.Transaction_id
                WHERE t.TransactionID = ?
            """, (transaction_id,))
            tx = cur.fetchone()
        finally:
            conn.close()
        if not tx:
            QMessageBox.warning(self, "Error", "Transaction not found.")
            return

        dlg = QDialog(self)
        dlg.setWindowTitle("Edit Transaction")
        dlg.setStyleSheet(DialogStyles())
        lyt = QVBoxLayout(dlg)
        form = QFormLayout()

        # Transaction Date
        date_input = QDateEdit()
        date_input.setCalendarPopup(True)
        if tx["TransactionDate"]:
            date_input.setDate(QDate.fromString(tx["TransactionDate"], "yyyy-MM-dd"))
        else:
            date_input.setDate(QDate.currentDate())

        # Transaction Type
        type_input = QComboBox()
        type_input.addItems(["Funds", "Expense"])
        idx = type_input.findText(tx["TransactionType"])
        if idx >= 0:
            type_input.setCurrentIndex(idx)

        # Fund ComboBox (only for Funds type)
        fund_input = QComboBox()
        fund_input.addItem("Choose the Fund Name", None)
        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT FundID, FundName FROM Fund")
            funds = cur.fetchall()
        finally:
            conn.close()
        fund_idx = 0
        for i, fund in enumerate(funds):
            fund_input.addItem(fund["FundName"], fund["FundID"])
            if tx["fund_id"] == fund["FundID"]:
                fund_idx = i + 1
        fund_input.setCurrentIndex(fund_idx)
        fund_input.setVisible(tx["TransactionType"] == "Funds")

        # Budget Year (range format)
        year_input = QComboBox()
        years = generate_years(format_type="range", start_year=datetime.now().year, num_years=10)
        year_input.addItems(years)
        idx = year_input.findText(str(tx["BudgetYear"]))
        if idx >= 0:
            year_input.setCurrentIndex(idx)

        # Amount
        amount_input = QLineEdit(str(tx["Amount"]) if tx["Amount"] else "")
        amount_input.setValidator(QDoubleValidator(0, 1e12, 2))

        # Program ComboBox
        program_input = QComboBox()
        program_input.addItem("None", None)
        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT PA_Id, PA_Name FROM Program_administrations")
            programs = cur.fetchall()
        finally:
            conn.close()
        prog_idx = 0
        for i, prog in enumerate(programs):
            program_input.addItem(prog["PA_Name"], prog["PA_Id"])
            if tx["ProgramID"] == prog["PA_Id"]:
                prog_idx = i + 1
        program_input.setCurrentIndex(prog_idx)

        # Project ComboBox (filtered by program)
        project_input = QComboBox()
        project_input.addItem("None", None)
        def update_projects():
            project_input.blockSignals(True)
            project_input.clear()
            project_input.addItem("None", None)
            prog_id = program_input.currentData()
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                if prog_id:
                    cur.execute("SELECT ProjectID, ProjectName FROM Projects WHERE ProgramID=?", (prog_id,))
                else:
                    cur.execute("SELECT ProjectID, ProjectName FROM Projects")
                projects = cur.fetchall()
            finally:
                conn.close()
            proj_idx = 0
            for i, proj in enumerate(projects):
                project_input.addItem(proj["ProjectName"], proj["ProjectID"])
                if tx["ProjectID"] == proj["ProjectID"]:
                    proj_idx = i + 1
            project_input.setCurrentIndex(proj_idx)
            project_input.blockSignals(False)
        update_projects()
        program_input.currentIndexChanged.connect(update_projects)

        # Activity ComboBox (filtered by project)
        activity_input = QComboBox()
        activity_input.addItem("None", None)
        def update_activities():
            activity_input.blockSignals(True)
            activity_input.clear()
            activity_input.addItem("None", None)
            proj_id = project_input.currentData()
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                if proj_id:
                    cur.execute("SELECT ActivityID, ActivityName FROM Project_Activities WHERE ProjectID=?", (proj_id,))
                else:
                    cur.execute("SELECT ActivityID, ActivityName FROM Project_Activities")
                acts = cur.fetchall()
            finally:
                conn.close()
            act_idx = 0
            for i, act in enumerate(acts):
                activity_input.addItem(act["ActivityName"], act["ActivityID"])
                if tx["ActivityID"] == act["ActivityID"]:
                    act_idx = i + 1
            activity_input.setCurrentIndex(act_idx)
            activity_input.blockSignals(False)
        update_activities()
        project_input.currentIndexChanged.connect(update_activities)

        # Category ComboBox (for filtering subcategories)
        category_input = QComboBox()
        category_input.addItem("None", None)
        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT CategoryID, Name FROM Categories")
            categories = cur.fetchall()
        finally:
            conn.close()
        cat_idx = 0
        for i, cat in enumerate(categories):
            category_input.addItem(cat["Name"], cat["CategoryID"])
            # Try to set category if subcategory is present
            if tx["SubCategories"]:
                conn2 = get_db_connection()
                try:
                    cur2 = conn2.cursor()
                    cur2.execute("SELECT category_id FROM Subcategories WHERE SubCategoryID=?", (tx["SubCategories"],))
                    subcat_row = cur2.fetchone()
                finally:
                    conn2.close()
                if subcat_row and cat["CategoryID"] == subcat_row["category_id"]:
                    cat_idx = i + 1
        category_input.setCurrentIndex(cat_idx)

        # Subcategory ComboBox (filtered by category)
        subcat_input = QComboBox()
        subcat_input.addItem("None", None)
        def update_subcategories():
            subcat_input.blockSignals(True)
            subcat_input.clear()
            subcat_input.addItem("None", None)
            cat_id = category_input.currentData()
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                if cat_id:
                    cur.execute("SELECT SubCategoryID, Name FROM Subcategories WHERE category_id = ?", (cat_id,))
                else:
                    cur.execute("SELECT SubCategoryID, Name FROM Subcategories")
                subcats = cur.fetchall()
            finally:
                conn.close()
            sub_idx = 0
            for i, sub in enumerate(subcats):
                subcat_input.addItem(sub["Name"], sub["SubCategoryID"])
                if tx["SubCategories"] == sub["SubCategoryID"]:
                    sub_idx = i + 1
            subcat_input.setCurrentIndex(sub_idx)
            subcat_input.blockSignals(False)
        update_subcategories()
        category_input.currentIndexChanged.connect(update_subcategories)

        # Description and Reference
        description_input = QLineEdit(tx["Description"] or "")
        reference_input = QLineEdit(tx["Reference"] or "")

        # Add widgets to form (Fund comes after Type)
        form.addRow("Transaction Date:", date_input)
        form.addRow("Transaction Type:", type_input)
        form.addRow("Fund:", fund_input)
        form.addRow("Budget Year:", year_input)
        form.addRow("Amount:", amount_input)
        form.addRow("Program:", program_input)
        form.addRow("Project:", project_input)
        form.addRow("Activity:", activity_input)
        form.addRow("Category:", category_input)
        form.addRow("Subcategory:", subcat_input)
        form.addRow("Description:", description_input)
        form.addRow("Reference:", reference_input)
        lyt.addLayout(form)

        # Buttons
        btns = QHBoxLayout()
        save_btn = button("Save", "primary", "sm")
        cancel_btn = button("Cancel", "secondary", "sm")
        btns.addStretch()
        btns.addWidget(save_btn)
        btns.addWidget(cancel_btn)
        lyt.addLayout(btns)
        cancel_btn.clicked.connect(dlg.reject)

        # Enable/disable fields based on transaction type
        def on_type_changed(idx):
            ttype = type_input.currentText()
            if ttype == "Funds":
                fund_input.setVisible(True)
                activity_input.setEnabled(False)
                subcat_input.setEnabled(False)
            else:
                fund_input.setVisible(False)
                activity_input.setEnabled(True)
                subcat_input.setEnabled(True)
        type_input.currentIndexChanged.connect(on_type_changed)
        on_type_changed(type_input.currentIndex())

        # When Fund is selected, auto-select Program and Project
        def on_fund_changed(idx):
            fund_id = fund_input.currentData()
            if fund_id:
                conn = get_db_connection()
                try:
                    cur = conn.cursor()
                    cur.execute("SELECT ProgramID, ProjectID FROM Fund WHERE FundID=?", (fund_id,))
                    fund = cur.fetchone()
                finally:
                    conn.close()
                # Set Program
                if fund and fund["ProgramID"]:
                    prog_idx = program_input.findData(fund["ProgramID"])
                    if prog_idx >= 0:
                        program_input.setCurrentIndex(prog_idx)
                # Set Project
                if fund and fund["ProjectID"]:
                    def set_project():
                        proj_idx = project_input.findData(fund["ProjectID"])
                        if proj_idx >= 0:
                            project_input.setCurrentIndex(proj_idx)
                    QTimer.singleShot(0, set_project)
        fund_input.currentIndexChanged.connect(on_fund_changed)

        def save():
            tdate = date_input.date().toString("yyyy-MM-dd")
            year = year_input.currentText()
            ttype = type_input.currentText()
            try:
                amount = float(amount_input.text())
            except Exception:
                QMessageBox.warning(dlg, "Error", "Amount is required and must be a number.")
                return
            program_id = program_input.currentData()
            project_id = project_input.currentData()
            activity_id = activity_input.currentData() if activity_input.isEnabled() else None
            category_id = category_input.currentData()
            subcat_id = subcat_input.currentData() if subcat_input.isEnabled() else None
            fund_id = fund_input.currentData() if fund_input.isVisible() else None
            description = description_input.text().strip()
            reference = reference_input.text().strip()

            # Validation
            if not tdate or not year or not ttype or not amount or not program_id or not project_id:
                QMessageBox.warning(dlg, "Error", "Date, Year, Type, Amount, Program, and Project are required.")
                return
            # If Expense, validate against Budget
            if ttype == "Expense":
                # Check for matching budget
                conn2 = get_db_connection()
                try:
                    cur2 = conn2.cursor()
                    cur2.execute("""
                        SELECT BudgetAmount
                        FROM Budget
                        WHERE BudgetYear=? AND ProgramID=? AND ProjectID=? AND ActivityID=?
                    """, (year, program_id, project_id, activity_id))
                    budget_row = cur2.fetchone()
                    if not budget_row:
                        QMessageBox.warning(dlg, "Error", "No budget allocated for the selected Year, Program, Project, and Activity. Please allocate a budget first.")
                        return
                    budget_amount = budget_row["BudgetAmount"]
                    # Sum all expenses for this budget, excluding this transaction
                    cur2.execute("""
                        SELECT IFNULL(SUM(Amount),0) as total_expense
                        FROM Transactions
                        WHERE TransactionType='Expense'
                          AND BudgetYear=? AND ProgramID=? AND ProjectID=? AND ActivityID=?
                          AND TransactionID != ?
                    """, (year, program_id, project_id, activity_id, transaction_id))
                    total_expense = cur2.fetchone()["total_expense"]
                    # Check if new expense would exceed budget
                    if total_expense + amount > budget_amount:
                        QMessageBox.warning(
                            dlg, "Warning",
                            f"Expense exceeds allocated budget.\n"
                            f"Budget: {budget_amount:.2f}, Already Spent: {total_expense:.2f}, Requested: {amount:.2f}\n"
                            "This transaction will still be saved."
                        )
                        # Do not return; allow transaction to proceed
                finally:
                    conn2.close()
            if ttype == "Funds":
                if not fund_id:
                    QMessageBox.warning(dlg, "Error", "Fund is required for Funds transaction.")
                    return
            else:
                if not activity_id or not subcat_id:
                    QMessageBox.warning(dlg, "Error", "Activity and Subcategory are required for Expense transaction.")
                    return

            conn = get_db_connection()
            try:
                cur = conn.cursor()
                # Update Transactions
                cur.execute("""
                    UPDATE Transactions SET
                        TransactionDate=?, BudgetYear=?, TransactionType=?, Amount=?, ProgramID=?, ProjectID=?,
                        ActivityID=?, Description=?, Reference=?, SubCategories=?
                    WHERE TransactionID=?
                """, (
                    tdate, year, ttype, amount, program_id, project_id,
                    activity_id if activity_id else None,
                    description, reference,
                    subcat_id if subcat_id else None,
                    transaction_id
                ))
                # Update FundTransactions
                if ttype == "Funds":
                    # Remove old, insert new
                    cur.execute("DELETE FROM FundTransactions WHERE Transaction_id=?", (transaction_id,))
                    cur.execute("INSERT INTO FundTransactions (fund_id, Transaction_id) VALUES (?, ?)", (fund_id, transaction_id))
                else:
                    cur.execute("DELETE FROM FundTransactions WHERE Transaction_id=?", (transaction_id,))
                conn.commit()
            except Exception as e:
                QMessageBox.warning(dlg, "Error", f"Failed to update transaction: {e}")
                return
            finally:
                conn.close()
            dlg.accept()
            self.refresh_transaction_table()

        save_btn.clicked.connect(save)
        dlg.exec_()

    def delete_transaction(self, transaction_id):
        reply = QMessageBox.question(
            self, "Delete", "Delete this transaction?", QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                # Delete from FundTransaction first (if exists)
                cur.execute("DELETE FROM FundTransactions WHERE TransactionID=?", (transaction_id,))
                # Then delete from Transactions
                cur.execute("DELETE FROM Transactions WHERE TransactionID=?", (transaction_id,))
                conn.commit()
            finally:
                conn.close()
            self.refresh_transaction_table()

class FundPage(QWidget):
    def __init__(self):
        super().__init__()
        Layout = QVBoxLayout()
        self.setLayout(Layout)
        # Content header Area
        ContentAreaHeader = QWidget()
        ContentAreaHeaderLayout = QHBoxLayout()
        self.Title = Title("Funds")
        self.AddButton = button("Add", "primary", "md", icon_path="Icons/add.svg", icon_toolTip="Add New Fund")
        self.ExportButton = button("Export", "success", "md", icon_path="Icons/print.svg", icon_toolTip="Export as Pdf")
        ContentAreaHeaderLayout.addWidget(self.Title, alignment=Qt.AlignLeft)
        ContentAreaHeaderLayout.addStretch()
        ContentAreaHeaderLayout.addWidget(self.AddButton, alignment=Qt.AlignRight)
        ContentAreaHeaderLayout.addWidget(self.ExportButton, alignment=Qt.AlignRight)
        ContentAreaHeader.setLayout(ContentAreaHeaderLayout)
        Layout.addWidget(ContentAreaHeader, alignment=Qt.AlignTop)

        # Table header
        TableTitleLabel = TableTitle("Funds List")
        TableHeader = QWidget()
        TableHeaderLayout = QHBoxLayout()
        self.SearchBar = QLineEdit()
        self.SearchBar.setClearButtonEnabled(True)
        self.SearchBar.setMinimumWidth(200)
        self.SearchBar.setPlaceholderText("Search")
        self.SearchBar.setStyleSheet(FormStyles())
        self.cancelButton = QPushButton()
        self.cancelButton.setFlat(True)
        self.cancelButton.setIcon(QIcon("Icons/cancel.svg"))
        self.cancelButton.setIconSize(QSize(16, 16))
        self.cancelButton.setToolTip("Cancel")
        self.cancelButton.setVisible(False)
        Filter = QLabel("Filter:")
        Filter.setStyleSheet("""
            color: #1B263B;
            font-size: 12px;
            font-family: Lato-light;
        """)
        self.type_filter = QComboBox()
        self.type_filter.setStyleSheet(FormStyles())
        self.type_filter.addItems(["All","Restricted","Unrestricted"])
        self.year_filter = QComboBox()
        self.year_filter.addItems(["All"] + generate_years(format_type="range", start_year=datetime.now().year, num_years=10))
        self.year_filter.setStyleSheet(FormStyles())
        TableHeaderLayout.addWidget(TableTitleLabel)
        TableHeaderLayout.addStretch()
        TableHeaderLayout.addWidget(self.SearchBar, alignment=Qt.AlignRight)
        TableHeaderLayout.addWidget(self.cancelButton)
        TableHeaderLayout.addWidget(Filter)
        TableHeaderLayout.addWidget(QLabel("Type:"))
        TableHeaderLayout.addWidget(self.type_filter)
        TableHeaderLayout.addWidget(QLabel("Year:"))
        TableHeaderLayout.addWidget(self.year_filter)
        TableHeader.setLayout(TableHeaderLayout)
        Layout.addWidget(TableHeader, alignment=Qt.AlignTop)

        # Table of Funds
        self.TableofFunds = QTableWidget()
        self.TableofFunds.setStyleSheet(TableStyles())
        self.TableofFunds.setColumnCount(9)
        self.TableofFunds.setHorizontalHeaderLabels(["Name", "Budget Year" ,"Date", "Donor Name","Program/Admin","Project", "FundType", "Amount","Actions"])
        self.TableofFunds.horizontalHeader().setStretchLastSection(True)
        self.TableofFunds.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        Layout.addWidget(self.TableofFunds)

        # Connect Add button
        self.AddButton.clicked.connect(self.add_fund)

        # Connect search and filter
        self.SearchBar.textChanged.connect(self.refresh_fund_table)
        self.type_filter.currentIndexChanged.connect(self.refresh_fund_table)

        # Initial load
        self.refresh_fund_table()

    def refresh_fund_table(self):
        search_text = self.SearchBar.text().strip().lower()
        type_val = self.type_filter.currentText()
        year_val = self.year_filter.currentText()

        # Query: Fund info + Donor + Program + Project + SUM of all related Transaction amounts for each Fund
        query = """
            SELECT 
                f.FundID, 
                f.FundName, 
                f.initialDate as Date, 
                d.Name as DonorName, 
                f.FundType,
                f.BudgetYear,
                pa.PA_Name as ProgramName,
                p.ProjectName,
                IFNULL(SUM(t.Amount), 0) as TotalAmount
            FROM Fund f
            LEFT JOIN Donors d ON f.DonorId = d.DonorID
            LEFT JOIN Program_administrations pa ON f.ProgramID = pa.PA_Id
            LEFT JOIN Projects p ON f.ProjectID = p.ProjectID
            LEFT JOIN FundTransactions ft ON f.FundID = ft.Fund_id
            LEFT JOIN Transactions t ON ft.Transaction_id = t.TransactionID
            WHERE 1=1
        """
        params = []
        if type_val != "All":
            query += " AND f.FundType = ?"
            params.append(type_val)
        if year_val and year_val != "All":
            query += " AND f.BudgetYear = ?"
            params.append(year_val)
            # Always group by FundID to aggregate transactions for each fund
            query += " GROUP BY f.FundID"
            # If year filter is set, add BudgetYear condition
            if year_val and year_val != "All":
                query += " HAVING f.BudgetYear = ?"
                params.append(year_val)
            # If search is used, add it after GROUP BY/HAVING
            if search_text:
                if "HAVING" in query:
                    query += " AND"
                else:
                    query += " HAVING"
                    query += " (LOWER(f.FundName) LIKE ? OR LOWER(f.FundType) LIKE ? OR LOWER(d.Name) LIKE ? OR LOWER(pa.PA_Name) LIKE ? OR LOWER(p.ProjectName) LIKE ?)"
                    params.extend([f"%{search_text}%"] * 5)

        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute(query, params)
            rows = cur.fetchall()
        finally:
            conn.close()

        table = self.TableofFunds
        table.setRowCount(0)
        for row_idx, fund in enumerate(rows):
            table.insertRow(row_idx)
            table.setRowHeight(row_idx, 45)
            table.setItem(row_idx, 0, QTableWidgetItem(fund["FundName"] or ""))
            table.setItem(row_idx, 1, QTableWidgetItem(str(fund["BudgetYear"]) if fund["BudgetYear"] else ""))
            table.setItem(row_idx, 2, QTableWidgetItem(fund["Date"] or ""))
            table.setItem(row_idx, 3, QTableWidgetItem(fund["DonorName"] or ""))
            table.setItem(row_idx, 4, QTableWidgetItem(fund["ProgramName"] if fund["ProgramName"] else "All Programs"))
            table.setItem(row_idx, 5, QTableWidgetItem(fund["ProjectName"] if fund["ProjectName"] else "All Projects"))
            table.setItem(row_idx, 6, QTableWidgetItem(fund["FundType"] or ""))
            table.setItem(row_idx, 7, QTableWidgetItem(str(fund["TotalAmount"])))
            action_widget = QWidget()
            action_layout = QHBoxLayout()
            edit_btn = TableButton("Edit")
            delete_btn = TableButton("Delete")
            action_layout.addWidget(edit_btn)
            action_layout.addWidget(delete_btn)
            action_layout.setContentsMargins(0, 0, 0, 0)
            action_widget.setLayout(action_layout)
            table.setCellWidget(row_idx, 8, action_widget)
            edit_btn.clicked.connect(lambda _, fid=fund["FundID"]: self.edit_fund(fid))
            delete_btn.clicked.connect(lambda _, fid=fund["FundID"]: self.delete_fund(fid))

    def add_fund(self):
        dlg = QDialog(self)
        dlg.setWindowTitle("Add Fund")
        dlg.setStyleSheet(DialogStyles())
        lyt = QVBoxLayout(dlg)
        form = QFormLayout()
        name_input = QLineEdit()
        # Budget Year (required)
        year_input = QComboBox()
        years = generate_years(format_type="range", start_year=datetime.now().year, num_years=10)
        year_input.addItems(years)
        year_input.setCurrentText(str(datetime.now().year))
        # initialDate (date) input
        date_input = QDateEdit()
        date_input.setCalendarPopup(True)
        date_input.setDate(QDate.currentDate())
        # Donor ComboBox
        donor_combo = QComboBox()
        donor_list = []
        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT DonorID, Name FROM Donors")
            donor_list = cur.fetchall()
        finally:
            conn.close()
        donor_combo.addItem("Choose a Donor", None)
        for d in donor_list:
            donor_combo.addItem(d["Name"], d["DonorID"])
        # Program ComboBox
        program_combo = QComboBox()
        program_list = []
        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT PA_Id, PA_Name FROM Program_administrations")
            program_list = cur.fetchall()
        finally:
            conn.close()
        program_combo.addItem("All Programs", None)
        for prog in program_list:
            program_combo.addItem(prog["PA_Name"], prog["PA_Id"])
        # Project ComboBox (filtered by program)
        project_combo = QComboBox()
        project_combo.addItem("All Projects", None)
        def update_projects():
            project_combo.blockSignals(True)
            project_combo.clear()
            prog_id = program_combo.currentData()
            # If ProgramID is None, only allow Project None and disable the combo
            if prog_id is None:
                project_combo.addItem("All Projects", None)
                project_combo.setEnabled(False)
            else:
                conn = get_db_connection()
                try:
                    cur = conn.cursor()
                    cur.execute("SELECT ProjectID, ProjectName FROM Projects WHERE ProgramID=?", (prog_id,))
                    projects = cur.fetchall()
                finally:
                    conn.close()
                project_combo.addItem("All Projects", None)
                for proj in projects:
                    project_combo.addItem(proj["ProjectName"], proj["ProjectID"])
                project_combo.setEnabled(True)
            project_combo.blockSignals(False)

        update_projects()
        program_combo.currentIndexChanged.connect(update_projects)
        fundtype_input = QComboBox()
        fundtype_input.addItems(["Restricted", "Unrestricted"])

        # If both program and project are None, set Unrestricted and disable FundType selection
        def update_fundtype():
            prog_id = program_combo.currentData()
            proj_id = project_combo.currentData()
            idx = fundtype_input.findText("Unrestricted")
            if prog_id is None and proj_id is None:
                if idx >= 0:
                    fundtype_input.setCurrentIndex(idx)
                fundtype_input.setEnabled(False)
            else:
                fundtype_input.setEnabled(True)

        # Call on startup and whenever program/project changes
        program_combo.currentIndexChanged.connect(update_fundtype)
        project_combo.currentIndexChanged.connect(update_fundtype)
        update_fundtype()
        form.addRow("Name:", name_input)
        form.addRow("Budget Year:", year_input)
        form.addRow("Initial Date:", date_input)
        form.addRow("Donor:", donor_combo)
        form.addRow("Program:", program_combo)
        form.addRow("Project:", project_combo)
        form.addRow("FundType:", fundtype_input)
        lyt.addLayout(form)
        btns = QHBoxLayout()
        save_btn = button("Save", "primary", "sm")
        cancel_btn = button("Cancel", "secondary", "sm")
        btns.addStretch()
        btns.addWidget(save_btn)
        btns.addWidget(cancel_btn)
        lyt.addLayout(btns)
        cancel_btn.clicked.connect(dlg.reject)
        def save():
            conn = get_db_connection()
            name = name_input.text().strip()
            budget_year = year_input.currentText()
            initial_date = date_input.date().toString("yyyy-MM-dd")
            donor_id = donor_combo.currentData()
            program_id = program_combo.currentData()
            project_id = project_combo.currentData()
            fundtype = fundtype_input.currentText().strip()
            # Allow program_id and project_id to be None (null)
            if not name or not fundtype or not budget_year:
                QMessageBox.warning(dlg, "Error", "Name, Budget Year, and FundType are required.")
                return
            # Uniqueness validation for FundName
            try:
                cur = conn.cursor()
                cur.execute("SELECT 1 FROM Fund WHERE FundName = ?", (name,))
                if cur.fetchone():
                    QMessageBox.warning(dlg, "Error", "Fund Name must be unique. This name already exists.")
                    return
                cur.execute(
                    "INSERT INTO Fund (FundName, DonorId, BudgetYear, ProgramID, ProjectID, FundType, initialDate) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (name, donor_id, budget_year, program_id, project_id, fundtype, initial_date)
                )
                conn.commit()
            except sqlite3.IntegrityError:
                QMessageBox.warning(dlg, "Error", "Fund Name must be unique. This name already exists.")
                return
            finally:
                conn.close()
            dlg.accept()
            self.refresh_fund_table()
        save_btn.clicked.connect(save)
        dlg.exec_()

    def edit_fund(self, fund_id):
        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Fund WHERE FundID=?", (fund_id,))
            fund = cur.fetchone()
        finally:
            conn.close()
        if not fund:
            QMessageBox.warning(self, "Error", "Fund not found.")
            return

        dlg = QDialog(self)
        dlg.setWindowTitle("Edit Fund")
        dlg.setStyleSheet(DialogStyles())
        lyt = QVBoxLayout(dlg)
        form = QFormLayout()

        # Name
        name_input = QLineEdit(fund["FundName"])

        # Budget Year (required)
        year_input = QComboBox()
        years = generate_years(format_type="range", start_year=datetime.now().year, num_years=10)
        year_input.addItems(years)
        if fund["BudgetYear"]:
            idx = year_input.findText(str(fund["BudgetYear"]))
            if idx >= 0:
                year_input.setCurrentIndex(idx)
        else:
            year_input.setCurrentText(str(datetime.now().year))

        # initialDate (date) input
        date_input = QDateEdit()
        date_input.setCalendarPopup(True)
        if fund["initialDate"]:
            date_input.setDate(QDate.fromString(fund["initialDate"], "yyyy-MM-dd"))
        else:
            date_input.setDate(QDate.currentDate())

        # Donor ComboBox
        donor_combo = QComboBox()
        donor_list = []
        conn2 = get_db_connection()
        try:
            cur2 = conn2.cursor()
            cur2.execute("SELECT DonorID, Name FROM Donors")
            donor_list = cur2.fetchall()
        finally:
            conn2.close()
        donor_combo.addItem("Choose a Donor", None)
        idx = 0
        for i, d in enumerate(donor_list):
            donor_combo.addItem(d["Name"], d["DonorID"])
            if fund["DonorId"] == d["DonorID"]:
                idx = i + 1  # +1 for "Choose a Donor"
        donor_combo.setCurrentIndex(idx)

        # Program ComboBox
        program_combo = QComboBox()
        program_list = []
        conn3 = get_db_connection()
        try:
            cur3 = conn3.cursor()
            cur3.execute("SELECT PA_Id, PA_Name FROM Program_administrations")
            program_list = cur3.fetchall()
        finally:
            conn3.close()
        program_combo.addItem("All Programs", None)
        prog_idx = 0
        for i, prog in enumerate(program_list):
            program_combo.addItem(prog["PA_Name"], prog["PA_Id"])
            if fund["ProgramID"] == prog["PA_Id"]:
                prog_idx = i + 1
        program_combo.setCurrentIndex(prog_idx)

        # Project ComboBox (filtered by program)
        project_combo = QComboBox()
        project_combo.addItem("All Projects", None)
        def update_projects():
            project_combo.blockSignals(True)
            project_combo.clear()
            prog_id = program_combo.currentData()
            if prog_id is None:
                project_combo.addItem("All Projects", None)
                project_combo.setEnabled(False)
            else:
                conn = get_db_connection()
                try:
                    cur = conn.cursor()
                    cur.execute("SELECT ProjectID, ProjectName FROM Projects WHERE ProgramID=?", (prog_id,))
                    projects = cur.fetchall()
                finally:
                    conn.close()
                project_combo.addItem("All Projects", None)
                for proj in projects:
                    project_combo.addItem(proj["ProjectName"], proj["ProjectID"])
                project_combo.setEnabled(True)
            # Set current index to match fund["ProjectID"]
            proj_idx = 0
            for i in range(project_combo.count()):
                if project_combo.itemData(i) == fund["ProjectID"]:
                    proj_idx = i
                    break
            project_combo.setCurrentIndex(proj_idx)
            project_combo.blockSignals(False)
        update_projects()
        program_combo.currentIndexChanged.connect(update_projects)

        fundtype_input = QComboBox()
        fundtype_input.addItems(["Restricted", "Unrestricted"])
        idx = fundtype_input.findText(fund["FundType"])
        if idx >= 0:
            fundtype_input.setCurrentIndex(idx)

        # If both program and project are None, set Unrestricted and disable FundType selection
        def update_fundtype():
            prog_id = program_combo.currentData()
            proj_id = project_combo.currentData()
            idx = fundtype_input.findText("Unrestricted")
            if prog_id is None and proj_id is None:
                if idx >= 0:
                    fundtype_input.setCurrentIndex(idx)
                fundtype_input.setEnabled(False)
            else:
                fundtype_input.setEnabled(True)
        program_combo.currentIndexChanged.connect(update_fundtype)
        project_combo.currentIndexChanged.connect(update_fundtype)
        update_fundtype()

        form.addRow("Name:", name_input)
        form.addRow("Budget Year:", year_input)
        form.addRow("Initial Date:", date_input)
        form.addRow("Donor:", donor_combo)
        form.addRow("Program:", program_combo)
        form.addRow("Project:", project_combo)
        form.addRow("FundType:", fundtype_input)
        lyt.addLayout(form)

        btns = QHBoxLayout()
        save_btn = button("Save", "primary", "sm")
        cancel_btn = button("Cancel", "secondary", "sm")
        btns.addStretch()
        btns.addWidget(save_btn)
        btns.addWidget(cancel_btn)
        lyt.addLayout(btns)
        cancel_btn.clicked.connect(dlg.reject)

        def save():
            conn = get_db_connection()
            name = name_input.text().strip()
            budget_year = year_input.currentText()
            initial_date = date_input.date().toString("yyyy-MM-dd")
            donor_id = donor_combo.currentData()
            program_id = program_combo.currentData()
            project_id = project_combo.currentData()
            fundtype = fundtype_input.currentText().strip()
            # Validation: Name, Budget Year, FundType required
            if not name or not fundtype or not budget_year:
                QMessageBox.warning(dlg, "Error", "Name, Budget Year, and FundType are required.")
                return
            # If both program and project are None, force Unrestricted
            if program_id is None and project_id is None:
                fundtype = "Unrestricted"
            # Uniqueness validation for FundName (excluding current fund)
            try:
                cur = conn.cursor()
                cur.execute("SELECT 1 FROM Fund WHERE FundName = ? AND FundID != ?", (name, fund_id))
                if cur.fetchone():
                    QMessageBox.warning(dlg, "Error", "Fund Name must be unique. This name already exists.")
                    return
                cur.execute(
                    "UPDATE Fund SET FundName=?, DonorId=?, BudgetYear=?, ProgramID=?, ProjectID=?, FundType=?, initialDate=? WHERE FundID=?",
                    (name, donor_id, budget_year, program_id, project_id, fundtype, initial_date, fund_id)
                )
                conn.commit()
            except sqlite3.IntegrityError:
                QMessageBox.warning(dlg, "Error", "Fund Name must be unique. This name already exists.")
                return
            finally:
                conn.close()
            dlg.accept()
            self.refresh_fund_table()
        save_btn.clicked.connect(save)
        dlg.exec_()

    def delete_fund(self, fund_id):
        reply = QMessageBox.question(self, "Delete", "Delete this fund?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                cur.execute("DELETE FROM Fund WHERE FundID=?", (fund_id,))
                conn.commit()
            finally:
                conn.close()
            self.refresh_fund_table()

class BudgetsPage(QWidget):
    def __init__(self):
        super().__init__()
        Layout = QVBoxLayout()
        self.setLayout(Layout)
        # Content header Area
        ContentAreaHeader = QWidget()
        ContentAreaHeaderLayout = QHBoxLayout()
        self.Title = Title("Budgets")
        self.AddButton = button("Add", "primary", "md", icon_path="Icons/add.svg", icon_toolTip="Add New Budget")
        self.ExportButton = button("Export", "success", "md", icon_path="Icons/print.svg", icon_toolTip="Export as Pdf")
        ContentAreaHeaderLayout.addWidget(self.Title, alignment=Qt.AlignLeft)
        ContentAreaHeaderLayout.addStretch()
        ContentAreaHeaderLayout.addWidget(self.AddButton, alignment=Qt.AlignRight)
        ContentAreaHeaderLayout.addWidget(self.ExportButton, alignment=Qt.AlignRight)
        ContentAreaHeader.setLayout(ContentAreaHeaderLayout)
        Layout.addWidget(ContentAreaHeader, alignment=Qt.AlignTop)

        # Table header
        TableTitleLabel = TableTitle("Budgets List")
        TableHeader = QWidget()
        TableHeaderLayout = QHBoxLayout()
        self.SearchBar = QLineEdit()
        self.SearchBar.setClearButtonEnabled(True)
        self.SearchBar.setMinimumWidth(200)
        self.SearchBar.setPlaceholderText("Search")
        self.SearchBar.setStyleSheet(FormStyles())
        self.cancelButton = QPushButton()
        self.cancelButton.setFlat(True)
        self.cancelButton.setIcon(QIcon("Icons/cancel.svg"))
        self.cancelButton.setIconSize(QSize(16, 16))
        self.cancelButton.setToolTip("Cancel")
        self.cancelButton.setVisible(False)
        Filter = QLabel("Filter:")
        Filter.setStyleSheet("""
            color: #1B263B;
            font-size: 12px;
            font-family: Lato-light;
        """)
        self.year_filter = QComboBox()
        self.year_filter.setStyleSheet(FormStyles())
        self.year_filter.addItem("All")
        # Placeholder: Add more filter items as needed

        TableHeaderLayout.addWidget(TableTitleLabel)
        TableHeaderLayout.addStretch()
        TableHeaderLayout.addWidget(self.SearchBar, alignment=Qt.AlignRight)
        TableHeaderLayout.addWidget(self.cancelButton)
        TableHeaderLayout.addWidget(Filter)
        TableHeaderLayout.addWidget(QLabel("Year:"))
        TableHeaderLayout.addWidget(self.year_filter)
        TableHeader.setLayout(TableHeaderLayout)
        Layout.addWidget(TableHeader, alignment=Qt.AlignTop)

        # Table of Budgets
        self.TableofBudgets = QTableWidget()
        self.TableofBudgets.setStyleSheet(TableStyles())
        self.TableofBudgets.setColumnCount(8)
        self.TableofBudgets.setHorizontalHeaderLabels([
            "Budget Year", "Program/Admin", "Project", "Activity", "Amount", "Source","Description","Actions"
        ])
        self.TableofBudgets.horizontalHeader().setStretchLastSection(True)
        self.TableofBudgets.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        Layout.addWidget(self.TableofBudgets)

        # Connect Add button (no logic yet)
        self.AddButton.clicked.connect(self.add_budget_dialog)

        # Connect search and filter (no logic yet)
        self.SearchBar.textChanged.connect(self.refresh_budget_table)
        self.year_filter.currentIndexChanged.connect(self.refresh_budget_table)

        # Initial load
        self.refresh_budget_table()

    def refresh_budget_table(self):
        table = self.TableofBudgets
        table.setRowCount(0)

        # Get filter values
        search_text = self.SearchBar.text().strip().lower()
        year_val = self.year_filter.currentText()
        year_filter = None if year_val == "All" else year_val

        # Build SQL query
        query = """
            SELECT b.BudgetID, b.BudgetYear, pa.PA_Name, p.ProjectName, a.ActivityName,
                   b.BudgetAmount, f.FundName, b.BudgetDescription
            FROM Budget b
            LEFT JOIN Program_administrations pa ON b.ProgramID = pa.PA_Id
            LEFT JOIN Projects p ON b.ProjectID = p.ProjectID
            LEFT JOIN Project_Activities a ON b.ActivityID = a.ActivityID
            LEFT JOIN Fund f ON b.FundID = f.FundID
            WHERE 1=1
        """
        params = []
        if year_filter:
            query += " AND b.BudgetYear = ?"
            params.append(year_filter)
        if search_text:
            query += """ AND (
                LOWER(b.BudgetYear) LIKE ? OR
                LOWER(pa.PA_Name) LIKE ? OR
                LOWER(p.ProjectName) LIKE ? OR
                LOWER(a.ActivityName) LIKE ? OR
                LOWER(f.FundName) LIKE ? OR
                LOWER(b.BudgetDescription) LIKE ?
            )"""
            params.extend([f"%{search_text}%"] * 6)

        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute(query, params)
            rows = cur.fetchall()
        finally:
            conn.close()

        for row_idx, budget in enumerate(rows):
            table.insertRow(row_idx)
            table.setRowHeight(row_idx, 45)
            table.setItem(row_idx, 0, QTableWidgetItem(str(budget["BudgetYear"]) if budget["BudgetYear"] else ""))
            table.setItem(row_idx, 1, QTableWidgetItem(budget["PA_Name"] or ""))
            table.setItem(row_idx, 2, QTableWidgetItem(budget["ProjectName"] or ""))
            table.setItem(row_idx, 3, QTableWidgetItem(budget["ActivityName"] or ""))
            table.setItem(row_idx, 4, QTableWidgetItem(str(budget["BudgetAmount"]) if budget["BudgetAmount"] else ""))
            table.setItem(row_idx, 5, QTableWidgetItem(budget["FundName"] or ""))
            table.setItem(row_idx, 6, QTableWidgetItem(budget["BudgetDescription"] or ""))
            action_widget = QWidget()
            action_layout = QHBoxLayout()
            edit_btn = TableButton("Edit")
            delete_btn = TableButton("Delete")
            action_layout.addWidget(edit_btn)
            action_layout.addWidget(delete_btn)
            action_layout.setContentsMargins(0, 0, 0, 0)
            action_widget.setLayout(action_layout)
            table.setCellWidget(row_idx, 7, action_widget)
            # Connect edit/delete actions if needed
            edit_btn.clicked.connect(lambda _, bid=budget["BudgetID"]: self.edit_budget(bid))
            delete_btn.clicked.connect(lambda _, bid=budget["BudgetID"]: self.delete_budget(bid))

    def add_budget_dialog(self):
        dlg = QDialog(self)
        dlg.setWindowTitle("Add Budget")
        dlg.setStyleSheet(DialogStyles())
        lyt = QVBoxLayout(dlg)
        form = QFormLayout()

        # Budget Year
        year_input = QComboBox()
        years = generate_years(format_type="range", start_year=datetime.now().year, num_years=10)
        year_input.addItems(years)
        year_input.setCurrentText(str(datetime.now().year))

        # Program ComboBox
        program_input = QComboBox()
        program_input.addItem("None", None)
        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT PA_Id, PA_Name FROM Program_administrations")
            programs = cur.fetchall()
        finally:
            conn.close()
        for prog in programs:
            program_input.addItem(prog["PA_Name"], prog["PA_Id"])

        # Project ComboBox (filtered by program)
        project_input = QComboBox()
        project_input.addItem("None", None)
        def update_projects():
            project_input.blockSignals(True)
            project_input.clear()
            project_input.addItem("None", None)
            prog_id = program_input.currentData()
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                if prog_id:
                    cur.execute("SELECT ProjectID, ProjectName FROM Projects WHERE ProgramID=?", (prog_id,))
                else:
                    cur.execute("SELECT ProjectID, ProjectName FROM Projects")
                projects = cur.fetchall()
            finally:
                conn.close()
            for proj in projects:
                project_input.addItem(proj["ProjectName"], proj["ProjectID"])
            project_input.blockSignals(False)
        update_projects()
        program_input.currentIndexChanged.connect(update_projects)

        # Activity ComboBox (filtered by project)
        activity_input = QComboBox()
        activity_input.addItem("None", None)
        def update_activities():
            activity_input.blockSignals(True)
            activity_input.clear()
            activity_input.addItem("None", None)
            proj_id = project_input.currentData()
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                if proj_id:
                    cur.execute("SELECT ActivityID, ActivityName FROM Project_Activities WHERE ProjectID=?", (proj_id,))
                else:
                    cur.execute("SELECT ActivityID, ActivityName FROM Project_Activities")
                acts = cur.fetchall()
            finally:
                conn.close()
            for act in acts:
                activity_input.addItem(act["ActivityName"], act["ActivityID"])
            activity_input.blockSignals(False)
        update_activities()
        project_input.currentIndexChanged.connect(update_activities)

        # Amount
        amount_input = QLineEdit()
        amount_input.setValidator(QDoubleValidator(0, 1e12, 2))

        # Source (FundID)
        source_input = QComboBox()
        source_input.addItem("None", None)
        fund_map = {}  # FundID -> fund row
        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT FundID, FundName, FundType, ProgramID, ProjectID, BudgetYear FROM Fund")
            funds = cur.fetchall()
        finally:
            conn.close()
        for fund in funds:
            source_input.addItem(fund["FundName"], fund["FundID"])
            fund_map[fund["FundID"]] = fund

        # Description
        description_input = QLineEdit()

        # Add to form
        form.addRow("Budget Year:", year_input)
        form.addRow("Program:", program_input)
        form.addRow("Project:", project_input)
        form.addRow("Activity:", activity_input)
        form.addRow("Amount:", amount_input)
        form.addRow("Source (Fund):", source_input)
        form.addRow("Description:", description_input)
        lyt.addLayout(form)

        # Buttons
        btns = QHBoxLayout()
        save_btn = button("Save", "primary", "sm")
        cancel_btn = button("Cancel", "secondary", "sm")
        btns.addStretch()
        btns.addWidget(save_btn)
        btns.addWidget(cancel_btn)
        lyt.addLayout(btns)
        cancel_btn.clicked.connect(dlg.reject)

        def save():
            year = year_input.currentText()
            program_id = program_input.currentData()
            project_id = project_input.currentData()
            activity_id = activity_input.currentData()
            try:
                amount = float(amount_input.text())
            except Exception:
                QMessageBox.warning(dlg, "Error", "Amount is required and must be a number.")
                return
            fund_id = source_input.currentData()
            description = description_input.text().strip()

            # Validation: Required fields
            if not year or not amount or not fund_id:
                QMessageBox.warning(dlg, "Error", "Year, Amount, and Source (Fund) are required.")
                return

            # Validation: Uniqueness (BudgetYear, ProgramID, ProjectID, ActivityID)
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                cur.execute(
                    "SELECT 1 FROM Budget WHERE BudgetYear=? AND ProgramID=? AND ProjectID=? AND ActivityID=?",
                    (year, program_id, project_id, activity_id)
                )
                if cur.fetchone():
                    QMessageBox.warning(
                        dlg, "Error",
                        "A budget with the same Year, Program, Project, and Activity already exists. "
                        "Each combination must be unique."
                    )
                    return
            finally:
                conn.close()

            # Validation: FundType and Program/Project match for Restricted
            fund = fund_map.get(fund_id)
            if not fund:
                QMessageBox.warning(dlg, "Error", "Selected fund not found.")
                return
            fund_type = fund["FundType"]
            fund_prog = fund["ProgramID"]
            fund_proj = fund["ProjectID"]
            fund_year = fund["BudgetYear"]

            if fund_type == "Restricted":
                # Must match program and project, or if fund's Project is None, allow any project under the same program
                if program_id != fund_prog or (fund_proj is not None and project_id != fund_proj):
                    QMessageBox.warning(
                        dlg, "Error",
                        "For Restricted funds, the selected Program must match the Fund's Program, "
                        "and the Project must match the Fund's Project unless the Fund is for all projects under the Program."
                    )
                    return
                # Optionally, check year match
                if str(year) != str(fund_year):
                    QMessageBox.warning(
                        dlg, "Error",
                        "For Restricted funds, the Budget Year must match the Fund's Budget Year."
                    )
                    return
            # For Unrestricted, allow any program/project

            # Validation: Budget amount does not exceed available fund
            # Sum all budgets for this fund (for all years/programs/projects/activities)
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                cur.execute(
                    "SELECT IFNULL(SUM(BudgetAmount),0) FROM Budget WHERE FundID=?",
                    (fund_id,)
                )
                total_budgeted = cur.fetchone()[0]
                # Get total fund amount (sum of all transactions for this fund)
                cur.execute("""
                    SELECT IFNULL(SUM(t.Amount),0)
                    FROM FundTransactions ft
                    JOIN Transactions t ON ft.Transaction_id = t.TransactionID
                    WHERE ft.fund_id=?
                """, (fund_id,))
                total_fund = cur.fetchone()[0]
            finally:
                conn.close()
            # If no transactions exist, treat fund as 0 (cannot allocate)
            if total_fund == 0:
                QMessageBox.warning(
                    dlg, "Error",
                    "No available funds for this source. Please add a fund transaction first."
                )
                return
            # Check if new budget would exceed available fund
            if total_budgeted + amount > total_fund:
                QMessageBox.warning(
                    dlg, "Error",
                    f"Budget exceeds available fund amount.\n"
                    f"Available: {total_fund - total_budgeted:.2f}, Requested: {amount:.2f}"
                )
                return

            # Passed all validations, insert
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                cur.execute("""
                    INSERT INTO Budget (BudgetYear, ProgramID, ProjectID, ActivityID, BudgetAmount, FundID, BudgetDescription)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (year, program_id, project_id, activity_id, amount, fund_id, description))
                conn.commit()
            except Exception as e:
                QMessageBox.warning(dlg, "Error", f"Failed to add budget: {e}")
                return
            finally:
                conn.close()
            dlg.accept()
            self.refresh_budget_table()

        save_btn.clicked.connect(save)
        dlg.exec_()
   
    def edit_budget(self, budget_id):
        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Budget WHERE BudgetID=?", (budget_id,))
            budget = cur.fetchone()
        finally:
            conn.close()
        if not budget:
            QMessageBox.warning(self, "Error", "Budget not found.")
            return

        dlg = QDialog(self)
        dlg.setWindowTitle("Edit Budget")
        dlg.setStyleSheet(DialogStyles())
        lyt = QVBoxLayout(dlg)
        form = QFormLayout()

        # Budget Year
        year_input = QComboBox()
        current_year = QDate.currentDate().year()
        years = [str(y) for y in range(current_year - 5, current_year + 6)]
        year_input.addItems(years)
        year_input.setCurrentText(str(budget["BudgetYear"]))

        # Program ComboBox
        program_input = QComboBox()
        program_input.addItem("None", None)
        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT PA_Id, PA_Name FROM Program_administrations")
            programs = cur.fetchall()
        finally:
            conn.close()
        prog_idx = 0
        for i, prog in enumerate(programs):
            program_input.addItem(prog["PA_Name"], prog["PA_Id"])
            if budget["ProgramID"] == prog["PA_Id"]:
                prog_idx = i + 1
        program_input.setCurrentIndex(prog_idx)

        # Project ComboBox (filtered by program)
        project_input = QComboBox()
        project_input.addItem("None", None)
        def update_projects():
            project_input.blockSignals(True)
            project_input.clear()
            project_input.addItem("None", None)
            prog_id = program_input.currentData()
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                if prog_id:
                    cur.execute("SELECT ProjectID, ProjectName FROM Projects WHERE ProgramID=?", (prog_id,))
                else:
                    cur.execute("SELECT ProjectID, ProjectName FROM Projects")
                projects = cur.fetchall()
            finally:
                conn.close()
            proj_idx = 0
            for i, proj in enumerate(projects):
                project_input.addItem(proj["ProjectName"], proj["ProjectID"])
                if budget["ProjectID"] == proj["ProjectID"]:
                    proj_idx = i + 1
            project_input.setCurrentIndex(proj_idx)
            project_input.blockSignals(False)
        update_projects()
        program_input.currentIndexChanged.connect(update_projects)

        # Activity ComboBox (filtered by project)
        activity_input = QComboBox()
        activity_input.addItem("None", None)
        def update_activities():
            activity_input.blockSignals(True)
            activity_input.clear()
            activity_input.addItem("None", None)
            proj_id = project_input.currentData()
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                if proj_id:
                    cur.execute("SELECT ActivityID, ActivityName FROM Project_Activities WHERE ProjectID=?", (proj_id,))
                else:
                    cur.execute("SELECT ActivityID, ActivityName FROM Project_Activities")
                acts = cur.fetchall()
            finally:
                conn.close()
            act_idx = 0
            for i, act in enumerate(acts):
                activity_input.addItem(act["ActivityName"], act["ActivityID"])
                if budget["ActivityID"] == act["ActivityID"]:
                    act_idx = i + 1
            activity_input.setCurrentIndex(act_idx)
            activity_input.blockSignals(False)
        update_activities()
        project_input.currentIndexChanged.connect(update_activities)

        # Amount
        amount_input = QLineEdit(str(budget["BudgetAmount"]) if budget["BudgetAmount"] else "")
        amount_input.setValidator(QDoubleValidator(0, 1e12, 2))

        # Source (FundID)
        source_input = QComboBox()
        source_input.addItem("None", None)
        fund_map = {}
        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT FundID, FundName, FundType, ProgramID, ProjectID, BudgetYear FROM Fund")
            funds = cur.fetchall()
        finally:
            conn.close()
        fund_idx = 0
        for i, fund in enumerate(funds):
            source_input.addItem(fund["FundName"], fund["FundID"])
            fund_map[fund["FundID"]] = fund
            if budget["FundID"] == fund["FundID"]:
                fund_idx = i + 1
        source_input.setCurrentIndex(fund_idx)

        # Description
        description_input = QLineEdit(budget["BudgetDescription"] or "")

        # Add to form
        form.addRow("Budget Year:", year_input)
        form.addRow("Program:", program_input)
        form.addRow("Project:", project_input)
        form.addRow("Activity:", activity_input)
        form.addRow("Amount:", amount_input)
        form.addRow("Source (Fund):", source_input)
        form.addRow("Description:", description_input)
        lyt.addLayout(form)

        # Buttons
        btns = QHBoxLayout()
        save_btn = button("Save", "primary", "sm")
        cancel_btn = button("Cancel", "secondary", "sm")
        btns.addStretch()
        btns.addWidget(save_btn)
        btns.addWidget(cancel_btn)
        lyt.addLayout(btns)
        cancel_btn.clicked.connect(dlg.reject)

        def save():
            year = year_input.currentText()
            program_id = program_input.currentData()
            project_id = project_input.currentData()
            activity_id = activity_input.currentData()
            try:
                amount = float(amount_input.text())
            except Exception:
                QMessageBox.warning(dlg, "Error", "Amount is required and must be a number.")
                return
            fund_id = source_input.currentData()
            description = description_input.text().strip()

            # Validation: Required fields
            if not year or not amount or not fund_id:
                QMessageBox.warning(dlg, "Error", "Year, Amount, and Source (Fund) are required.")
                return

            # Validation: Uniqueness (BudgetYear, ProgramID, ProjectID, ActivityID) excluding current
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                cur.execute(
                    "SELECT 1 FROM Budget WHERE BudgetYear=? AND ProgramID=? AND ProjectID=? AND ActivityID=? AND BudgetID != ?",
                    (year, program_id, project_id, activity_id, budget_id)
                )
                if cur.fetchone():
                    QMessageBox.warning(
                        dlg, "Error",
                        "A budget with the same Year, Program, Project, and Activity already exists. "
                        "Each combination must be unique."
                    )
                    return
            finally:
                conn.close()

            # Validation: FundType and Program/Project match for Restricted
            fund = fund_map.get(fund_id)
            if not fund:
                QMessageBox.warning(dlg, "Error", "Selected fund not found.")
                return
            fund_type = fund["FundType"]
            fund_prog = fund["ProgramID"]
            fund_proj = fund["ProjectID"]
            fund_year = fund["BudgetYear"]

            if fund_type == "Restricted":
                # Must match program and project
                if (program_id != fund_prog) or (project_id != fund_proj):
                    QMessageBox.warning(
                        dlg, "Error",
                        "For Restricted funds, the selected Program and Project must match those of the Fund.\n"
                        f"Fund Program: {fund_prog}, Fund Project: {fund_proj}"
                    )
                    return
                # Optionally, check year match
                if str(year) != str(fund_year):
                    QMessageBox.warning(
                        dlg, "Error",
                        "For Restricted funds, the Budget Year must match the Fund's Budget Year."
                    )
                    return
            # For Unrestricted, allow any program/project

            # Validation: Budget amount does not exceed available fund
            # Sum all budgets for this fund (for all years/programs/projects/activities), excluding current
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                cur.execute(
                    "SELECT IFNULL(SUM(BudgetAmount),0) FROM Budget WHERE FundID=? AND BudgetID != ?",
                    (fund_id, budget_id)
                )
                total_budgeted = cur.fetchone()[0]
                # Get total fund amount (sum of all transactions for this fund)
                cur.execute("""
                    SELECT IFNULL(SUM(t.Amount),0)
                    FROM FundTransactions ft
                    JOIN Transactions t ON ft.Transaction_id = t.TransactionID
                    WHERE ft.fund_id=?
                """, (fund_id,))
                total_fund = cur.fetchone()[0]
            finally:
                conn.close()
            # If no transactions exist, treat fund as 0 (cannot allocate)
            if total_fund == 0:
                QMessageBox.warning(
                    dlg, "Error",
                    "No available funds for this source. Please add a fund transaction first."
                )
                return
            # Check if new budget would exceed available fund
            if total_budgeted + amount > total_fund:
                QMessageBox.warning(
                    dlg, "Error",
                    f"Budget exceeds available fund amount.\n"
                    f"Available: {total_fund - total_budgeted:.2f}, Requested: {amount:.2f}"
                )
                return

            # Passed all validations, update
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                cur.execute("""
                    UPDATE Budget SET BudgetYear=?, ProgramID=?, ProjectID=?, ActivityID=?, BudgetAmount=?, FundID=?, BudgetDescription=?
                    WHERE BudgetID=?
                """, (year, program_id, project_id, activity_id, amount, fund_id, description, budget_id))
                conn.commit()
            except Exception as e:
                QMessageBox.warning(dlg, "Error", f"Failed to update budget: {e}")
                return
            finally:
                conn.close()
            dlg.accept()
            self.refresh_budget_table()

        save_btn.clicked.connect(save)
        dlg.exec_()

    def delete_budget(self, budget_id):
        reply = QMessageBox.question(self, "Delete", "Delete this budget?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                cur.execute("DELETE FROM Budget WHERE BudgetID=?", (budget_id,))
                conn.commit()
            finally:
                conn.close()
            self.refresh_budget_table()

class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.load_data()
        
    def setup_ui(self):
        """Initialize all UI components with modern design"""
        # Main layout with subtle gradient background
        self.setStyleSheet("""
            DashboardPage {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #f8f9fa, stop:1 #e9ecef);
            }
        """)
        
        # Main scroll area
        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)
        scroll.setStyleSheet(self.get_scrollbar_styles())
        
        # Content container
        content = QWidget()
        self.main_layout = QVBoxLayout(content)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(20)
        
        # Header with title and quick stats
        self.setup_header()
        
        # Cards grid layout
        self.cards_grid = QGridLayout()
        self.cards_grid.setSpacing(20)
        self.cards_grid.setContentsMargins(0, 0, 0, 0)
        
        # Add cards to the grid
        self.setup_fund_card()
        self.setup_budget_card()
        self.setup_transaction_card()
        self.setup_projects_card()
        
        self.main_layout.addLayout(self.cards_grid)
        scroll.setWidget(content)
        
        # Main window layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(scroll)
    
    def get_scrollbar_styles(self):
        """Return modern scrollbar styles"""
        return """
            QScrollArea {
                border: none;
                background: transparent;
            }
            QScrollBar:vertical {
                background: rgba(0,0,0,0);
                width: 10px;
                margin: 2px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical {
                background: #adb5bd;
                min-height: 30px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical:hover {
                background: #6c757d;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
        """
    
    def setup_header(self):
        """Setup the dashboard header with title and quick stats"""
        header = QWidget()
        header.setStyleSheet("background: rgba(255,255,255,0.7); border-radius: 12px;")
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(20, 15, 20, 15)
        
        # Title with icon
        title_container = QWidget()
        title_layout = QHBoxLayout(title_container)
        title_layout.setContentsMargins(0, 0, 0, 0)
        
        icon = QLabel()
        icon.setPixmap(QPixmap("Icons/dashboard.svg").scaled(32, 32, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        title_layout.addWidget(icon)
        
        title = QLabel("Financial Dashboard")
        title.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: #212529;
            margin-left: 10px;
        """)
        title_layout.addWidget(title)
        title_layout.addStretch()
        
        # Quick stats
        stats_container = QWidget()
        stats_layout = QHBoxLayout(stats_container)
        stats_layout.setSpacing(15)
        
        def quick_stat(value, label, color):
            stat = QWidget()
            stat_layout = QVBoxLayout(stat)
            stat_layout.setSpacing(2)
            
            value_label = QLabel(str(value))
            value_label.setStyleSheet(f"""
                font-size: 18px;
                font-weight: bold;
                color: {color};
            """)
            value_label.setAlignment(Qt.AlignRight)
            
            label_label = QLabel(label)
            label_label.setStyleSheet("""
                font-size: 12px;
                color: #6c757d;
            """)
            label_label.setAlignment(Qt.AlignRight)
            
            stat_layout.addWidget(value_label)
            stat_layout.addWidget(label_label)
            return stat
        
        # Placeholder stats - will be updated in load_data()
        self.total_funds_stat = quick_stat("0", "Total Funds", "#007bff")
        self.total_expenses_stat = quick_stat("0", "Expenses", "#dc3545")
        self.budget_utilization_stat = quick_stat("0%", "Utilization", "#28a745")
        
        stats_layout.addWidget(self.total_funds_stat)
        stats_layout.addWidget(QLabel("|"))
        stats_layout.addWidget(self.total_expenses_stat)
        stats_layout.addWidget(QLabel("|"))
        stats_layout.addWidget(self.budget_utilization_stat)
        
        header_layout.addWidget(title_container)
        header_layout.addStretch()
        header_layout.addWidget(stats_container)
        
        self.main_layout.addWidget(header)
    
    def setup_fund_card(self):
        """Fund Overview card with charts"""
        card = self.create_card("Fund Overview", "#007bff")
        layout = QVBoxLayout(card)
        layout.setSpacing(15)
        
        # Stats row
        stats_row = QHBoxLayout()
        stats_row.setSpacing(15)
        
        def stat_box(value, label, color, icon=None):
            widget = QWidget()
            widget.setStyleSheet("""
                background: white;
                border-radius: 8px;
                padding: 10px;
            """)
            box_layout = QVBoxLayout(widget)
            box_layout.setSpacing(5)
            
            if icon:
                icon_label = QLabel()
                icon_label.setPixmap(QPixmap(icon).scaled(24, 24, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                icon_label.setAlignment(Qt.AlignRight)
                box_layout.addWidget(icon_label)
            
            value_label = QLabel(str(value))
            value_label.setStyleSheet(f"""
                font-size: 18px;
                font-weight: bold;
                color: {color};
            """)
            
            label_label = QLabel(label)
            label_label.setStyleSheet("""
                font-size: 12px;
                color: #6c757d;
            """)
            
            box_layout.addWidget(value_label)
            box_layout.addWidget(label_label)
            return widget
        
        # Placeholder stats - will be updated in load_data()
        self.fund_received_stat = stat_box("0", "Received", "#007bff", "Icons/funds.svg")
        self.fund_allocated_stat = stat_box("0", "Allocated", "#28a745", "Icons/budget.svg")
        self.fund_available_stat = stat_box("0", "Available", "#dc3545", "Icons/wallet.svg")
        
        stats_row.addWidget(self.fund_received_stat)
        stats_row.addWidget(self.fund_allocated_stat)
        stats_row.addWidget(self.fund_available_stat)
        layout.addLayout(stats_row)
        
        # Charts container
        charts_container = QWidget()
        charts_layout = QHBoxLayout(charts_container)
        charts_layout.setContentsMargins(0, 0, 0, 0)
        charts_layout.setSpacing(15)
        
        # Funds flow chart
        self.funds_flow_chart = FigureCanvas(Figure(figsize=(5, 3)))
        self.funds_flow_chart.setStyleSheet("background: transparent;")
        self.funds_flow_chart.setMinimumHeight(250)
        
        # Funds type chart
        self.funds_type_chart = FigureCanvas(Figure(figsize=(3, 3)))
        self.funds_type_chart.setStyleSheet("background: transparent;")
        self.funds_type_chart.setMinimumHeight(250)
        
        charts_layout.addWidget(self.funds_flow_chart, 2)
        charts_layout.addWidget(self.funds_type_chart, 1)
        layout.addWidget(charts_container)
        
        self.cards_grid.addWidget(card, 0, 0, 1, 2)  # Span 2 columns
    
    def setup_budget_card(self):
        """Budget Summary card with utilization meter"""
        card = self.create_card("Budget Summary", "#28a745")
        layout = QVBoxLayout(card)
        layout.setSpacing(15)
        
        # Utilization meter
        meter_container = QWidget()
        meter_layout = QVBoxLayout(meter_container)
        meter_layout.setSpacing(5)
        
        meter_header = QHBoxLayout()
        meter_header.addWidget(QLabel("Budget Utilization"))
        meter_header.addStretch()
        self.utilization_value = QLabel("0%")
        self.utilization_value.setStyleSheet("font-weight: bold; color: #28a745;")
        meter_header.addWidget(self.utilization_value)
        meter_layout.addLayout(meter_header)
        
        self.utilization_meter = QProgressBar()
        self.utilization_meter.setRange(0, 100)
        self.utilization_meter.setTextVisible(False)
        self.utilization_meter.setStyleSheet("""
            QProgressBar {
                height: 12px;
                background: #e9ecef;
                border-radius: 6px;
            }
            QProgressBar::chunk {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #28a745, stop:1 #5cb85c);
                border-radius: 6px;
            }
        """)
        meter_layout.addWidget(self.utilization_meter)
        layout.addWidget(meter_container)
        
        # Budget by program chart
        self.budget_program_chart = FigureCanvas(Figure(figsize=(5, 3)))
        self.budget_program_chart.setStyleSheet("background: transparent;")
        self.budget_program_chart.setMinimumHeight(250)
        layout.addWidget(self.budget_program_chart)
        
        self.cards_grid.addWidget(card, 1, 0)
    
    def setup_transaction_card(self):
        """Transaction Summary card with recent transactions"""
        card = self.create_card("Transactions", "#17a2b8")
        layout = QVBoxLayout(card)
        layout.setSpacing(15)
        
        # Transaction type breakdown
        type_container = QWidget()
        type_layout = QHBoxLayout(type_container)
        type_layout.setContentsMargins(0, 0, 0, 0)
        
        def type_indicator(color, label):
            widget = QWidget()
            widget_layout = QHBoxLayout(widget)
            widget_layout.setSpacing(5)
            
            dot = QLabel()
            dot.setFixedSize(12, 12)
            dot.setStyleSheet(f"""
                background: {color};
                border-radius: 6px;
            """)
            
            label = QLabel(label)
            label.setStyleSheet("font-size: 12px; color: #495057;")
            
            widget_layout.addWidget(dot)
            widget_layout.addWidget(label)
            widget_layout.addStretch()
            return widget
        
        # Placeholder indicators - will be updated in load_data()
        self.funds_indicator = type_indicator("#007bff", "Funds: $0")
        self.expenses_indicator = type_indicator("#dc3545", "Expenses: $0")
        
        type_layout.addWidget(self.funds_indicator)
        type_layout.addWidget(self.expenses_indicator)
        type_layout.addStretch()
        layout.addWidget(type_container)
        
        # Recent transactions table
        self.transaction_table = QTableWidget()
        self.transaction_table.setColumnCount(4)
        self.transaction_table.setHorizontalHeaderLabels(["Date", "Type", "Amount", "Reference"])
        self.transaction_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.transaction_table.verticalHeader().setVisible(False)
        self.transaction_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.transaction_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.transaction_table.setStyleSheet("""
            QTableWidget {
                background: white;
                border-radius: 8px;
                border: 1px solid #dee2e6;
                font-size: 12px;
            }
            QTableWidget::item {
                padding: 5px;
            }
            QHeaderView::section {
                background: #f8f9fa;
                padding: 5px;
                border: none;
            }
        """)
        self.transaction_table.setMinimumHeight(200)
        layout.addWidget(self.transaction_table)
        
        self.cards_grid.addWidget(card, 1, 1)
    
    def setup_projects_card(self):
        """Projects Insights card with program performance"""
        card = self.create_card("Programs & Projects", "#6f42c1")
        layout = QVBoxLayout(card)
        layout.setSpacing(15)
        
        # Stats row
        stats_row = QHBoxLayout()
        stats_row.setSpacing(15)
        
        def mini_stat(value, label, color):
            widget = QWidget()
            widget_layout = QVBoxLayout(widget)
            widget_layout.setSpacing(2)
            
            value_label = QLabel(str(value))
            value_label.setStyleSheet(f"""
                font-size: 16px;
                font-weight: bold;
                color: {color};
            """)
            value_label.setAlignment(Qt.AlignCenter)
            
            label_label = QLabel(label)
            label_label.setStyleSheet("""
                font-size: 11px;
                color: #6c757d;
            """)
            label_label.setAlignment(Qt.AlignCenter)
            
            widget_layout.addWidget(value_label)
            widget_layout.addWidget(label_label)
            return widget
        
        # Placeholder stats - will be updated in load_data()
        self.programs_stat = mini_stat("0", "Programs", "#6f42c1")
        self.projects_stat = mini_stat("0", "Projects", "#17a2b8")
        self.top_project_stat = mini_stat("-", "Top Project", "#dc3545")
        
        stats_row.addWidget(self.programs_stat)
        stats_row.addWidget(self.projects_stat)
        stats_row.addWidget(self.top_project_stat)
        layout.addLayout(stats_row)
        
        # Program performance chart
        self.program_performance_chart = FigureCanvas(Figure(figsize=(5, 3)))
        self.program_performance_chart.setStyleSheet("background: transparent;")
        self.program_performance_chart.setMinimumHeight(250)
        layout.addWidget(self.program_performance_chart)
        
        self.cards_grid.addWidget(card, 2, 0, 1, 2)  # Span 2 columns
    
    def create_card(self, title, color):
        """Create a styled card container"""
        card = QGroupBox(title)
        card.setStyleSheet(f"""
            QGroupBox {{
                font-size: 16px;
                font-weight: bold;
                color: {color};
                border: 1px solid #dee2e6;
                border-radius: 12px;
                background: white;
                margin-top: 10px;
                padding-top: 20px;
            }}
            QGroupBox::title {{
                subcontrol-origin: margin;
                left: 12px;
                padding: 0 5px;
            }}
        """)
        return card
    
    def load_data(self):
        """Load and display all dashboard data"""
        try:
            year = str(datetime.now().year)
            conn = get_db_connection()
            
            # Fund data
            cur = conn.cursor()
            cur.execute("""
                SELECT IFNULL(SUM(t.Amount),0) as total
                FROM FundTransactions ft
                JOIN Transactions t ON ft.Transaction_id = t.TransactionID
                WHERE t.BudgetYear LIKE ?
            """, (f"{year}%",))
            total_funds = cur.fetchone()["total"]
            
            cur.execute("""
                SELECT IFNULL(SUM(BudgetAmount),0) as total
                FROM Budget
                WHERE BudgetYear LIKE ?
            """, (f"{year}%",))
            total_budget = cur.fetchone()["total"]
            
            cur.execute("""
                SELECT FundType, IFNULL(SUM(t.Amount),0) as total
                FROM Fund f
                LEFT JOIN FundTransactions ft ON f.FundID = ft.fund_id
                LEFT JOIN Transactions t ON ft.Transaction_id = t.TransactionID
                WHERE f.BudgetYear LIKE ?
                GROUP BY FundType
            """, (f"{year}%",))
            fund_types = {row["FundType"]: row["total"] for row in cur.fetchall()}
            
            # Budget data
            cur.execute("""
                SELECT IFNULL(SUM(Amount),0) as total
                FROM Transactions
                WHERE TransactionType='Expense' AND BudgetYear LIKE ?
            """, (f"{year}%",))
            total_expense = cur.fetchone()["total"]
            
            # Program data
            cur.execute("SELECT COUNT(*) as cnt FROM Program_administrations")
            prog_count = cur.fetchone()["cnt"]
            
            cur.execute("SELECT COUNT(*) as cnt FROM Projects")
            proj_count = cur.fetchone()["cnt"]
            
            cur.execute("""
                SELECT pa.PA_Name, IFNULL(SUM(t.Amount),0) as total
                FROM Transactions t
                LEFT JOIN Program_administrations pa ON t.ProgramID = pa.PA_Id
                WHERE t.TransactionType='Expense' AND t.BudgetYear LIKE ?
                GROUP BY pa.PA_Name
                ORDER BY total DESC LIMIT 1
            """, (f"{year}%",))
            top_proj = cur.fetchone()
            
            # Transaction data
            cur.execute("""
                SELECT TransactionType, IFNULL(SUM(Amount),0) as total
                FROM Transactions
                WHERE BudgetYear LIKE ?
                GROUP BY TransactionType
            """, (f"{year}%",))
            tx_types = cur.fetchall()
            
            cur.execute("""
                SELECT TransactionDate, TransactionType, Amount, Reference
                FROM Transactions
                WHERE BudgetYear LIKE ?
                ORDER BY TransactionDate DESC, TransactionID DESC
                LIMIT 5
            """, (f"{year}%",))
            recent_tx = cur.fetchall()
            
            # Budget by program
            cur.execute("""
                SELECT pa.PA_Name, IFNULL(SUM(b.BudgetAmount),0) as budgeted
                FROM Budget b
                LEFT JOIN Program_administrations pa ON b.ProgramID = pa.PA_Id
                WHERE b.BudgetYear LIKE ?
                GROUP BY pa.PA_Name
            """, (f"{year}%",))
            prog_budgets = cur.fetchall()
            
            # Program performance
            cur.execute("""
                SELECT pa.PA_Name,
                    IFNULL(SUM(b.BudgetAmount),0) as budgeted,
                    IFNULL(SUM(t.Amount),0) as spent
                FROM Program_administrations pa
                LEFT JOIN Budget b ON pa.PA_Id = b.ProgramID AND b.BudgetYear LIKE ?
                LEFT JOIN Transactions t ON pa.PA_Id = t.ProgramID AND t.TransactionType='Expense' AND t.BudgetYear LIKE ?
                GROUP BY pa.PA_Name
            """, (f"{year}%", f"{year}%"))
            prog_performance = cur.fetchall()
            
        finally:
            conn.close()
        
        # Update UI with data
        self.update_fund_card(total_funds, total_budget, fund_types)
        self.update_budget_card(total_budget, total_expense, prog_budgets)
        self.update_transaction_card(tx_types, recent_tx)
        self.update_projects_card(prog_count, proj_count, top_proj, prog_performance)
        
        # Update header stats
        self.total_funds_stat.findChild(QLabel).setText(f"${total_funds:,.2f}")
        self.total_expenses_stat.findChild(QLabel).setText(f"${total_expense:,.2f}")
        utilization = (total_expense / total_budget * 100) if total_budget else 0
        self.budget_utilization_stat.findChild(QLabel).setText(f"{utilization:.1f}%")
    
    def update_fund_card(self, total_funds, total_budget, fund_types):
        """Update the fund overview card with data"""
        available = total_funds - total_budget
        restricted = fund_types.get("Restricted", 0)
        unrestricted = fund_types.get("Unrestricted", 0)
        
        # Update stats
        self.fund_received_stat.findChild(QLabel).setText(f"${total_funds:,.2f}")
        self.fund_allocated_stat.findChild(QLabel).setText(f"${total_budget:,.2f}")
        self.fund_available_stat.findChild(QLabel).setText(f"${available:,.2f}")
        
        # Update funds flow chart
        fig1 = self.funds_flow_chart.figure
        fig1.clear()
        ax1 = fig1.add_subplot(111)
        
        labels = ["Received", "Allocated", "Available"]
        values = [total_funds, total_budget, available]
        colors = ["#007bff", "#28a745", "#dc3545"]
        
        bars = ax1.bar(labels, values, color=colors)
        ax1.set_title("Funds Flow Overview", fontsize=12)
        
        for bar in bars:
            height = bar.get_height()
            ax1.annotate(f'${height:,.0f}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=9)
        
        fig1.tight_layout()
        self.funds_flow_chart.draw()
        
        # Update funds type chart
        fig2 = self.funds_type_chart.figure
        fig2.clear()
        ax2 = fig2.add_subplot(111)
        
        labels = ["Restricted", "Unrestricted"]
        values = [restricted, unrestricted]
        colors = ["#6f42c1", "#17a2b8"]
        
        wedges, texts, autotexts = ax2.pie(
            values,
            labels=labels,
            autopct='%1.1f%%',
            colors=colors,
            startangle=90,
            textprops={'color': "white", 'fontsize': 10}
        )
        ax2.set_title("Funds by Type", fontsize=12)
        fig2.tight_layout()
        self.funds_type_chart.draw()
    
    def update_budget_card(self, total_budget, total_expense, prog_budgets):
        """Update the budget summary card with data"""
        # Update utilization meter
        utilization = (total_expense / total_budget * 100) if total_budget else 0
        self.utilization_meter.setValue(int(utilization))
        self.utilization_value.setText(f"{utilization:.1f}%")
        
        # Update program budget chart
        fig = self.budget_program_chart.figure
        fig.clear()
        ax = fig.add_subplot(111)
        
        prog_names = [row["PA_Name"] or "Unassigned" for row in prog_budgets]
        budget_values = [row["budgeted"] for row in prog_budgets]
        
        # Sort by budget amount (descending)
        sorted_data = sorted(zip(prog_names, budget_values), key=lambda x: x[1], reverse=True)
        prog_names = [x[0] for x in sorted_data]
        budget_values = [x[1] for x in sorted_data]
        
        bars = ax.barh(prog_names, budget_values, color="#17a2b8")
        ax.set_title("Budget by Program", fontsize=12)
        
        for bar in bars:
            width = bar.get_width()
            ax.annotate(f'${width:,.0f}',
                       xy=(width, bar.get_y() + bar.get_height() / 2),
                       xytext=(3, 0),
                       textcoords="offset points",
                       ha='left', va='center', fontsize=9)
        
        fig.tight_layout()
        self.budget_program_chart.draw()
    
    def update_transaction_card(self, tx_types, recent_tx):
        """Update the transaction summary card with data"""
        # Update type indicators
        funds = next((row["total"] for row in tx_types if row["TransactionType"] == "Funds"), 0)
        expenses = next((row["total"] for row in tx_types if row["TransactionType"] == "Expense"), 0)
        
        self.funds_indicator.findChild(QLabel).setText(f"Funds: ${funds:,.2f}")
        self.expenses_indicator.findChild(QLabel).setText(f"Expenses: ${expenses:,.2f}")
        
        # Update recent transactions table
        self.transaction_table.setRowCount(len(recent_tx))
        for i, row in enumerate(recent_tx):
            self.transaction_table.setItem(i, 0, QTableWidgetItem(row["TransactionDate"] or ""))
            
            type_item = QTableWidgetItem(row["TransactionType"] or "")
            if row["TransactionType"] == "Funds":
                type_item.setForeground(QColor("#007bff"))
            else:
                type_item.setForeground(QColor("#dc3545"))
            self.transaction_table.setItem(i, 1, type_item)
            
            amount = row["Amount"]
            amount_item = QTableWidgetItem(f"${abs(amount):,.2f}")
            amount_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            if row["TransactionType"] == "Funds":
                amount_item.setForeground(QColor("#28a745"))
            else:
                amount_item.setForeground(QColor("#dc3545"))
            self.transaction_table.setItem(i, 2, amount_item)
            
            self.transaction_table.setItem(i, 3, QTableWidgetItem(row["Reference"] or ""))
    
    def update_projects_card(self, prog_count, proj_count, top_proj, prog_performance):
        """Update the projects insights card with data"""
        # Update stats
        self.programs_stat.findChild(QLabel).setText(str(prog_count))
        self.projects_stat.findChild(QLabel).setText(str(proj_count))
        
        if top_proj:
            self.top_project_stat.findChild(QLabel).setText(top_proj["PA_Name"] or "N/A")
            self.top_project_stat.findChild(QLabel).setText(f"${top_proj['total']:,.2f}")
       
        # Update program performance chart
        fig = self.program_performance_chart.figure
        fig.clear()
        ax = fig.add_subplot(111)
        
        prog_names = [row["PA_Name"] or "Unassigned" for row in prog_performance]
        budgeted = [row["budgeted"] for row in prog_performance]
        spent = [abs(row["spent"]) for row in prog_performance]  # Make spent positive
        
        # Sort by budgeted amount (descending)
        sorted_data = sorted(zip(prog_names, budgeted, spent), key=lambda x: x[1], reverse=True)
        prog_names = [x[0] for x in sorted_data]
        budgeted = [x[1] for x in sorted_data]
        spent = [x[2] for x in sorted_data]
        
        x = np.arange(len(prog_names))
        width = 0.35
        
        bars1 = ax.bar(x - width/2, budgeted, width, label="Budgeted", color="#28a745")
        bars2 = ax.bar(x + width/2, spent, width, label="Spent", color="#dc3545")
        
        ax.set_xticks(x)
        ax.set_xticklabels(prog_names, rotation=45, ha='right')
        ax.set_title("Program Performance", fontsize=12)
        ax.legend()
        
        # Add percentage labels
        for i, (b, s) in enumerate(zip(budgeted, spent)):
            if b > 0:
                pct = (s / b * 100)
                ax.text(i, max(b, s) * 1.05, f"{pct:.1f}%", 
                       ha='center', va='bottom', fontsize=9, color="#6c757d")
        
        fig.tight_layout()
        self.program_performance_chart.draw()

class ReportPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.connect_signals()
        self.generate_report()  # Initial load

    def setup_ui(self):
        """Initialize all UI components with responsive layouts"""
        # Main scroll area setup
        self.scroll = QScrollArea(self)
        self.scroll.setWidgetResizable(True)
        self.scroll.setFrameShape(QFrame.NoFrame)
        self.scroll.setStyleSheet(self.get_scrollbar_styles())

        # Content container
        self.content = QWidget()
        self.main_layout = QVBoxLayout(self.content)
        self.main_layout.setContentsMargins(24, 24, 24, 24)
        self.main_layout.setSpacing(24)

        # Header section
        self.setup_header()
        
        # Sections
        self.setup_section1()  # Funds & Expenses Overview
        self.setup_section2()  # Expenses vs Budget
        self.setup_section3()  # Transaction Summary
        self.setup_section4()  # Additional Insights (optional)

        self.main_layout.addStretch(1)
        self.scroll.setWidget(self.content)
        
        # Main layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.scroll)

    def get_scrollbar_styles(self):
        """Return consistent scrollbar styles"""
        return """
            QScrollArea {
                border: none;
                background: transparent;
            }
            QScrollBar:vertical {
                background: #f8f9fa;
                width: 10px;
                margin: 2px 0 2px 0;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical {
                background: #007bff;
                min-height: 30px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical:hover {
                background: #0056b3;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
        """

    def setup_header(self):
        """Setup the header with filters and title"""
        self.header = QWidget()
        header_layout = QHBoxLayout(self.header)
        header_layout.setContentsMargins(0, 0, 0, 0)
        header_layout.setSpacing(12)

        # Title
        title = QLabel("Report")
        title.setStyleSheet("""
            font-size: 28px; 
            font-weight: bold; 
            color: #1B263B;
        """)
        header_layout.addWidget(title, alignment=Qt.AlignLeft)
        header_layout.addStretch()

        # Filters
        self.year_filter = QComboBox()
        years = generate_years(format_type="range", 
                             start_year=datetime.now().year, 
                             num_years=10)
        self.year_filter.addItems(years)
        self.year_filter.setCurrentText(str(datetime.now().year))
        self.year_filter.setStyleSheet(FormStyles())
        self.year_filter.setMinimumWidth(100)

        self.month_filter = QComboBox()
        months = ["All"] + [QDate.longMonthName(i) for i in range(1, 13)]
        self.month_filter.addItems(months)
        self.month_filter.setCurrentIndex(QDate.currentDate().month())
        self.month_filter.setStyleSheet(FormStyles())
        self.month_filter.setMinimumWidth(120)

        self.generate_btn = button("Generate", "primary", "md", 
                                  icon_path="Icons/print.svg", 
                                  icon_toolTip="Generate Report")

        # Add widgets with proper spacing
        header_layout.addWidget(QLabel("Year:"))
        header_layout.addWidget(self.year_filter)
        header_layout.addWidget(QLabel("Month:"))
        header_layout.addWidget(self.month_filter)
        header_layout.addWidget(self.generate_btn)
        
        self.main_layout.addWidget(self.header)

    def setup_section1(self):
        """Funds & Expenses Overview section"""
        self.section1 = QGroupBox("Funds & Expenses Overview")
        self.section1.setStyleSheet(self.get_section_style("#007bff"))
        s1_layout = QVBoxLayout(self.section1)
        s1_layout.setSpacing(16)

        # Charts container with responsive layout
        charts_container = QWidget()
        charts_layout = QHBoxLayout(charts_container)
        charts_layout.setContentsMargins(0, 0, 0, 0)
        charts_layout.setSpacing(16)

        # Left chart (Funds & Expenses)
        self.funds_expenses_chart = FigureCanvas(Figure(figsize=(6, 4)))
        self.funds_expenses_chart.setMinimumSize(400, 300)
        charts_layout.addWidget(self.funds_expenses_chart, 2)

        # Right chart (Unused Funds)
        self.unused_funds_chart = FigureCanvas(Figure(figsize=(4, 4)))
        self.unused_funds_chart.setMinimumSize(300, 300)
        charts_layout.addWidget(self.unused_funds_chart, 1)

        s1_layout.addWidget(charts_container)
        self.main_layout.addWidget(self.section1)

    def setup_section2(self):
        """Expenses vs Budget section"""
        self.section2 = QGroupBox("Expenses vs Budget Allocated (by Project)")
        self.section2.setStyleSheet(self.get_section_style("#28a745"))
        s2_layout = QVBoxLayout(self.section2)
        s2_layout.setSpacing(16)

        self.project_expense_chart = FigureCanvas(Figure(figsize=(10, 5)))
        self.project_expense_chart.setMinimumHeight(400)
        s2_layout.addWidget(self.project_expense_chart)
        
        self.main_layout.addWidget(self.section2)

    def setup_section3(self):
        """Transaction Summary section"""
        self.section3 = QGroupBox("Transaction Summary by Subcategory")
        self.section3.setStyleSheet(self.get_section_style("#17a2b8"))
        s3_layout = QVBoxLayout(self.section3)
        s3_layout.setSpacing(16)

        self.subcat_table = QTableWidget()
        self.subcat_table.setColumnCount(3)
        self.subcat_table.setHorizontalHeaderLabels([
            "Subcategory", "Total Funds", "Total Expenses"
        ])
        self.subcat_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.subcat_table.verticalHeader().setVisible(False)
        self.subcat_table.setStyleSheet(TableStyles())
        self.subcat_table.setMinimumHeight(300)
        
        s3_layout.addWidget(self.subcat_table)
        self.main_layout.addWidget(self.section3)

    def setup_section4(self):
        """Optional section for future expansion"""
        self.section4 = QGroupBox("Additional Insights")
        self.section4.setStyleSheet(self.get_section_style("#6f42c1"))
        s4_layout = QVBoxLayout(self.section4)
        s4_layout.addWidget(QLabel("Customize this section for more insights..."))
        self.main_layout.addWidget(self.section4)

    def get_section_style(self, border_color):
        """Return consistent section styling"""
        return f"""
            QGroupBox {{
                font-size: 18px;
                font-weight: bold;
                color: #1B263B;
                border: 1.5px solid {border_color};
                border-radius: 10px;
                margin-top: 8px;
                padding: 20px 16px 20px 16px;
            }}
            QGroupBox::title {{
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 3px;
            }}
        """

    def connect_signals(self):
        """Connect all signals and slots"""
        self.generate_btn.clicked.connect(self.generate_report)
        self.year_filter.currentIndexChanged.connect(self.generate_report)
        self.month_filter.currentIndexChanged.connect(self.generate_report)

    def generate_report(self):
        """Generate and display the report data"""
        try:
            year = self.year_filter.currentText()
            month = self.month_filter.currentText()
            
            # Prepare date filter
            date_filter = self.prepare_date_filter(year, month)
            
            # Get data from database
            data = self.fetch_report_data(year, date_filter)
            
            # Update charts and tables
            self.update_section1(data)
            self.update_section2(data)
            self.update_section3(data)
            
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to generate report: {str(e)}")

    def prepare_date_filter(self, year, month):
        """Prepare the date filter string based on selections"""
        if month == "All":
            return f"{year[:4]}%"
        else:
            month_num = [QDate.longMonthName(i) for i in range(1, 13)].index(month) + 1
            return f"{year[:4]}-{month_num:02d}%"

    def fetch_report_data(self, year, date_filter):
        """Fetch all report data from database"""
        data = {}
        conn = get_db_connection()
        try:
            cur = conn.cursor()
            
            # Section 1 data
            cur.execute("""
                SELECT strftime('%m', TransactionDate) as month, 
                    SUM(CASE WHEN TransactionType='Funds' THEN Amount ELSE 0 END) as funds,
                    SUM(CASE WHEN TransactionType='Expense' THEN Amount ELSE 0 END) as expenses
                FROM Transactions
                WHERE BudgetYear LIKE ? AND TransactionDate LIKE ?
                GROUP BY month
                ORDER BY month
            """, (f"{year[:4]}%", date_filter))
            data['monthly'] = cur.fetchall()
            
            # Unused funds data
            cur.execute("""
                SELECT f.FundName,
                    IFNULL(SUM(t.Amount),0) as received,
                    IFNULL((SELECT SUM(BudgetAmount) FROM Budget b WHERE b.FundID=f.FundID AND b.BudgetYear LIKE ?),0) as allocated
                FROM Fund f
                LEFT JOIN FundTransactions ft ON f.FundID = ft.fund_id
                LEFT JOIN Transactions t ON ft.Transaction_id = t.TransactionID
                WHERE f.BudgetYear LIKE ?
                GROUP BY f.FundID
            """, (f"{year[:4]}%", f"{year[:4]}%"))
            data['unused_funds'] = cur.fetchall()
            
            # Section 2 data
            cur.execute("""
                SELECT p.ProjectName,
                    IFNULL(SUM(b.BudgetAmount),0) as budgeted,
                    IFNULL(SUM(t.Amount),0) as spent
                FROM Projects p
                LEFT JOIN Budget b ON p.ProjectID = b.ProjectID AND b.BudgetYear LIKE ?
                LEFT JOIN Transactions t ON p.ProjectID = t.ProjectID AND t.TransactionType='Expense' AND t.BudgetYear LIKE ?
                GROUP BY p.ProjectID
            """, (f"{year[:4]}%", f"{year[:4]}%"))
            data['projects'] = cur.fetchall()
            
            # Section 3 data
            cur.execute("""
                SELECT s.Name as Subcategory,
                    SUM(CASE WHEN t.TransactionType='Funds' THEN t.Amount ELSE 0 END) as total_funds,
                    SUM(CASE WHEN t.TransactionType='Expense' THEN t.Amount ELSE 0 END) as total_expenses
                FROM Subcategories s
                LEFT JOIN Transactions t ON t.SubCategories = s.SubCategoryID AND t.BudgetYear LIKE ?
                GROUP BY s.SubCategoryID
            """, (f"{year[:4]}%",))
            data['subcategories'] = cur.fetchall()
            
        finally:
            conn.close()
            
        return data

    def update_section1(self, data):
        """Update the Funds & Expenses section"""
        # Process monthly data
        months_labels = []
        funds_vals = []
        expenses_vals = []
        for r in data['monthly']:
            m = int(r["month"]) if r["month"] else 0
            months_labels.append(QDate.longMonthName(m) if m else "")
            funds_vals.append(r["funds"] or 0)
            expenses_vals.append(abs(r["expenses"] or 0))  # Make expenses positive for chart
            
        # Plot Funds vs Expenses
        fig1 = self.funds_expenses_chart.figure
        fig1.clear()
        ax = fig1.add_subplot(111)
        
        x = np.arange(len(months_labels))
        width = 0.35
        ax.bar(x - width/2, funds_vals, width, label="Funds", color="#007bff")
        ax.bar(x + width/2, expenses_vals, width, label="Expenses", color="#dc3545")
        
        ax.set_xticks(x)
        ax.set_xticklabels(months_labels)
        ax.set_ylabel("Amount ($)")
        ax.set_title("Monthly Funds & Expenses")
        ax.legend()
        fig1.tight_layout()
        self.funds_expenses_chart.draw()
        
        # Process unused funds data
        fund_names = [r["FundName"] for r in data['unused_funds']]
        unused_vals = [r["received"] - r["allocated"] for r in data['unused_funds']]
        
        # Plot Unused Funds
        fig2 = self.unused_funds_chart.figure
        fig2.clear()
        ax2 = fig2.add_subplot(111)
        
        # Use horizontal bar for better readability
        ax2.barh(fund_names, unused_vals, color="#28a745")
        ax2.set_xlabel("Unused Amount ($)")
        ax2.set_title("Unused Funds by Source")
        fig2.tight_layout()
        self.unused_funds_chart.draw()

    def update_section2(self, data):
        """Update the Projects section"""
        proj_names = [r["ProjectName"] for r in data['projects']]
        budgeted = [r["budgeted"] or 0 for r in data['projects']]
        spent = [abs(r["spent"] or 0) for r in data['projects']]  # Make spent positive
        percent = [((s / b) * 100 if b else 0) for s, b in zip(spent, budgeted)]
        
        fig3 = self.project_expense_chart.figure
        fig3.clear()
        ax3 = fig3.add_subplot(111)
        
        x = np.arange(len(proj_names))
        width = 0.35
        ax3.bar(x - width/2, budgeted, width, label="Budgeted", color="#28a745")
        ax3.bar(x + width/2, spent, width, label="Spent", color="#dc3545")
        
        ax3.set_xticks(x)
        ax3.set_xticklabels(proj_names, rotation=45, ha='right')
        ax3.set_ylabel("Amount ($)")
        ax3.set_title("Project Budget vs Actual Spending")
        
        # Add percentage labels
        for i, pct in enumerate(percent):
            ax3.text(i, max(budgeted[i], spent[i]) * 1.05, 
                    f"{pct:.1f}%", 
                    ha='center', va='bottom', 
                    fontsize=10, color="#6c757d")
        
        ax3.legend()
        fig3.tight_layout()
        self.project_expense_chart.draw()

    def update_section3(self, data):
        """Update the Subcategories table"""
        self.subcat_table.setRowCount(len(data['subcategories']))
        
        for i, row in enumerate(data['subcategories']):
            self.subcat_table.setItem(i, 0, QTableWidgetItem(row["Subcategory"] or "N/A"))
            
            funds_item = QTableWidgetItem(f"{row['total_funds'] or 0:,.2f}")
            funds_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.subcat_table.setItem(i, 1, funds_item)
            
            expenses_item = QTableWidgetItem(f"{abs(row['total_expenses'] or 0):,.2f}")
            expenses_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.subcat_table.setItem(i, 2, expenses_item)

#security
class UserManager:
    def __init__(self):
        self.conn = sqlite3.connect('Database/database.db')
        self.conn.row_factory = sqlite3.Row
    
    def __del__(self):
        self.conn.close()
    
    def create_user(self, username, password, email=None, full_name=None, is_admin=False):
        """Create a new user with hashed password"""
        if self.get_user_by_username(username):
            raise ValueError("Username already exists")
        
        password_hash, salt = hash_password(password)
        
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO users (username, password_hash, salt, email, full_name, is_admin)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (username, password_hash, salt, email, full_name, int(is_admin)))
        
        user_id = cursor.lastrowid
        
        # Add to password history
        cursor.execute('''
            INSERT INTO password_history (user_id, password_hash, salt)
            VALUES (?, ?, ?)
        ''', (user_id, password_hash, salt))
        
        # Audit log
        self.log_action(user_id, "USER_CREATED", f"User {username} created")
        
        self.conn.commit()
        return user_id
    
    def authenticate_user(self, username, password):
        """Authenticate a user with username and password"""
        user = self.get_user_by_username(username)
        if not user or not user['is_active']:
            return None
        
        # Check if account is locked
        if user['account_locked_until']:
            locked_until = datetime.datetime.strptime(user['account_locked_until'], '%Y-%m-%d %H:%M:%S')
            if datetime.datetime.now() < locked_until:
                remaining = (locked_until - datetime.datetime.now()).seconds // 60
                raise AccountLockedException(f"Account locked. Try again in {remaining} minutes.")
        
        # Verify password
        password_hash, _ = hash_password(password, user['salt'])
        if password_hash == user['password_hash']:
            # Reset failed attempts on successful login
            self.reset_failed_login_attempts(user['id'])
            
            # Update last login
            self.update_last_login(user['id'])
            
            return user
        else:
            # Increment failed login attempts
            self.increment_failed_login_attempts(user['id'])
            return None
    
    def reset_password(self, username, new_password):
        """Reset a user's password"""
        user = self.get_user_by_username(username)
        if not user:
            raise ValueError("User not found")
        
        # Check if new password is different from current
        new_hash, _ = hash_password(new_password, user['salt'])
        if new_hash == user['password_hash']:
            raise ValueError("New password must be different from current password")
        
        # Check against password history (optional)
        
        # Update password
        new_hash, new_salt = hash_password(new_password)
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE users 
            SET password_hash = ?, salt = ?, 
                password_reset_token = NULL, 
                reset_token_expiry = NULL,
                updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        ''', (new_hash, new_salt, user['id']))
        
        # Add to password history
        cursor.execute('''
            INSERT INTO password_history (user_id, password_hash, salt)
            VALUES (?, ?, ?)
        ''', (user['id'], new_hash, new_salt))
        
        # Audit log
        self.log_action(user['id'], "PASSWORD_RESET", "Password reset")
        
        self.conn.commit()
        return True
    
    def generate_password_reset_token(self, username):
        """Generate a password reset token"""
        user = self.get_user_by_username(username)
        if not user:
            raise ValueError("User not found")
        
        token = binascii.hexlify(os.urandom(32)).decode('utf-8')
        expiry = (datetime.datetime.now() + datetime.timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
        
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE users 
            SET password_reset_token = ?, 
                reset_token_expiry = ?
            WHERE id = ?
        ''', (token, expiry, user['id']))
        
        self.conn.commit()
        return token
    
    def validate_reset_token(self, username, token):
        """Validate a password reset token"""
        user = self.get_user_by_username(username)
        if not user:
            return False
        
        if not user['password_reset_token'] or not user['reset_token_expiry']:
            return False
        
        if user['password_reset_token'] != token:
            return False
        
        expiry = datetime.datetime.strptime(user['reset_token_expiry'], '%Y-%m-%d %H:%M:%S')
        if datetime.datetime.now() > expiry:
            return False
        
        return True
    
    def update_user(self, user_id, email=None, full_name=None, is_active=None):
        """Update user information"""
        updates = []
        params = []
        
        if email is not None:
            updates.append("email = ?")
            params.append(email)
        if full_name is not None:
            updates.append("full_name = ?")
            params.append(full_name)
        if is_active is not None:
            updates.append("is_active = ?")
            params.append(int(is_active))
        
        if not updates:
            return False
        
        params.append(user_id)
        query = f"UPDATE users SET {', '.join(updates)}, updated_at = CURRENT_TIMESTAMP WHERE id = ?"
        
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        
        # Audit log
        self.log_action(user_id, "USER_UPDATED", "User information updated")
        
        self.conn.commit()
        return cursor.rowcount > 0
    
    def get_user_by_username(self, username):
        """Get user by username"""
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        return cursor.fetchone()
    
    def get_user_by_id(self, user_id):
        """Get user by ID"""
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        return cursor.fetchone()
    
    def increment_failed_login_attempts(self, user_id):
        """Increment failed login attempts and lock account if threshold reached"""
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE users 
            SET failed_login_attempts = failed_login_attempts + 1,
                account_locked_until = CASE 
                    WHEN failed_login_attempts + 1 >= 5 THEN datetime('now', '+30 minutes')
                    ELSE NULL
                END
            WHERE id = ?
        ''', (user_id,))
        
        user = self.get_user_by_id(user_id)
        if user['failed_login_attempts'] >= 5:
            self.log_action(user_id, "ACCOUNT_LOCKED", "Account locked due to too many failed attempts")
        
        self.conn.commit()
    
    def reset_failed_login_attempts(self, user_id):
        """Reset failed login attempts"""
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE users 
            SET failed_login_attempts = 0,
                account_locked_until = NULL
            WHERE id = ?
        ''', (user_id,))
        self.conn.commit()
    
    def update_last_login(self, user_id):
        """Update last login timestamp"""
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE users 
            SET last_login = CURRENT_TIMESTAMP
            WHERE id = ?
        ''', (user_id,))
        self.conn.commit()
    
    def log_action(self, user_id, action, description, ip_address=None, user_agent=None):
        """Log an action to the audit log"""
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO audit_log (user_id, action, description, ip_address, user_agent)
            VALUES (?, ?, ?, ?, ?)
        ''', (user_id, action, description, ip_address, user_agent))
        self.conn.commit()

class AccountLockedException(Exception):
    pass            

class UserManagementPage(QWidget):
    def __init__(self, current_user):
        super().__init__()
        self.current_user = current_user
        self.user_manager = UserManager()
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the user interface"""
        self.setWindowTitle("User Management System")
        self.resize(800, 600)
        
        # Main layout
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)
        
        # Title
        title = QLabel("User Management System")
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(title)
        
        # Tab widget for different sections
        tabs = QTabWidget()
        
        # User List Tab
        user_list_tab = QWidget()
        self.setup_user_list_tab(user_list_tab)
        tabs.addTab(user_list_tab, "User List")
        
        # Add User Tab
        add_user_tab = QWidget()
        self.setup_add_user_tab(add_user_tab)
        tabs.addTab(add_user_tab, "Add User")
        
        # Edit Profile Tab
        edit_profile_tab = QWidget()
        self.setup_edit_profile_tab(edit_profile_tab)
        tabs.addTab(edit_profile_tab, "My Profile")
        
        # Password Reset Tab
        reset_password_tab = QWidget()
        self.setup_reset_password_tab(reset_password_tab)
        tabs.addTab(reset_password_tab, "Reset Password")
        
        layout.addWidget(tabs)
        self.setLayout(layout)
    
    def setup_user_list_tab(self, tab):
        """Setup the user list tab"""
        layout = QVBoxLayout()
        
        # Table for displaying users
        self.user_table = QTableWidget()
        self.user_table.setColumnCount(5)
        self.user_table.setHorizontalHeaderLabels(["ID", "Username", "Email", "Full Name", "Status"])
        self.user_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.user_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.user_table.setSelectionMode(QTableWidget.SingleSelection)
        
        # Buttons for user actions
        button_layout = QHBoxLayout()
        self.refresh_btn = QPushButton("Refresh")
        self.refresh_btn.clicked.connect(self.load_users)
        self.edit_btn = QPushButton("Edit User")
        self.edit_btn.clicked.connect(self.edit_selected_user)
        self.toggle_status_btn = QPushButton("Toggle Status")
        self.toggle_status_btn.clicked.connect(self.toggle_user_status)
        self.reset_pw_btn = QPushButton("Reset Password")
        self.reset_pw_btn.clicked.connect(self.reset_password_for_user)
        
        button_layout.addWidget(self.refresh_btn)
        button_layout.addWidget(self.edit_btn)
        button_layout.addWidget(self.toggle_status_btn)
        button_layout.addWidget(self.reset_pw_btn)
        
        layout.addWidget(self.user_table)
        layout.addLayout(button_layout)
        
        tab.setLayout(layout)
        self.load_users()
    
    def setup_add_user_tab(self, tab):
        """Setup the add user tab"""
        layout = QFormLayout()
        layout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        
        # Form fields
        self.new_username = QLineEdit()
        self.new_password = QLineEdit()
        self.new_password.setEchoMode(QLineEdit.Password)
        self.confirm_password = QLineEdit()
        self.confirm_password.setEchoMode(QLineEdit.Password)
        self.new_email = QLineEdit()
        self.new_full_name = QLineEdit()
        self.new_is_admin = QCheckBox("Admin User")
        
        # Add to layout
        layout.addRow("Username:", self.new_username)
        layout.addRow("Password:", self.new_password)
        layout.addRow("Confirm Password:", self.confirm_password)
        layout.addRow("Email:", self.new_email)
        layout.addRow("Full Name:", self.new_full_name)
        layout.addRow(self.new_is_admin)
        
        # Submit button
        self.add_user_btn = QPushButton("Add User")
        self.add_user_btn.clicked.connect(self.add_new_user)
        layout.addRow(self.add_user_btn)
        
        tab.setLayout(layout)
    
    def setup_edit_profile_tab(self, tab):
        """Setup the edit profile tab"""
        layout = QFormLayout()
        
        # Display current user info
        self.current_username = QLabel(self.current_user['username'])
        self.current_email = QLineEdit(self.current_user.get('email', ''))
        self.current_full_name = QLineEdit(self.current_user.get('full_name', ''))
        
        # Make email and full name editable
        layout.addRow("Username:", self.current_username)
        layout.addRow("Email:", self.current_email)
        layout.addRow("Full Name:", self.current_full_name)
        
        # Save button
        self.save_profile_btn = QPushButton("Save Changes")
        self.save_profile_btn.clicked.connect(self.save_profile_changes)
        layout.addRow(self.save_profile_btn)
        
        tab.setLayout(layout)
    
    def setup_reset_password_tab(self, tab):
        """Setup the password reset tab"""
        layout = QFormLayout()
        
        # Current password
        self.current_password = QLineEdit()
        self.current_password.setEchoMode(QLineEdit.Password)
        
        # New password
        self.new_password_reset = QLineEdit()
        self.new_password_reset.setEchoMode(QLineEdit.Password)
        
        # Confirm new password
        self.confirm_new_password = QLineEdit()
        self.confirm_new_password.setEchoMode(QLineEdit.Password)
        
        # Add to layout
        layout.addRow("Current Password:", self.current_password)
        layout.addRow("New Password:", self.new_password_reset)
        layout.addRow("Confirm New Password:", self.confirm_new_password)
        
        # Reset button
        self.reset_password_btn = QPushButton("Change Password")
        self.reset_password_btn.clicked.connect(self.change_password)
        layout.addRow(self.reset_password_btn)
        
        # Forgot password section
        forgot_group = QGroupBox("Forgot Password")
        forgot_layout = QFormLayout()
        
        self.forgot_username = QLineEdit()
        self.request_reset_btn = QPushButton("Request Reset Link")
        self.request_reset_btn.clicked.connect(self.request_password_reset)
        
        forgot_layout.addRow("Username:", self.forgot_username)
        forgot_layout.addRow(self.request_reset_btn)
        forgot_group.setLayout(forgot_layout)
        
        layout.addRow(forgot_group)
        tab.setLayout(layout)
    
    def load_users(self):
        """Load all users into the table"""
        cursor = self.user_manager.conn.cursor()
        cursor.execute('SELECT id, username, email, full_name, is_active FROM users')
        users = cursor.fetchall()
        
        self.user_table.setRowCount(len(users))
        for row_idx, user in enumerate(users):
            self.user_table.setItem(row_idx, 0, QTableWidgetItem(str(user['id'])))
            self.user_table.setItem(row_idx, 1, QTableWidgetItem(user['username']))
            self.user_table.setItem(row_idx, 2, QTableWidgetItem(user['email'] or ''))
            self.user_table.setItem(row_idx, 3, QTableWidgetItem(user['full_name'] or ''))
            
            status = "Active" if user['is_active'] else "Inactive"
            status_item = QTableWidgetItem(status)
            status_item.setForeground(Qt.green if user['is_active'] else Qt.red)
            self.user_table.setItem(row_idx, 4, status_item)
    
    def add_new_user(self):
        """Add a new user to the system"""
        username = self.new_username.text().strip()
        password = self.new_password.text()
        confirm_password = self.confirm_password.text()
        email = self.new_email.text().strip()
        full_name = self.new_full_name.text().strip()
        is_admin = self.new_is_admin.isChecked()
        
        # Validate inputs
        if not username:
            QMessageBox.warning(self, "Error", "Username is required")
            return
        
        if not password:
            QMessageBox.warning(self, "Error", "Password is required")
            return
        
        if password != confirm_password:
            QMessageBox.warning(self, "Error", "Passwords do not match")
            return
        
        try:
            # Create the user
            self.user_manager.create_user(
                username=username,
                password=password,
                email=email if email else None,
                full_name=full_name if full_name else None,
                is_admin=is_admin
            )
            
            # Clear the form
            self.new_username.clear()
            self.new_password.clear()
            self.confirm_password.clear()
            self.new_email.clear()
            self.new_full_name.clear()
            self.new_is_admin.setChecked(False)
            
            # Refresh user list
            self.load_users()
            
            QMessageBox.information(self, "Success", "User created successfully")
        except ValueError as e:
            QMessageBox.warning(self, "Error", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to create user: {str(e)}")
    
    def edit_selected_user(self):
        """Edit the selected user"""
        selected = self.user_table.selectedItems()
        if not selected:
            QMessageBox.warning(self, "Error", "Please select a user first")
            return
        
        user_id = int(selected[0].text())
        user = self.user_manager.get_user_by_id(user_id)
        
        if not user:
            QMessageBox.warning(self, "Error", "User not found")
            return
        
        # Create edit dialog
        dialog = QDialog(self)
        dialog.setWindowTitle("Edit User")
        layout = QFormLayout()
        
        # Form fields
        username = QLabel(user['username'])
        email = QLineEdit(user.get('email', ''))
        full_name = QLineEdit(user.get('full_name', ''))
        is_active = QCheckBox("Active")
        is_active.setChecked(bool(user['is_active']))
        is_admin = QCheckBox("Admin")
        is_admin.setChecked(bool(user['is_admin']))
        
        # Add to layout
        layout.addRow("Username:", username)
        layout.addRow("Email:", email)
        layout.addRow("Full Name:", full_name)
        layout.addRow(is_active)
        layout.addRow(is_admin)
        
        # Buttons
        btn_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        btn_box.accepted.connect(dialog.accept)
        btn_box.rejected.connect(dialog.reject)
        layout.addRow(btn_box)
        
        dialog.setLayout(layout)
        
        if dialog.exec_() == QDialog.Accepted:
            try:
                self.user_manager.update_user(
                    user_id=user_id,
                    email=email.text().strip() or None,
                    full_name=full_name.text().strip() or None,
                    is_active=is_active.isChecked()
                )
                
                # For admin status, we might need a separate method if it requires special permissions
                if self.current_user['is_admin']:
                    cursor = self.user_manager.conn.cursor()
                    cursor.execute('''
                        UPDATE users 
                        SET is_admin = ?,
                            updated_at = CURRENT_TIMESTAMP
                        WHERE id = ?
                    ''', (int(is_admin.isChecked()), user_id))
                    self.user_manager.conn.commit()
                
                self.load_users()
                QMessageBox.information(self, "Success", "User updated successfully")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to update user: {str(e)}")
    
    def toggle_user_status(self):
        """Toggle the active status of the selected user"""
        selected = self.user_table.selectedItems()
        if not selected:
            QMessageBox.warning(self, "Error", "Please select a user first")
            return
        
        user_id = int(selected[0].text())
        user = self.user_manager.get_user_by_id(user_id)
        
        if not user:
            QMessageBox.warning(self, "Error", "User not found")
            return
        
        new_status = not user['is_active']
        
        try:
            self.user_manager.update_user(
                user_id=user_id,
                is_active=new_status
            )
            
            self.load_users()
            status = "activated" if new_status else "deactivated"
            QMessageBox.information(self, "Success", f"User {status} successfully")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to toggle user status: {str(e)}")
    
    def reset_password_for_user(self):
        """Reset password for the selected user"""
        selected = self.user_table.selectedItems()
        if not selected:
            QMessageBox.warning(self, "Error", "Please select a user first")
            return
        
        user_id = int(selected[0].text())
        user = self.user_manager.get_user_by_id(user_id)
        
        if not user:
            QMessageBox.warning(self, "Error", "User not found")
            return
        
        # Create password reset dialog
        dialog = QDialog(self)
        dialog.setWindowTitle("Reset Password")
        layout = QFormLayout()
        
        # Form fields
        new_password = QLineEdit()
        new_password.setEchoMode(QLineEdit.Password)
        confirm_password = QLineEdit()
        confirm_password.setEchoMode(QLineEdit.Password)
        
        # Add to layout
        layout.addRow("New Password:", new_password)
        layout.addRow("Confirm Password:", confirm_password)
        
        # Buttons
        btn_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        btn_box.accepted.connect(dialog.accept)
        btn_box.rejected.connect(dialog.reject)
        layout.addRow(btn_box)
        
        dialog.setLayout(layout)
        
        if dialog.exec_() == QDialog.Accepted:
            password = new_password.text()
            confirm = confirm_password.text()
            
            if not password:
                QMessageBox.warning(self, "Error", "Password cannot be empty")
                return
            
            if password != confirm:
                QMessageBox.warning(self, "Error", "Passwords do not match")
                return
            
            try:
                self.user_manager.reset_password(user['username'], password)
                QMessageBox.information(self, "Success", "Password reset successfully")
            except ValueError as e:
                QMessageBox.warning(self, "Error", str(e))
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to reset password: {str(e)}")
    
    def save_profile_changes(self):
        """Save changes to the current user's profile"""
        email = self.current_email.text().strip()
        full_name = self.current_full_name.text().strip()
        
        try:
            self.user_manager.update_user(
                user_id=self.current_user['id'],
                email=email if email else None,
                full_name=full_name if full_name else None
            )
            
            # Update current user data
            self.current_user = self.user_manager.get_user_by_id(self.current_user['id'])
            
            QMessageBox.information(self, "Success", "Profile updated successfully")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to update profile: {str(e)}")
    
    def change_password(self):
        """Change the current user's password"""
        current_password = self.current_password.text()
        new_password = self.new_password_reset.text()
        confirm_password = self.confirm_new_password.text()
        
        if not current_password:
            QMessageBox.warning(self, "Error", "Current password is required")
            return
        
        if not new_password:
            QMessageBox.warning(self, "Error", "New password is required")
            return
        
        if new_password != confirm_password:
            QMessageBox.warning(self, "Error", "New passwords do not match")
            return
        
        # Verify current password
        user = self.user_manager.authenticate_user(self.current_user['username'], current_password)
        if not user:
            QMessageBox.warning(self, "Error", "Current password is incorrect")
            return
        
        try:
            self.user_manager.reset_password(self.current_user['username'], new_password)
            
            # Clear the form
            self.current_password.clear()
            self.new_password_reset.clear()
            self.confirm_new_password.clear()
            
            QMessageBox.information(self, "Success", "Password changed successfully")
        except ValueError as e:
            QMessageBox.warning(self, "Error", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to change password: {str(e)}")
    
    def request_password_reset(self):
        """Request a password reset for a user"""
        username = self.forgot_username.text().strip()
        
        if not username:
            QMessageBox.warning(self, "Error", "Username is required")
            return
        
        try:
            token = self.user_manager.generate_password_reset_token(username)
            
            # In a real application, you would send this token via email
            # For this example, we'll just show it in a message box
            QMessageBox.information(
                self, 
                "Password Reset", 
                f"Password reset token generated (would be sent by email in a real app):\n\n{token}\n\n"
                "This token will expire in 1 hour."
            )
        except ValueError as e:
            QMessageBox.warning(self, "Error", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to generate reset token: {str(e)}")

class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.user_manager = UserManager()
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the login dialog"""
        self.setWindowTitle("Login")
        self.setFixedSize(300, 200)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # Form fields
        form_layout = QFormLayout()
        
        self.username = QLineEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        
        form_layout.addRow("Username:", self.username)
        form_layout.addRow("Password:", self.password)
        
        # Buttons
        btn_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        btn_box.accepted.connect(self.authenticate)
        btn_box.rejected.connect(self.reject)
        
        # Forgot password link
        forgot_link = QLabel("<a href='#'>Forgot password?</a>")
        forgot_link.setOpenExternalLinks(False)
        forgot_link.linkActivated.connect(self.show_forgot_password)
        
        layout.addLayout(form_layout)
        layout.addWidget(btn_box)
        layout.addWidget(forgot_link, alignment=Qt.AlignRight)
        
        self.setLayout(layout)
    
    def authenticate(self):
        """Authenticate the user"""
        username = self.username.text().strip()
        password = self.password.text()
        
        if not username or not password:
            QMessageBox.warning(self, "Error", "Username and password are required")
            return
        
        try:
            user = self.user_manager.authenticate_user(username, password)
            if user:
                self.user = user
                self.accept()
            else:
                QMessageBox.warning(self, "Error", "Invalid username or password")
        except AccountLockedException as e:
            QMessageBox.warning(self, "Account Locked", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Login failed: {str(e)}")
    
    def show_forgot_password(self):
        """Show the forgot password dialog"""
        dialog = QDialog(self)
        dialog.setWindowTitle("Reset Password")
        layout = QVBoxLayout()
        
        instruction = QLabel("Enter your username to receive a password reset link:")
        username = QLineEdit()
        submit_btn = QPushButton("Submit")
        
        def submit():
            username_text = username.text().strip()
            if not username_text:
                QMessageBox.warning(dialog, "Error", "Username is required")
                return
            
            try:
                token = self.user_manager.generate_password_reset_token(username_text)
                QMessageBox.information(
                    dialog,
                    "Reset Link Sent",
                    f"Password reset token generated (would be sent by email in a real app):\n\n{token}"
                )
                dialog.accept()
            except ValueError as e:
                QMessageBox.warning(dialog, "Error", str(e))
            except Exception as e:
                QMessageBox.critical(dialog, "Error", f"Failed to generate reset token: {str(e)}")
        
        submit_btn.clicked.connect(submit)
        
        layout.addWidget(instruction)
        layout.addWidget(username)
        layout.addWidget(submit_btn)
        dialog.setLayout(layout)
        dialog.exec_()
# Styles and General Design
class Links(QPushButton):
    def __init__(self, text="", icon_path=None, parent=None):
        super().__init__(text, parent)
        self.icon_path = icon_path

        self.setFlat(True)
        self.setStyleSheet("""
            QPushButton {
                color: white;
                background-color: transparent;
                padding: 20px 12px;
                text-align: left;
                font-size: 16px;
                font-family: Lato-Regular;
            }
            QPushButton:hover{
                color: #006666;
            }                             
        """)
        self.setCheckable(True)
        self.setAutoExclusive(True)  # Only one active at a time

        self.toggled.connect(self.update_active_style)

        # Set icon if provided, else reserve space
        if self.icon_path:
            self.setIcon(QIcon(self.icon_path))
            self.setIconSize(QSize(18, 18))
        else:
            self.setIconSize(QSize(18, 18))  # reserve space for alignment

    def update_active_style(self, checked):
        if checked:
            self.setStyleSheet("""
                QPushButton {
                    color: #1B263B;
                    background-color: white;
                    border: none;
                    outline: none;
                    padding: 20px 12px;
                    text-align: left;
                    font-size: 16px;
                    font-family: Lato-Regular;
                }
                QPushButton:hover{
                    color: #006666;
                }
            """)
        else:
            self.setStyleSheet("""
                QPushButton {
                    color: white;
                    background-color: transparent;
                    border: none;
                    outline: none;
                    padding: 20px 12px;
                    text-align: left;
                    font-size: 16px;
                    font-family: Lato-Regular;
                }
                QPushButton:hover{
                    color: #006666;
                }
            """)

class Title(QLabel):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: #1B263B;
            font-family: Lato-Regular;
        """)
        self.setAlignment(Qt.AlignLeft)

class TableButton(QPushButton):
    ICONS = {
        "Edit": "Icons/edit.svg",
        "Delete": "Icons/delete.svg"
    }
    COLORS = {
        "Edit": "#28a745",    # Bootstrap success
        "Delete": "#dc3545"   # Bootstrap danger
    }

    def __init__(self, label, parent=None):
        super().__init__(parent)
        self.setText("")
        icon_path = self.ICONS.get(label, None)
        if icon_path:
            self.setIcon(QIcon(icon_path))
        self.setIconSize(QSize(15, 15))
        color = self.COLORS.get(label, "#6c757d")  # Default to secondary
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                border: none;
                border-radius: 4px;
                padding: 4px;
                min-width: 24px;
                min-height: 24px;
            }}
            QPushButton:hover {{
                background-color: #222222;
                opacity: 0.85;
            }}
        """)
        self.setToolTip(label)
        self.setCursor(Qt.PointingHandCursor)

def FormStyles():
    form_css = """
       *{
        background-color: white;
        }
        QLineEdit{
        padding: 375rem 75rem;
        border: 1px solid #ced4da;
        border-radius: 3px;
        height: 30px;
        font: 10pt;
        } 
        QSpinBox{
        padding: 375rem 75rem;
        border: 1px solid #ced4da;
        border-radius: 3px;
        height: 30px;
        font: 10pt;
        } 
        QDateEdit {
        border: 1px solid #ced4da; /* Light gray border */
        border-radius: 8px; /* Rounded corners */
        background-color: #ffffff; /* White background */
        padding: 5px 10px; /* Padding inside the input */
        color: #495057; /* Text color */
        font-size: 14px; /* Font size */
        height: 30px; /* Input height */
        }
    
        QDateEdit:hover {
            border: 1px solid #80bdff; /* Blue border on hover */
            background-color: #f8f9fa; /* Light gray background */
        }
    
        QDateEdit:focus {
            border: 1px solid #007bff; /* Bootstrap blue for focus */
            outline: none; /* Remove outline */
        }
    
        QDateEdit::drop-down {
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 20px; /* Dropdown width */
            border-left: 1px solid #ced4da; /* Divider for dropdown */
        }
    
        QDateEdit::down-arrow {
            image: url('icons/calendar.png'); /* Replace with your icon path */
            width: 14px;
            height: 14px;
        }
    
        QDateEdit::down-arrow:hover {
            image: url('icons/calendar_hover_16px.png'); /* Hover icon */
        }
    
        QDateEdit::down-arrow:pressed {
            image: url('icons/calendar_pressed_16px.png'); /* Pressed icon */
        }
    
        QCalendarWidget {
            border: 1px solid #dee2e6; /* Border for calendar popup */
            border-radius: 8px;
            background-color: #ffffff; /* White background */
            color: #212529; /* Text color */
            font-size: 14px;
        }
    
        QCalendarWidget QToolButton {
            color: #495057; /* Month and Year text color */
            background-color: #f8f9fa; /* Light gray button background */
            border: none; /* No border */
            border-radius: 5px;
            padding: 5px;
            font-weight: bold;
        }
    
        QCalendarWidget QToolButton:hover {
            background-color: #e2e6ea; /* Hover background color */
        }
    
        QCalendarWidget QToolButton:pressed {
            background-color: #d4d8dc; /* Pressed background color */
        }
    
        QCalendarWidget QTableView {
            border: none;
            color: #495057; /* Day numbers color */
            gridline-color: #dee2e6; /* Gridline color */
        }
    
        QCalendarWidget QTableView:selected {
            background-color: #007bff; /* Selected day background */
            color: #ffffff; /* Selected day text */
        }
        QComboBox {
        border: 1px solid #ced4da;
        border-radius: 4px;
        padding: 5px;
        background-color: #f8f9fa;
        font-size: 14px;
        color: #495057;
        }

        QComboBox:hover {
            border-color: #86b7fe;
        }

        QComboBox:focus {
            border-color: #0d6efd;
        }

        QComboBox QAbstractItemView {
            border: 1px solid #ced4da;
            background-color: #fff;
            selection-background-color: #0d6efd;
            selection-color: white;
            padding: 5px;
            font-size: 14px;
        }

        QComboBox::drop-down {
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 25px;
            border-left: 1px solid #ced4da;
            background-color: #e9ecef;
        }

        QComboBox::down-arrow {
            image: url('icons/down-arrow.png');
            width: 16px;
            height: 16px;
        }
        QFrame{
        border-radius: 5px;
        }
        QPushButton {
        border-radius: 5px;
        font-family: 'Poppins', sans-serif;
        font-weight: bold;
        background-color: #007bff;
        color: white; 
        border: 1px solid #007bff;
        padding: 6px 12px;
        font-size: 14px;
        text-align: center;
        transition: background-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
         }

        /* Hover State */
        QPushButton:hover {
            background-color: #0056b3; /* Darker blue like Bootstrap */
            border: 1px solid #0056b3;
        }

        /* Pressed (Active) State */
        QPushButton:pressed {
            background-color: #004080;
            border: 1px solid #004080;
        }

        /* Focus (When Clicked or Tabbed) */
        QPushButton:focus {
            outline: none;
            box-shadow: 0 0 5px rgba(0, 123, 255, 0.5); /* Bootstrap-like glow effect */
        }
         """
    return form_css

def DialogStyles():
    dialog = """
    QDialog {
        background-color: #F9F9F9;
        border-radius: 12px;
        font-family: 'Segoe UI', 'Lato', sans-serif;
        font-size: 14px;
        color: #2E2E2E;
    }

    QLabel {
        font-weight: 500;
        margin-bottom: 4px;
    }

    QLineEdit, QComboBox, QDateEdit, QSpinBox {
        background-color: #FFFFFF;
        border: 1px solid #CCCCCC;
        border-radius: 6px;
        padding: 6px 10px;
        font-size: 14px;
        color: #2E2E2E;
    }

    QLineEdit:focus, QComboBox:focus, QDateEdit:focus, QSpinBox:focus {
        border: 1.5px solid #007BFF;
        background-color: #FFFFFF;
    }

    QPushButton {
        background-color: #007BFF;
        color: white;
        padding: 8px 16px;
        border: none;
        border-radius: 6px;
        font-weight: 600;
    }

    QPushButton:hover {
        background-color: #0056b3;
    }

    QPushButton:disabled {
        background-color: #cccccc;
        color: #666666;
    }

    QCheckBox {
        spacing: 6px;
    }

    QCheckBox::indicator {
        width: 16px;
        height: 16px;
    }

    QCheckBox::indicator:checked {
        background-color: #007BFF;
        border: 1px solid #007BFF;
    }

    QGroupBox {
        border: 1px solid #E0E0E0;
        border-radius: 8px;
        margin-top: 10px;
        padding: 10px;
    }

    QGroupBox::title {
        subcontrol-origin: margin;
        left: 10px;
        padding: 0 3px 0 3px;
        font-weight: bold;
    }
"""
    return dialog

def TableStyles():
    table_stylesheet = """
    QTableWidget {
        border: 1px solid #dee2e6; /* Bootstrap-like border */
        border-radius: 5px; /* Rounded corners */
        gridline-color: #dee2e6; /* Gridline color */
        background-color: #ffffff; /* Background color for the table */
    }

    QTableWidget::item {
        padding: 6px; /* Padding for table cells */
        border: none; /* Remove individual cell borders */
    }

    QHeaderView::section {
        background-color: #f8f9fa; /* Bootstrap table header background */
        color: #212529; /* Text color for the header */
        padding: 8px; /* Padding for header cells */
        border: 1px solid #dee2e6; /* Header border color */
        font-weight: bold; /* Make header text bold */
        text-align: center; /* Center-align header text */
    }

    QTableWidget::item:alternate {
        background-color: #f8f9fa; /* Alternate row background color */
    }

    QTableWidget::item:hover {
        background-color: #e9ecef; /* Hover color for rows */
    }

    QTableWidget::item:selected {
        background-color: #007bff; /* Selection background color */
        color: #ffffff; /* Selection text color */
    }

    /* Target Scrollbars Specifically in QTableWidget */
    QTableWidget QScrollBar:vertical {
        background: #f8f9fa; /* Scrollbar background */
        width: 12px; /* Width of the vertical scrollbar */
        border: none; /* Remove border */
    }

    QTableWidget QScrollBar::handle:vertical {
        background: #3f48cc; /* Handle color */
        border-radius: 6px; /* Rounded handle */
        min-height: 20px; /* Minimum handle height */
    }

    QTableWidget QScrollBar::handle:vertical:hover {
        background: #0056b3; /* Hover effect */
    }

    QTableWidget QScrollBar:horizontal {
        background: #f8f9fa; /* Scrollbar background */
        height: 12px; /* Height of the horizontal scrollbar */
        border: none; /* Remove border */
    }

    QTableWidget QScrollBar::handle:horizontal {
        background: #3f48cc; /* Handle color */
        border-radius: 6px; /* Rounded handle */
        min-width: 20px; /* Minimum handle width */
    }

    QTableWidget QScrollBar::handle:horizontal:hover {
        background: #0056b3; /* Hover effect */
    }

    /* Optional: Remove Arrows */
    QTableWidget QScrollBar::add-line:vertical, QTableWidget QScrollBar::sub-line:vertical {
        height: 0px; /* Remove up/down arrows */
    }

    QTableWidget QScrollBar::add-line:horizontal, QTableWidget QScrollBar::sub-line:horizontal {
        width: 0px; /* Remove left/right arrows */
    }
    QTableWidget::item {
        min-height: 45px;
    }
    """
    return table_stylesheet

def button(text, button_type="primary", size="md", icon_path=None, icon_toolTip = None, icon_size=24 ):
    """
    Create a Bootstrap-inspired button with optional icons.

    :param text: The text to display on the button.
    :param button_type: The type of the button (primary, success, danger, etc.).
    :param size: The size of the button (sm, md, lg).
    :param icon_path: The file path to the icon (optional).
    :param icon_size: The size of the icon (default: 24px).
    :return: QPushButton styled as a Bootstrap button.
    """
    button = QPushButton(text)
    button.setToolTip(icon_toolTip)
    # Button Styles Dictionary
    styles = {
        "primary": "background-color: #007bff; color: white; border: 1px solid #007bff;",
        "secondary": "background-color: #6c757d; color: white; border: 1px solid #6c757d;",
        "success": "background-color: #28a745; color: white; border: 1px solid #28a745;",
        "danger": "background-color: #dc3545; color: white; border: 1px solid #dc3545;",
        "warning": "background-color: #ffc107; color: black; border: 1px solid #ffc107;",
        "info": "background-color: #17a2b8; color: white; border: 1px solid #17a2b8;",
        "light": "background-color: #f8f9fa; color: black; border: 1px solid #f8f9fa;",
        "dark": "background-color: #343a40; color: white; border: 1px solid #343a40;",
    }

    # Button Sizes Dictionary
    sizes = {
        "sm": "padding: 4px 10px; font-size: 12px;",
        "md": "padding: 6px 12px; font-size: 14px;",
        "lg": "padding: 10px 16px; font-size: 18px;",
    }

    # Apply Styles
    button.setStyleSheet(f"""
        QPushButton {{
            border-radius: 5px;
            font-family: 'Poppins', sans-serif;
            font-weight: bold;
            {styles.get(button_type, styles['primary'])} /* Default to primary if type is invalid */
            {sizes.get(size, sizes['md'])} /* Default to medium if size is invalid */
        }}
        QPushButton:hover {{
            opacity: 0.9; /* Slight fade effect on hover */
        }}
    """)

    # Optional: Set Icon
    if icon_path:
        button.setIcon(QIcon(icon_path))
        button.setIconSize(QSize(icon_size, icon_size))

    # Optional: Set Cursor to Hand Pointer
    button.setCursor(Qt.PointingHandCursor)

    return button

def outline_button(text, button_type="primary", size="md", icon_path=None, icon_toolTip=None, icon_size=24):
    """
    Create a Bootstrap-inspired outline button with optional icons.

    :param text: The text to display on the button.
    :param button_type: The type of the button (primary, success, danger, etc.).
    :param size: The size of the button (sm, md, lg).
    :param icon_path: The file path to the icon (optional).
    :param icon_toolTip: Tooltip for the button (optional).
    :param icon_size: The size of the icon (default: 24px).
    :return: QPushButton styled as a Bootstrap outline button.
    """
    button = QPushButton(text)
    button.setToolTip(icon_toolTip)
    # Outline Button Styles Dictionary
    styles = {
        "primary": "background-color: transparent; color: #007bff; border: 1.5px solid #007bff;",
        "secondary": "background-color: transparent; color: #6c757d; border: 1.5px solid #6c757d;",
        "success": "background-color: transparent; color: #28a745; border: 1.5px solid #28a745;",
        "danger": "background-color: transparent; color: #dc3545; border: 1.5px solid #dc3545;",
        "warning": "background-color: transparent; color: #ffc107; border: 1.5px solid #ffc107;",
        "info": "background-color: transparent; color: #17a2b8; border: 1.5px solid #17a2b8;",
        "light": "background-color: transparent; color: #f8f9fa; border: 1.5px solid #f8f9fa;",
        "dark": "background-color: transparent; color: #343a40; border: 1.5px solid #343a40;",
    }

    # Button Sizes Dictionary
    sizes = {
        "sm": "padding: 4px 10px; font-size: 12px;",
        "md": "padding: 6px 12px; font-size: 14px;",
        "lg": "padding: 10px 16px; font-size: 18px;",
    }

    # Apply Styles
    button.setStyleSheet(f"""
        QPushButton {{
            border-radius: 5px;
            font-family: 'Poppins', sans-serif;
            font-weight: bold;
            {styles.get(button_type, styles['primary'])}
            {sizes.get(size, sizes['md'])}
        }}
        QPushButton:hover {{
            background-color: {styles.get(button_type, styles['primary']).split(';')[1].split(':')[1].strip()};
            opacity: 0.1;
            color: White;
        }}
    """)

    # Optional: Set Icon
    if icon_path:
        button.setIcon(QIcon(icon_path))
        button.setIconSize(QSize(icon_size, icon_size))

    # Optional: Set Cursor to Hand Pointer
    button.setCursor(Qt.PointingHandCursor)

    return button

def dropdown_button(text, items, button_type="primary", size="md", icon_path=None, icon_toolTip=None, icon_size=24):
    """
    Create a Bootstrap-inspired dropdown button using QComboBox, styled like button/outline_button.
    The first item is an unselectable placeholder (e.g., "Funds"), and the rest are selectable options.

    :param text: The label to show as the first item (placeholder, unselectable).
    :param items: List of (display_text, value) tuples or just strings.
    :param button_type: Bootstrap color (primary, success, etc.).
    :param size: sm, md, lg.
    :param icon_path: Optional icon.
    :param icon_toolTip: Tooltip.
    :param icon_size: Icon size.
    :return: QComboBox styled as a dropdown button.
    """
    combo = QComboBox()
    combo.setToolTip(icon_toolTip)
    # Button Styles Dictionary
    styles = {
        "primary": "background-color: #007bff; color: white; border: 1.5px solid #007bff;",
        "secondary": "background-color: #6c757d; color: white; border: 1.5px solid #6c757d;",
        "success": "background-color: #28a745; color: white; border: 1.5px solid #28a745;",
        "danger": "background-color: #dc3545; color: white; border: 1.5px solid #dc3545;",
        "warning": "background-color: #ffc107; color: black; border: 1.5px solid #ffc107;",
        "info": "background-color: #17a2b8; color: white; border: 1.5px solid #17a2b8;",
        "light": "background-color: #f8f9fa; color: black; border: 1.5px solid #f8f9fa;",
        "dark": "background-color: #343a40; color: white; border: 1.5px solid #343a40;",
    }
    sizes = {
        "sm": "padding: 4px 10px; font-size: 12px; min-height: 28px;",
        "md": "padding: 6px 12px; font-size: 14px; min-height: 34px;",
        "lg": "padding: 10px 16px; font-size: 18px; min-height: 42px;",
    }
    combo.setStyleSheet(f"""
        QComboBox {{
            border-radius: 5px;
            font-family: 'Poppins', sans-serif;
            font-weight: bold;
            {styles.get(button_type, styles['primary'])}
            {sizes.get(size, sizes['md'])}
        }}
        QComboBox:hover {{
            opacity: 0.9;
        }}
        QComboBox QAbstractItemView {{
            border: 1.5px solid #dee2e6;
            background-color: #fff;
            selection-background-color: #007bff;
            selection-color: white;
            font-size: 14px;
        }}
        QComboBox::drop-down {{
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 28px;
            border-left: 1px solid #ced4da;
            {styles.get(button_type, styles['primary'])}
        }}
        QComboBox::down-arrow {{
            image: url('icons/down-arrow.svg');
            width: 20px;
            height: 20px;
        }}
    """)
    # Add the unselectable placeholder as the first item
    combo.addItem(text, None)
    model = combo.model()
    index = model.index(0, 0)
    # Make the first item unselectable and disabled
    model.setData(index, 0, Qt.UserRole - 1)  # Not enabled
    # Optionally set icon for the placeholder
    if icon_path:
        combo.setItemIcon(0, QIcon(icon_path))
        combo.setIconSize(QSize(icon_size, icon_size))
    # Add items
    for item in items:
        if isinstance(item, tuple):
            combo.addItem(item[0], item[1])
        else:
            combo.addItem(str(item))
    combo.setCursor(Qt.PointingHandCursor)

    # Always reset to placeholder after selection
    def handle_index_changed(idx):
        if idx > 0:
            # Emit a custom signal or call a callback here if needed
            combo.setCurrentIndex(0)
    combo.currentIndexChanged.connect(handle_index_changed)

    return combo

class TableTitle(QLabel):
    def __init__(self, Text):
        super().__init__()
        self.setText(Text)
        self.setFont(QFont("Lato-Regular", 14))
        self.setStyleSheet("color:#1B263B;")

def main():
    app = QApplication([])
    
    # Show login dialog
    login = LoginDialog()
    if login.exec_() == QDialog.Accepted:
        # If login successful, show user management system
        user = login.user
        window = UserManagementPage(user)
        window.show()
        app.exec_()

if __name__ == "__main__":
    # Create a default admin user if none exists
    user_manager = UserManager()
    if not user_manager.get_user_by_username("admin"):
        user_manager.create_user("admin", "admin123", is_admin=True)
    
    main()
        


       