#!/usr/bin/python
# The MIT License (MIT)
# Copyright (c) 2017 "Laxminarayan Kamath G A"<kamathln@gmail.com>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
# OR OTHER DEALINGS IN THE SOFTWARE.


from kivy.app import App
from kivy.uix.widget import Widget
from arrow import *
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from random import random
from kivy.clock import Clock

class ArrowTest(App):
    def add_random_arrow(self,*args):
        newarrow = Arrow(
                         main_color=[random(),random(),random(),0.8],
                         outline_color=[random()/2.0,random()/2.0,random()/2.0,0.8],
                         o_x= -random()*self.layout.width/10.0, 
                         o_y=random()*self.layout.height,
                         #to_x=random()*self.layout.width,
                         #to_y=random()*self.layout.height,
                         angle=random()*30,
                         distance=40+(random()*100),
                         fletching_radius=cm(0.2),
                         distortions=[random() * -0.2, random() *0.3] if random()>0.5 else [],
                         head_angle=40+(random()*60)
                        )
        self.layout.add_widget(newarrow)
        self.arrows.append(newarrow)
        #self.move_arrows()

    def move_arrows(self,dt,*args):
        #self.dtsum += dt
        #self.dtcounter += 1
        for arrow in self.arrows:
            arrow.o_x, arrow.o_y = move_point(arrow.o_x,arrow.o_y,arrow.angle,16)
            arrow.main_color=[x for x in map(lambda y:y * 0.97, arrow.main_color)]
            arrow.outline_color=[x for x in map(lambda y:y * 0.97, arrow.outline_color)]
            if arrow.distortions:
                arrow.distortions= [x+(random()*0.1) -(random()*0.1) for x in arrow.distortions]
                arrow.head_angle = arrow.head_angle + (random() * 10) - (random() * 10)
            if arrow.main_color[3] < 0.1:
                self.arrows.remove(arrow)
                self.layout.remove_widget(arrow)
            
#    def debug_dt(self,*args):
#        print ("DT avg ",self.dtsum/float(self.dtcounter)) 

    def build(self):
        self.arrows = []
        self.dtsum=0.0
        self.dtcounter=0.0
        self.layout = FloatLayout()
#        self.button = Button(text='Debug DT', on_press=self.debug_dt,size=[100,100],size_hint=[None,None])
#        self.layout.add_widget(self.button)
        Clock.schedule_interval(self.move_arrows, 1/34.0)
        Clock.schedule_interval(self.add_random_arrow, 0.1)
        
        return self.layout

if __name__ == '__main__':
    ArrowTest().run()
