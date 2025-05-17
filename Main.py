from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

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
        FundsWidget = QWidget()
        BudgetsWidget = QWidget()
        TransactionsWidget = QWidget()
        CategoriesWidget = QWidget()
        ProgramsWidget = QWidget()
        ProjectsWidget = QWidget()
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
        self.AddButton = button("Add","primary","lg",icon_path="Icons/add.svg",icon_toolTip="Add New Donor")
        self.ExportButton = button("Export","success","lg",icon_path="Icons/print.svg",icon_toolTip="Export as Pdf")
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
        SearchBar = QLineEdit()
        SearchBar.setMinimumWidth(200)
        SearchBar.setPlaceholderText("Search")
        SearchBar.setStyleSheet(FormStyles())
        Filter = QLabel("Filter:")
        Filter.setStyleSheet("""
            color: #1B263B;
            font-size: 12px;
            font-family: Lato-light;
            """
            )
        FilterComboBox1 = QComboBox()
        FilterComboBox1.addItems(["All", "Active", "Inactive"])
        FilterComboBox1.setStyleSheet(FormStyles())
        FilterComboBox2 = QComboBox()
        FilterComboBox2.setStyleSheet(FormStyles())
        FilterComboBox2.addItems(["All", "Individual", "Organization"])
        FilterComboBox3 = QComboBox()
        FilterComboBox3.setStyleSheet(FormStyles())
        FilterComboBox3.addItems(["All", "Donor Type 1", "Donor Type 2"])
        TableHeaderLayout.addWidget(DonorTableTitle)
        TableHeaderLayout.addWidget(SearchBar, alignment=Qt.AlignLeft)
        # TableHeaderLayout.addStretch()
        TableHeaderLayout.addWidget(Filter, alignment=Qt.AlignLeft)
        TableHeaderLayout.addWidget(FilterComboBox1)
        TableHeaderLayout.addWidget(FilterComboBox2)
        TableHeaderLayout.addWidget(FilterComboBox3)
        TableHeader.setLayout(TableHeaderLayout)
        Layout.addWidget(TableHeader, alignment=Qt.AlignTop)
        # Table of Donors
        TableofDonors = QTableWidget()
        TableofDonors.setStyleSheet(TableStyles())
        TableofDonors.setColumnCount(5)
        TableofDonors.setRowCount(10)
        TableofDonors.setHorizontalHeaderLabels(["Name", "Type", "Status", "Date Added", "Actions"])
        TableofDonors.horizontalHeader().setStretchLastSection(True)
        TableofDonors.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        TableofDonors.setItem(0, 0, QTableWidgetItem("John Doe"))
        TableofDonors.setItem(0, 1, QTableWidgetItem("Individual"))
        TableofDonors.setItem(0, 2, QTableWidgetItem("Active"))
        TableofDonors.setItem(0, 3, QTableWidgetItem("2023-10-01"))
        EditBtn = QPushButton("Edit")
        DeleteBtn = QPushButton("Delete")
        Actionbuttons = QWidget()
        ActionbtnsLyt = QHBoxLayout()
        ActionbtnsLyt.addWidget(EditBtn)
        ActionbtnsLyt.addWidget(DeleteBtn)
        Actionbuttons.setLayout(ActionbtnsLyt)
        TableofDonors.setCellWidget(0, 4, Actionbuttons)
        TableHeaderLayout.addWidget(TableofDonors)
        Layout.addWidget(TableofDonors)
    
    def DonorForm(self):
        self.Container = QDialog()
        self.FormLayout = QFormLayout()
        self.FormTitle  = QLabel("Register New Donor")
        self.FirstNameLayout = QVBoxLayout()
        self.FirstName_Label = QLabel("Firstname:")
        self.FirstName_Input = QLineEdit()
        self.FirstNameLayout.addWidget(self.FirstName_Label)
        self.FirstNameLayout.addWidget(self.FirstName_Input)
        self.LastNameLayout = QVBoxLayout()
        self.LastName_Label = QLabel("Lastname:")
        self.LastName_Input = QLineEdit()
        self.LastNameLayout.addWidget(self.LastName_Label)
        self.LastNameLayout.addWidget(self.LastName_Input)
        self.FormLayout.addWidget(self.FirstNameLayout,self.LastNameLayout)
        self.AddressLayout = QVBoxLayout()
        self.Address_Label = QLabel("Address")
        self.Address_Input = QLineEdit()
        self.AddressLayout.addWidget(self.Address_Label)
        self.AddressLayout.addWidget(self.Address_Input)
        self.ContactLayout = QVBoxLayout()
        self.Contact_Label = QLabel("Contact")
        self.Contact_Input = QLineEdit()
        self.ContactLayout.addWidget(self.Contact_Label)
        self.ContactLayout.addWidget(self.Contact_Input)
        self.FormLayout.addWidget(self.AddressLayout,self.ContactLayout)
        self.DonorTypeLayout = QVBoxLayout()
        self.DonorType_Label = QLabel("Donor Type:")
        self.DonorType_Input = QComboBox()

        
        
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
    def __init__(self, Type):
        super().__init__()
        if Type == 'Edit':
            # Set the icon
            icon = QIcon()
            icon.addPixmap(QPixmap('icons/edit_32px.png'), QIcon.Normal, QIcon.Off)
            self.setIcon(icon)
            self.setIconSize(QSize(20, 20))  # Set the icon size

            # Apply correct background-color
            self.setStyleSheet('background-color: #28a745; text-align: center;')  # Lowercase 'background-color'
        else:
            # Set the icon
            icon = QIcon()
            icon.addPixmap(QPixmap('icons/trash_can_32px.png'), QIcon.Normal, QIcon.Off)
            self.setIcon(icon)
            self.setIconSize(QSize(20, 20))  # Set the icon size

            # Apply correct background-color
            self.setStyleSheet('background-color: #dc3545; text-align: center')  # Lowercase 'background-color'

        # Set tooltip
        self.setToolTip(Type)

        # Set cursor to pointing hand
        self.setCursor(QCursor(Qt.PointingHandCursor))

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

class TableTitle(QLabel):
    def __init__(self,Text):
        super().__init__()
        self.setText(Text)
        self.setFont(QFont("Lato-Regular", 12))
        self.setStyleSheet("font-weight: bold;color:#1B263B;")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
        


       