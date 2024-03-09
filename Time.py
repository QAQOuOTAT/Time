# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time
import os
while True:
    print('=======================','\n Type x to exit')
    print('=======================')
    t=input('Time: ')
    print('-----------------------')
    if t == 'x':
        print('Exit','\nThanks for using')
        print('=======================')
        time.sleep(2)
        os.system('cls')
        break
    a=int(t)
    if a<=10:
        for i in range(a+1):
            print("\r",a,"s ",end="")
            a=a-1
            time.sleep(1)
        print('\n-----------------------')
        print('\a','\rm9OuO You Stupid')
    else:
        delay=1
        print("is time to speed up")
        time.sleep(1)
        print("  Made in Heaven   ")
        print("       m9OuO       ")
        print('\n-----------------------')
        for i in range(a+1):
            print("\r",a,"s ",end="")
            a=a-1
            time.sleep(delay)
            delay*=0.8
        print('\a','\rm9OuO You Stupid')