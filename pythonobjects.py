import time

class MasterPiInterface:

    def __init__(self):
        self.led = False
        return
    
    def switch_led(self, value=True):
        self.led = value
        print("LED",self.led)
        return

#INHERITS ALL CODE FROM MASTERPIINTERFACE
class Robot(MasterPiInterface):

    def __init__(self, music):
        super().__init__()
        self.status = "Ready"
        self.command = None
        self.music = music
    
    def move(self):
        if self.status == "Ready":
            print("moving")
            self.status = "Moving"
            time.sleep(2)
            self.status = "Ready"

    def play_music(self):
        print(self.music)
        return

robot1 = Robot("missionimpossible.mp3")
robot1.play_music()
robot1.switch_led()
robot2 = Robot("bad.mp3")
robot2.play_music()
robot2.switch_led(value=False)

class SoundInterface:

    def __init__(self):
        self.voice = 'english'
        self.accent = "irish"
        self.music = "With or without you"
        return
    
    def play(self):
        print("Music", self.music)
        return

    def stop(self):
        print("Music stopped")
        return
    

        