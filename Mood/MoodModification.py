class MoodModification :
    def __init__(self, tanggal, rate, relaxLevel, energyLevel) :
        self.tanggal = tanggal
        self.rate = rate
        self.relaxLevel = relaxLevel
        self.energyLevel = energyLevel

    def getTanggal(self) :
        return self.tanggal
    
    def getRate(self) :
        return self.rate
    
    def getRelaxLevel(self) :
        return self.relaxLevel
    
    def getEnergyLevel (self) :
        return self.energyLevel

    def modifyData(self,rate=None,relaxLevel=None,energyLevel=None) :
        # Melakukan perubahan data mood hasil validasi dan pengecekan oleh controller.
        if (rate != None) :
            self.rate = rate
        if (relaxLevel != None) :
            self.relaxLevel = relaxLevel
        if (energyLevel != None) :
            self.energyLevel = energyLevel