import RPi.GPIO as GPIO
import time

def flash_yellow():
        
    COUNT = 5
    BCM_NUM = 19
    GPIO.setmode(GPIO.BCM)  #GPIOへアクセスする番号をBCMの番号で指定することを宣言します。                        
    GPIO.setup(BCM_NUM, GPIO.OUT) #BCMの4番ピン、物理的には10番ピンを出力に設定します。                                

    try:
        #while True:
        for _i in range(1, 11):
            GPIO.output(BCM_NUM, GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(BCM_NUM, GPIO.HIGH)
            time.sleep(0.1)
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()

def flash_blue():
        
    COUNT = 5
    BCM_NUM = 13
    GPIO.setmode(GPIO.BCM)  #GPIOへアクセスする番号をBCMの番号で指定することを宣言します。                        
    GPIO.setup(BCM_NUM, GPIO.OUT) #BCMの4番ピン、物理的には10番ピンを出力に設定します。                                

    try:
        #while True:
        for _i in range(1, 11):
            GPIO.output(BCM_NUM, GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(BCM_NUM, GPIO.HIGH)
            time.sleep(0.1)
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()



if __name__ == '__main__':
    flash()