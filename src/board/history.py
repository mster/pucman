# this will be temporary and removed with A* 

class History():
    def __init__(self, maxLen):
        # bind
        self.maxLen = maxLen

        # props
        self._ = []

    def eq(self, pos):
        self._.append(pos)
        while (len(self._) >= self.maxLen): self._.pop(0)
