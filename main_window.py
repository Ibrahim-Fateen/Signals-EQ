# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1183, 810)
        MainWindow.setStyleSheet(u"/*\n"
"Dark Style Sheet for QT Applications\n"
"Author: Oussama Ben Sassi\n"
"Last updated: 29/7/2021\n"
"*/\n"
"QMainWindow {\n"
"	background-color:#1e1d23;\n"
"}\n"
"QDialog {\n"
"	background-color:#1e1d23;\n"
"}\n"
"QColorDialog {\n"
"	background-color:#1e1d23;\n"
"}\n"
"QTextEdit {\n"
"	background-color:#1e1d23;\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color:#8e44ad;\n"
"	border-bottom-width: 4px;\n"
"	border-width: 1px;\n"
"   	padding: 0 2px;\n"
"\n"
"	color: #a9b7c6;\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"	selection-background-color:#007b50;\n"
"	background-color:#1e1d23;\n"
"    border-style: solid;\n"
"     border-radius: 4px;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color:#8e44ad;\n"
"	border-bottom-width: 4px;\n"
"	border-width: 1px;\n"
"   	padding: 0 2px;\n"
"    color:"
                        " #a9b7c6;\n"
"}\n"
"QPushButton{\n"
"	border-style: solid;\n"
"\n"
"	border-color: #37efba;\n"
"	border-bottom-width: 4px;\n"
"	border-width: 1px;\n"
"	color: #a9b7c6;\n"
"	padding: 2px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QPushButton::default{\n"
"	border-style: inset;\n"
"	border-color: #04b97f;\n"
"	border-width: 1px;\n"
"	color: #a9b7c6;\n"
"	padding: 2px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QToolButton {\n"
"	border-style: solid;\n"
"	border-color: #04b97f;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	color: #a9b7c6;\n"
"	padding: 2px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QToolButton:hover{\n"
"	border-style: solid;\n"
"	border-color: #37efba;\n"
"	border-width: 2px;\n"
"	border-style: solid;\n"
"	color: #FFFFFF;\n"
"	padding-bottom: 1px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QPushButton:hover{\n"
"	border-style: solid;\n"
"	border-color: #37efba;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	color: #FFFFFF;\n"
"	padding-bottom: 2px;\n"
"	background-color: #1e1d23;\n"
""
                        "}\n"
"QPushButton:pressed{\n"
"	border-style: solid;\n"
"	border-color: #37efba;\n"
"	border-width: 2px;\n"
"	border-style: solid;\n"
"	color: #37efba;\n"
"	padding-bottom: 1px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QPushButton:disabled{\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: #808086;\n"
"	border-bottom-width: 2px;\n"
"	border-style: solid;\n"
"	color: #808086;\n"
"	padding-bottom: 1px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QLineEdit {\n"
"	border-width: 1px; border-radius: 4px;\n"
"    border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color:#8e44ad;\n"
"	border-bottom-width: 4px;\n"
"	border-width: 1px;\n"
"	padding: 0 8px;\n"
"	color: #a9b7c6;\n"
"	background:#1e1d23;\n"
"	selection-background-color:#007b50;\n"
"	selection-color: #FFFFFF;\n"
"}\n"
"QLabel {\n"
"	color: #37efba;\n"
""
                        "}\n"
"QLCDNumber {\n"
"	color: #37e6b4;\n"
"}\n"
"QProgressBar {\n"
"	text-align: center;\n"
"	color: rgb(240, 240, 240);\n"
"	border-width: 1px; \n"
"	border-radius: 10px;\n"
"	border-color: rgb(58, 58, 58);\n"
"	border-style: inset;\n"
"	background-color:#1e1d23;\n"
"}\n"
"QProgressBar::chunk {\n"
"	background-color: #04b97f;\n"
"	border-radius: 5px;\n"
"}\n"
"QMenuBar {\n"
"  background-color: #1e1d23;\n"
"  padding: 2px;\n"
"  \n"
"  color: #a9b7c6;\n"
"}\n"
"\n"
"QMenuBar:focus {\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"  background: transparent;\n"
"  padding: 4px;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"  padding: 4px;\n"
"  background: transparent;\n"
"  border: 0px solid #32414B;\n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
"  padding: 4px;\n"
"  border: 0px solid #32414B;\n"
"  background-color: #148CD2;\n"
"  color: #F0F0F0;\n"
"  margin-bottom: 0px;\n"
"  padding-bottom: 0px;\n"
"}\n"
"\n"
"/* QMenu ------------------------------------------------------------------\n"
""
                        "\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qmenu\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QMenu\n"
"{\n"
"    background-color: #1e1d23;\n"
"    border: 1px solid #4a5157;\n"
"    padding: 10px;\n"
"	color: #a9b7c6;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item\n"
"{\n"
"    background-color: transparent;\n"
"    padding: 2px 20px 2px 20px;\n"
"	min-width: 200px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::separator\n"
"{\n"
"   	background-color: #242424;\n"
"	height: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:disabled\n"
"{\n"
"    color: #555;\n"
"    background-color: transparent;\n"
"    padding: 2px 20px 2px 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"	background-color: #148CD2;\n"
"	border: 1px solid #006666;\n"
"	color: #fff;\n"
"\n"
"}\n"
"QTabWidget {\n"
"	color:rgb(0,0,0);\n"
"	background-color:#1e1d23;\n"
"}\n"
"QTabWidget::pane {\n"
"		border-color: rgb(77,77,77);\n"
"		background-color:#1e1d23;\n"
"		border-style: solid;\n"
"		b"
                        "order-width: 1px;\n"
"    	border-radius: 6px;\n"
"}\n"
"QTabBar::tab {\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: transparent;\n"
"	border-bottom-width: 1px;\n"
"	border-style: solid;\n"
"	color: #808086;\n"
"	padding: 3px;\n"
"	margin-left:3px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"  	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: #04b97f;\n"
"	border-bottom-width: 2px;\n"
"	border-style: solid;\n"
"	color: #FFFFFF;\n"
"	padding-left: 3px;\n"
"	padding-bottom: 2px;\n"
"	margin-left:3px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"\n"
"QCheckBox {\n"
"	color: #a9b7c6;\n"
"	padding: 2px;\n"
"}\n"
"QCheckBox:disabled {\n"
"	color: #808086;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"	border-radiu"
                        "s:4px;\n"
"	border-style:solid;\n"
"	padding-left: 1px;\n"
"	padding-right: 1px;\n"
"	padding-bottom: 1px;\n"
"	padding-top: 1px;\n"
"	border-width:1px;\n"
"	border-color: rgb(87, 97, 106);\n"
"	background-color:#1e1d23;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #04b97f;\n"
"	color: #a9b7c6;\n"
"	background-color: #04b97f;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #04b97f;\n"
"	color: #a9b7c6;\n"
"	background-color: transparent;\n"
"}\n"
"QRadioButton {\n"
"	color: #a9b7c6;\n"
"	background-color: #1e1d23;\n"
"	padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: #04b97f;\n"
"	color: #a9b7c6;\n"
"	background-color: #04b97f;\n"
"}\n"
"QRadioButton::indicator:!check"
                        "ed {\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: #04b97f;\n"
"	color: #a9b7c6;\n"
"	background-color: transparent;\n"
"}\n"
"QStatusBar {\n"
"	color:#027f7f;\n"
"}\n"
"QSpinBox {\n"
"	color: #a9b7c6;	\n"
"	background-color: #1e1d23;\n"
"}\n"
"QDoubleSpinBox {\n"
"	color: #a9b7c6;	\n"
"	background-color: #1e1d23;\n"
"}\n"
"QTimeEdit {\n"
"	color: #a9b7c6;	\n"
"	background-color: #1e1d23;\n"
"}\n"
"QDateTimeEdit {\n"
"	color: #a9b7c6;	\n"
"	background-color: #1e1d23;\n"
"}\n"
"QDateEdit {\n"
"	color: #a9b7c6;	\n"
"	background-color: #1e1d23;\n"
"}\n"
"QComboBox {\n"
"	color: #a9b7c6;	\n"
"	background: #1e1d23;\n"
"}\n"
"QComboBox:editable {\n"
"	background: #1e1d23;\n"
"	color: #a9b7c6;\n"
"	selection-background-color: #1e1d23;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: #a9b7c6;	\n"
"	background: #1e1d23;\n"
"	selection-color: #FFFFFF;\n"
"	selection-background-color: #1e1d23;\n"
"}\n"
"QComboBox:!editable:on, QComboBox"
                        "::drop-down:editable:on {\n"
"	color: #a9b7c6;	\n"
"	background: #1e1d23;\n"
"}\n"
"QFontComboBox {\n"
"	color: #a9b7c6;	\n"
"	background-color: #1e1d23;\n"
"}\n"
"QToolBox {\n"
"	color: #a9b7c6;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QToolBox::tab {\n"
"	color: #a9b7c6;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QToolBox::tab:selected {\n"
"	color: #FFFFFF;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QScrollArea {\n"
"	color: #FFFFFF;\n"
"	background-color: #2c3e50;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"	height: 5px;\n"
"	background: #04b97f;\n"
"\n"
"}\n"
"QSlider::groove:vertical {\n"
"	width: 5px;\n"
"	background: #04b97f;\n"
"	\n"
"}\n"
"QSlider::handle:horizontal {\n"
"	background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"	border: 1px solid #5c5c5c;\n"
"	width: 14px;\n"
"	margin: -5px 0;\n"
"	border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"	background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"	border: 1px solid #5c5"
                        "c5c;\n"
"	height: 14px;\n"
"	margin: 0 -5px;\n"
"	border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background: white;\n"
"}\n"
"QSlider::add-page:vertical {\n"
"  background: #04b97f;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background: #04b97f;\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"   background: white;\n"
"}\n"
"QListWidget {\n"
"    color: #a9b7c6;	\n"
"	background-color: #1e1d23;\n"
"    border-style:solid;\n"
"    border-top-color:#3498db;\n"
"    border-bottom-color:#3498db;\n"
"    border-radius:4px;\n"
"    border-width:1px;\n"
"\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_28 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(self.centralwidget)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMaximumSize(QSize(16777215, 50))
        self.top_frame.setStyleSheet(u"background-color: rgb(28, 32, 43);")
        self.horizontalLayout_3 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_3.setSpacing(7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.browse_btn = QPushButton(self.top_frame)
        self.browse_btn.setObjectName(u"browse_btn")
        self.browse_btn.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_3.addWidget(self.browse_btn)

        self.modes_combo = QComboBox(self.top_frame)
        self.modes_combo.setObjectName(u"modes_combo")
        self.modes_combo.setMinimumSize(QSize(250, 25))

        self.horizontalLayout_3.addWidget(self.modes_combo)

        self.horizontalSpacer_top = QSpacerItem(864, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_top)

        self.spectrogram_checkbox = QCheckBox(self.top_frame)
        self.spectrogram_checkbox.setObjectName(u"spectrogram_checkbox")
        self.spectrogram_checkbox.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_3.addWidget(self.spectrogram_checkbox)


        self.verticalLayout_28.addWidget(self.top_frame)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_28.addWidget(self.line_2)

        self.graphs_widget = QWidget(self.centralwidget)
        self.graphs_widget.setObjectName(u"graphs_widget")
        self.graphs_widget.setStyleSheet(u"background-color: rgb(19, 19, 31);")
        self.verticalLayout = QVBoxLayout(self.graphs_widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.graphs_layout = QHBoxLayout()
        self.graphs_layout.setSpacing(3)
        self.graphs_layout.setObjectName(u"graphs_layout")
        self.graph1_widget = QWidget(self.graphs_widget)
        self.graph1_widget.setObjectName(u"graph1_widget")
        self.verticalLayout_29 = QVBoxLayout(self.graph1_widget)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.original_plot_label = QLabel(self.graph1_widget)
        self.original_plot_label.setObjectName(u"original_plot_label")

        self.verticalLayout_29.addWidget(self.original_plot_label)


        self.graphs_layout.addWidget(self.graph1_widget)

        self.graph2_widget = QWidget(self.graphs_widget)
        self.graph2_widget.setObjectName(u"graph2_widget")
        self.verticalLayout_32 = QVBoxLayout(self.graph2_widget)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.equalized_plot_label = QLabel(self.graph2_widget)
        self.equalized_plot_label.setObjectName(u"equalized_plot_label")

        self.verticalLayout_32.addWidget(self.equalized_plot_label)


        self.graphs_layout.addWidget(self.graph2_widget)


        self.verticalLayout.addLayout(self.graphs_layout)

        self.spectrograph_layout = QHBoxLayout()
        self.spectrograph_layout.setSpacing(3)
        self.spectrograph_layout.setObjectName(u"spectrograph_layout")
        self.spectro1_widget = QWidget(self.graphs_widget)
        self.spectro1_widget.setObjectName(u"spectro1_widget")
        self.verticalLayout_30 = QVBoxLayout(self.spectro1_widget)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.original_spectro_label = QLabel(self.spectro1_widget)
        self.original_spectro_label.setObjectName(u"original_spectro_label")

        self.verticalLayout_30.addWidget(self.original_spectro_label)


        self.spectrograph_layout.addWidget(self.spectro1_widget)

        self.spectro2_widget = QWidget(self.graphs_widget)
        self.spectro2_widget.setObjectName(u"spectro2_widget")
        self.verticalLayout_31 = QVBoxLayout(self.spectro2_widget)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.equalized_spectro_label = QLabel(self.spectro2_widget)
        self.equalized_spectro_label.setObjectName(u"equalized_spectro_label")

        self.verticalLayout_31.addWidget(self.equalized_spectro_label)


        self.spectrograph_layout.addWidget(self.spectro2_widget)


        self.verticalLayout.addLayout(self.spectrograph_layout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 5, -1, 5)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.zoomin_btn = QPushButton(self.graphs_widget)
        self.zoomin_btn.setObjectName(u"zoomin_btn")
        icon = QIcon()
        icon.addFile(u"icons/zoom-in.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.zoomin_btn.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.zoomin_btn)

        self.zoomout_btn = QPushButton(self.graphs_widget)
        self.zoomout_btn.setObjectName(u"zoomout_btn")
        icon1 = QIcon()
        icon1.addFile(u"icons/zoom-out.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.zoomout_btn.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.zoomout_btn)

        self.graph_replay_btn = QPushButton(self.graphs_widget)
        self.graph_replay_btn.setObjectName(u"graph_replay_btn")
        icon2 = QIcon()
        icon2.addFile(u"icons/rotate-left.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.graph_replay_btn.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.graph_replay_btn)

        self.graph_play_btn = QPushButton(self.graphs_widget)
        self.graph_play_btn.setObjectName(u"graph_play_btn")
        icon3 = QIcon()
        icon3.addFile(u"icons/play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.graph_play_btn.setIcon(icon3)

        self.horizontalLayout_5.addWidget(self.graph_play_btn)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(3, -1, -1, -1)
        self.label_5 = QLabel(self.graphs_widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_4.addWidget(self.label_5)

        self.speed_slider = QSlider(self.graphs_widget)
        self.speed_slider.setObjectName(u"speed_slider")
        self.speed_slider.setMaximumSize(QSize(200, 150))
        self.speed_slider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_4.addWidget(self.speed_slider)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.verticalLayout_28.addWidget(self.graphs_widget)

        self.controls_frame = QFrame(self.centralwidget)
        self.controls_frame.setObjectName(u"controls_frame")
        self.controls_frame.setMaximumSize(QSize(16777215, 350))
        self.controls_frame.setStyleSheet(u"background-color: rgb(28, 32, 43);")
        self.controls_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.controls_frame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_10 = QHBoxLayout(self.controls_frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.audio_widget = QWidget(self.controls_frame)
        self.audio_widget.setObjectName(u"audio_widget")
        self.audio_widget.setMinimumSize(QSize(300, 0))
        self.audio_widget.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_21 = QVBoxLayout(self.audio_widget)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.audio_before_label = QLabel(self.audio_widget)
        self.audio_before_label.setObjectName(u"audio_before_label")
        self.audio_before_label.setStyleSheet(u"font: 75 9pt \"MS Shell Dlg 2\";")

        self.verticalLayout_2.addWidget(self.audio_before_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.audio1_slider = QSlider(self.audio_widget)
        self.audio1_slider.setObjectName(u"audio1_slider")
        self.audio1_slider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout.addWidget(self.audio1_slider)

        self.aduio1_play_btn = QPushButton(self.audio_widget)
        self.aduio1_play_btn.setObjectName(u"aduio1_play_btn")
        self.aduio1_play_btn.setIcon(icon3)

        self.horizontalLayout.addWidget(self.aduio1_play_btn)

        self.audio1_replay_btn = QPushButton(self.audio_widget)
        self.audio1_replay_btn.setObjectName(u"audio1_replay_btn")
        self.audio1_replay_btn.setIcon(icon2)

        self.horizontalLayout.addWidget(self.audio1_replay_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.audio1_time_label = QLabel(self.audio_widget)
        self.audio1_time_label.setObjectName(u"audio1_time_label")

        self.verticalLayout_2.addWidget(self.audio1_time_label)


        self.verticalLayout_21.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.audio_after_label = QLabel(self.audio_widget)
        self.audio_after_label.setObjectName(u"audio_after_label")
        self.audio_after_label.setStyleSheet(u"font: 75 9pt \"MS Shell Dlg 2\";")

        self.verticalLayout_3.addWidget(self.audio_after_label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.audio2_slider = QSlider(self.audio_widget)
        self.audio2_slider.setObjectName(u"audio2_slider")
        self.audio2_slider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_2.addWidget(self.audio2_slider)

        self.audio2_play_btn = QPushButton(self.audio_widget)
        self.audio2_play_btn.setObjectName(u"audio2_play_btn")
        self.audio2_play_btn.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.audio2_play_btn)

        self.audio2_replay_btn = QPushButton(self.audio_widget)
        self.audio2_replay_btn.setObjectName(u"audio2_replay_btn")
        self.audio2_replay_btn.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.audio2_replay_btn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.audio2_time_label = QLabel(self.audio_widget)
        self.audio2_time_label.setObjectName(u"audio2_time_label")

        self.verticalLayout_3.addWidget(self.audio2_time_label)


        self.verticalLayout_21.addLayout(self.verticalLayout_3)


        self.horizontalLayout_10.addWidget(self.audio_widget)

        self.line = QFrame(self.controls_frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_10.addWidget(self.line)

        self.sliders_widget = QWidget(self.controls_frame)
        self.sliders_widget.setObjectName(u"sliders_widget")
        self.verticalLayout_20 = QVBoxLayout(self.sliders_widget)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.uniform_widget = QWidget(self.sliders_widget)
        self.uniform_widget.setObjectName(u"uniform_widget")
        self.uniform_layout = QHBoxLayout(self.uniform_widget)
        self.uniform_layout.setSpacing(0)
        self.uniform_layout.setObjectName(u"uniform_layout")
        self.uniform_layout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.uniform_layout.addItem(self.horizontalSpacer_3)

        self.uniform_slider_widget1 = QWidget(self.uniform_widget)
        self.uniform_slider_widget1.setObjectName(u"uniform_slider_widget1")
        self.verticalLayout_4 = QVBoxLayout(self.uniform_slider_widget1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.uniform_label1 = QLabel(self.uniform_slider_widget1)
        self.uniform_label1.setObjectName(u"uniform_label1")
        self.uniform_label1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.uniform_label1)

        self.uniform_slider1 = QSlider(self.uniform_slider_widget1)
        self.uniform_slider1.setObjectName(u"uniform_slider1")
        self.uniform_slider1.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_4.addWidget(self.uniform_slider1)


        self.uniform_layout.addWidget(self.uniform_slider_widget1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.uniform_layout.addItem(self.horizontalSpacer_4)

        self.line_3 = QFrame(self.uniform_widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.uniform_layout.addWidget(self.line_3)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.uniform_layout.addItem(self.horizontalSpacer_5)

        self.uniform_slider_widget2 = QWidget(self.uniform_widget)
        self.uniform_slider_widget2.setObjectName(u"uniform_slider_widget2")
        self.verticalLayout_5 = QVBoxLayout(self.uniform_slider_widget2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.uniform_label2 = QLabel(self.uniform_slider_widget2)
        self.uniform_label2.setObjectName(u"uniform_label2")
        self.uniform_label2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.uniform_label2)

        self.uniform_slider2 = QSlider(self.uniform_slider_widget2)
        self.uniform_slider2.setObjectName(u"uniform_slider2")
        self.uniform_slider2.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_5.addWidget(self.uniform_slider2)


        self.uniform_layout.addWidget(self.uniform_slider_widget2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.uniform_layout.addItem(self.horizontalSpacer_6)

        self.line_5 = QFrame(self.uniform_widget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.uniform_layout.addWidget(self.line_5)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.uniform_layout.addItem(self.horizontalSpacer_7)

        self.uniform_slider_widget3 = QWidget(self.uniform_widget)
        self.uniform_slider_widget3.setObjectName(u"uniform_slider_widget3")
        self.verticalLayout_6 = QVBoxLayout(self.uniform_slider_widget3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.uniform_label3 = QLabel(self.uniform_slider_widget3)
        self.uniform_label3.setObjectName(u"uniform_label3")
        self.uniform_label3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.uniform_label3)

        self.uniform_slider3 = QSlider(self.uniform_slider_widget3)
        self.uniform_slider3.setObjectName(u"uniform_slider3")
        self.uniform_slider3.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_6.addWidget(self.uniform_slider3)


        self.uniform_layout.addWidget(self.uniform_slider_widget3)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.uniform_layout.addItem(self.horizontalSpacer_8)

        self.line_6 = QFrame(self.uniform_widget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.uniform_layout.addWidget(self.line_6)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.uniform_layout.addItem(self.horizontalSpacer_9)

        self.uniform_slider_widget4 = QWidget(self.uniform_widget)
        self.uniform_slider_widget4.setObjectName(u"uniform_slider_widget4")
        self.verticalLayout_27 = QVBoxLayout(self.uniform_slider_widget4)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.uniform_label4 = QLabel(self.uniform_slider_widget4)
        self.uniform_label4.setObjectName(u"uniform_label4")
        self.uniform_label4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_27.addWidget(self.uniform_label4)

        self.uniform_slider4 = QSlider(self.uniform_slider_widget4)
        self.uniform_slider4.setObjectName(u"uniform_slider4")
        self.uniform_slider4.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_27.addWidget(self.uniform_slider4)


        self.uniform_layout.addWidget(self.uniform_slider_widget4)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.uniform_layout.addItem(self.horizontalSpacer_10)

        self.line_15 = QFrame(self.uniform_widget)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.Shape.VLine)
        self.line_15.setFrameShadow(QFrame.Shadow.Sunken)

        self.uniform_layout.addWidget(self.line_15)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.uniform_layout.addItem(self.horizontalSpacer_11)

        self.uniform_slider_widget5 = QWidget(self.uniform_widget)
        self.uniform_slider_widget5.setObjectName(u"uniform_slider_widget5")
        self.verticalLayout_23 = QVBoxLayout(self.uniform_slider_widget5)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.uniform_label5 = QLabel(self.uniform_slider_widget5)
        self.uniform_label5.setObjectName(u"uniform_label5")
        self.uniform_label5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_23.addWidget(self.uniform_label5)

        self.uniform_slider5 = QSlider(self.uniform_slider_widget5)
        self.uniform_slider5.setObjectName(u"uniform_slider5")
        self.uniform_slider5.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_23.addWidget(self.uniform_slider5)


        self.uniform_layout.addWidget(self.uniform_slider_widget5)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.uniform_layout.addItem(self.horizontalSpacer_12)

        self.line_17 = QFrame(self.uniform_widget)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.Shape.VLine)
        self.line_17.setFrameShadow(QFrame.Shadow.Sunken)

        self.uniform_layout.addWidget(self.line_17)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.uniform_layout.addItem(self.horizontalSpacer_13)

        self.uniform_slider_widget6 = QWidget(self.uniform_widget)
        self.uniform_slider_widget6.setObjectName(u"uniform_slider_widget6")
        self.verticalLayout_25 = QVBoxLayout(self.uniform_slider_widget6)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.uniform_label6 = QLabel(self.uniform_slider_widget6)
        self.uniform_label6.setObjectName(u"uniform_label6")
        self.uniform_label6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_25.addWidget(self.uniform_label6)

        self.uniform_slider6 = QSlider(self.uniform_slider_widget6)
        self.uniform_slider6.setObjectName(u"uniform_slider6")
        self.uniform_slider6.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_25.addWidget(self.uniform_slider6)


        self.uniform_layout.addWidget(self.uniform_slider_widget6)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.uniform_layout.addItem(self.horizontalSpacer_14)

        self.line_18 = QFrame(self.uniform_widget)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.Shape.VLine)
        self.line_18.setFrameShadow(QFrame.Shadow.Sunken)

        self.uniform_layout.addWidget(self.line_18)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.uniform_layout.addItem(self.horizontalSpacer_15)

        self.uniform_slider_widget7 = QWidget(self.uniform_widget)
        self.uniform_slider_widget7.setObjectName(u"uniform_slider_widget7")
        self.verticalLayout_22 = QVBoxLayout(self.uniform_slider_widget7)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.uniform_label7 = QLabel(self.uniform_slider_widget7)
        self.uniform_label7.setObjectName(u"uniform_label7")
        self.uniform_label7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_22.addWidget(self.uniform_label7)

        self.uniform_slider7 = QSlider(self.uniform_slider_widget7)
        self.uniform_slider7.setObjectName(u"uniform_slider7")
        self.uniform_slider7.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_22.addWidget(self.uniform_slider7)


        self.uniform_layout.addWidget(self.uniform_slider_widget7)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.uniform_layout.addItem(self.horizontalSpacer_16)

        self.line_19 = QFrame(self.uniform_widget)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.Shape.VLine)
        self.line_19.setFrameShadow(QFrame.Shadow.Sunken)

        self.uniform_layout.addWidget(self.line_19)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.uniform_layout.addItem(self.horizontalSpacer_17)

        self.uniform_slider_widget8 = QWidget(self.uniform_widget)
        self.uniform_slider_widget8.setObjectName(u"uniform_slider_widget8")
        self.verticalLayout_24 = QVBoxLayout(self.uniform_slider_widget8)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.uniform_label8 = QLabel(self.uniform_slider_widget8)
        self.uniform_label8.setObjectName(u"uniform_label8")
        self.uniform_label8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_24.addWidget(self.uniform_label8)

        self.uniform_slider8 = QSlider(self.uniform_slider_widget8)
        self.uniform_slider8.setObjectName(u"uniform_slider8")
        self.uniform_slider8.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_24.addWidget(self.uniform_slider8)


        self.uniform_layout.addWidget(self.uniform_slider_widget8)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.uniform_layout.addItem(self.horizontalSpacer_18)

        self.line_20 = QFrame(self.uniform_widget)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShape(QFrame.Shape.VLine)
        self.line_20.setFrameShadow(QFrame.Shadow.Sunken)

        self.uniform_layout.addWidget(self.line_20)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.uniform_layout.addItem(self.horizontalSpacer_19)

        self.uniform_slider_widget9 = QWidget(self.uniform_widget)
        self.uniform_slider_widget9.setObjectName(u"uniform_slider_widget9")
        self.verticalLayout_26 = QVBoxLayout(self.uniform_slider_widget9)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.uniform_label9 = QLabel(self.uniform_slider_widget9)
        self.uniform_label9.setObjectName(u"uniform_label9")
        self.uniform_label9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_26.addWidget(self.uniform_label9)

        self.uniform_slider9 = QSlider(self.uniform_slider_widget9)
        self.uniform_slider9.setObjectName(u"uniform_slider9")
        self.uniform_slider9.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_26.addWidget(self.uniform_slider9)


        self.uniform_layout.addWidget(self.uniform_slider_widget9)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.uniform_layout.addItem(self.horizontalSpacer_20)

        self.line_16 = QFrame(self.uniform_widget)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.Shape.VLine)
        self.line_16.setFrameShadow(QFrame.Shadow.Sunken)

        self.uniform_layout.addWidget(self.line_16)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.uniform_layout.addItem(self.horizontalSpacer_21)

        self.uniform_slider_widget10 = QWidget(self.uniform_widget)
        self.uniform_slider_widget10.setObjectName(u"uniform_slider_widget10")
        self.verticalLayout_7 = QVBoxLayout(self.uniform_slider_widget10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.uniform_label10 = QLabel(self.uniform_slider_widget10)
        self.uniform_label10.setObjectName(u"uniform_label10")
        self.uniform_label10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.uniform_label10)

        self.uniform_slider10 = QSlider(self.uniform_slider_widget10)
        self.uniform_slider10.setObjectName(u"uniform_slider10")
        self.uniform_slider10.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_7.addWidget(self.uniform_slider10)


        self.uniform_layout.addWidget(self.uniform_slider_widget10)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.uniform_layout.addItem(self.horizontalSpacer_22)


        self.verticalLayout_20.addWidget(self.uniform_widget)

        self.music_vowels_widget = QWidget(self.sliders_widget)
        self.music_vowels_widget.setObjectName(u"music_vowels_widget")
        self.animal_layout = QHBoxLayout(self.music_vowels_widget)
        self.animal_layout.setObjectName(u"animal_layout")
        self.animal_layout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.animal_layout.addItem(self.horizontalSpacer_23)

        self.animal_slider_widget1_2 = QWidget(self.music_vowels_widget)
        self.animal_slider_widget1_2.setObjectName(u"animal_slider_widget1_2")
        self.animal_slider_widget1 = QVBoxLayout(self.animal_slider_widget1_2)
        self.animal_slider_widget1.setObjectName(u"animal_slider_widget1")
        self.vowel_label1 = QLabel(self.animal_slider_widget1_2)
        self.vowel_label1.setObjectName(u"vowel_label1")
        self.vowel_label1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.animal_slider_widget1.addWidget(self.vowel_label1)

        self.vowel_slider1 = QSlider(self.animal_slider_widget1_2)
        self.vowel_slider1.setObjectName(u"vowel_slider1")
        self.vowel_slider1.setOrientation(Qt.Orientation.Vertical)

        self.animal_slider_widget1.addWidget(self.vowel_slider1)


        self.animal_layout.addWidget(self.animal_slider_widget1_2)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.animal_layout.addItem(self.horizontalSpacer_24)

        self.line_4 = QFrame(self.music_vowels_widget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.animal_layout.addWidget(self.line_4)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.animal_layout.addItem(self.horizontalSpacer_25)

        self.animal_slider_widget2 = QWidget(self.music_vowels_widget)
        self.animal_slider_widget2.setObjectName(u"animal_slider_widget2")
        self.verticalLayout_9 = QVBoxLayout(self.animal_slider_widget2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.vowel_label2 = QLabel(self.animal_slider_widget2)
        self.vowel_label2.setObjectName(u"vowel_label2")
        self.vowel_label2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.vowel_label2)

        self.vowel_slider2 = QSlider(self.animal_slider_widget2)
        self.vowel_slider2.setObjectName(u"vowel_slider2")
        self.vowel_slider2.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_9.addWidget(self.vowel_slider2)


        self.animal_layout.addWidget(self.animal_slider_widget2)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.animal_layout.addItem(self.horizontalSpacer_26)

        self.line_7 = QFrame(self.music_vowels_widget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.animal_layout.addWidget(self.line_7)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.animal_layout.addItem(self.horizontalSpacer_27)

        self.animal_slider_widget3 = QWidget(self.music_vowels_widget)
        self.animal_slider_widget3.setObjectName(u"animal_slider_widget3")
        self.verticalLayout_10 = QVBoxLayout(self.animal_slider_widget3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.vowel_label3 = QLabel(self.animal_slider_widget3)
        self.vowel_label3.setObjectName(u"vowel_label3")
        self.vowel_label3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.vowel_label3)

        self.vowel_slider3 = QSlider(self.animal_slider_widget3)
        self.vowel_slider3.setObjectName(u"vowel_slider3")
        self.vowel_slider3.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_10.addWidget(self.vowel_slider3)


        self.animal_layout.addWidget(self.animal_slider_widget3)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.animal_layout.addItem(self.horizontalSpacer_28)

        self.line_8 = QFrame(self.music_vowels_widget)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.animal_layout.addWidget(self.line_8)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.animal_layout.addItem(self.horizontalSpacer_29)

        self.animal_slider_widget4 = QWidget(self.music_vowels_widget)
        self.animal_slider_widget4.setObjectName(u"animal_slider_widget4")
        self.verticalLayout_11 = QVBoxLayout(self.animal_slider_widget4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.vowel_label4 = QLabel(self.animal_slider_widget4)
        self.vowel_label4.setObjectName(u"vowel_label4")
        self.vowel_label4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.vowel_label4)

        self.vowel_slider4 = QSlider(self.animal_slider_widget4)
        self.vowel_slider4.setObjectName(u"vowel_slider4")
        self.vowel_slider4.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_11.addWidget(self.vowel_slider4)


        self.animal_layout.addWidget(self.animal_slider_widget4)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.animal_layout.addItem(self.horizontalSpacer_30)


        self.verticalLayout_20.addWidget(self.music_vowels_widget)

        self.music_animals_widget = QWidget(self.sliders_widget)
        self.music_animals_widget.setObjectName(u"music_animals_widget")
        self.music_layout = QHBoxLayout(self.music_animals_widget)
        self.music_layout.setSpacing(0)
        self.music_layout.setObjectName(u"music_layout")
        self.music_layout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.music_layout.addItem(self.horizontalSpacer_31)

        self.music_slider_widget1 = QWidget(self.music_animals_widget)
        self.music_slider_widget1.setObjectName(u"music_slider_widget1")
        self.verticalLayout_12 = QVBoxLayout(self.music_slider_widget1)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.music_animals_label1 = QLabel(self.music_slider_widget1)
        self.music_animals_label1.setObjectName(u"music_animals_label1")
        self.music_animals_label1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.music_animals_label1)

        self.music_animals_slider1 = QSlider(self.music_slider_widget1)
        self.music_animals_slider1.setObjectName(u"music_animals_slider1")
        self.music_animals_slider1.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_12.addWidget(self.music_animals_slider1)


        self.music_layout.addWidget(self.music_slider_widget1)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.music_layout.addItem(self.horizontalSpacer_32)

        self.line_9 = QFrame(self.music_animals_widget)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.VLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.music_layout.addWidget(self.line_9)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.music_layout.addItem(self.horizontalSpacer_33)

        self.music_slider_widget2 = QWidget(self.music_animals_widget)
        self.music_slider_widget2.setObjectName(u"music_slider_widget2")
        self.verticalLayout_13 = QVBoxLayout(self.music_slider_widget2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.music_animals_label2 = QLabel(self.music_slider_widget2)
        self.music_animals_label2.setObjectName(u"music_animals_label2")
        self.music_animals_label2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.music_animals_label2)

        self.music_animals_slider2 = QSlider(self.music_slider_widget2)
        self.music_animals_slider2.setObjectName(u"music_animals_slider2")
        self.music_animals_slider2.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_13.addWidget(self.music_animals_slider2)


        self.music_layout.addWidget(self.music_slider_widget2)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.music_layout.addItem(self.horizontalSpacer_34)

        self.line_10 = QFrame(self.music_animals_widget)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.Shape.VLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.music_layout.addWidget(self.line_10)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.music_layout.addItem(self.horizontalSpacer_35)

        self.music_slider_widget3 = QWidget(self.music_animals_widget)
        self.music_slider_widget3.setObjectName(u"music_slider_widget3")
        self.verticalLayout_14 = QVBoxLayout(self.music_slider_widget3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.music_animals_label3 = QLabel(self.music_slider_widget3)
        self.music_animals_label3.setObjectName(u"music_animals_label3")
        self.music_animals_label3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.music_animals_label3)

        self.music_animals_slider3 = QSlider(self.music_slider_widget3)
        self.music_animals_slider3.setObjectName(u"music_animals_slider3")
        self.music_animals_slider3.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_14.addWidget(self.music_animals_slider3)


        self.music_layout.addWidget(self.music_slider_widget3)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.music_layout.addItem(self.horizontalSpacer_36)

        self.line_11 = QFrame(self.music_animals_widget)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.Shape.VLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.music_layout.addWidget(self.line_11)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.music_layout.addItem(self.horizontalSpacer_37)

        self.music_slider_widget4 = QWidget(self.music_animals_widget)
        self.music_slider_widget4.setObjectName(u"music_slider_widget4")
        self.verticalLayout_15 = QVBoxLayout(self.music_slider_widget4)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.music_animals_label4 = QLabel(self.music_slider_widget4)
        self.music_animals_label4.setObjectName(u"music_animals_label4")
        self.music_animals_label4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.music_animals_label4)

        self.music_animals_slider4 = QSlider(self.music_slider_widget4)
        self.music_animals_slider4.setObjectName(u"music_animals_slider4")
        self.music_animals_slider4.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_15.addWidget(self.music_animals_slider4)


        self.music_layout.addWidget(self.music_slider_widget4)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.music_layout.addItem(self.horizontalSpacer_38)

        self.line_12 = QFrame(self.music_animals_widget)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.Shape.VLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.music_layout.addWidget(self.line_12)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.music_layout.addItem(self.horizontalSpacer_39)

        self.verticalWidget = QWidget(self.music_animals_widget)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalWidget.setMinimumSize(QSize(0, 0))
        self.verticalLayout_8 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.music_animals_label5 = QLabel(self.verticalWidget)
        self.music_animals_label5.setObjectName(u"music_animals_label5")

        self.verticalLayout_8.addWidget(self.music_animals_label5)

        self.music_animals_slider5 = QSlider(self.verticalWidget)
        self.music_animals_slider5.setObjectName(u"music_animals_slider5")
        self.music_animals_slider5.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_8.addWidget(self.music_animals_slider5)


        self.music_layout.addWidget(self.verticalWidget)

        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.music_layout.addItem(self.horizontalSpacer_40)

        self.line_13 = QFrame(self.music_animals_widget)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.Shape.VLine)
        self.line_13.setFrameShadow(QFrame.Shadow.Sunken)

        self.music_layout.addWidget(self.line_13)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.music_layout.addItem(self.horizontalSpacer_41)

        self.verticalWidget1 = QWidget(self.music_animals_widget)
        self.verticalWidget1.setObjectName(u"verticalWidget1")
        self.verticalWidget1.setMinimumSize(QSize(33, 0))
        self.verticalLayout_16 = QVBoxLayout(self.verticalWidget1)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.music_animals_label6 = QLabel(self.verticalWidget1)
        self.music_animals_label6.setObjectName(u"music_animals_label6")

        self.verticalLayout_16.addWidget(self.music_animals_label6)

        self.music_animals_slider6 = QSlider(self.verticalWidget1)
        self.music_animals_slider6.setObjectName(u"music_animals_slider6")
        self.music_animals_slider6.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_16.addWidget(self.music_animals_slider6)


        self.music_layout.addWidget(self.verticalWidget1)

        self.horizontalSpacer_42 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.music_layout.addItem(self.horizontalSpacer_42)


        self.verticalLayout_20.addWidget(self.music_animals_widget)


        self.horizontalLayout_10.addWidget(self.sliders_widget)


        self.verticalLayout_28.addWidget(self.controls_frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1183, 29))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.browse_btn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.spectrogram_checkbox.setText(QCoreApplication.translate("MainWindow", u"Show spectrogram", None))
        self.original_plot_label.setText(QCoreApplication.translate("MainWindow", u"Original plot", None))
        self.equalized_plot_label.setText(QCoreApplication.translate("MainWindow", u"Equalized plot", None))
        self.original_spectro_label.setText(QCoreApplication.translate("MainWindow", u"Original spectrogram", None))
        self.equalized_spectro_label.setText(QCoreApplication.translate("MainWindow", u"Equalized spectrogram", None))
        self.zoomin_btn.setText("")
        self.zoomout_btn.setText("")
        self.graph_replay_btn.setText("")
        self.graph_play_btn.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"speed", None))
        self.audio_before_label.setText(QCoreApplication.translate("MainWindow", u"Audio before", None))
        self.aduio1_play_btn.setText("")
        self.audio1_replay_btn.setText("")
        self.audio1_time_label.setText(QCoreApplication.translate("MainWindow", u"00:00 / 00:00", None))
        self.audio_after_label.setText(QCoreApplication.translate("MainWindow", u"Audio after", None))
        self.audio2_play_btn.setText("")
        self.audio2_replay_btn.setText("")
        self.audio2_time_label.setText(QCoreApplication.translate("MainWindow", u"00:00 / 00:00", None))
        self.uniform_label1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.uniform_label2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.uniform_label3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.uniform_label4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.uniform_label5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.uniform_label6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.uniform_label7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.uniform_label8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.uniform_label9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.uniform_label10.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.vowel_label1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.vowel_label2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.vowel_label3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.vowel_label4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.music_animals_label1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.music_animals_label2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.music_animals_label3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.music_animals_label4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.music_animals_label5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.music_animals_label6.setText(QCoreApplication.translate("MainWindow", u"6", None))
    # retranslateUi

