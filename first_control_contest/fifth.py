class GasHolder:
    R = 8.31

    def __init__(self, volume):
        if volume < 0:
            raise ValueError
        self.volume = volume
        self.temperature = 273
        self.total_moles = 0

    def inject(self, m, M):
        if m < 0 or M <= 0:
            raise ValueError
        moles = m / M
        self.total_moles += moles

    def heat(self, dT):
        self.temperature += dT

    def cool(self, dT):
        self.temperature -= dT
        if self.temperature < 0:
            self.temperature = 0

    def get_pressure(self):
        if self.total_moles == 0:
            return 0
        pressure = (self.total_moles * self.R * self.temperature) / self.volume
        return pressure
