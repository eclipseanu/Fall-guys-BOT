import pyautogui
import time 


class FullHD():
    def lobby(self):
     while True:  
        lobby = pyautogui.locateOnScreen("1080\lobby.png",)
        e.error()
        if lobby !=None:
         print ("Lobby")
         pyautogui.click(lobby)
         pyautogui.press("space")
         e.matching()
         break
     
    def matching(self):
     while True:
         e.error()
         match = pyautogui.locateOnScreen("1080\search.png")
         if match !=None:
             print ("Matching")
             e.ingame()
             break
         
            
    def ingame(self):    
     while True:
         e.error()
         ingame = pyautogui.locateOnScreen("1080\ingame.png")   
         if ingame !=None:
            print ("Ingame")
            e.exit()
            break
            
    def exit(self):
      while True:
         e.error()
         salir = pyautogui.locateOnScreen("1080\exit.png")
         if salir != None:
             print ("exit found")
             time.sleep(3)
             pyautogui.press("esc")
             e.ok()
             break  
             
    def ok(self):
      while True:
         e.error()
         ok1 = pyautogui.locateOnScreen("1080\ok.png")
         if ok1 != None:
             print ("ok")
             pyautogui.press("space")
             e.results()
             break
             
    def results(self):
      while True:
        e.error()
        time.sleep(1)
        result = pyautogui.locateOnScreen("1080\endgame.png")
        if result !=None:
            time.sleep(7)
            pyautogui.press("space")
            global money
            global exp
            money=money+30
            exp = exp+15
            print ("You have won",money,"money")
            print ("You have won",exp,"exp")
            e.lobby()

    def error(self):
         disc = pyautogui.locateOnScreen("1080\disconnected.png",confidence=0.6)
         connect = pyautogui.locateOnScreen("1080\connect.png", confidence=0.6)
         connect2 = pyautogui.locateOnScreen("1080\error2.png", confidence=0.6)
         connect3 = pyautogui.locateOnScreen("1080\error3.png", confidence=0.6)
         if connect != None or disc !=None or connect2 != None or connect3 != None :
          print ("error")
          pyautogui.press("space")
          time.sleep(1)
          pyautogui.click()
          pyautogui.press("enter")
          e.lobby()
class HD():
    def lobby(self):
     while True:  
        lobby = pyautogui.locateOnScreen("720\lobby.png",)
        i.error()
        if lobby !=None:
         print ("Lobby")
         pyautogui.click(lobby)
         pyautogui.press("space")
         i.matching()
         break
     
    def matching(self):
     while True:
         i.error()
         match = pyautogui.locateOnScreen("720\search.png",confidence=0.6)
         if match !=None:
             print ("Matching")
             i.ingame()
             break
         
            
    def ingame(self):    
     while True:
         i.error()
         ingame = pyautogui.locateOnScreen("720\ingame.png")   
         if ingame !=None:
            print ("Ingame")
            i.exit()
            break
            
    def exit(self):
      while True:
         i.error()
         salir = pyautogui.locateOnScreen("720\exit.png")
         if salir != None:
             print ("exit found")
             time.sleep(3)
             pyautogui.press("esc")
             i.ok()
             break  
             
    def ok(self):
      while True:
         i.error()
         ok1 = pyautogui.locateOnScreen("720\ok.png")
         if ok1 != None:
             print ("ok")
             pyautogui.press("space")
             i.results()
             break
             
    def results(self):
      while True:
        i.error()
        time.sleep(1)
        result = pyautogui.locateOnScreen("720\endgame.png")
        if result !=None:
            time.sleep(7)
            pyautogui.press("space")
            global money
            global exp
            money=money+30
            exp = exp+15
            print ("You have won",money,"money")
            print ("You have won",exp,"exp")
            i.lobby()

    def error(self):
         disc = pyautogui.locateOnScreen("1080\disconnected.png",confidence=0.6)
         connect = pyautogui.locateOnScreen("1080\connect.png", confidence=0.6)
         connect2 = pyautogui.locateOnScreen("1080\error2.png", confidence=0.6)
         connect3 = pyautogui.locateOnScreen("1080\error3.png", confidence=0.6)
         if connect != None or disc !=None or connect2 != None or connect3 != None :
          print ("error")
          pyautogui.press("space")
          time.sleep(1)
          pyautogui.click()
          pyautogui.press("enter")
          i.lobby()
class FullHDLow():
    def lobby(self):
     while True:  
        lobby = pyautogui.locateOnScreen("1080\lobby.png",confidence=0.6)
        o.error()
        if lobby !=None:
         print ("Lobby")
         pyautogui.click(lobby)
         pyautogui.press("space")
         o.matching()
         break
     
    def matching(self):
     while True:
         o.error()
         match = pyautogui.locateOnScreen("1080\search.png",confidence=0.6)
         if match !=None:
             print ("Matching")
             o.ingame()
             break
         
            
    def ingame(self):    
     while True:
         o.error()
         ingame = pyautogui.locateOnScreen("1080\ingame.png",confidence=0.6)   
         if ingame !=None:
            print ("Ingame")
            o.exit()
            break
            
    def exit(self):
      while True:
         o.error()
         salir = pyautogui.locateOnScreen("1080\exit.png",confidence=0.6)
         if salir != None:
             print ("exit found")
             time.sleep(3)
             pyautogui.press("esc")
             o.ok()
             break  
             
    def ok(self):
      while True:
         o.error()
         ok1 = pyautogui.locateOnScreen("1080\ok.png",confidence=0.6)
         if ok1 != None:
             print ("ok")
             pyautogui.press("space")
             e.results()
             break
             
    def results(self):
      while True:
        o.error()
        time.sleep(1)
        result = pyautogui.locateOnScreen("1080\endgame.png",confidence=0.6)
        if result !=None:
            time.sleep(7)
            pyautogui.press("space")
            global money
            global exp
            money=money+30
            exp = exp+15
            print ("You have won",money,"money")
            print ("You have won",exp,"exp")
            o.lobby()

    def error(self):
         disc = pyautogui.locateOnScreen("1080\disconnected.png",confidence=0.6)
         connect = pyautogui.locateOnScreen("1080\connect.png", confidence=0.6)
         connect2 = pyautogui.locateOnScreen("1080\error2.png", confidence=0.6)
         connect3 = pyautogui.locateOnScreen("1080\error3.png", confidence=0.6)
         if connect != None or disc !=None or connect2 != None or connect3 != None :
          print ("error")
          pyautogui.press("space")
          time.sleep(1)
          pyautogui.click()
          pyautogui.press("enter")
          o.lobby()
class HDLow():
    def lobby(self):
     while True:  
        lobby = pyautogui.locateOnScreen("720\lobby.png",confidence=0.6)
        u.error()
        if lobby !=None:
         print ("Lobby")
         pyautogui.click(lobby)
         pyautogui.press("space")
         u.matching()
         break
     
    def matching(self):
     while True:
         u.error()
         match = pyautogui.locateOnScreen("720\search.png",confidence=0.6)
         if match !=None:
             print ("Matching")
             u.ingame()
             break
         
            
    def ingame(self):    
     while True:
         u.error()
         ingame = pyautogui.locateOnScreen("720\ingame.png",confidence=0.6)   
         if ingame !=None:
            print ("Ingame")
            u.exit()
            break
            
    def exit(self):
      while True:
         u.error()
         salir = pyautogui.locateOnScreen("720\exit.png",confidence=0.6)
         if salir != None:
             print ("exit found")
             time.sleep(3)
             pyautogui.press("esc")
             u.ok()
             break  
             
    def ok(self):
      while True:
         u.error()
         ok1 = pyautogui.locateOnScreen("720\ok.png",confidence=0.6)
         if ok1 != None:
             print ("ok")
             pyautogui.press("space")
             u.results()
             break
             
    def results(self):
      while True:
        u.error()
        time.sleep(1)
        result = pyautogui.locateOnScreen("720\endgame.png",confidence=0.6)
        if result !=None:
            time.sleep(7)
            pyautogui.press("space")
            global money
            global exp
            money=money+30
            exp = exp+15
            print ("You have won",money,"money")
            print ("You have won",exp,"exp")
            u.lobby()

    def error(self):
         disc = pyautogui.locateOnScreen("1080\disconnected.png",confidence=0.6)
         connect = pyautogui.locateOnScreen("1080\connect.png", confidence=0.6)
         connect2 = pyautogui.locateOnScreen("1080\error2.png", confidence=0.6)
         connect3 = pyautogui.locateOnScreen("1080\error3.png", confidence=0.6)
         if connect != None or disc !=None or connect2 != None or connect3 != None :
          print ("error")
          pyautogui.press("space")
          time.sleep(1)
          pyautogui.click()
          pyautogui.press("enter")
          u.lobby()



def checkresolution():
    while True:
        fullhd = pyautogui.locateOnScreen("1080\lobby.png")
        if fullhd !=None:
            e.lobby()
        hd = pyautogui.locateOnScreen("720\lobby.png")
        if hd !=None:
            i.lobby()
        fullhdlow = pyautogui.locateOnScreen("1080\lobby.png", confidence=0.6)
        if fullhdlow != None:
            o.lobby()
        hdlow = pyautogui.locateOnScreen("720\lobby.png", confidence=0.6)
        if hdlow !=None:
            u.lobby()
       
    

e = FullHD()
i = HD()
o = FullHDLow()
u = HDLow()


money = 0
exp = 0 


print ('1920x1080 = 1')
print ("1280x720 = 2 ")
print ("Auto-Select = 3")


menu = int(input("enter your option : "))




if menu == 1:
    e.lobby()
if menu == 2:
    i.lobby()

if menu == 3:
    checkresolution()
        
if menu <3 or menu >1:
    print ("error")
