#!/usr/bin/env python3

import time
from src.tools import IkonBot

# TODO: make credentials an untracked config file
class user:
    name = ''
    password = ''
    day = 'Sat Feb 27 2021'
    resort = '' # big sky

interval_in_minutes = 15

while True:
    ikonbot = IkonBot(user)
    ikonbot.login()
    time.sleep(2)
    ikonbot.get_reservation_page()
    time.sleep(2)
    ikonbot.choose_resort()
    time.sleep(2)
    ikonbot.press_continue_button()
    time.sleep(2)
    ikonbot.right_month()
    time.sleep(2)
    ikonbot.pick_day()
    time.sleep(2)
    got_ikon_reservation = ikonbot.is_there_a_dismiss_button()
    if got_ikon_reservation:
        break
    else:
        ikonbot.driver.close()
        time.sleep(10) 


