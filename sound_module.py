# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 23:27:42 2018

@author: Garry
"""

import pyttsx3
engine = pyttsx3.init('sapi5')

def sound(f):
  if f==0:
    engine.say('Digit is zero ')
    engine.runAndWait()
  elif f==1:
    engine.say('Digit is one ')
    engine.runAndWait()
  elif f==2:
    engine.say('Digit is two ')
    engine.runAndWait()
  elif f==3:
    engine.say('Digit is three ')
    engine.runAndWait()
  elif f==4:
    engine.say('Digit is four ')
    engine.runAndWait()
  elif f==5:
    engine.say('Digit is five ')
    engine.runAndWait()
  elif f==6:
    engine.say('Digit is six')
    engine.runAndWait()
  elif f==7:
    engine.say('Digit is seven')
    engine.runAndWait()
  elif f==8:
    engine.say('Digit is eight ')
    engine.runAndWait()
  elif f==9:
    engine.say('Digit is nine ')
    engine.runAndWait()
  
