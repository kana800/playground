from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
import csv
from datetime import datetime
import pandas as pd
from PyQt5 import QtChart as qtch


months = ['','January','February','March','April','May','June','July','August','September','October','November',
            'December']

colors = ['#ee82ee']



class ComboboxModel:
    '''
    AbstractStringModel for our combobox, This model contains all the items that is needed for our inventory.
    User can Add items
        >Detect if the same item is entered
        >Detect if the user enters an empty string
    User can remove items
        
    '''
    def __init__(self,*args,**kwargs):
        super().__init__()
        self.filename = 'items.csv'
        with open(self.filename) as fh:
            csvreader = csv.reader(fh)
            self._headers = next(csvreader)
            self._data = list(csvreader)
        self._data = [t for i in self._data for t in i] 
        self.model = qtc.QStringListModel(self._data)
    
    def add_data(self,item_name):
        '''
        Adds the "item" to the end of the list
        '''
        self._data.append(item_name)

    def remove_data(self,item_name):
        '''
        Removes the "item" from the list
        '''
        self._data.remove(item_name)

    def save_data(self):
        '''
        Saves the item names in the model to the file
        '''
        with open(self.filename,'w',encoding='utf-8') as fh:
                writer = csv.writer(fh)
                writer.writerow(self._headers)
                writer.writerow(self._data)
class ChartWidget(qtw.QWidget):
    '''
    This chart shows the Income/Expense/Balance that is earned DAILY
    '''
    def __init__(self):
        super().__init__()
        
        self.setLayout(qtw.QVBoxLayout())
            
        grpbxwidgt = qtw.QGroupBox()
        grpbxwidgt.setTitle("Visualization of Data")
        grpbxwidgt.setLayout(qtw.QVBoxLayout())

        # BAR GRAPH

        self.series = qtch.QBarSeries() 
        self.chart = qtch.QChart()      
        self.chart.addSeries(self.series) 
        self.chart.setTitle("<h5>Daily Income & Expense</h5>")
        self.chart.setAnimationOptions(qtch.QChart.SeriesAnimations)
        self.axis = qtch.QBarCategoryAxis() 
        self.chart.createDefaultAxes()
        self.chart.setAxisX(self.axis,self.series)
        self.chart.axisY(self.series).setRange(0,10000)
        self.chart.axisY(self.series).setTitleText("Money (LKR)")
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(qtc.Qt.AlignBottom)
        self.chartview = qtch.QChartView(self.chart)
        self.chartview.setRenderHint(qtg.QPainter.Antialiasing)


        # PIE CHART
        
        self.pieseries = qtch.QPieSeries()
        self.piechart = qtch.QChart()
        self.piechart.addSeries(self.pieseries)
        self.piechart.setTitle("Item's Sold  and Remaining")
        self.piechart.setAnimationOptions(qtch.QChart.AllAnimations)
        self.piechartview = qtch.QChartView(self.piechart)
        self.piechartview.setRenderHint(qtg.QPainter.Antialiasing)


        # selection widget
        
        product_widget = qtw.QGroupBox()
        product_widget.setTitle("Item Selection")
        product_layout = qtw.QHBoxLayout()
        product_widget.setLayout(product_layout)
        
        pushbutton = qtw.QPushButton("Filter",clicked = self.update_piechart)
        self.combobox = qtw.QComboBox(currentText = "select an item") 
        
        self.c = ComboboxModel() #comboxlist model
        self.combobox.setModel(self.c.model)

        product_layout.addWidget(self.combobox) 
        product_layout.addWidget(pushbutton)
        # calendar widget

        calendar_widget = qtw.QGroupBox()
        calendar_widget.setTitle("Date Selection")
        
        calendar_layout = qtw.QHBoxLayout()
        calendar_widget.setLayout(calendar_layout)
        # calculating the current month and current year
        
        current_month = int(datetime.now().month)
        current_year  = int(datetime.now().year)
        
        date = qtc.QDate(current_year,current_month,1)
        
        self.to_date = qtw.QDateEdit()
        to_label = qtw.QLabel("To")
        self.to_date.setCalendarPopup(True)
        
        self.to_date.setDate(date)
        
        self.from_date = qtw.QDateEdit()
        from_label = qtw.QLabel("From")
        self.from_date.setCalendarPopup(True)
        self.from_date.setDate(qtc.QDate.currentDate())
        
        pushbtn = qtw.QPushButton("Filter",clicked =self.update_data)

        
        calendar_layout.addWidget(to_label)
        calendar_layout.addWidget(self.to_date)
        calendar_layout.addWidget(from_label)
        calendar_layout.addWidget(self.from_date)
        calendar_layout.addWidget(pushbtn)
        # end of calendar widget
        
        self.chartview.setSizePolicy(qtw.QSizePolicy.Minimum,qtw.QSizePolicy.Expanding)

        self.piechartview.setSizePolicy(qtw.QSizePolicy.Minimum,qtw.QSizePolicy.Expanding)
        
        grpbxwidgt.layout().addWidget(calendar_widget)
        
        grpbxwidgt.layout().addWidget(self.chartview)
        
        grpbxwidgt.layout().addWidget(product_widget)

        grpbxwidgt.layout().addWidget(self.piechartview)
        self.layout().addWidget(grpbxwidgt)
    
    def update_data(self):
        
        '''
        Updates the data in the graph when the filter is applied.
        '''

        self.series.clear()
        self.pieseries.clear()

        todate =  (self.to_date.date().toString('yyyy-MM-dd'))
        fromdate = (self.from_date.date().toString('yyyy-MM-dd'))

        self.df = pd.read_csv('test.csv')
        self.days = pd.date_range(start= todate,end=fromdate)

        x = [i for i in self.df['Date'] if i in self.days]
        self.temp_list = sorted(list(set(x)))
        
        income =  [sum(self.df.loc[(self.df['Date'] == i) & (self.df['Transaction Type'] == 'Sell'),'Total Price']) for i in self.temp_list] 
        expense = [sum(self.df.loc[(self.df['Date'] == i) & (self.df['Transaction Type'] == 'Buy' ),'Total Price']) for i in self.temp_list]
        
        
        piecount = len(self.c._data)
        item_list = self.c._data
        
        for i in range(piecount):
            item_name = item_list[i]
            item_sold = [sum(self.df.loc[(self.df['Date'] == i ) & (self.df['Transaction Type'] == 'Buy') & (self.df[' Product ']== item_name),
                ' Amount (kg) ']) for i in self.temp_list]
            
            slice_ = qtch.QPieSlice(item_list[i],sum(item_sold))
            self.pieseries.append(slice_)


        categories = self.temp_list  # x axis   
        
        Income = qtch.QBarSet("Income") # dataset in the bar 
        Expense = qtch.QBarSet("Expense") # dateset

        Income.append(income) 
        Expense.append(expense)
        
        self.series.append(Income)      
        self.series.append(Expense)     
        
        self.axis.append(categories)        
    
    def update_piechart(self):

        self.pieseries.clear()

        if self.combobox.currentText():
            self.pieseries.clear()
            item_name = self.combobox.currentText()
            item_sold = [sum(self.df.loc[(self.df['Date'] == i ) & (self.df['Transaction Type'] == 'Sell') & (self.df[' Product ']== item_name),
                ' Amount (kg) ']) for i in self.temp_list] 
            item_bought = [sum(self.df.loc[(self.df['Date'] == i ) & (self.df['Transaction Type'] == 'Buy') & (self.df[' Product ']== item_name),
                ' Amount (kg) ']) for i in self.temp_list]

            slice_s = qtch.QPieSlice(item_name + "sold",sum(item_sold))
            slice_b = qtch.QPieSlice(item_name + "bought",sum(item_bought))
            
            self.pieseries.append(slice_s)
            self.pieseries.append(slice_b)




class OverviewPage(qtw.QWidget):
    '''
    Overview Page shows the data that user need to see "in-a-glance"
    Kinda Like a Dashboard
    '''
    def __init__(self,*args,**kwargs):
        super().__init__()

        self.setLayout(qtw.QVBoxLayout()) # our main layout
        
        days_widget = qtw.QGroupBox()
        days_layout = qtw.QHBoxLayout()
        
        days_widget.setLayout(days_layout)
               
        # greetings
 
        self.greeting = qtw.QLabel("<h1>Welcome!</h1>")
        
        self.layout().addWidget(self.greeting,alignment = qtc.Qt.AlignVCenter | qtc.Qt.AlignHCenter)

        # financial information

        financial_widget = qtw.QGroupBox()


        current_month = int(datetime.now().month)
        current_year  = int(datetime.now().year)
        
        todate = f"{current_year}-{current_month}-{1}"
        fromdate = datetime.now().date()
        df = pd.read_csv('test.csv')
        days = pd.date_range(start= todate,end=fromdate)
        
        x = [i for i in df['Date'] if i in days]
        temp_list = sorted(list(set(x)))
        income =  [sum(df.loc[(df['Date'] == i) & (df['Transaction Type'] == 'Sell'),'Total Price']) for i in temp_list] 
        expense = [sum(df.loc[(df['Date'] == i) & (df['Transaction Type'] == 'Buy' ),'Total Price']) for i in temp_list]
                                        
    
        financial_widget.setTitle(f'''Information For {months[current_month]}''')
        financial_widget.setSizePolicy(qtw.QSizePolicy.Minimum,qtw.QSizePolicy.Fixed)

        financial_layout = qtw.QGridLayout()
        financial_widget.setLayout(financial_layout)
         
        
        income_label = qtw.QLabel('''<b><font color="#336699">Income</b>''')
        expense_label = qtw.QLabel("<b>Expense</b>")
        balance_label = qtw.QLabel("<b>Balance</b>")
        transaction_label = qtw.QLabel("<b>Transaction</b>")
        

        # calculation balance
        balance = sum(income) - sum(expense)
        if balance < 0:
            self.balance = qtw.QLabel(f'''<b><font color="#df1c44">{sum(income)-sum(expense)}</b>''')
        else:
            self.balance = qtw.QLabel(f'''<b><font color="#000000">{sum(income)-sum(expense)}</b>''')

        self.income = qtw.QLabel(f"<b>{sum(income)}</b>")
        self.expense = qtw.QLabel(f"<b>{sum(expense)}</b>")
        self.transaction = qtw.QLabel(f"<b>{len(x)}")
        
        financial_layout.addWidget(income_label,1,0)
        financial_layout.addWidget(self.income,1,1)
        
        financial_layout.addWidget(expense_label,2,0)
        financial_layout.addWidget(self.expense,2,1)
        
        financial_layout.addWidget(balance_label,3,0)
        financial_layout.addWidget(self.balance,3,1)
        
        financial_layout.addWidget(transaction_label,4,0)
        financial_layout.addWidget(self.transaction,4,1)
        

        self.layout().addWidget(financial_widget)
        #self.layout().insertStretch(5,1)
        self.layout().addWidget(ChartWidget())

