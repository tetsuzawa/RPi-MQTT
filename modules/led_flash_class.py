import RPi.GPIO as GPIO
import time

class Flash:
    def __init__(self, COUNT, BCM_NUM):

        self.count = COUNT
        self.bcm_num = BCM_NUM
        GPIO.setmode(GPIO.BCM)  #GPIOへアクセスする番号をBCMの番号で指定することを宣言します。                        
        GPIO.setup(self.bcm_num, GPIO.OUT) #BCMの4番ピン、物理的には10番ピンを出力に設定します。                                

    def flash(self):

        try:
            for _i in range(self.count):
                GPIO.output(self.bcm_num, GPIO.LOW)
                time.sleep(0.1)
                GPIO.output(self.bcm_num, GPIO.HIGH)
                time.sleep(0.1)
            GPIO.cleanup()

        except KeyboardInterrupt:
            GPIO.cleanup()

    def __del__(self):
        GPIO.cleanup()

if __name__ == '__main__':
    flash()