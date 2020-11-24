START /B emulator -avd Nexus_6P_API_30
START /B appium -a 127.0.0.1 -p 4723
TIMEOUT 10
robot %* --argumentfile default_arguments_emu.txt
adb -s emulator-5554 emu kill
npx kill-port 4723
