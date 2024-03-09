# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 22:46:38 2024

@author: LAM Quincy
"""
import time
import os
while True:
    print('=======================','\n Type x to exit','\n Type p to play')
    print('=======================')
    x=input('input: ')
    print('-----------------------')
    if x == 'x':
        print('Exit','\nThanks for using')
        print('=======================')
        time.sleep(2)
        os.system("cls")
        break
    if x == 'p':
        a=int(5)
        delay=1
        print("\r    你 相信引力嗎    ",end="")
        time.sleep(2)
        print("\r     時間加速吧      ",end="")
        time.sleep(2)
        print("\r  Made in Heaven   ",end="")
        print('\n-----------------------')
        for i in range(a):
            for char in ['*__________','_*_________','__*________','___*_______','____*______','_____*_____','______*____','_______*___','________*__','_________*_','__________*']:
                print(f'\r{char}                  ',end='')
                time.sleep(delay)
                delay *= 0.96
        print('\r___________')
        print('\n=======================')
        time.sleep(1)
        os.system("cls")
        break