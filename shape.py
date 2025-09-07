from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivymd.uix.screen import Screen
from kivy.uix.popup import Popup

from kivy.core.window import Window
from kivymd.uix.button import MDIconButton , MDFillRoundFlatIconButton, MDFillRoundFlatButton, MDRaisedButton
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import MDList,OneLineListItem, OneLineIconListItem
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDIcon
from kivy.uix.image import Image
from kivymd.uix.label import MDLabel
from kivy.uix.label import Label
from kivymd.uix.dialog import MDDialog
from kivy.clock import Clock
import os
import sys
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.card import MDCard
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.scrollview import MDScrollView
Window.size=(400 , 600)





Builder.load_string("""
      
      
      
<Main>:
      
    Image:
        source:'img_file//main2.jpeg' 
        allow_stretch: True
        keep_ratio: False
        size_hint: 1,1
                    
<Maincom>:
   
    BoxLayout:
        orientation: 'vertical'
        spacing: 2
        
   
        Image:
            source: 'img_file//sane.jpeg'
            size_hint: None , None
            size: 400, 330
            size_hint_y: 0.9
            
            
          
           
     
        MDCard:
            size_hint: None , None
            size: 250 , 300
            md_bg_color: '#c88236'
            pos_hint: {'x': 0.18}
            elevation: 3
            BoxLayout:
                orientation: 'vertical'
                spacing: 10
                MDIcon:
                    icon: 'account-circle-outline'
                    pos_hint: {'x': 0.4}
                    font_size: 60
                    
                MDLabel:
                    text: 'Login'
                    font_style: 'H6'
                    pos_hint: {'x': 0.4}
                
                    
                MDTextField:
                    id: my_text_inp1
                    hint_text: 'Enter gmali'
                    mode: 'round'
                    size_hint_x: 0.8
                    pos_hint: {'x': 0.1, 'y': 0.5}
                    

                    multiline: False
               
                
                MDTextField:
                    id: my_text_inp2
                    hint_text: 'Enter Password:'
                    mode: 'round'
                    size_hint_x: 0.8
                    pos_hint: {'x': 0.1}
                    password: True
                    password_mask: '*'

                MDFillRoundFlatButton:
                    id: buttn
                    text: 'Login'
                    size_hint_x: 0.8
                    pos_hint: {'x': 0.1}
                    on_release:
                     
                     
                        app.root.current = "Apple" if my_text_inp1.text != "" or my_text_inp2.text != "" else root.eroor()
                        
                        
                            
                    
                    
                    
                MDLabel:
                    id: label_erorr
                    text: ''
                    pos_hint: {'x': 0.1}
                    color: 'red'
                    font_size: 13
                   
                BoxLayout:
            
            
            
            
            
                   
        BoxLayout:
            size_hint: 0.5 , 0.5
        

             
    
            
        

       
                    
                    
<Apple>:  
     
    Screen:
        MDLabel:
            text : "Go to marketing"
            font_size: 20
            pos_hint: {"center_x": 0.53, "center_y": 0.35}
            size_hint: 0.5 , 0.5
            theme_text_color:"Custom"
            text_color: '#0c8ea7'
        MDIcon:
            icon: "shopping-outline"
            pos_hint: {"center_x": 0.71, "center_y": 0.35}
            size_hint: 0.7 , 0.5        
            theme_text_color: 'Custom'
            text_color: "#0c8ea7"
                
            
            
            
        MDIconButton:
            icon: "google-play"
            pos_hint: {"x": 0.37, "y": 0.45}
            icon_size: 70
            md_bg_color: "orange"
            theme_text_color:"Custom"
            text_color: '#0c8ea7'
           
            on_release: root.goto_main()
          
            
         
            
# شاشه رائيسي بعد الدخول

<MainScreen>:
      
    
    MDScrollView:
        id: container     
        y: self.parent.height - self.height - 52
        
       
         
        
        
        BoxLayout:
            orientation: 'vertical'
            height: 990
            size_hint_y: None
            height:self.minimum_height
            
            
            Image:
                source: 'img_file//trw.jpg'
                size_hint: None , None
                size:380 , 250
                pos_hint: {'x': 0.02}
                
                
            MDCard:
                md_bg_color: 'grey'
                size_hint:  None , None
                size: 380 ,90
                pos_hint: {'x':0.02}
                
                BoxLayout:
                    orientation: 'vertical'
                
                    
                    BoxLayout:
                        orientation: 'horizontal'
                        BoxLayout:
                            orientation: 'vertical'
      
                            MDIconButton:
                                id: butn
                                icon: 'shopping'
                                icon_size: 40
                            
                                theme_text_color: "Custom"
                                text_color: '#013d85'
                                on_release: root.goto_shapeng()
                            
                            MDLabel:
                                text: 'shapi'
                                font_size: 15
                                padding: 12
                                
                            
                                
                                
                        BoxLayout:
                            orientation: 'vertical'        
                                    
                        
                            MDIconButton:
                                icon: 'store-marker'
                                icon_size: 40
                                theme_text_color:'Custom'
                                text_color: '#c82a00' 
                                on_release: root.gotoposmarc()
                                
                            MDLabel:
                                text: 'posmark'
                                font_size: 15
                           
                          
                  
                        BoxLayout:
                            orientation: 'vertical'         
                
                            MDIconButton:
                                icon: 'credit-card'
                                icon_size: 40
                                theme_text_color:'Custom'
                                text_color: '#000000'   
                                on_release: root.goto_card() 
                            MDLabel:
                                text: 'Card'
                                font_size: 15
                                padding: 14
                                
                           
                        BoxLayout:
                            orientation: 'vertical'     
                
                            MDIconButton:
                                icon: 'truck'
                                icon_size: 40
                                theme_text_color:'Custom'
                                text_color: '#003689'
                                on_release: root.goto_rets()  
                            MDLabel:
                                text: 'Rets'
                                font_size: 15
                                padding: 14
                                
                            
                                
                        BoxLayout:
                            orientation: 'vertical'  
                
                            MDIconButton:
                                icon: 'bookmark'
                                icon_size: 40
                                theme_text_color:'Custom'
                                text_color: '#a36528'   
                                on_release:root.goto_arves()
                                        
                            MDLabel:
                                text: 'Arves'
                                font_size: 15
                                padding: 12
                                    
                    
                        BoxLayout:
                            orientation: 'vertical'  
                
                            MDIconButton:
                                icon: 'account'
                                
                                icon_size: 35
                                theme_text_color:'Custom'
                                text_color: '#ad7b48'  
                                on_release: root.goto_peon()
                                
                            MDLabel:
                                text: 'peon'
                                font_size: 15
                                padding: 14
                        
                        
                    
                            
                                
            Image:
                source: 'img_file//sane.png'  
                size_hint: None , None
                size:380 , 250
                pos_hint: {'x': 0.02}
            
            
                
            Image:
                source: 'img_file//mintw.jpg'  
                size_hint: None , None
                size:380 , 250
                pos_hint: {'x': 0.02}
                
                
            Image:
                source: 'img_file//selt.png'      
                size_hint: None , None
                size:380 , 250
                pos_hint: {'x': 0.02}
                
                  
                        
            Image:
                source: 'img_file//must.jpg'      
                size_hint: None , None
                size:380 , 250
                pos_hint: {'x': 0.02}
                
                  
                        
    MDTopAppBar:
        pos_hint: {'top': 1} 
        height: 56
        title: 'Shapeng Marcitng'
        left_action_items: [["arrow-left", lambda x: root.goto_apple()]]
        right_action_items:[["cog-outline", lambda x: nav_drawer.set_state("open")]]
   
    MDNavigationDrawer:
        id: nav_drawer
        radius: [0,20,20,0]
        BoxLayout:
            spacing: 1
            padding: 10
            orientation: "vertical"
            rows: None
            pos_hint: {'y': -0.05}
            
            Image:
                source: 'img_file//nav.png'
                size_hint: None , None
                size: 270 , 200
            
            Image:
                source: 'img_file//nav2.png'
                size_hint: None , None
                size: 270 ,200
            
            Image:
                source: 'img_file//nav3.png'
                size_hint: None , None
                size: 270 ,200
            
       
                
                
                

                
<Shapeng>:
    MDCard:
        size_hint: None , None
        size: 320 ,33
        md_bg_color: "orange"
        pos_hint: {"x": 0.1,"y": 0.94}
        
        
    MDIconButton:
        icon: "arrow-left"
        pos_hint: {"x": 0.1,"y": 0.93}
        on_release: root.goto_qsm_mntj()
        
    MDIconButton:
        icon: "magnify"
        pos_hint: {"x": 0.8,"y": 0.93}
        
        

    ScrollView: 
        y: self.parent.height - self.height -40
        
        GridLayout:
            cols: 2
            rows: 12
            size_hint_y: None
            spacing: 15, 20
            padding: 42 , 20
            height: self.minimum_height
    #======================================1
            Image:
                id: img1
                source:"img_munt//suuf.png"
                size_hint: None, None
                size: 150,150
          
                
            Image:
                id: img2
                source:"img_munt//put.png"
                radius: [20,]
                size_hint: None, None
                size: 150,150
                    
                    
          
                
            MDLabel:
                id: lab1
                text:'Tish $ 20'
                font_style: 'Subtitle1'
                text_color: (0,0,0,1)
                padding: 40
                
                    
            MDLabel:
                text:'Putt $50'
                font_style: 'Subtitle1'
                text_color: (0,0,0,1)
                padding: 40
                
                
            MDFillRoundFlatIconButton:
                id: butonmun1
                text: 'Boys'
                disabled: False
                size_hint: 0.3 , 0.1
                md_bg_color: 'orange'
                on_press: root.munt1()
                
                
                
                
                
            MDFillRoundFlatIconButton:
                text: 'Boys'
                size_hint: 0.3 , 0.1
                md_bg_color: 'orange'
                on_press: root.munt2()
                
                
    #=====================================  2   
            
            Image:
                id: img3
                source:"img_munt//shhata.png"
                size_hint: None, None
                size: 150,150
          
                
            Image:
                id: img4
                source:"img_munt//saa.png"
                radius: [20,]
                size_hint: None, None
                size: 150,150 
                
                
            MDLabel:
                text:'Shaf $ 10'
                font_style: 'Subtitle1'
                text_color: (0,0,0,1)
                padding: 40
                    
            MDLabel:
                text:'Bag $ 66'
                font_style: 'Subtitle1'
                text_color: (0,0,0,1)
                padding: 40
            MDFillRoundFlatIconButton:
                text: 'Boys'
                size_hint: 0.3 , 0.1
                md_bg_color: 'orange'
                on_press: root.munt3()
                
            MDFillRoundFlatIconButton:
                text: 'Boys'
                size_hint: 0.3 , 0.1
                md_bg_color: 'orange'
                on_press: root.munt4()
                
                
        # =============================3
            
            Image:
                id: img5
                source:"img_munt//comp.png"
                size_hint: None, None
                size: 150,150
          
                
            Image:
                id: img6
                source:"img_munt//het.png"
                radius: [20,]
                size_hint: None, None
                size: 150,150 
                
                
            MDLabel:
                text:'Shafq $ 750.0'
                font_style: 'Subtitle1'
                text_color: (0,0,0,1)
                padding: 40
                    
            MDLabel:
                text:'Bag $ 66'
                font_style: 'Subtitle1'
                text_color: (0,0,0,1)
                padding: 40
            MDFillRoundFlatIconButton:
                text: 'Boys'
                size_hint: 0.3 , 0.1
                md_bg_color: 'orange'
                on_press: root.munt5()
                
            MDFillRoundFlatIconButton:
                text: 'Boys'
                size_hint: 0.3 , 0.1
                md_bg_color: 'orange'
                on_press: root.munt6()
                
                
        #====================================4
            
          
                        
                    
<Posmarc>:
    canvas:
        Rectangle:
            source: 'img_munt//counpos.png'
            size: self.size
    BoxLayout:
        orientation: 'vertical'
        MDIconButton:
            icon: 'arrow-left'
            on_release: root.goto_gsm_mn()
            theme_text_color: 'Custom'
            text_color: '#fefefe'
        
            
        Image:
            source: 'img_munt//pos_mar.png'
            size_hint: None, None
            size: 430 , 250
            pos_hint: {'x': -0.03 , 'y': 0.2}
        BoxLayout:   
            
        Image:
            source: 'img_munt//pos_mar2.png'  
            size_hint: None , None
            size: 400, 230    
        BoxLayout:        
          
                
        
        
<Card>: 

    BoxLayout:
        orientation: 'vertical'
        
        BoxLayout:
            size_hint: 0.1 , 0.3
        MDIconButton:
            icon: 'arrow-left'
            on_release: root.goto_gs_mnt()
            

                
        MDCard:
            size_hint: None ,None
            size: 350 , 125
            md_bg_color: "orange"
            pos_hint: {'x': 0.06, 'y': 0.3}
            GridLayout:
                cols: 2
                rows: 2
                spacing: 5
                col_default_width: 20
                
            

                MDLabel:
                    text: 'Cride Card'
                    font_size: 17
                    padding: 40
                            
                            
                MDCheckbox:
                    id: chace1
                    pos_hint: {'x': 0.2}
                    padding: 20
                    ripple_scale: 0
                    scale: 0.2
                    on_active: chace2.active = False if self.active else True
                
                    
                MDLabel:
                    text: 'Debt Card'
                    
                    padding: 40
                    font_size: 17
                    
                    
                        
                MDCheckbox:
                    id: chace2
                    pos: 100 , 100
                    ripple_scale: 0
                    scale: 0.2
                    on_active: chace1.active = False if self.active else True
                    

            
            
          
        
            
        
        MDLabel:
            text: 'Enter Number Carding and password Criding'
            padding: 40
            pos_hint: {'y': -0.2}
            color: (0.5,0.5,0.5,1)
            
        MDTextField:
            id: fiel1
            text: 'MM/YY'    
            pos_hint: {'x': 0.08, 'y': 0.5}
            mode: 'round'
            size_hint: 0.84 , 0.0
            
        GridLayout:
            cols: 2
            padding: 33
            spacing: 25
            size_hint_x: 0.99
            
            
            
                       
    
            MDTextField:
                id: fiel2
                text: 'CVC'   
                mode: 'round'
                size_hint_x: 0.5
            
                
            MDTextField:
                id: fiel3
                text: 'pass'    
                
                mode: 'round'
                size_hint_x: 0.6
                
                
        MDFillRoundFlatButton:
            text: 'Login'
            size_hint_x: 0.83
            md_bg_color: 'orange'
            
            pos_hint: {'x': 0.08}
            on_release: 
                root.popupd() if fiel1.text == 'ccyy' and fiel2.text == 'ccvv' and fiel3.text == '12345' else root.eroorno()
                    

            
        BoxLayout:

            
            
<Rets>:        
    MDTopAppBar:
        id: topapp
        pos_hint: {'top': 1}
        
        title: 'Delivery orders section'
        left_action_items: [["arrow-left", lambda x: root.goto_app()]]


    BoxLayout:
        orientation: 'vertical'
        height: 990
        size_hint_y: None
        height:self.minimum_height
            
    MDLabel:
        id: labnonerets
        text: 'None Requests'
        pos_hint: {'x': 0.35}
    MDIconButton:
        icon: 'plus-circle'
        pos_hint: {'x': 0.8 , 'y': 0.1}
        icon_size: 35
        on_press: root.goto_shaping()

        
     
<Arves>: # قسم المحفوضات
    MDTopAppBar:
        pos_hint: {'top': 1}
        title: 'Arvese'
        left_action_items: [['arrow-left', lambda x: root.goto_app_in_Arves()]]
        right_action_items:[['progress-alert', lambda x: root.pop()]]
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: 'None Arves'
            pos_hint:{'x': 0.38}


<peon>:

                
                
                
                

                        
                

     
            
    
# المنتجات قسم الشرائ     
<Mntaj1>:

             
                                                                                  
                                                                                                                                                                                                                                                                                              
            
    
        
       
       
""")
class Mntaj1(Screen):
    pass



class Peon(Screen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.my_dialog= None

        self.layout6=BoxLayout(orientation='vertical',spacing=5)
        self.ico=MDIconButton(icon='arrow-left')
        self.ico.bind(on_release=self.goto_msr_in_peon)
        self.img=Image(source='img_file//log.png')
        self.label=MDLabel(text='', pos_hint={'x':0.25},size_hint_y=0.5)
        self.label2=MDLabel(text='',pos_hint={'x':0.25},size_hint_y=0.1)
        self.layout_down=BoxLayout(size_hint=(0.5, 0.99))
        self.butt=MDIconButton(icon='logout', pos_hint={'x': 0.05,'y': 0.1}, theme_text_color='Custom',text_color=(1,0,0,1),on_release=self.on_dealog)
        self.labext=MDLabel(text='logout', pos_hint={'x': 0.05, 'y': 0.2}, size_hint=(0.2, 0.3), theme_text_color='Custom',text_color=(1,0,0,1))
        
        
        
        self.layout6.add_widget(self.ico)
        self.layout6.add_widget(self.img)
        self.layout6.add_widget(self.label)
        self.layout6.add_widget(self.label2)
        self.layout6.add_widget(self.layout_down)
        self.layout6.add_widget(self.butt)
        self.layout6.add_widget(self.labext)
        
        self.add_widget(self.layout6)
        
        
        
        
        
    def close_app(self, instance):  #dialog اغلاق تطبيق من xx
        MDApp.get_running_app().stop()
        
        
    #def run_app(self, dt):   اعاده تشغيل تبيق بعد اغلاق قيد التطوير XX
        #os.execv(sys.executable, ['python'] + sys.argv)    
    
        
    def off_dialog(self, instance): # dialog اغلاق dialog من  xx
        self.my_dialog.dismiss()
        
        
        
    def on_dealog(self, instance):
        
        self.my_dialog=MDDialog(title='Do you want to close the application?',text='Do you want to log out of the program?',
                            buttons=[MDRaisedButton(text='Cancel', on_press=self.off_dialog),
                                     MDRaisedButton(text='Ok',md_bg_color=('red'),on_press=self.close_app)])
        self.my_dialog.open()
        
        
            
        
        
        

        
        
        
        
        
    def goto_msr_in_peon(self, instance):
        self.manager.current= 'MainScreen'
        
        


class Arves(Screen):
    def goto_app_in_Arves(self): # استدعاء قسم اللرائيسي مستقل مع كلاسس
        self.manager.current= "MainScreen"
        
    def goto_qsm_munt(self, instance): # استدعاء قسم المنتجات  غير مستقل
        self.manager.current='Shapeng'
        self.popup.dismiss()
        
        
        
    def pop(self):
        self.layout5=BoxLayout(orientation='vertical')
        self.labe=Label(text= "There are no archives \nTo save any likes you can add the seve button ",pos_hint={'x': 0.01},font_size=13)
        self.butt=MDRaisedButton(text="OK", pos_hint={'x': 0.38})
        self.butt.bind(on_release=self.goto_qsm_munt)
        
        self.layout5.add_widget(self.labe)    
        
        self.layout5.add_widget(self.butt)    
        
        self.popup=Popup(title='Progres in seve',size_hint=(0.7, 0.3),
                    content=self.layout5)
        self.popup.open()
        
        
        
        
        
        


class Rets(Screen):
    def __init__(self, **kwargs):
        super(Rets, self).__init__(**kwargs)

        self.main_layout= GridLayout(rows=6, cols=1, padding=20)
        self.orientation= 'landscape'

        self.add_widget(self.main_layout)

       
    dialog1=None
    dialog2=None
    dialog3=None
    dialog4=None
    dialog5=None
    dialog6=None
    
    
    def goto_shaping(self):
        self.manager.current = "Shapeng"
         
    
    box_joker=GridLayout(rows=15, cols=1) 
        
    # شراؤ اوال منتج وادخال بياناتك 
    def paying1(self):
        self.box_up1=BoxLayout()
        
        self.layout_munt1=BoxLayout(orientation='vertical',spacing=20)
        self.text_name1=MDTextField(hint_text='Enter Your Name:',mode='round')
        self.text_nmber1=MDTextField(hint_text='Enter your Number:',mode='round')
        self.text_place1=MDTextField(hint_text=f'Enter your Place / from',mode='round')
        self.box_down1=BoxLayout()
        self.boot1=MDFillRoundFlatIconButton(text='Paying',pos_hint={'x': 0.35})
        self.boot1.bind(on_press=self.rets_munton)
       
        
        self.layout_munt1.add_widget(self.box_up1)
        self.layout_munt1.add_widget(self.text_name1)
        self.layout_munt1.add_widget(self.text_nmber1)
        self.layout_munt1.add_widget(self.text_place1) 
        
        self.layout_munt1.add_widget(self.box_down1)
        
        self.layout_munt1.add_widget(self.boot1)
        
     
        
        self.popup1=Popup(title='Booking Fill in the fields',size_hint=(0.7, 0.6),
                    content=self.layout_munt1)
        self.popup1.open()
      
      
     # بعد الشراء اضهار صوره منتج ومده الوصول اليك وسعر    
    def rets_munton(self, instance):
       
        self.hor_munt1=24
        self.ids.labnonerets.text = ''
        self.popup1.dismiss()
 
        
        self.layout1=BoxLayout(orientation='horizontal',pos_hint={'x': 0.05, 'y': 0.05},spacing=15)
    
        
        self.img_1=Image(source='img_munt//suuf.png',size_hint=(None, None), size=(65 , 60))
        self.label1=MDLabel(text=f'{self.text_name1.text} \ {self.text_nmber1.text} \ {self.text_place1.text}',size_hint=(0.05, 0.05))
        self.icobut=MDIconButton(icon='delete-circle-outline',pos_hint={'x': -0.3, 'y': 0.01}, theme_text_color='Custom',text_color=(1,0,0,1),on_press=self.on_dialog1)
        
        self.boxlef=BoxLayout(size_hint=(0.01, 0.5))
        self.layout1.add_widget(self.img_1)
        self.layout1.add_widget(self.label1)
        self.layout1.add_widget(self.icobut)
        self.layout1.add_widget(self.boxlef)
        

        self.main_layout.add_widget(self.layout1)
        
        
        
        
        
    def on_dialog1(self, instance):
      
        self.dialog1=MDDialog(title='Do you want to cancel the order?',
                        buttons=[MDRaisedButton(text='Cansle',on_press=self.off_dialog1),MDRaisedButton(text='Ok',md_bg_color='red',on_press=self.delet_munt1)])
        self.dialog1.open()
            
    def off_dialog1(self,instance):
        self.dialog1.dismiss()  
    
    def delet_munt1(self, *args):
        self.layout1.clear_widgets()
        self.dialog1.dismiss()  
        self.ids.labnonerets.text = 'None not in Rets'
        
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''===========================================''''''''''''''''''''''
  
    def paying2(self):
        self.box_up2=BoxLayout()
        
        self.layout_munt2=BoxLayout(orientation='vertical',spacing=20)
        self.text_name2=MDTextField(hint_text='Enter Your Name:',mode='round')
        self.text_nmber2=MDTextField(hint_text='Enter your Number:',mode='round')
        self.text_place2=MDTextField(hint_text=f'Enter your Place / from',mode='round')
        self.box_down2=BoxLayout()
        self.boot2=MDFillRoundFlatIconButton(text='Paying',pos_hint={'x': 0.35},on_press=self.rets_munt2)
        
        self.layout_munt2.add_widget(self.box_up2)
        self.layout_munt2.add_widget(self.text_name2)
        self.layout_munt2.add_widget(self.text_nmber2)
        self.layout_munt2.add_widget(self.text_place2) 
        
        self.layout_munt2.add_widget(self.box_down2)
        
        self.layout_munt2.add_widget(self.boot2)
        
     
        
        self.popup2=Popup(title='Booking Fill in the fields',size_hint=(0.7, 0.6),
                    content=self.layout_munt2)
        self.popup2.open()
      
      
     # بعد الشراء اضهار صوره منتج ومده الوصول اليك وسعر    
    def rets_munt2(self, instance):
       
        self.hor_munt2=24
        self.ids.labnonerets.text = ''
        self.popup2.dismiss()
 
        
        self.layout2=BoxLayout(orientation='horizontal',pos_hint={'x': 0.05, 'y': 0.7},spacing=15)
    
        
        self.img_2=Image(source='img_munt//put.png',size_hint=(None, None), size=(75 , 75))
        self.label2=MDLabel(text=f'{self.text_name2.text} \ {self.text_nmber2.text} \ {self.text_place2.text}',size_hint=(0.05, 0.2))
        self.icobut2=MDIconButton(icon='delete-circle-outline',pos_hint={'x': -0.3, 'y': 0.03}, theme_text_color='Custom',text_color=(1,0,0,1),on_press=self.on_dialog2)
        self.boxlef2=BoxLayout(size_hint=(0.01, 0.5))
        self.layout2.add_widget(self.img_2)
        self.layout2.add_widget(self.label2)
        self.layout2.add_widget(self.icobut2)
        self.layout2.add_widget(self.boxlef2)
        

        self.main_layout.add_widget(self.layout2)
        
        
        
        
        
    def on_dialog2(self, instance):
        if not self.dialog2:
            self.dialog2=MDDialog(title='Do you want to cancel the order?',
                        buttons=[MDRaisedButton(text='Cansle',on_press=self.off_dialog2),MDRaisedButton(text='Ok',md_bg_color='red',on_press=self.delet_munt2)])
            self.dialog2.open()
            
    def off_dialog2(self,instance):
        self.dialog2.dismiss()  
    
    def delet_munt2(self, *args):
        self.layout2.clear_widgets()
        self.dialog2.dismiss()  
        self.ids.labnonerets.text = 'None not in Rets'
    
        
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''===========================================''''''''''''''''''''''
  
    def paying3(self):
        self.box_up3=BoxLayout()
        
        self.layout_munt3=BoxLayout(orientation='vertical',spacing=20)
        self.text_name3=MDTextField(hint_text='Enter Your Name:',mode='round')
        self.text_nmber3=MDTextField(hint_text='Enter your Number:',mode='round')
        self.text_place3=MDTextField(hint_text=f'Enter your Place / from',mode='round')
        self.box_down3=BoxLayout()
        self.boot3=MDFillRoundFlatIconButton(text='Paying',pos_hint={'x': 0.35},on_press=self.rets_munt3)
        
        self.layout_munt3.add_widget(self.box_up3)
        self.layout_munt3.add_widget(self.text_name3)
        self.layout_munt3.add_widget(self.text_nmber3)
        self.layout_munt3.add_widget(self.text_place3) 
        
        self.layout_munt3.add_widget(self.box_down3)
        
        self.layout_munt3.add_widget(self.boot3)
        
     
        
        self.popup3=Popup(title='Booking Fill in the fields',size_hint=(0.7, 0.6),
                    content=self.layout_munt3)
        self.popup3.open()
      
      
     # بعد الشراء اضهار صوره منتج ومده الوصول اليك وسعر    
    def rets_munt3(self, instance):
       
        self.hor_munt3=24
        self.ids.labnonerets.text = ''
        self.popup3.dismiss()
 
        
        self.layout3=BoxLayout(orientation='horizontal',pos_hint={'x': 0.05, 'y': 0.7},spacing=15)
    
        
        self.img_3=Image(source='img_munt//shhata.png',size_hint=(None, None), size=(75 , 75))
        self.label3=MDLabel(text=f'{self.text_name3.text} \ {self.text_nmber3.text} \ {self.text_place3.text}',size_hint=(0.05, 0.2))
        self.icobut3=MDIconButton(icon='delete-circle-outline',pos_hint={'x': -0.3, 'y': 0.03}, theme_text_color='Custom',text_color=(1,0,0,1),on_press=self.on_dialog3)
        self.boxlef3=BoxLayout(size_hint=(0.01, 0.5))
        self.layout3.add_widget(self.img_3)
        self.layout3.add_widget(self.label3)
        self.layout3.add_widget(self.icobut3)
        self.layout3.add_widget(self.boxlef3)
        

        self.main_layout.add_widget(self.layout3)
        
        
        
        
        
    def on_dialog3(self, instance):
        
        self.dialog3=MDDialog(title='Do you want to cancel the order?',
                        buttons=[MDRaisedButton(text='Cansle',on_press=self.off_dialog3),MDRaisedButton(text='Ok',md_bg_color='red',on_press=self.delet_munt3)])
        self.dialog3.open()
            
    def off_dialog3(self,instance):
        self.dialog3.dismiss()  
    
    def delet_munt3(self, *args):
        self.layout3.clear_widgets()
        self.dialog3.dismiss()  
        self.ids.labnonerets.text = 'None not in Rets'
        
        
        
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''===========================================''''''''''''''''''''''
  
    def paying4(self):
        self.box_up4=BoxLayout()
        
        self.layout_munt4=BoxLayout(orientation='vertical',spacing=20)
        self.text_name4=MDTextField(hint_text='Enter Your Name:',mode='round')
        self.text_nmber4=MDTextField(hint_text='Enter your Number:',mode='round')
        self.text_place4=MDTextField(hint_text=f'Enter your Place / from',mode='round')
        self.box_down4=BoxLayout()
        self.boot4=MDFillRoundFlatIconButton(text='Paying',pos_hint={'x': 0.35},on_press=self.rets_munt4)
        
        self.layout_munt4.add_widget(self.box_up4)
        self.layout_munt4.add_widget(self.text_name4)
        self.layout_munt4.add_widget(self.text_nmber4)
        self.layout_munt4.add_widget(self.text_place4) 
        
        self.layout_munt4.add_widget(self.box_down4)
        
        self.layout_munt4.add_widget(self.boot4)
        
     
        
        self.popup4=Popup(title='Booking Fill in the fields',size_hint=(0.7, 0.6),
                    content=self.layout_munt4)
        self.popup4.open()
      
      
     # بعد الشراء اضهار صوره منتج ومده الوصول اليك وسعر    
    def rets_munt4(self, instance):
       
        self.hor_munt4=24
        self.ids.labnonerets.text = ''
        self.popup4.dismiss()
 
        
        self.layout4=BoxLayout(orientation='horizontal',pos_hint={'x': 0.05, 'y': 0.7},spacing=15)
    
        
        self.img_4=Image(source='img_munt//saa.png',size_hint=(None, None), size=(75 , 75))
        self.label4=MDLabel(text=f'{self.text_name4.text} \ {self.text_nmber4.text} \ {self.text_place4.text}',size_hint=(0.05, 0.2))
        self.icobut4=MDIconButton(icon='delete-circle-outline',pos_hint={'x': -0.3, 'y': 0.03}, theme_text_color='Custom',text_color=(1,0,0,1),on_press=self.on_dialog4)
        self.boxlef4=BoxLayout(size_hint=(0.01, 0.5))
        self.layout4.add_widget(self.img_4)
        self.layout4.add_widget(self.label4)
        self.layout4.add_widget(self.icobut4)
        self.layout4.add_widget(self.boxlef4)
        

        self.main_layout.add_widget(self.layout4)
        
        
        
        
        
    def on_dialog4(self, instance):
       
        self.dialog4=MDDialog(title='Do you want to cancel the order?',
                        buttons=[MDRaisedButton(text='Cansle',on_press=self.off_dialog4),MDRaisedButton(text='Ok',md_bg_color='red',on_press=self.delet_munt4)])
        self.dialog4.open()
            
    def off_dialog4(self,instance):
        self.dialog4.dismiss()  
    
    def delet_munt4(self, *args):
        self.layout4.clear_widgets()
        self.dialog4.dismiss()  
        self.ids.labnonerets.text = 'None not in Rets'
        
    
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''=====================================''''''''''''''''''''''''''
        

  
    def paying5(self):
        self.box_up5=BoxLayout()
        
        self.layout_munt5=BoxLayout(orientation='vertical',spacing=20)
        self.text_name5=MDTextField(hint_text='Enter Your Name:',mode='round')
        self.text_nmber5=MDTextField(hint_text='Enter your Number:',mode='round')
        self.text_place5=MDTextField(hint_text=f'Enter your Place / from',mode='round')
        self.box_down5=BoxLayout()
        self.boot5=MDFillRoundFlatIconButton(text='Paying',pos_hint={'x': 0.35},on_press=self.rets_munt5)
        
        self.layout_munt5.add_widget(self.box_up5)
        self.layout_munt5.add_widget(self.text_name5)
        self.layout_munt5.add_widget(self.text_nmber5)
        self.layout_munt5.add_widget(self.text_place5) 
        
        self.layout_munt5.add_widget(self.box_down5)
        
        self.layout_munt5.add_widget(self.boot5)
        
     
        
        self.popup5=Popup(title='Booking Fill in the fields',size_hint=(0.7, 0.6),
                    content=self.layout_munt5)
        self.popup5.open()
      
      
     # بعد الشراء اضهار صوره منتج ومده الوصول اليك وسعر    
    def rets_munt5(self, instance):
       
        self.hor_munt5=24
        self.ids.labnonerets.text = ''
        self.popup5.dismiss()
 
        
        self.layout5=BoxLayout(orientation='horizontal',pos_hint={'x': 0.05, 'y': 0.7},spacing=15)
    
        
        self.img_5=Image(source='img_munt//comp.png',size_hint=(None, None), size=(75 , 75))
        self.label5=MDLabel(text=f'{self.text_name5.text} \ {self.text_nmber5.text} \ {self.text_place5.text}',size_hint=(0.05, 0.2))
        self.icobut5=MDIconButton(icon='delete-circle-outline',pos_hint={'x': -0.3, 'y': 0.03}, theme_text_color='Custom',text_color=(1,0,0,1),on_press=self.on_dialog5)
        self.boxlef5=BoxLayout(size_hint=(0.01, 0.5))
        self.layout5.add_widget(self.img_5)
        self.layout5.add_widget(self.label5)
        self.layout5.add_widget(self.icobut5)
        self.layout5.add_widget(self.boxlef5)
        

        self.main_layout.add_widget(self.layout5)
        
        
        
        
        
    def on_dialog5(self, instance):
     
        self.dialog5=MDDialog(title='Do you want to cancel the order?',
                        buttons=[MDRaisedButton(text='Cansle',on_press=self.off_dialog5),MDRaisedButton(text='Ok',md_bg_color='red',on_press=self.delet_munt5)])
        self.dialog5.open()
            
    def off_dialog5(self,instance):
        self.dialog5.dismiss()  
    
    def delet_munt5(self, *args):
        self.layout5.clear_widgets()
        self.dialog5.dismiss()  
        self.ids.labnonerets.text = 'None not in Rets'
        


   
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''=====================================''''''''''''''''''''''''''
        

  
    def paying6(self):
        self.box_up6=BoxLayout()
        
        self.layout_munt6=BoxLayout(orientation='vertical',spacing=20)
        self.text_name6=MDTextField(hint_text='Enter Your Name:',mode='round')
        self.text_nmber6=MDTextField(hint_text='Enter your Number:',mode='round')
        self.text_place6=MDTextField(hint_text=f'Enter your Place / from',mode='round')
        self.box_down6=BoxLayout()
        self.boot6=MDFillRoundFlatIconButton(text='Paying',pos_hint={'x': 0.35},on_press=self.rets_munt6)
        
        self.layout_munt6.add_widget(self.box_up6)
        self.layout_munt6.add_widget(self.text_name6)
        self.layout_munt6.add_widget(self.text_nmber6)
        self.layout_munt6.add_widget(self.text_place6) 
        
        self.layout_munt6.add_widget(self.box_down6)
        
        self.layout_munt6.add_widget(self.boot6)
        
     
        
        self.popup6=Popup(title='Booking Fill in the fields',size_hint=(0.7, 0.6),
                    content=self.layout_munt6)
        self.popup6.open()
      
      
     # بعد الشراء اضهار صوره منتج ومده الوصول اليك وسعر    
    def rets_munt6(self, instance):
       
        self.hor_munt6=24
        self.ids.labnonerets.text = ''
        self.popup6.dismiss()
 
        
        self.layout6=BoxLayout(orientation='horizontal',pos_hint={'x': 0.05, 'y': 0.7},spacing=15)
    
        
        self.img_6=Image(source='img_munt//het.png',size_hint=(None, None), size=(75 , 75))
        self.label6=MDLabel(text=f'{self.text_name6.text} \ {self.text_nmber6.text} \ {self.text_place6.text}',size_hint=(0.05, 0.2))
        self.icobut6=MDIconButton(icon='delete-circle-outline',pos_hint={'x': -0.3, 'y': 0.03}, theme_text_color='Custom',text_color=(1,0,0,1),on_press=self.on_dialog6)
        self.boxlef6=BoxLayout(size_hint=(0.01, 0.5))
        self.layout6.add_widget(self.img_6)
        self.layout6.add_widget(self.label6)
        self.layout6.add_widget(self.icobut6)
        self.layout6.add_widget(self.boxlef6)
        

        self.main_layout.add_widget(self.layout6)
        
        
        
        
        
    def on_dialog6(self, instance):
   
        self.dialog6=MDDialog(title='Do you want to cancel the order?',
                        buttons=[MDRaisedButton(text='Cansle',on_press=self.off_dialog6),MDRaisedButton(text='Ok',md_bg_color='red',on_press=self.delet_munt6)])
        self.dialog6.open()
            
    def off_dialog6(self,instance):
        self.dialog6.dismiss()  
    
    def delet_munt6(self, *args):
        self.layout6.clear_widgets()
        self.dialog6.dismiss()  
        self.ids.labnonerets.text = 'None not in Rets'
        


   
    
    
    def goto_app(self):
        self.manager.current= "MainScreen"
        
        
        

 
            
        
        
class Card(Screen):
    def __init__(self, **kw):
        super(Card, self).__init__(**kw)
    
    
    def goto_gs_mnt(self):
       self.manager.current = "MainScreen" # زر خروج قبل الدخول للكارت
       
       
    def goto_gs_inopen(self,instance): # زر خروج بعد دخول للكارت
        self.manager.current = "MainScreen"
        
    # ايرور تابع في كارت عند ادخال حسابك خطاء
    def diseror(self, instance):
        self.popup2.dismiss()
    
    def eroorno(self):
        self.leayout1=BoxLayout(orientation='vertical')
        self.ico=MDIcon(icon='credit-card-remove',theme_text_color='Custom',text_color=(1,0,0,1),pos_hint={'x':0.45 , 'y': 0.8})
        self.layout2=BoxLayout(size_hint=(0.2, 0.01))
        self.but=MDRaisedButton(text='OK',pos_hint={'x': 0.37})
        self.but.bind(on_press=self.diseror)
        
        self.leayout1.add_widget(self.ico)
        self.leayout1.add_widget(self.layout2)
        self.leayout1.add_widget(self.but)
        
        
        self.popup2=Popup(title='Eroor sentax Carding',size_hint=(0.7, 0.3),title_color=(1,0,0,1),
                            content=self.leayout1)
        self.popup2.open()
        
       
       
    def clear_wid(self, instance):
        self.clear_widgets()   
        self.popup.dismiss()
  
       
        
    

        
        layout3=BoxLayout(orientation='vertical')
        img=Image(source='img_file//viza.png',size_hint=(None, None),size=(350, 200),pos_hint={'x': 0.05, 'y':0.2})
        lab=MDLabel(text='$ 158.65 USD',pos_hint={'x': 0.26},font_style='H4',theme_text_color='Custom',text_color=(0,0.5,0,1))
        
        but=MDIconButton(icon='arrow-left',size_hint=(0.2, 0.3))
        but.bind(on_release=self.goto_gs_inopen)
        
        layout3.add_widget(but)
        layout3.add_widget(img)
        layout3.add_widget(lab)
        layout_jok=BoxLayout(size_hint=(0.9, 0.9))
      
        
       
        layout3.add_widget(layout_jok)
   
        self.add_widget(layout3) 
        
     
        
        
        

       

    # عندما يكون صح حساب كارت
    def popupd(self):
        layout=BoxLayout(orientation='vertical')
        icon=MDIcon(icon='credit-card-check', pos_hint={'x':0.45 , 'y': 0.8},theme_text_color='Custom',text_color=(0,1,0,1))
        layout2=BoxLayout(size_hint=(0.2, 0.05))
        butn=MDRaisedButton(text  ='OK',pos_hint={'x':0.38 , 'y':0.3})
        butn.bind(on_release=self.clear_wid)
   
       
       
        layout.add_widget(icon)
        layout.add_widget(layout2)
        layout.add_widget(butn)
      
        self.popup=Popup(title="The card has been linked to the program.",size_hint=(0.8, 0.3),
                    content=layout)
        
        self.popup.open()
    


class Posmarc(Screen):  # قسم الاضهار الخريطه الماركت
    def goto_gsm_mn(self):
        self.manager.current = "MainScreen"
    

class Shapeng(Screen):  # قسم المنتجات للشراء
    def goto_qsm_mntj(self):
        self.manager.current = "MainScreen"
        self.manager.transition.direction='right'
        
        
# --------------------------------------------------------------------------------  
# اقسام بعد الدخول في قسم الشراء   

    def munt1(self):
        self.layout=BoxLayout(orientation='vertical')
        self.label=MDLabel(text='Its old price was $ 40.0'
                ,theme_text_color='Custom',text_color=(1,0,0,1), pos_hint={'x': 0.2},strikethrough=True)
        
        
        self.img=Image(source=self.ids.img1.source,size_hint=(None, None),size=(272 ,250))


        self.grid=GridLayout(rows=1, cols=3, pos_hint={'x': 0.15},spacing=10)
        self.but1=MDFillRoundFlatIconButton(text='paying',icon='currency-usd', md_bg_color='orange',on_press=self.goto_in_munt_1)
        self.lefico=MDIconButton(icon='arrow-left',theme_text_color='Custom',text_color=(1,1,1,1),on_press=self.change_img)
        
        self.raisico=MDIconButton(icon='arrow-right',theme_text_color='Custom',text_color=(1,1,1,1),on_press=self.change_img)
        
        
        self.grid.add_widget(self.but1)
        self.grid.add_widget(self.lefico)
        self.grid.add_widget(self.raisico)
        
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.img)
        self.layout.add_widget(self.grid)
        
        self.pop1=Popup(title='Tisert $ 20.0',size_hint=(0.75 , 0.8),background_color='lavender',
                       content=self.layout)
        

        self.pop1.open()
        
        
        # مجموعات الصوره للموتاج hgh,g
        self.image=['img_munt//suuf2.png','img_munt//suuf3.png','img_munt//suuf.png','img_munt//suuf4.png']
        
        # اختيارات الصوره بارقام ابدي من 0
        self.current_image_index= 0

        # تحويلات صوره والمنتج الاول 1 

    def change_img(self, instance):
        if instance.icon == 'arrow-left': # اد كان ايقون اليمين تعرض للضغط 
            self.current_image_index -=1  # نقص عل ارقام الصوره -1
            
        elif instance.icon == 'arrow-right':# اد كان ايقون يسار تعرض للضغط 
            self.current_image_index +=1    # زيد عل ارقام الصوره + 1
            
            
        self.current_image_index %= len(self.image)  # قيمه رقم من صوره اقسمها في عدد الصوره و اخد الباقي قيمه اعملها كقيمه جديد
        self.img.source = self.image[self.current_image_index] # ادخل في متغير من مسار اخد المسار من صوره و من ارقام الصوره 
# --------------------------------------------------------------------------------    
    
    
    
        
    
    def munt2(self):
        self.layout=BoxLayout(orientation='vertical')
        self.label=MDLabel(text='Its old price was $ 70.0'
                ,theme_text_color='Custom',text_color=(1,0,0,1), pos_hint={'x': 0.2},strikethrough=True)
        
        
        self.img2=Image(source=self.ids.img2.source,size_hint=(None, None),size=(272 ,250))


        self.grid=GridLayout(rows=1, cols=3, pos_hint={'x': 0.15},spacing=10)
        self.but1=MDFillRoundFlatIconButton(text='paying',icon='currency-usd', md_bg_color='orange',on_press=self.goto_in_munt_2)
        self.lefico=MDIconButton(icon='arrow-left',theme_text_color='Custom',text_color=(1,1,1,1), on_press=self.change_image2)
        
        self.raisico=MDIconButton(icon='arrow-right',theme_text_color='Custom',text_color=(1,1,1,1),on_press=self.change_image2)
        
        
        self.grid.add_widget(self.but1)
        self.grid.add_widget(self.lefico)
        self.grid.add_widget(self.raisico)
        
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.img2)
        self.layout.add_widget(self.grid)
        
        self.pop2=Popup(title='Putt $ 20.0',size_hint=(0.75 , 0.8),background_color='lavender',
                       content=self.layout)
        

        self.pop2.open()
    
    
        self.image_mun2=['img_munt//put2.png','img_munt//put3.png','img_munt//put.png']
        
        self.current_image_index_2=0
    def change_image2(self, instance):
        if instance.icon == 'arrow-left':
            self.current_image_index_2 -=1
            
        elif instance.icon == 'arrow-right':
            self.current_image_index_2 +=1
        
        self.current_image_index_2 %= len(self.image_mun2)
        
        self.img2.source = self.image_mun2[self.current_image_index_2]
    
    # --------------------------------------------------------------
    
    def munt3(self):
        self.layout=BoxLayout(orientation='vertical')
        self.label=MDLabel(text='Its old price was $ 16.0'
                ,theme_text_color='Custom',text_color=(1,0,0,1), pos_hint={'x': 0.2},strikethrough=True)
        
        
        self.img3=Image(source=self.ids.img3.source,size_hint=(None, None),size=(272 ,250))


        self.grid=GridLayout(rows=1, cols=3, pos_hint={'x': 0.15},spacing=10)
        self.but1=MDFillRoundFlatIconButton(text='paying',icon='currency-usd', md_bg_color='orange', on_press=self.goto_in_munt_3)
        self.lefico=MDIconButton(icon='arrow-left',theme_text_color='Custom',text_color=(1,1,1,1), on_press=self.change_image3)
        
        self.raisico=MDIconButton(icon='arrow-right',theme_text_color='Custom',text_color=(1,1,1,1),on_press=self.change_image3)
        
        
        self.grid.add_widget(self.but1)
        self.grid.add_widget(self.lefico)
        self.grid.add_widget(self.raisico)
        
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.img3)
        self.layout.add_widget(self.grid)
        
        self.pop3=Popup(title='Shaf $ 20.0',size_hint=(0.75 , 0.8),background_color='lavender',
                       content=self.layout)
        

        self.pop3.open()
        
        
        
        self.image_mun3=['img_munt//shhata2.png','img_munt//shhata3.png','img_munt//shhata4.png']
        
        self.current_image_index_3= 0
        
    def change_image3(self, instance):
        if instance.icon =='arrow-left':
            self.current_image_index_3 -=1
        elif instance.icon == 'arrow-right':
            self.current_image_index_3 +=1
        self.current_image_index_3 %= len(self.image_mun3)
        self.img3.source = self.image_mun3[self.current_image_index_3]
        
    #-------------------------------------------------
    
    def munt4(self):
        self.layout=BoxLayout(orientation='vertical')
        self.label=MDLabel(text='Its old price was $ 75.50'
                ,theme_text_color='Custom',text_color=(1,0,0,1), pos_hint={'x': 0.2},strikethrough=True)
        
        
        self.img4=Image(source=self.ids.img4.source,size_hint=(None, None),size=(272 ,250))


        self.grid=GridLayout(rows=1, cols=3, pos_hint={'x': 0.15},spacing=10)
        self.but1=MDFillRoundFlatIconButton(text='paying',icon='currency-usd', md_bg_color='orange',on_press=self.goto_in_munt_4)
        self.lefico=MDIconButton(icon='arrow-left',theme_text_color='Custom',text_color=(1,1,1,1), on_press=self.change_image4)
        
        self.raisico=MDIconButton(icon='arrow-right',theme_text_color='Custom',text_color=(1,1,1,1),on_press=self.change_image4)
        
        
        self.grid.add_widget(self.but1)
        self.grid.add_widget(self.lefico)
        self.grid.add_widget(self.raisico)
        
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.img4)
        self.layout.add_widget(self.grid)
        
        self.pop4=Popup(title='Bagre $ 20.0',size_hint=(0.75 , 0.8),background_color='lavender',
                       content=self.layout)
        

        self.pop4.open()
        
        self.image_mun4=['img_munt//saa2.png','img_munt//saa3.png','img_munt//saa4.png']
        
        self.current_image_index_4=0
    def change_image4(self, instance):
        if instance.icon == 'arrow-left':
            self.current_image_index_4 -=1
        elif instance.icon == 'arrow-right':
            self.current_image_index_4 +=1
            
        self.current_image_index_4 %= len(self.image_mun4)
        self.img4.source = self.image_mun4[self.current_image_index_4]
     #-------------------------------------------------------------------------------   
        
    def munt5(self):
        self.layout=BoxLayout(orientation='vertical')
        self.label=MDLabel(text='Its old price was $ 920.50'
                ,theme_text_color='Custom',text_color=(1,0,0,1), pos_hint={'x': 0.2},strikethrough=True)
        
        
        self.img5=Image(source=self.ids.img5.source,size_hint=(None, None),size=(272 ,250))


        self.grid=GridLayout(rows=1, cols=3, pos_hint={'x': 0.15},spacing=10)
        self.but1=MDFillRoundFlatIconButton(text='paying',icon='currency-usd', md_bg_color='orange', on_press=self.goto_in_munt_5)
        self.lefico=MDIconButton(icon='arrow-left',theme_text_color='Custom',text_color=(1,1,1,1), on_press=self.change_image5)
        
        self.raisico=MDIconButton(icon='arrow-right',theme_text_color='Custom',text_color=(1,1,1,1),on_press=self.change_image5)
        
        
        self.grid.add_widget(self.but1)
        self.grid.add_widget(self.lefico)
        self.grid.add_widget(self.raisico)
        
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.img5)
        self.layout.add_widget(self.grid)
        
        self.pop5=Popup(title='Dell $ 20.0',size_hint=(0.75 , 0.8),background_color='lavender',
                       content=self.layout)
        

        self.pop5.open()
        
        self.image_mun5=['img_munt//comp2.png','img_munt//comp.png']
        
        self.current_image_index_5= 0
        
    def change_image5(self, instance):
        if instance.icon == 'arrow-left':
            self.current_image_index_5 -=1
            
        elif instance.icon == 'arrow-right':
            self.current_image_index_5 +=1
            
        self.current_image_index_5 %= len(self.image_mun5)
        self.img5.source = self.image_mun5[self.current_image_index_5]
    #------------------------------------------------------------------------
    
    def munt6(self):
        self.layout=BoxLayout(orientation='vertical')
        self.label=MDLabel(text='Its old price was $ 920.50'
                ,theme_text_color='Custom',text_color=(1,0,0,1), pos_hint={'x': 0.2},strikethrough=True)
        
        
        self.img6=Image(source=self.ids.img6.source,size_hint=(None, None),size=(272 ,250))


        self.grid=GridLayout(rows=1, cols=3, pos_hint={'x': 0.15},spacing=10)
        self.but1=MDFillRoundFlatIconButton(text='paying',icon='currency-usd', md_bg_color='orange', on_press=self.goto_in_munt_6)
        self.lefico=MDIconButton(icon='arrow-left',theme_text_color='Custom',text_color=(1,1,1,1), on_press=self.change_image6)
        
        self.raisico=MDIconButton(icon='arrow-right',theme_text_color='Custom',text_color=(1,1,1,1),on_press=self.change_image6)
        
        
        self.grid.add_widget(self.but1)
        self.grid.add_widget(self.lefico)
        self.grid.add_widget(self.raisico)
        
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.img6)
        self.layout.add_widget(self.grid)
        
        self.pop6=Popup(title='Htfon $ 66.0',size_hint=(0.75 , 0.8),background_color='lavender',
                       content=self.layout)
        

        self.pop6.open()
        
        self.image_munt6= ['img_munt//het2.png','img_munt//het3.png','img_munt//het4.png']
        
        self.current_image_index_6=0
    
    def change_image6(self, instance):
        if instance.icon == 'arrow-left':
            self.current_image_index_6 -=1
            
        elif instance.icon == 'arrow-right':
            self.current_image_index_6 +=1
            
        self.current_image_index_6 %= len(self.image_munt6)
        self.img6.source = self.image_munt6[self.current_image_index_6]
     
     
     #  منتج الاول للدهاب في قسم الشراء  1
     
    def goto_in_munt_1(self , _1):
        self.manager.current = 'Rets'
        self.manager.get_screen('Rets').paying1()
        self.pop1.dismiss()
  
   
     
     
    def goto_in_munt_2(self , _2):
        self.manager.current = 'Rets'
        self.manager.get_screen('Rets').paying2()
        self.pop2.dismiss()
  
     
     
    def goto_in_munt_3(self , _3):
        self.manager.current = 'Rets'
        self.manager.get_screen('Rets').paying3()
        self.pop3.dismiss()
  


     
     
    def goto_in_munt_4(self , _4):
        self.manager.current = 'Rets'
        self.manager.get_screen('Rets').paying4()
        self.pop4.dismiss()
  
     
    def goto_in_munt_5(self , _5):
        self.manager.current = 'Rets'
        self.manager.get_screen('Rets').paying5()
        self.pop5.dismiss()
  
  
     
    def goto_in_munt_6(self , _6):
        self.manager.current = 'Rets'
        self.manager.get_screen('Rets').paying6()
        self.pop6.dismiss()
  

     
     
     

     
     
     
     
     
     
     
     
     
     
     
     
class MainScreen(Screen): # قسم الرائيسي بعد الدخول للتطبيق
    def goto_apple(self):    
        self.manager.current = "Apple"
        self.manager.transition.direction='right'
       

            
    def goto_peon(self):
        self.manager.current= 'Peon'
        
    def goto_arves(self):
        self.manager.current='Arves'
        
    def goto_card(self):
        self.manager.current = 'Card'
    
    def goto_rets(self):
        self.manager.current = 'Rets'
        
        
        
    def goto_shapeng(self):
        self.manager.current = 'Shapeng'
    
    def goto_share(self):
        self.ids.container.clear_widgets()
        text_but=MDTextField(text='Search for a product',size_hint=(0.6, 0.05),pos_hint={'x': 0.2, 'y':0.82 }
                             ,mode='round',multiline=False,background_color=(0.5,0.5,0.5, 1))
        self.add_widget(text_but)
        
    def gotoposmarc(self):
        self.manager.current = 'Posmarc'
        
   


class Apple(Screen):  # قسم الدخول البدائي
    def goto_main(self):
        self.manager.current = "MainScreen"

    



class Marketing(MDApp):
    def build(self):
        scr = ScreenManager(transition=FadeTransition(duration=0.03))
        scr.add_widget(Main(name='Main'))
        scr.add_widget(Maincom(name='Maincom'))
        scr.add_widget(Apple(name="Apple"))
        scr.add_widget(MainScreen(name="MainScreen"))
        scr.add_widget(Shapeng(name='Shapeng'))
        scr.add_widget(Posmarc(name='Posmarc'))
        scr.add_widget(Card(name='Card'))
        
        scr.add_widget(Rets(name='Rets'))
        scr.add_widget(Arves(name='Arves'))
        scr.add_widget(Peon(name='Peon'))
        
        

        

        return scr
       

    
class Maincom(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.buttn.on_release=self.tanc
        
        
    
    def tanc(self):
        text= self.ids.my_text_inp1.text
        text2=self.ids.my_text_inp2.text
        self.manager.get_screen('Peon').label.text =f'gmali: {text}'
        self.manager.get_screen('Peon').label2.text= f'Password: {text2}'
        
     
        
        
        
    def eroor(self):
        self.ids.label_erorr.text= "Error please choose the right words"
        
        
class Main(Screen):
    def __init__(self , **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.swith_scre, 5)
        
    def swith_scre(self, dt):
        self.manager.current = 'Maincom'

  
  
    
Marketing().run()













