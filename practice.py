# from kivy.app import App
# from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
# from kivy.graphics.context_instructions import Color
# from kivy.properties import StringProperty, BooleanProperty, Clock
# from kivy.uix.widget import Widget
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.anchorlayout import AnchorLayout
# from kivy.uix.button import Button
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.stacklayout import StackLayout
# from kivy.uix.scrollview import ScrollView
# from kivy.uix.pagelayout import PageLayout
# from kivy.metrics import dp
# import math as m


# class CanvasExample(Widget):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.bind(size=self.on_size)
#         self.n_h_lines = 11
#         self.n_v_lines = 10
#         # Clock.schedule_interval(self.update, 1/60)
#         self.current_offset_y = 0

#     def on_size(self, *args):
#         with self.canvas:

#             self.canvas.clear()
           
#             for i in range(1,self.n_v_lines):
#                 i = i - 0.5
#                 Line(points=(self.width * (0.5-(i*0.1)), 0 , self.width/2 , self.height * 0.75), width=1)
                
#                 Line(points=(self.width * (0.5+(i*0.1)), 0 ,self.width/2, self.height * 0.75), width=1)

#             for j in range(1, self.n_h_lines):
#                 a = .05+(.1*(self.n_v_lines-2))
#                 val_left = 0.5 - a
#                 c = val_left + (self.width * a * 0.1 * j)/self.width
#                 d = 1 - c

#                 Line(points=(self.width* c, self.height * 0.75 * .1 * j, self.width * d , self.height * 0.75 * .1 * j))

#     def update(self, dt):
#         # self.current_offset_y +=0.01
#         pass

# class CanvasExample5(Widget):
    
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.ball_size = dp(50)
#         self.vx = dp(10)
#         self.vy = dp(10)
#         with self.canvas:
#             self.ball = Ellipse(pos=self.center,size=(self.ball_size, self.ball_size))
#         Clock.schedule_interval(self.update, 0.0000000000000001)
            
    
#     def on_size(self, *args):
#         print(self.width, self.height)
#         self.ball.pos = (self.center_x - self.ball_size/2, self.center_y - self.ball_size/2)

#     def update(self,dt):
#         x, y = self.ball.pos
#         if x + self.ball_size > self.width:
#             # x = self.width - self.ball_size
#             self.vx = -self.vx
#         elif x < 0:
#             # x = self.width + self.ball_size
#             self.vx = -self.vx
#         elif y + self.ball_size > self.height:
#             self.vy = -self.vy
#         elif y < 0:
#             self.vy = -self.vy

#         x+=self.vx
#         y+=self.vy

#         self.ball.pos = (x, y)
#         print(x)


   


# class CanvasExample4(Widget):
#     i = 20
#     y = 20
#     x = 200

#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         # self.canvas.add(Line(points=(100,100,400,500)))
#         with self.canvas:

#             Color(.6,.4,.2)
#             Line(points=(100,100,400,500))
#             Line(circle=(400, 200, 80), width=2)
#             Line(circle=(100,400,80),width=2)
#             Line(rectangle=(100,400,80, 40),width=2)
#             self.rect = Rectangle(pos=(self.x,400), size=(150, 100))
        
#     def move_rect_right(self):
#         if self.rect.pos[0]+150 <= self.width * .98:
#             self.rect.pos=(self.rect.pos[0]+self.i, 400)

    
#     def move_rect_left(self):
#         self.rect.pos = (self.rect.pos[0]-self.y, 400)
        
        
  
# class CanvasExample3(Widget):
#     pass


# class CanvasExample2(Widget):
#     pass


# class CanvasExample1(Widget):
#     pass

# class ImagesExample(GridLayout):
#     pass

# class WidgetsExample(GridLayout):

#     count = 0
#     # vol = 0
#     text_input = ""
#     my_text = StringProperty(str(count))

#     button_disabled = BooleanProperty(True)

#     toggle_disabled = BooleanProperty(True)

#     Text_Input = StringProperty(text_input)
#    # vol_value = StringProperty(str(vol))

#     def on_button_up(self):
#         self.count+=1
#         self.my_text = str(self.count)

#     def on_button_down(self):
#         if self.count > 0:
#             self.count -= 1
#             self.my_text = str(self.count)

#     def on_toggle_button_state(self, ToggleButton):

#         if ToggleButton.state == "down":
#             ToggleButton.text = "On"
#             self.button_disabled = False
    
#         else:
#             ToggleButton.text = "Off"
#             self.button_disabled = True
    
#     def on_switch_active(self, Switch):

#         if Switch.active == True:
#             self.toggle_disabled = False

#         else:
#             self.toggle_disabled = True

#     def on_slider_value(self, Slider):
#         # self.vol_value = str(int(Slider.value))
#         pass

#     def on_text_validate(self, TextInput):
#         self.Text_Input = TextInput.text


# class PageLayoutExample(PageLayout):
#     pass

# class ScrollViewExample(ScrollView):
#     pass

# class StackLayoutExample(StackLayout):

#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.size_hint = 1, None
#         self.minimum_height

#         for i in range(1,101):
#             b = Button(text=str(i))
#             self.add_widget(b)

# class GridLayoutExample(GridLayout):
#     pass

# class AnchorLayoutExample(AnchorLayout):
#     pass

# class BoxLayoutExample(BoxLayout):
#     pass

# class MainWidget(Widget):
#     pass


# class TheLabApp(App):
#     pass

# TheLabApp().run()




