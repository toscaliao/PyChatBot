from chatterbot import ChatBot as bot
import pyautogui as m
import pyperclip as pc
import keyboard as kb
import time
time.clock = time.time

chatbot = bot("ChatAi")
exit_conditions = (":q", "quit", "exit")


while True:
    query = pc.paste()
    if query in exit_conditions:
        break
    else:
        if (kb.is_pressed('`')):
            break
        else:
            m.moveTo(940,1288)
            m.click()
            m.write(f"{chatbot.get_response(query)}",interval=0.1)
            m.press('enter')
            time.sleep(3)
            m.moveTo(984,1183)
            m.click()