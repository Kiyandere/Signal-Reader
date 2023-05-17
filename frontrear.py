from maxgain import MaxGain

class FrontRear:
    def __init__(self):
        self.front_gain = None
        self.rear_gain = None

    def execute(self):
        print("Option FrontRear selected.")
        self.get_front()
        self.get_rear()
        fr_ratio = self.calculate_fr_ratio()
        print("The front-to-rear ratio of the antenna is: {}".format(fr_ratio))

    def get_front(self):
        # this requires finding MaxGain
        # however, MaxGain need to be implement diffrerently

        self.front_gain = MaxGain()

    
    def get_rear(self):
        # this need to be implemented

        self.rear_gain = 0
        
    
    def calculate_fr_ratio(self, wavelength):
        #calculate the front-to-rear ratio of the antenna
        frRatio = self.front_gain / self.rear_gain
        return frRatio