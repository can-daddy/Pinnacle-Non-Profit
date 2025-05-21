from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sqlite3


# Create a connection to the SQLite database
def get_db_connection():
    conn = sqlite3.connect("Database/database.db")
    conn.row_factory = sqlite3.Row  # Optional: for dict-like row access
    return conn

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
        DashboardWidget = QWidget()
        DashboardLayout = QVBoxLayout()
        DashboardLabel = QLabel("Dashboard")
        DashboardLayout.addWidget(DashboardLabel, alignment=Qt.AlignCenter)
        DashboardWidget.setLayout(DashboardLayout)
        DonorsWidget = DonorsPage()
        FundsWidget = FundPage()
        BudgetsWidget = QWidget()
        TransactionsWidget = TransactionsPage()
        CategoriesWidget = Categories_SubCategories()
        ProgramsWidget = Program_Admnistration()
        ProjectsWidget = Projects_Activities()
        ReportsWidget = QWidget()
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
        self.AddButton = button("Add","primary","md",icon_path="Icons/add.svg",icon_toolTip="Add New Donor")
        self.AddButton.clicked.connect(self.DonorForm)
        self.ExportButton = button("Export","success","md",icon_path="Icons/print.svg",icon_toolTip="Export as Pdf")
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
        self.cancelButton.setIcon(QIcon("Icons/cancel.svg"))  # Put your icon in Icons/cancel.svg
        self.cancelButton.setIconSize(QSize(16, 16))  # Increased size
        self.cancelButton.setToolTip("Cancel")
        self.cancelButton.setVisible(False)
        Filter = QLabel("Filter:")
        Filter.setStyleSheet("""
            color: #1B263B;
            font-size: 12px;
            font-family: Lato-light;
            """
            )
        type_filter = QComboBox()
        type_filter.addItems(["All", "Active", "Inactive"])
        type_filter.setStyleSheet(FormStyles())
        category_filter = QComboBox()
        category_filter.setStyleSheet(FormStyles())
        category_filter.addItems(["All", "Individual", "Organization"])
        TableHeaderLayout.addWidget(DonorTableTitle)
        TableHeaderLayout.addStretch()
        TableHeaderLayout.addWidget(self.SearchBar, alignment=Qt.AlignRight)
        TableHeaderLayout.addWidget(self.cancelButton)
        TableHeaderLayout.addWidget(Filter)
        TableHeaderLayout.addWidget(QLabel("Type:"))
        TableHeaderLayout.addWidget(type_filter)
        TableHeaderLayout.addWidget(QLabel("Category:"))
        TableHeaderLayout.addWidget(category_filter)
        TableHeader.setLayout(TableHeaderLayout)
        Layout.addWidget(TableHeader, alignment=Qt.AlignTop)
        # Table of Donors
        TableofDonors = QTableWidget()
        TableofDonors.setStyleSheet(TableStyles())
        TableofDonors.setColumnCount(7)
        TableofDonors.setHorizontalHeaderLabels(["Name", "Address","Contact","Type", "Category", "Date Joined", "Actions"])
        TableofDonors.horizontalHeader().setStretchLastSection(True)
        TableofDonors.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        EditBtn = TableButton("Edit")
        DeleteBtn = TableButton("Delete")
        Actionbuttons = QWidget()
        ActionbtnsLyt = QHBoxLayout()
        ActionbtnsLyt.addWidget(EditBtn)
        ActionbtnsLyt.addWidget(DeleteBtn)
        Actionbuttons.setLayout(ActionbtnsLyt)
        TableofDonors.setCellWidget(0, 4, Actionbuttons)
        TableHeaderLayout.addWidget(TableofDonors)
        Layout.addWidget(TableofDonors)
    
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

        # Firstname
        firstname_input = QLineEdit()
        firstname_input.setPlaceholderText("Enter Firstname")
        form.addRow("Firstname:", firstname_input)

        # Lastname
        lastname_input = QLineEdit()
        lastname_input.setPlaceholderText("Enter Lastname")
        form.addRow("Lastname:", lastname_input)

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

        # Connect buttons
        cancel_btn.clicked.connect(dialog.reject)
        save_btn.clicked.connect(lambda: self.insert_donor(
            firstname_input.text(),
            lastname_input.text(),
            address_input.text(),
            contact_input.text(),
            type_combo.currentText(),
            category_combo.currentText(),
            date_joined.date().toString("yyyy-MM-dd")
        ))

        dialog.setLayout(layout)
        dialog.exec_()
    
    def insert_donor(self, firstname, lastname, address, contact, donor_type, category, date_joined):
        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO Donors (firstname, lastname, address, contact, Donor_Type,Donor_Category, Date_Joined)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (firstname, lastname, address, contact, donor_type, category, date_joined))
            conn.commit()
        finally:
            conn.close()
        QMessageBox.information(self, "Success", "Donor added successfully!")
    
 
    def showEvent(self, event):
        super().showEvent(event)
        self.refresh_donor_table()

    def insert_donor(self, firstname, lastname, address, contact, donor_type, category, date_joined):
        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO Donors (firstname, lastname, address, contact, Donor_Type,Donor_Category, Date_Joined)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (firstname, lastname, address, contact, donor_type, category, date_joined))
            conn.commit()
        finally:
            conn.close()
        QMessageBox.information(self, "Success", "Donor added successfully!")
        self.refresh_donor_table()
    
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

        firstname_input = QLineEdit(donor["firstname"])
        form.addRow("Firstname:", firstname_input)
        lastname_input = QLineEdit(donor["lastname"])
        form.addRow("Lastname:", lastname_input)
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
                    UPDATE Donors SET firstname=?, lastname=?, address=?, contact=?, Donor_Type=?, Donor_Category=?, Date_Joined=?
                    WHERE DonorID=?
                """, (
                    firstname_input.text(),
                    lastname_input.text(),
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
        type_filter = self.findChild(QComboBox, None).currentText() if self.findChildren(QComboBox) else "All"
        # The first QComboBox is Type, the second is Category
        combo_boxes = self.findChildren(QComboBox)
        if len(combo_boxes) >= 2:
            type_filter = combo_boxes[0].currentText()
            category_filter = combo_boxes[1].currentText()
        else:
            type_filter = "All"
            category_filter = "All"

        # Build SQL query dynamically
        query = "SELECT DonorID, firstname, lastname, address, contact, Donor_Type, Donor_Category, Date_Joined FROM Donors WHERE 1=1"
        params = []

        if type_filter != "All":
            query += " AND Donor_Type = ?"
            params.append(type_filter)
        if category_filter != "All":
            query += " AND Donor_Category = ?"
            params.append(category_filter)
        if search_text:
            query += " AND (LOWER(firstname) LIKE ? OR LOWER(lastname) LIKE ? OR LOWER(address) LIKE ? OR LOWER(contact) LIKE ?)"
            params.extend([f"%{search_text}%"] * 4)

        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute(query, params)
            donors = cur.fetchall()
        finally:
            conn.close()

        table = self.findChild(QTableWidget)
        if not table:
            return

        table.setRowCount(0)
        for row_idx, donor in enumerate(donors):
            table.insertRow(row_idx)
            table.setRowHeight(row_idx, 45)
            name = f"{donor['firstname']} {donor['lastname']}"
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

        # Connect signals for live update if not already connected
        self.SearchBar.textChanged.disconnect()
        self.SearchBar.textChanged.connect(self.refresh_donor_table)
        for combo in combo_boxes:
            try:
                combo.currentIndexChanged.disconnect()
            except Exception:
                pass
            combo.currentIndexChanged.connect(self.refresh_donor_table)

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
                conn = get_db_connection()
                try:
                    cur = conn.cursor()
                    cur.execute("INSERT INTO Categories (Name, Description) VALUES (?, ?)", (name, desc))
                    conn.commit()
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
                conn2 = get_db_connection()
                try:
                    cur2 = conn2.cursor()
                    cur2.execute("UPDATE Categories SET Name=?, Description=? WHERE CategoryID=?", (name, desc, cat_id))
                    conn2.commit()
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
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                cur.execute("INSERT INTO Subcategories (Name, Description, CategoryID) VALUES (?, ?, ?)", (name, desc, cat_id))
                conn.commit()
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
            conn2 = get_db_connection()
            try:
                cur2 = conn2.cursor()
                cur2.execute("UPDATE Subcategories SET category_id=?, Name=?, Description=? WHERE SubCategoryID=?", (cat_id, name, desc, subcat_id))
                conn2.commit()
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
            conn = get_db_connection()
            try:
                cur = conn.cursor()
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
            conn2 = get_db_connection()
            try:
                cur2 = conn2.cursor()
                cur2.execute(
                    "UPDATE Program_administrations SET PA_Name=?, PA_Description=?, Manager=? WHERE PA_Id=?",
                    (name, desc, manager,prog_id)
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
                conn = get_db_connection()
                try:
                    cur = conn.cursor()
                    cur.execute(
                        "INSERT INTO Project_Activities (ActivityName, ActivityDescription, ActivityStartDate, ActivityEndDate, ProjectID) VALUES (?, ?, ?, ?, ?)",
                        (name, desc, start, end, proj_id)
                    )
                    conn.commit()
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
                conn3 = get_db_connection()
                try:
                    cur3 = conn3.cursor()
                    cur3.execute(
                        "UPDATE Project_Activities SET ActivityName=?, ActivityDescription=?, ActivityStartDate=?, ActivityEndDate=?, ProjectID=? WHERE ActivityID=?",
                        (name, desc, start, end, proj_id, act_id)
                    )
                    conn3.commit()
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

    # --- Projects CRUD Management (like Category in Categories_SubCategories) ---
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
                conn = get_db_connection()
                try:
                    cur = conn.cursor()
                    cur.execute(
                        "INSERT INTO Projects (ProjectName, ProjectDescription, ProjectStartDate, ProjectEndDate, ProgramID) VALUES (?, ?, ?, ?, ?)",
                        (name, desc, start, end, prog_id)
                    )
                    conn.commit()
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
                conn3 = get_db_connection()
                try:
                    cur3 = conn3.cursor()
                    cur3.execute(
                        "UPDATE Projects SET ProjectName=?, ProjectDescription=?, ProjectStartDate=?, ProjectEndDate=?, ProgramID=? WHERE ProjectID=?",
                        (name, desc, start, end, prog_id, proj_id)
                    )
                    conn3.commit()
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
        self.AddButton = button("Add", "primary", "md", icon_path="Icons/add.svg", icon_toolTip="Add New Transaction")
        self.AddButton.clicked.connect(self.add_transaction)
        self.ExportButton = button("Export", "success", "md", icon_path="Icons/print.svg", icon_toolTip="Export as Pdf")
        ContentAreaHeaderLayout.addWidget(self.Title, alignment=Qt.AlignLeft)
        ContentAreaHeaderLayout.addStretch()
        ContentAreaHeaderLayout.addWidget(self.AddButton, alignment=Qt.AlignRight)
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
        self.type_filter.addItems(["All", "Income", "Expense"])
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

        # Connect Add button (implement add_transaction if needed)
        # self.AddButton.clicked.connect(self.add_transaction)

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
        dlg = QDialog(self)
        dlg.setWindowTitle("Add Transaction")
        dlg.setStyleSheet(DialogStyles())
        lyt = QVBoxLayout(dlg)
        form = QFormLayout()

        # Date
        date_input = QDateEdit()
        date_input.setCalendarPopup(True)
        date_input.setDate(QDate.currentDate())
        form.addRow("Date:", date_input)

        # Fiscal Year (BudgetYear)
        fiscal_year_input = QSpinBox()
        fiscal_year_input.setMinimum(1900)
        fiscal_year_input.setMaximum(2100)
        fiscal_year_input.setValue(QDate.currentDate().year())
        form.addRow("Fiscal Year:", fiscal_year_input)

        # Type
        type_combo = QComboBox()
        type_combo.addItems(["Income", "Expense"])
        form.addRow("Type:", type_combo)

        # Amount
        amount_input = QLineEdit()
        amount_input.setValidator(QDoubleValidator(0, 1e12, 2))
        form.addRow("Amount:", amount_input)

        # Program
        program_combo = QComboBox()
        program_combo.addItem("None", None)
        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT PA_Id, PA_Name FROM Program_administrations")
            programs = cur.fetchall()
        finally:
            conn.close()
        for prog in programs:
            program_combo.addItem(prog["PA_Name"], prog["PA_Id"])
        form.addRow("Program:", program_combo)

        # Project (filtered by program)
        project_combo = QComboBox()
        project_combo.addItem("None", None)
        def update_projects():
            project_combo.blockSignals(True)
            project_combo.clear()
            project_combo.addItem("None", None)
            prog_id = program_combo.currentData()
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
                project_combo.addItem(proj["ProjectName"], proj["ProjectID"])
            project_combo.blockSignals(False)
        update_projects()
        program_combo.currentIndexChanged.connect(update_projects)
        form.addRow("Project:", project_combo)

        # Activity (filtered by project)
        activity_combo = QComboBox()
        activity_combo.addItem("None", None)
        def update_activities():
            activity_combo.blockSignals(True)
            activity_combo.clear()
            activity_combo.addItem("None", None)
            proj_id = project_combo.currentData()
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
                activity_combo.addItem(act["ActivityName"], act["ActivityID"])
            activity_combo.blockSignals(False)
        update_activities()
        project_combo.currentIndexChanged.connect(update_activities)
        form.addRow("Activity:", activity_combo)

        # Reference
        reference_input = QLineEdit()
        form.addRow("Reference:", reference_input)

        # Description
        description_input = QLineEdit()
        form.addRow("Description:", description_input)

        # Category (for subcategory navigation)
        category_combo = QComboBox()
        category_combo.addItem("None", None)
        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT CategoryID, Name FROM Categories")
            cats = cur.fetchall()
        finally:
            conn.close()
        for cat in cats:
            category_combo.addItem(cat["Name"], cat["CategoryID"])
        form.addRow("Category:", category_combo)

        # Subcategory (filtered by category)
        subcategory_combo = QComboBox()
        subcategory_combo.addItem("None", None)
        def update_subcategories():
            subcategory_combo.blockSignals(True)
            subcategory_combo.clear()
            subcategory_combo.addItem("None", None)
            cat_id = category_combo.currentData()
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                if cat_id:
                    cur.execute("SELECT SubCategoryID, Name FROM Subcategories WHERE category_id=?", (cat_id,))
                else:
                    cur.execute("SELECT SubCategoryID, Name FROM Subcategories")
                subs = cur.fetchall()
            finally:
                conn.close()
            for sub in subs:
                subcategory_combo.addItem(sub["Name"], sub["SubCategoryID"])
            subcategory_combo.blockSignals(False)
        update_subcategories()
        category_combo.currentIndexChanged.connect(update_subcategories)
        form.addRow("Subcategory:", subcategory_combo)

        # Logic: Disable Activity, Category, Subcategory if Income is selected
        def update_fields_for_type():
            is_income = type_combo.currentText() == "Income"
            activity_combo.setEnabled(not is_income)
            category_combo.setEnabled(not is_income)
            subcategory_combo.setEnabled(not is_income)
        type_combo.currentIndexChanged.connect(update_fields_for_type)
        update_fields_for_type()

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
            date = date_input.date().toString("yyyy-MM-dd")
            fiscal_year = fiscal_year_input.value()
            ttype = type_combo.currentText()
            try:
                amount = float(amount_input.text())
            except Exception:
                QMessageBox.warning(dlg, "Error", "Amount is required and must be a number.")
                return
            program_id = program_combo.currentData()
            project_id = project_combo.currentData()
            activity_id = activity_combo.currentData() if not (ttype == "Income") else None
            reference = reference_input.text().strip()
            desc = description_input.text().strip()
            subcat_id = subcategory_combo.currentData() if not (ttype == "Income") else None

            # Validation
            if not date or not ttype or not amount or not fiscal_year:
                QMessageBox.warning(dlg, "Error", "Date, Type, Amount, and Fiscal Year are required.")
                return
            if ttype == "Expense" and not subcat_id:
                QMessageBox.warning(dlg, "Error", "Subcategory is required for Expense.")
                return

            conn = get_db_connection()
            try:
                cur = conn.cursor()
                cur.execute("""
                    INSERT INTO Transactions
                    (TransactionDate, BudgetYear, TransactionType, Amount, ProgramID, ProjectID, ActivityID, Reference, Description, SubCategories)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (date, fiscal_year, ttype, amount, program_id, project_id, activity_id, reference, desc, subcat_id))
                conn.commit()
                transaction_id = cur.lastrowid
            finally:
                conn.close()
            dlg.accept()
            self.refresh_transaction_table()
            if ttype == "Income":
                self.add_fund_after_income(transaction_id)

        save_btn.clicked.connect(save)
        dlg.exec_()

    def add_fund_after_income(self, transaction_id):
        dlg = QDialog(self)
        dlg.setWindowTitle("Add Fund for Income Transaction")
        dlg.setStyleSheet(DialogStyles())
        lyt = QVBoxLayout(dlg)
        form = QFormLayout()
        name_input = QLineEdit()
        # TransactionID (readonly)
        tid_label = QLabel(str(transaction_id))
        # Donor ComboBox
        donor_combo = QComboBox()
        donor_combo.addItem("None", None)
        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT DonorID, firstname, lastname FROM Donors")
            donors = cur.fetchall()
        finally:
            conn.close()
        for d in donors:
            donor_combo.addItem(f"{d['firstname']} {d['lastname']}", d["DonorID"])
        fundtype_input = QLineEdit()
        form.addRow("Fund Name:", name_input)
        form.addRow("Transaction ID:", tid_label)
        form.addRow("Donor:", donor_combo)
        form.addRow("Fund Type:", fundtype_input)
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
            donor_id = donor_combo.currentData()
            fundtype = fundtype_input.text().strip()
            if not name or not fundtype:
                QMessageBox.warning(dlg, "Error", "Fund Name and Fund Type are required.")
                return
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                cur.execute(
                    "INSERT INTO Fund (FundName , TransactionID, DonorID, FundType) VALUES (?, ?, ?, ?)",
                    (name, transaction_id, donor_id, fundtype)
                )
                conn.commit()
            finally:
                conn.close()
            dlg.accept()
            if hasattr(self, "refresh_fund_table"):
                self.refresh_fund_table()
        save_btn.clicked.connect(save)
        dlg.exec_()

    def edit_transaction(self, transaction_id):
        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Transactions WHERE TransactionID=?", (transaction_id,))
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
        date_input = QDateEdit()
        date_input.setCalendarPopup(True)
        if tx["TransactionDate"]:
            date_input.setDate(QDate.fromString(tx["TransactionDate"], "yyyy-MM-dd"))
        else:
            date_input.setDate(QDate.currentDate())
        type_combo = QComboBox()
        type_combo.addItems(["Income", "Expense"])
        idx = type_combo.findText(tx["TransactionType"])
        if idx >= 0:
            type_combo.setCurrentIndex(idx)
        amount_input = QLineEdit(str(tx["Amount"]))
        amount_input.setValidator(QDoubleValidator(0, 1e12, 2))
        # Program
        program_combo = QComboBox()
        program_combo.addItem("None", None)
        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT PA_Id, PA_Name FROM Program_administrations")
            programs = cur.fetchall()
        finally:
            conn.close()
        prog_idx = 0
        for i, prog in enumerate(programs):
            program_combo.addItem(prog["PA_Name"], prog["PA_Id"])
            if tx["ProgramID"] == prog["PA_Id"]:
                prog_idx = i + 1
        program_combo.setCurrentIndex(prog_idx)
        # Project
        project_combo = QComboBox()
        project_combo.addItem("None", None)
        def update_projects():
            project_combo.blockSignals(True)
            project_combo.clear()
            project_combo.addItem("None", None)
            prog_id = program_combo.currentData()
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
                project_combo.addItem(proj["ProjectName"], proj["ProjectID"])
                if tx["ProjectID"] == proj["ProjectID"]:
                    proj_idx = i + 1
            project_combo.setCurrentIndex(proj_idx)
            project_combo.blockSignals(False)
        update_projects()
        program_combo.currentIndexChanged.connect(update_projects)
        # Activity
        activity_combo = QComboBox()
        activity_combo.addItem("None", None)
        def update_activities():
            activity_combo.blockSignals(True)
            activity_combo.clear()
            activity_combo.addItem("None", None)
            proj_id = project_combo.currentData()
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
                activity_combo.addItem(act["ActivityName"], act["ActivityID"])
                if tx["ActivityID"] == act["ActivityID"]:
                    act_idx = i + 1
            activity_combo.setCurrentIndex(act_idx)
            activity_combo.blockSignals(False)
        update_activities()
        project_combo.currentIndexChanged.connect(update_activities)
        reference_input = QLineEdit(tx["Reference"] or "")
        description_input = QLineEdit(tx["Description"] or "")
        # Category
        category_combo = QComboBox()
        category_combo.addItem("None", None)
        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT CategoryID, Name FROM Categories")
            cats = cur.fetchall()
        finally:
            conn.close()
        cat_idx = 0
        for i, cat in enumerate(cats):
            category_combo.addItem(cat["Name"], cat["CategoryID"])
            # Find subcategory's category
            if tx["SubCategories"]:
                conn2 = get_db_connection()
                try:
                    cur2 = conn2.cursor()
                    cur2.execute("SELECT category_id FROM Subcategories WHERE SubCategoryID=?", (tx["SubCategories"],))
                    subcat = cur2.fetchone()
                finally:
                    conn2.close()
                if subcat and subcat["category_id"] == cat["CategoryID"]:
                    cat_idx = i + 1
        category_combo.setCurrentIndex(cat_idx)
        # Subcategory
        subcategory_combo = QComboBox()
        subcategory_combo.addItem("None", None)
        def update_subcategories():
            subcategory_combo.blockSignals(True)
            subcategory_combo.clear()
            subcategory_combo.addItem("None", None)
            cat_id = category_combo.currentData()
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                if cat_id:
                    cur.execute("SELECT SubCategoryID, Name FROM Subcategories WHERE category_id=?", (cat_id,))
                else:
                    cur.execute("SELECT SubCategoryID, Name FROM Subcategories")
                subs = cur.fetchall()
            finally:
                conn.close()
            sub_idx = 0
            for i, sub in enumerate(subs):
                subcategory_combo.addItem(sub["Name"], sub["SubCategoryID"])
                if tx["SubCategories"] == sub["SubCategoryID"]:
                    sub_idx = i + 1
            subcategory_combo.setCurrentIndex(sub_idx)
            subcategory_combo.blockSignals(False)
        update_subcategories()
        category_combo.currentIndexChanged.connect(update_subcategories)
        form.addRow("Date:", date_input)
        form.addRow("Type:", type_combo)
        form.addRow("Amount:", amount_input)
        form.addRow("Program:", program_combo)
        form.addRow("Project:", project_combo)
        form.addRow("Activity:", activity_combo)
        form.addRow("Reference:", reference_input)
        form.addRow("Description:", description_input)
        form.addRow("Category:", category_combo)
        form.addRow("Subcategory:", subcategory_combo)
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
            date = date_input.date().toString("yyyy-MM-dd")
            ttype = type_combo.currentText()
            try:
                amount = float(amount_input.text())
            except Exception:
                QMessageBox.warning(dlg, "Error", "Amount is required and must be a number.")
                return
            program_id = program_combo.currentData()
            project_id = project_combo.currentData()
            activity_id = activity_combo.currentData()
            reference = reference_input.text().strip()
            desc = description_input.text().strip()
            subcat_id = subcategory_combo.currentData()
            if not date or not ttype or not amount or not subcat_id:
                QMessageBox.warning(dlg, "Error", "Date, Type, Amount, and Subcategory are required.")
                return
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                cur.execute("""
                    UPDATE Transactions SET
                    TransactionDate=?, TransactionType=?, Amount=?, ProgramID=?, ProjectID=?, ActivityID=?, Reference=?, Description=?, SubCategories=?
                    WHERE TransactionID=?
                """, (date, ttype, amount, program_id, project_id, activity_id, reference, desc, subcat_id, transaction_id))
                conn.commit()
            finally:
                conn.close()
            dlg.accept()
            self.refresh_transaction_table()
        save_btn.clicked.connect(save)
        dlg.exec_()

    def delete_transaction(self, transaction_id):
        reply = QMessageBox.question(self, "Delete", "Delete this transaction?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            conn = get_db_connection()
            try:
                cur = conn.cursor()
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
        self.type_filter.addItem("All")
        # Populate FundType from DB
        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT DISTINCT FundType FROM Fund")
            types = cur.fetchall()
        finally:
            conn.close()
        for t in types:
            if t["FundType"]:
                self.type_filter.addItem(t["FundType"])
        TableHeaderLayout.addWidget(TableTitleLabel)
        TableHeaderLayout.addStretch()
        TableHeaderLayout.addWidget(self.SearchBar, alignment=Qt.AlignRight)
        TableHeaderLayout.addWidget(self.cancelButton)
        TableHeaderLayout.addWidget(Filter)
        TableHeaderLayout.addWidget(QLabel("Type:"))
        TableHeaderLayout.addWidget(self.type_filter)
        TableHeader.setLayout(TableHeaderLayout)
        Layout.addWidget(TableHeader, alignment=Qt.AlignTop)

        # Table of Funds
        self.TableofFunds = QTableWidget()
        self.TableofFunds.setStyleSheet(TableStyles())
        self.TableofFunds.setColumnCount(5)
        self.TableofFunds.setHorizontalHeaderLabels(["Name", "Date", "Donor Name", "FundType", "Actions"])
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
        query = """
            SELECT f.FundID, f.FundName , t.TransactionDate as Date, d.firstname, d.lastname, f.FundType
            FROM Fund f
            LEFT JOIN Donors d ON f.DonorID = d.DonorID
            LEFT JOIN Transactions t ON f.TransactionID = t.TransactionID
            WHERE 1=1
        """
        params = []
        if type_val != "All":
            query += " AND f.FundType = ?"
            params.append(type_val)
        if search_text:
            query += " AND (LOWER(f.FundName ) LIKE ? OR LOWER(f.FundType) LIKE ? OR LOWER(d.firstname) LIKE ? OR LOWER(d.lastname) LIKE ?)"
            params.extend([f"%{search_text}%"] * 4)
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
            table.setItem(row_idx, 0, QTableWidgetItem(fund["FundName "] or ""))
            table.setItem(row_idx, 1, QTableWidgetItem(fund["Date"] or ""))
            donor_name = f"{fund['firstname'] or ''} {fund['lastname'] or ''}".strip()
            table.setItem(row_idx, 2, QTableWidgetItem(donor_name))
            table.setItem(row_idx, 3, QTableWidgetItem(fund["FundType"] or ""))
            action_widget = QWidget()
            action_layout = QHBoxLayout()
            edit_btn = TableButton("Edit")
            delete_btn = TableButton("Delete")
            action_layout.addWidget(edit_btn)
            action_layout.addWidget(delete_btn)
            action_layout.setContentsMargins(0, 0, 0, 0)
            action_widget.setLayout(action_layout)
            table.setCellWidget(row_idx, 4, action_widget)
            edit_btn.clicked.connect(lambda _, fid=fund["FundID"]: self.edit_fund(fid))
            delete_btn.clicked.connect(lambda _, fid=fund["FundID"]: self.delete_fund(fid))

    def add_fund(self):
        dlg = QDialog(self)
        dlg.setWindowTitle("Add Fund")
        dlg.setStyleSheet(DialogStyles())
        lyt = QVBoxLayout(dlg)
        form = QFormLayout()
        name_input = QLineEdit()
        date_input = QDateEdit()
        date_input.setCalendarPopup(True)
        date_input.setDate(QDate.currentDate())
        # Donor ComboBox
        donor_combo = QComboBox()
        donor_list = []
        conn = get_db_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT DonorID, firstname, lastname FROM Donors")
            donor_list = cur.fetchall()
        finally:
            conn.close()
        donor_combo.addItem("None", None)
        for d in donor_list:
            donor_combo.addItem(f"{d['firstname']} {d['lastname']}", d["DonorID"])
        fundtype_input = QLineEdit()
        form.addRow("Name:", name_input)
        form.addRow("Date:", date_input)
        form.addRow("Donor:", donor_combo)
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
            name = name_input.text().strip()
            date = date_input.date().toString("yyyy-MM-dd")
            donor_id = donor_combo.currentData()
            fundtype = fundtype_input.text().strip()
            if not name or not fundtype:
                QMessageBox.warning(dlg, "Error", "Name and FundType are required.")
                return
            conn = get_db_connection()
            try:
                cur = conn.cursor()
                cur.execute(
                    "INSERT INTO Fund (FundName , Date, DonorID, FundType) VALUES (?, ?, ?, ?)",
                    (name, date, donor_id, fundtype)
                )
                conn.commit()
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
        name_input = QLineEdit(fund["FundName "])
        date_input = QDateEdit()
        date_input.setCalendarPopup(True)
        if fund["Date"]:
            date_input.setDate(QDate.fromString(fund["Date"], "yyyy-MM-dd"))
        else:
            date_input.setDate(QDate.currentDate())
        # Donor ComboBox
        donor_combo = QComboBox()
        donor_list = []
        conn2 = get_db_connection()
        try:
            cur2 = conn2.cursor()
            cur2.execute("SELECT DonorID, firstname, lastname FROM Donors")
            donor_list = cur2.fetchall()
        finally:
            conn2.close()
        donor_combo.addItem("None", None)
        idx = 0
        for i, d in enumerate(donor_list):
            donor_combo.addItem(f"{d['firstname']} {d['lastname']}", d["DonorID"])
            if fund["DonorID"] == d["DonorID"]:
                idx = i + 1  # +1 for "None"
        donor_combo.setCurrentIndex(idx)
        fundtype_input = QLineEdit(fund["FundType"])
        form.addRow("Name:", name_input)
        form.addRow("Date:", date_input)
        form.addRow("Donor:", donor_combo)
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
            name = name_input.text().strip()
            date = date_input.date().toString("yyyy-MM-dd")
            donor_id = donor_combo.currentData()
            fundtype = fundtype_input.text().strip()
            if not name or not fundtype:
                QMessageBox.warning(dlg, "Error", "Name and FundType are required.")
                return
            conn3 = get_db_connection()
            try:
                cur3 = conn3.cursor()
                cur3.execute(
                    "UPDATE Fund SET FundName =?, Date=?, DonorID=?, FundType=? WHERE FundID=?",
                    (name, date, donor_id, fundtype, fund_id)
                )
                conn3.commit()
            finally:
                conn3.close()
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

class TableTitle(QLabel):
    def __init__(self, Text):
        super().__init__()
        self.setText(Text)
        self.setFont(QFont("Lato-Regular", 14))
        self.setStyleSheet("color:#1B263B;")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
        


       