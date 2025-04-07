from kivy.config import Config
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from calendar import monthrange
from kivy.properties import ObjectProperty
from kivy.graphics import Rectangle, Color
from math import sqrt
from kivy.clock import Clock
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path
from kivy.core.window import Window
from workalendar.asia import Japan
from datetime import date
from kivy.uix.image import Image

resource_add_path('C:\\Windows\\Fonts')
LabelBase.register(DEFAULT_FONT, 'UDDIGIKYOKASHON-B.TTC')
class Data():
    '''データの保存される部分'''
    year = 2001
    month = 10
    length = 1

    def set_year(self, year):
        self.year = year

    def set_month(self, month):
        self.month = month

    def set_length(self, length):
        self.length = length

class StartWindow(Screen):
    pass

class MonthNumWindow(Screen):
    '''何月の部分のカレンダー作りますかの月の数'''
    data_instance = ObjectProperty()

    def __init__(self, **kwargs):
        super(MonthNumWindow, self).__init__(**kwargs)
        if self.data_instance is None:
            self.data_instance = MyMainApp.get_running_app().data_instance

    def drpdown_(self):
        self.menu_list=[
            {
                "viewclass":"OneLineListItem",
                "text": "1",
                "on_release": lambda x ="1":self.test1()
            },
            {
                "viewclass":"OneLineListItem",
                "text": "2",
                "on_release": lambda x ="2":self.test2()
            },
            {
                "viewclass":"OneLineListItem",
                "text": "3",
                "on_release": lambda x ="3":self.test3()
            },
            {
                "viewclass":"OneLineListItem",
                "text": "4",
                "on_release": lambda x ="4":self.test4()
            },
            {
                "viewclass":"OneLineListItem",
                "text": "5",
                "on_release": lambda x ="5":self.test5()
            },
            {
                "viewclass":"OneLineListItem",
                "text": "6",
                "on_release": lambda x ="6":self.test6()
            },
            {
                "viewclass":"OneLineListItem",
                "text": "7",
                "on_release": lambda x ="7":self.test7()
            },
            {
                "viewclass":"OneLineListItem",
                "text": "8",
                "on_release": lambda x ="8":self.test8()
            },
            {
                "viewclass":"OneLineListItem",
                "text": "9",
                "on_release": lambda x ="9":self.test9()
            },
            {
                "viewclass":"OneLineListItem",
                "text": "10",
                "on_release": lambda x ="10":self.test10()
            },
            {
                "viewclass":"OneLineListItem",
                "text": "11",
                "on_release": lambda x ="11":self.test11()
            },
            {
                "viewclass":"OneLineListItem",
                "text": "12",
                "on_release": lambda x ="12":self.test12()
            }

        ]
        self.menu = MDDropdownMenu(
            caller = self.ids.menu_,
            items = self.menu_list,
            width_mult =2
        )
        self.menu.open()

    def test1(self):
        print("test1 is pressed")
        self.data_instance.set_length(int(1))
        self.ids.menu_.text = str(1)

    def test2(self):
        print("test2 is pressed")
        self.data_instance.set_length(int(2))
        self.ids.menu_.text = str(2)
    
    def test3(self):
        print("test3 is pressed")
        self.data_instance.set_length(int(3))
        self.ids.menu_.text = str(3)
    
    def test4(self):
        print("test4 is pressed")
        self.data_instance.set_length(int(4))
        self.ids.menu_.text = str(4)

    def test5(self):
        print("test5 is pressed")
        self.data_instance.set_length(int(5))
        self.ids.menu_.text = str(5)

    def test6(self):
        print("test6 is pressed")
        self.data_instance.set_length(int(6))
        self.ids.menu_.text = str(6)
    
    def test7(self):
        print("test7 is pressed")
        self.data_instance.set_length(int(7))
        self.ids.menu_.text = str(7)
    
    def test8(self):
        print("test8 is pressed")
        self.data_instance.set_length(int(8))
        self.ids.menu_.text = str(8)

    def test9(self):
        print("test9 is pressed")
        self.data_instance.set_length(int(9))
        self.ids.menu_.text = str(9)

    def test10(self):
        print("test10 is pressed")
        self.data_instance.set_length(int(10))
        self.ids.menu_.text = str(10)

    def test11(self):
        print("test11 is pressed")
        self.data_instance.set_length(int(11))
        self.ids.menu_.text = str(11)

    def test12(self):
        print("test12 is pressed")
        self.data_instance.set_length(int(12))
        self.ids.menu_.text = str(12)

class StartMonthWindow(Screen):
    '''何年の何月から始めるかのデータをとる'''
    data_instance = ObjectProperty()

    def __init__(self, **kwargs):
        super(StartMonthWindow, self).__init__(**kwargs)
        if self.data_instance is None:
            self.data_instance = MyMainApp.get_running_app().data_instance


    def on_save(self, instance, value, date_range):
        self.ids.calBtn.text = str(value)
        self.data_instance.set_year( value.year) 
        self.data_instance.set_month( value.month) 

    def on_cancel(self, instance, value):
        print(instance, value)

    def show_date_picker(self):
        date_dialog = MDDatePicker(min_year=2024, max_year=2030)
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

class ExampleOfGridLayout(GridLayout):
    '''カレンダーを作成する部分'''
    data_instance = ObjectProperty()
    def __init__(self, **kwargs):
        super(ExampleOfGridLayout, self).__init__(**kwargs)
        if self.data_instance is None:
            self.data_instance = MyMainApp.get_running_app().data_instance
        self.cols = 7
        self.pos_hint = {'center_x': 0.5, 'top': 0.9}
        self.update_month()

    def update_month(self):
        self.clear_widgets()
        self.holidays = self.get_japanese_holidays(self.data_instance.year)
        start_day = monthrange(self.data_instance.year, self.data_instance.month)[0]
        length = monthrange(self.data_instance.year, self.data_instance.month)[1]
       
        
        self.add_widget(Label(text="日", color=(0, 0, 0, 1)))
        self.add_widget(Label(text="月", color=(0, 0, 0, 1)))
        self.add_widget(Label(text="火", color=(0, 0, 0, 1)))
        self.add_widget(Label(text="水", color=(0, 0, 0, 1)))
        self.add_widget(Label(text="木", color=(0, 0, 0, 1)))
        self.add_widget(Label(text="金", color=(0, 0, 0, 1)))
        self.add_widget(Label(text="土", color=(0, 0, 0, 1)))
        self.count = 0
        for i in range(0, start_day + 1):
            self.count += 1
            self.add_widget(self.make_label(-1))

        for i in range(1, length + 1):
            self.add_widget(self.make_label(i))
        
    def make_label(self, day):
        holiday_color = (1, 0, 0, 1)  # Red color for holidays
        saturday = 7 - self.count
        sunday = (saturday + 1) % 7

        if day == -1:
            return Label(text=" ", color=(0, 0, 0, 1))

        if 1 <= day <= monthrange(self.data_instance.year, self.data_instance.month)[1]:
            current_date = date(self.data_instance.year, self.data_instance.month, day)
            for holiday_date, _ in self.holidays:
                if holiday_date.year == current_date.year and holiday_date.month == current_date.month and holiday_date.day == current_date.day:
                    return Label(text="{}".format(day), color=holiday_color)

            if day % 7 == saturday:
                return Label(text="{}".format(day), color=(0, 0, 1, 1))

            elif day % 7 == sunday:
                return Label(text="{}".format(day), color=(1, 0, 0, 1))
            else:
                return Label(text="{}".format(day), color=(0, 0, 0, 1))
            # If day is not within the valid range, return an empty label
        return Label(text=" ", color=(0, 0, 0, 1))
        
        
  

    def get_japanese_holidays(self, year):
        cal = Japan()
        self.holidays = cal.holidays(year)
        return self.holidays
             
class CanvasWidget(GridLayout):
    def __init__(self, canvas_text, **kwargs):
        super(CanvasWidget, self).__init__(**kwargs)
        self.cols=1
        with self.canvas:
            Color(0.95, 0.95, 0.95, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
            self.bind(pos=self.update_rect, size=self.update_rect)
            

        label_text_year = canvas_text
        ex=ExampleOfGridLayout()
        self.label = Label(text=label_text_year, color=(0, 0, 0, 1), size_hint=(0.5, 0.2))
        self.add_widget(self.label)
        self.add_widget(ex)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.width, self.height

class Combine(BoxLayout):
    data_instance = ObjectProperty()
    example_grid_layout = ObjectProperty()
    canvas_layout = ObjectProperty()

    def __init__(self, **kwargs):
        super(Combine, self).__init__(**kwargs)
        self.width='620sp'
        self.height=self.width*sqrt(2)
        self.orientation='vertical'
        self.padding='25sp'
        with self.canvas: 
            Color(1, 1, 1, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
            self.bind(pos=self.update_rect, size=self.update_rect)
        if self.data_instance is None:
            self.data_instance = MyMainApp.get_running_app().data_instance
        self.example_grid_layout = ExampleOfGridLayout()
        

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.width, self.width

    def settei_of_month(self):
        self.clear_widgets()
        self.canvas_layout = GridLayout(cols = 3, size_hint=(0.8, 0.6), spacing=(10), padding='20sp')
        self.add_widget(Label(text=""))
        lengthofMonth=self.data_instance.length
        monthly=self.data_instance.month
        yearly=self.data_instance.year
        if lengthofMonth>=10:
            self.canvas_layout.cols=4
        elif lengthofMonth==4:
            self.canvas_layout.cols=2
            self.canvas_layout.size_hint=(0.85, 0.8)
        elif lengthofMonth==1:
            self.canvas_layout.cols=1
            self.canvas_layout.size_hint=(0.85, 0.4)

        if lengthofMonth==2 or lengthofMonth==3:
            self.canvas_layout.size_hint=(0.95, 0.3)
        elif lengthofMonth<7:
            self.canvas_layout.size_hint=(1, 0.6)
        elif lengthofMonth<13:
            self.canvas_layout.size_hint=(1, 0.9)
        for i in range(lengthofMonth):
            self.example_grid_layout.update_month()
            canvas_text="{}           {} ".format(yearly, monthly)
            canvas_widget = CanvasWidget(canvas_text=canvas_text)
            self.canvas_layout.add_widget(canvas_widget)
            monthly+=1
            if monthly >12:
                monthly=1
                yearly+=1
            self.data_instance.set_year(yearly)
            self.data_instance.set_month(monthly) 
        
        self.add_widget(self.canvas_layout)
        # Schedule the export after the rendering is complete
        Clock.schedule_once(lambda dt: self.save_as_picture(), 0.1)
        

    def save_as_picture(self):
        # Save the image
        filename = "{}_{}_{}".format(self.data_instance.year, self.data_instance.month, self.data_instance.length)
        self.export_to_png('.\\outputImage\\output_image_{}.png'.format(filename))
class addTemplate(Screen):
    data_instance = ObjectProperty()
    combine = ObjectProperty()
    def __init__(self, **kwargs):
        super(addTemplate, self).__init__(**kwargs)
        self.state = 0
        self.combine = Combine()
        if self.data_instance is None:
            self.data_instance = MyMainApp.get_running_app().data_instance
       
        self.overlayimg = None  # Initialize overlayimg attribute
        

    def btn1(self):
        self.combine.settei_of_month()
        self.filename = ".\\outputImage\\output_image_{}_{}_{}.png".format(
            self.data_instance.year, self.data_instance.month, self.data_instance.length
        )
        layout = FloatLayout(size=(620, 620 * sqrt(2)))

        if self.state ==1:
            overlaypath='.\\base\\A4-base.png'
        elif self.state ==2:
            overlaypath='.\\base\\animal2-3month.png'
        elif self.state ==3:
            overlaypath='.\\base\\bird-6month.png'
        elif self.state ==4:
            overlaypath='.\\base\\flower-3month.png'
        elif self.state ==5:
            overlaypath='.\\base\\pag-6month.png'
        elif self.state ==6:
            overlaypath='.\\base\\state6.png'
        
        Clock.schedule_once(lambda dt: self.load_base_image(layout), 0.2)
        Clock.schedule_once(lambda dt: self.load_overlay_image(layout, overlaypath), 0.5)
        Clock.schedule_once(lambda dt: self.save_as_picture( layout), 1.0)

    def load_base_image(self, layout):
        # Load the base image after 1 second
        self.img = Image(source=self.filename)
        self.img.allow_stretch = True
        self.img.size_hint = (1, 1)
        layout.add_widget(self.img)

    def load_overlay_image(self, layout, filename):
        self.overlayimg = Image(source=filename)
        self.overlayimg.allow_stretch = True

        if self.state==5:
            base_source='.\\base\\base-pag.PNG'
            self.base_ue=Image(source='.\\base\\pag-6month-ue.png')
            self.base_ue.pos_hint={'center_x': 0.5, 'center_y': 0.92}
            layout.add_widget(self.base_ue)
        else :
            base_source='.\\base\\base.png'
        self.base=Image(source=base_source)    
        self.base.pos_hint={'center_x': 0.5, 'center_y': 0.02}
        layout.add_widget(self.base)

        if self.data_instance.length==1:
            self.overlayimg.pos_hint = {'center_x': 0.5, 'center_y': 0.55}
        elif self.data_instance.length < 4:
            self.overlayimg.pos_hint = {'center_x': 0.5, 'center_y': 0.40}
        elif self.data_instance.length < 7:
            self.overlayimg.pos_hint = {'center_x': 0.5, 'center_y': 0.55}
        else:
            self.overlayimg.pos_hint = {'center_x': 0.5, 'center_y': 0.65}
        self.overlayimg.size_hint = (1, 1)
        layout.add_widget(self.overlayimg)
        
    def save_as_picture(self, layout):
        filename = "{}_{}_{}".format(self.data_instance.year, self.data_instance.month, self.data_instance.length)
        layout.export_to_png('.\\template\\output_image_{}.png'.format(filename))
    
class PreviewWindow(Screen):
    
    data_instance = ObjectProperty()
    combine = ObjectProperty()

    def __init__(self, **kwargs):
        super(PreviewWindow, self).__init__(**kwargs)
        
        if self.data_instance is None:
            self.data_instance = MyMainApp.get_running_app().data_instance
        self.example_grid_layout = ExampleOfGridLayout()
        self.combine = Combine()
        

       
    def settei_of_month(self):
        image_widget = self.ids.preview_image
        image_widget.source=''
        Clock.schedule_once(lambda dt: self.imgSource(image_widget), 1.5)

    def imgSource(self, image_widget):
        image_widget.source = '.\\template\\output_image_{}_{}_{}.png'.format(self.data_instance.year, self.data_instance.month, self.data_instance.length)     
       
class DrawingFile(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class MyMainApp(MDApp, App):
    def __init__(self, **kwargs):
        super(MyMainApp, self).__init__(**kwargs)
        self.data_instance = Data()
        self.title='オリジナルカレ'

    def build(self):
        desired_width = 1000
        desired_height = 750
        Window.size = (desired_width, desired_height)
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"

        return Builder.load_file("calendar1208.kv")        

if __name__ == '__main__':
    MyMainApp().run()