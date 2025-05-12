from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QTextEdit, QVBoxLayout, QHBoxLayout, QWidget, QMessageBox, QComboBox, QCheckBox, QRadioButton, QTableWidget, QTableWidgetItem, QTabWidget, QFileDialog, QProgressBar, QSlider, QSpinBox, QDateEdit, QTimeEdit, QDateTimeEdit, QFrame, QGroupBox, QScrollArea, QListWidget, QTreeWidget, QTreeWidgetItem, QMenuBar, QStatusBar, QAction, QStackedWidget, QHeaderView, QToolBar, QTabBar, QLineEdit, QScrollBar, QSpacerItem, QSizePolicy, QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt, QTimer, QDate, QTime, QDateTime, QObject, pyqtSignal, pyqtSlot, QEvent, QSize
from PyQt5.QtGui import QIcon, QPixmap, QFont, QColor, QPainter, QPen, QBrush, QCursor

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
        DashboardButton = Links("Dashboard")
        SidebarLayout.addWidget(DashboardButton)
        SidebarLayout.addWidget(Links("Donor"))
        SidebarLayout.addWidget(Links("Fund"))
        SidebarLayout.addWidget(Links("Budget"))
        SidebarLayout.addWidget(Links("Transaction"))        
        SidebarLayout.addWidget(Links("Categories && Subcategories"))
        SidebarLayout.addWidget(Links("Programs && Administration"))
        SidebarLayout.addWidget(Links("Projects && Activities"))
        SidebarLayout.addWidget(Links("Report"))
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
        ContentBody = QScrollArea()
        ContentBody.setWidgetResizable(True)
        ContentBody.setStyleSheet("background-color: #F0F0F0;")
        ContentBody.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        ContentBody.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        ContentArea = QStackedWidget()
        ContentArea.setStyleSheet("Background-color:White;")
        DashboardWidget = QWidget()
        DashboardLayout = QVBoxLayout()
        DashboardLabel = QLabel("Dashboard")
        DashboardLayout.addWidget(DashboardLabel, alignment=Qt.AlignCenter)
        DashboardWidget.setLayout(DashboardLayout)
        DonorsWidget = DonorsPage()
        ContentArea.addWidget(DonorsWidget)
        ContentArea.addWidget(DashboardWidget)
        ContentBody.setWidget(ContentArea)
        MainBodyLayout.addWidget(ContentBody)
        MainBody.setLayout(MainBodyLayout)
        Layout.addWidget(MainBody)
        # Set the main layout for the window
        self.setLayout(Layout)

class DonorsPage(QWidget):
    def __init__(self):
        super().__init__()
        Layout = QVBoxLayout()
        self.setLayout(Layout)
        # Content header Area
        ContentAreaHeader = QWidget()
        ContentAreaHeaderLayout = QHBoxLayout()
        Title = QLabel("Donors")
        AddButton = QPushButton("Add")
        ExportButton = QPushButton("Export")
        ContentAreaHeaderLayout.addWidget(Title, alignment=Qt.AlignLeft)
        ContentAreaHeaderLayout.addStretch()
        ContentAreaHeaderLayout.addWidget(AddButton, alignment=Qt.AlignRight)
        ContentAreaHeaderLayout.addWidget(ExportButton, alignment=Qt.AlignRight)
        ContentAreaHeader.setLayout(ContentAreaHeaderLayout)
        Layout.addWidget(ContentAreaHeader, alignment=Qt.AlignTop)
        # Table header
        TableHeader = QWidget()
        TableHeaderLayout = QHBoxLayout()
        SearchBar = QLineEdit()
        SearchBar.setPlaceholderText("Search")
        Filter = QLabel("Filter:")
        FilterComboBox1 = QComboBox()
        FilterComboBox1.addItems(["All", "Active", "Inactive"])
        FilterComboBox2 = QComboBox()
        FilterComboBox2.addItems(["All", "Individual", "Organization"])
        FilterComboBox3 = QComboBox()
        FilterComboBox3.addItems(["All", "Donor Type 1", "Donor Type 2"])
        TableHeaderLayout.addWidget(SearchBar, alignment=Qt.AlignLeft)
        TableHeaderLayout.addWidget(Filter, alignment=Qt.AlignLeft)
        TableHeaderLayout.addWidget(FilterComboBox1, alignment=Qt.AlignLeft)
        TableHeaderLayout.addWidget(FilterComboBox2, alignment=Qt.AlignLeft)
        TableHeaderLayout.addWidget(FilterComboBox3, alignment=Qt.AlignLeft)
        TableHeader.setLayout(TableHeaderLayout)
        Layout.addWidget(TableHeader, alignment=Qt.AlignTop)
        # Table of Donors
        TableofDonors = QTableWidget()
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

class Links(QPushButton):
    def __init__(self, text="", icon_path=None, parent=None):
        super().__init__(text, parent)

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
            QPushButton:active{
                Background-color: White;
            }               
                           
        """)

        # Set icon if provided, else reserve space
        if icon_path:
            self.setIcon(QIcon(icon_path))
            self.setIconSize(QSize(18, 18))
        else:
            self.setIconSize(QSize(18, 18))  # reserve space for alignment
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
        


       