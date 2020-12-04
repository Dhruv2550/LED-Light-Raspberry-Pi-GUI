from tkinter import *
from tkinter.ttk import *
from gpiozero import LED
from time import sleep

led = LED(4)
led1 = LED(17)
led2 = LED(26)
led4 = LED(19)

time = [1, 2, 3, 4, 5]

screen = Tk()


def on():
    led.on()
    led1.on()
    led2.on()
    led4.on()


def off():
    led.off()
    led1.off()
    led2.off()
    led4.off()


def blink():
    while True:
        led1.on()
        sleep(float(spinboxvar.get()))
        led1.off()
        led2.on()
        sleep(1)
        led2.off()
        led.on()
        sleep(float(spinboxvar.get()))
        led.off()
        led4.on()
        sleep(3)
        led4.off()
        led.on()
        led1.on()
        led2.on()
        led4.on()
        sleep(3)
        led.off()
        led1.off()
        led2.off()
        led4.off()


Button1 = Button(screen, text="On", style='TButton', state=ACTIVE,
                 command=on)  # Height is measures in lines and Width is defined in characters and not Pixels
Button1.grid(row=1, column=1, columnspan=2, sticky=NSEW)

Button1 = Button(screen, text="Off", style='TButton', state=ACTIVE,
                 command=off)  # Height is measures in lines and Width is defined in characters and not Pixels
Button1.grid(row=2, column=1, columnspan=2, sticky=NSEW)

spinboxvar = StringVar(screen)  # Creates a String Variable that will store the Value from the Option Menu
SpinBox1 = Spinbox(screen, width=10, from_=0, to=10, increment=0.5,
                   textvariable=spinboxvar)  # Always Stores Values as Text
SpinBox1.grid(row=3, column=1, columnspan=2, sticky=NSEW)

Button1 = Button(screen, text="Blink", style='TButton', state=ACTIVE,
                 command=blink)  # Height is measures in lines and Width is defined in characters and not Pixels
Button1.grid(row=4, column=1, columnspan=2, sticky=NSEW)

screen.mainloop()

