'''
ABC is a right triangle with 90 degrees at B. 
You are given the lengths AB and BC.
Your task is to find angle MBC
'''
import math as m
AB = int(input())
BC = int(input())
print(f'{round(m.degrees(m.atan(AB/BC)))}{chr(176)}')