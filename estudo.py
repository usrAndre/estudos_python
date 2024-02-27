#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 10 17:14:41 2022

@author: andreluizrodriguesdasilva
"""

def divide(a, denominator):
    try:
        return a / denominator
    except ZeroDivisionError as e:
        print('Divide by Zero! Terminate!!')
    finally:
        print('Division Complete.')
        

divide(4, 2)
divide(4, 0)

# ideia: pode ser usado no MASE lista_produtos?
# testar!
'''     
def divide(a, denominator):
    try:
        return a / denominator
    except ZeroDivisionError as e:
        print(e)
    finally:
        print('Division Complete.')
        
divide(9, 0)
9/0
'''

example = ["Sunday", "Monday", "Tuesday", "Wednesday"]

print(example[2])

                   
# pass
for i in range(5):
    if i % 2 == 0:
        pass
    else:
        print(i)
        
# continue
for i in range(17):
    if i == 13:
        continue
    print(i)
    
# break
for i in range(5):
    print(i)
    if i == 3:
        break
    
    
    
example = ["Sunday", "Monday", "Tuesday", "Wednesday"];
print(example)
example[0] = "Saturday"
print(example)

# Replicação
example1 = ["Weekdays", "Weekends"]
# Replication
example1 = example1 * 3
print(example1)



ex = list(range(8))[0:]
print(ex)

print([i in ex ])