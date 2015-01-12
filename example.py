__author__ = 'durango'

from strip_animations import *

led = LEDStrip()

anim = RainbowCycle(led)
for i in range(100)
    anim.step()
    led.update()


