from kivy import Config
Config.set('graphics', 'multisamples', '0')

import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

plt.ion()
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

times = [time.ctime()]
peoples = [0]
plt.plot(times,peoples)

ax1.plot(times, peoples)


class TestApp(App):
    title = "Graph app"

    def build(self):
        box = GridLayout()
        box.cols = 1
        box.add_widget(FigureCanvasKivyAgg(plt.gcf(),size_hint_y=50))
        self.innum = TextInput(text='Hello world', multiline=False, size_hint_y = 10)
        self.innum.bind(on_text_validate = self.on_enter)
        inbutton = Button(text = "Input", size_hint_y = 10)
        inbutton.bind(on_press = self.on_enter)
        box.add_widget(self.innum)
        box.add_widget(inbutton)
        return box
    def inp(self, instance):
        times.append(time.ctime())
        p = input("Kolik?")
        peoples.append(int(p))
        ax1.clear()
        ax1.plot(times, peoples)
    def on_enter(self,instance, value = 5):
        times.append(time.ctime())
        p = self.innum.text
        peoples.append(int(p))
        ax1.clear()
        ax1.plot(times, peoples)


if __name__ == "__main__":
    MyApp = TestApp()
    MyApp.run()
