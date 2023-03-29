import subprocess
import time

subprocess.call("adb shell input  swipe 900 1600 900 0")
time.sleep(2)
subprocess.call("adb shell am start -n  com.android.settings/com.android.settings.Settings")
time.sleep(2)
subprocess.call("adb shell input tap 300 1400")
time.sleep(2)
for i in range(2):
    subprocess.call("adb shell input tap 900 500")
time.sleep(2)
for i in range(3):
    subprocess.call("adb shell input keyevent 4")

