from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivymd.uix.screen import Screen

from kivy.core.window import Window
from kivymd.uix.button import MDIconButton , MDFillRoundFlatIconButton
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import MDList,OneLineListItem, OneLineIconListItem

Window.size=(400 , 600)





Builder.load_string("""
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
          
            
         
            


<MainScreen>:
  
            
    
    MDScrollView:
        id: container     
        y: self.parent.height - self.height - 70
        
       
         
        
        
        BoxLayout:
            orientation: 'vertical'
            height: 800
            size_hint_y: None
            height:self.minimum_height
            
            
            Image:
                source: 'img_file//trw.jpg'
                size_hint: None , None
                size:400 , 250
            MDCard:
                md_bg_color: 'grey'
                size_hint:  None , None
                size: 380 ,80
                pos_hint: {'x':0.02}

                    
                MDIconButton:
                    icon: 'shopping'
                    icon_size: 40
                    md_bg_color: "#7f7f7f"
                    theme_text_color: "Custom"
                    text_color: '#013d85'
                    
                    ripple_radius: [1,1,1,1]  
                    ripple_behavior: False
                    
                    on_release: root.goto_shapeng()
                            
                        
                        
                        
                                    
                MDIconButton:
                    icon: 'store-marker'
                    icon_size: 40
                    theme_text_color:'Custom'
                    text_color: '#c82a00' 
                                
                        
                MDIconButton:
                    icon: 'credit-card'
                    icon_size: 40
                    theme_text_color:'Custom'
                    text_color: '#000000'                    
                        
        
                MDIconButton:
                    icon: 'truck'
                    icon_size: 40
                    theme_text_color:'Custom'
                    text_color: '#003689'                    
                        
            
        
                MDIconButton:
                    icon: 'bookmark'
                    icon_size: 40
                    theme_text_color:'Custom'
                    text_color: '#a36528'                    
                        
            
            
        
                MDIconButton:
                    icon: 'account-multiple'
                    icon_size: 35
                    theme_text_color:'Custom'
                    text_color: '#ad7b48'  
                        
            Image:
                source: 'img_file//sane.png'  
                size_hint: None , None
                size:400 , 250                
                        
            
            
                
            Image:
                source: 'img_file//mintw.jpg'  
                size_hint: None , None
                size:400 , 250      
                
                
                          
                        
    MDTopAppBar:
        pos_hint: {'top': 1} 
        height: 56
        title: 'Shapeng Marcitng'
        left_action_items: [["arrow-left", lambda x: root.goto_apple()]]
        right_action_items:[["magnify", lambda x: root.goto_share()]]
   
           
                

                
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
            rows: None
            size_hint_y: None
            spacing: 15, 20
            padding: 42 , 20
            height: self.minimum_height
    #======================================1
            Image:
                source:"img_munt//suuf.png"
                size_hint: None, None
                size: 150,150
          
                
            Image:
                source:"img_munt//put.png"
                radius: [20,]
                size_hint: None, None
                size: 150,150
                    
                    
          
                
            MDLabel:
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
                text: 'Boys'
                size_hint: 0.3 , 0.1
                md_bg_color: 'orange'
                
            MDFillRoundFlatIconButton:
                text: 'Boys'
                size_hint: 0.3 , 0.1
                md_bg_color: 'orange'
    #=====================================  2   
            
            Image:
                source:"img_munt//suuf.png"
                size_hint: None, None
                size: 150,150
          
                
            Image:
                source:"img_munt//put.png"
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
                
            MDFillRoundFlatIconButton:
                text: 'Boys'
                size_hint: 0.3 , 0.1
                md_bg_color: 'orange'
                
                
        # =============================3
            
            Image:
                source:"img_munt//suuf.png"
                size_hint: None, None
                size: 150,150
          
                
            Image:
                source:"img_munt//put.png"
                radius: [20,]
                size_hint: None, None
                size: 150,150 
                
                
            MDLabel:
                text:'Shafq $ 5'
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
                
            MDFillRoundFlatIconButton:
                text: 'Boys'
                size_hint: 0.3 , 0.1
                md_bg_color: 'orange'
                #==================================4
            
          
                        
                    
                    
                
          
                
        
        
                
                                                                                                                                                                                                                                                                                                                        
            
    
        
       
       
""")


class Shapeng(Screen):
    def goto_qsm_mntj(self):
        self.manager.current = "MainScreen"
        self.manager.transition.direction='right'

        
    
            

            
            

class MainScreen(Screen):
    def goto_apple(self):    
        self.manager.current = "Apple"
        self.manager.transition.direction='left'
        
        
        
    def goto_shapeng(self):
        self.manager.current = 'Shapeng'
    
    def goto_share(self):
        self.ids.container.clear_widgets()
        text_but=MDTextField(text='Search for a product',size_hint=(0.6, 0.05),pos_hint={'x': 0.2, 'y':0.82 }
                             ,mode='round',multiline=False,background_color=(0.5,0.5,0.5, 1))
        self.add_widget(text_but)
        
        
   
        



class Apple(Screen):
    def goto_main(self):
        self.manager.current = "MainScreen"
        self.manager.transition.direction='left'
    



class Marketing(MDApp):
    def build(self):
        scr = ScreenManager()
        scr.add_widget(Apple(name="Apple"))
        scr.add_widget(MainScreen(name="MainScreen"))
        scr.add_widget(Shapeng(name='Shapeng'))

        return scr
       

    
  
  
  
  
    
Marketing().run()