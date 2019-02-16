import RPi.GPIO as GPIO
import time

class Flash:

    def __init__(self, BCM_NUM=19):

        #self.count = COUNT
        self.bcm_num = BCM_NUM
        GPIO.setmode(GPIO.BCM)  #GPIOへアクセスする番号をBCMの番号で指定することを宣言します。                        
        GPIO.setup(self.bcm_num, GPIO.OUT) #BCMの4番ピン、物理的には10番ピンを出力に設定します。                                

    def flash(self, COUNT):
        self.count = COUNT

        try:
            for _i in range(self.count):
                GPIO.output(self.bcm_num, GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(self.bcm_num, GPIO.LOW)
                time.sleep(0.1)

        except KeyboardInterrupt:
            GPIO.output(self.bcm_num, GPIO.LOW)

    def __del__(self):
        GPIO.cleanup(self.bcm_num)
        
"""
class FlashAlt(Flash):

    def __init__(self, BCM_NUM=19, BCM_NUM2=13):

        super().__init__(self, BCM_NUM=19)
        self.bcm_num2 = BCM_NUM2
        GPIO.setup(self.bcm_num2, GPIO.OUT)

    def flash_alt(self, COUNT):

        try:
            for _i in range(round(COUNT)):
                GPIO.output(self.bcm_num2, GPIO.LOW)
                GPIO.output(self.bcm_num, GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(self.bcm_num, GPIO.LOW)
                GPIO.output(self.bcm_num2, GPIO.HIGH)
                time.sleep(0.1)

        except KeyboardInterrupt:
            GPIO.output(self.bcm_num, GPIO.LOW)
            GPIO.output(self.bcm_num2, GPIO.LOW)

    def __del__(self):
        super().__del__(self)
        GPIO.cleanup(self.bcm_num2)

"""


if __name__ == '__main__':
    flash()