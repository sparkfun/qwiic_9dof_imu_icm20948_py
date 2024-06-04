from machine import SoftI2C, Pin
import micropython_icm20948
import time
i2c = SoftI2C(scl=Pin(5), sda=Pin(4), freq=400000)
print(i2c.scan())
def runExample():

    print("\nSparkFun 9DoF ICM-20948 Sensor  Example 1\n")
    IMU = micropython_icm20948.QwiicIcm20948(address=104, i2c_driver=i2c)



    IMU.begin()

    while True:
        if IMU.dataReady():
            IMU.getAgmt() # read all axis and temp from sensor, note this also updates all instance variables
            print(IMU.axRaw, IMU.ayRaw, IMU.azRaw)
            print(IMU.gxRaw, IMU.gyRaw, IMU.gzRaw)
            print(IMU.mxRaw, IMU.myRaw, IMU.mzRaw)

            time.sleep(0.03)
        else:
            print("Waiting for data")
            time.sleep(0.5)

if __name__ == '__main__':
    try:
        runExample()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 1")

