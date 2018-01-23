
# coding: utf-8

# In[1]:


from microbit import *
hrs = 0
mins = 0
sec = 0
full = str(hrs) + ':' + str(mins) + ':' + str(sec)
while True:
    if
while True:
    display.scroll(full)
    sleep(1000)
    sec += 1
    if sec >= 60:
        mins += 1
        sec = 0
    if mins >= 60:
        hrs += 1
        mins = 0
    if hrs >= 24:
        hrs = 0
    full = str(hrs) + ':' + str(mins) + ':' + str(sec)
    if button_a.was_pressed():
        hrs += button_a.get_presses()
    if button_b.was_pressed():
        mins += button_b.get_presses()

