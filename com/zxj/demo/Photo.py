class Photo:
    def __init__(self,cookedLevel):
        self.cookedString="生的"
        self.cookedLevel=cookedLevel

    def __str__(self):
        return "photo状态%s(%d)"%(self.cookedString,self.cookedLevel)
    def cook(self,cook_time):
        if cook_time>=0 and cook_time<3 :
            self.cookedString="生的"
        elif cook_time>=3 and cook_time<5 :
            self.cookedString="banshengbushu"
        elif cook_time>=5 and cook_time<8:
            self.cookedString="shule"
        elif cook_time>8:
            self.cookedString="hule"


photo = Photo(1)
photo.cook(1)
print(photo)
p = Photo(6)
print(p)
# print(Photo(6))