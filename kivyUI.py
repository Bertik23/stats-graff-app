from kivy import Config
Config.set('graphics', 'multisamples', '0')

import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from time import time

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

times = [time()]
peoples = [0]
plt.plot(times,peoples)

ax1.plot(times, peoples)

class TestApp(App):
    title = "Graph app"

    def build(self):
        box = BoxLayout()
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        inbutton = Button(text = "Inpt")
        inbutton.bind(on_press = self.inp)
        box.add_widget(inbutton)
        return box
    def inp(self, instance):
        times.append(time())
        peoples.append(input("Kolik?"))
        ax1.clear()
        ax1.plot(times,peoples)


if __name__ == "__main__":
    TestApp().run()
