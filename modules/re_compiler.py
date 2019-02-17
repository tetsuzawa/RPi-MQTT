import re

class ReMatch:
    
    def __init__(self, ORIGINAL_TEXT, TEXT):
        #self.original_text = ORIGINAL_TEXT
        #self.teot = TEXT
        self.re_pattern = re.compile(r"%s\s?"%TEXT, re.IGNORECASE)
        try:
            self.match = self.re_pattern.match(ORIGINAL_TEXT)
            print(self.match == None)
            self.res = self.match.group()
            self.start = self.match.start() 
            self.end = self.match.end() 
        except:
            self.res = None
            self.start = None
            self.end = None

    def severe_check(self):
        pass