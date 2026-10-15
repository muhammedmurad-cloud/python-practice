class Light:
    def __init__(self):
        self.is_on = False
    def turn_on(self):
        self.is_on = True
        return "Light is on"
    def turn_off(self):
        self.is_on = False
        return "Light is off"
    def status(self):
        state = "on" if self.is_on else "Off"
        return f"Current status:{state}"   

light = Light()
light.turn_on()
light.turn_off()
print(light.status())
