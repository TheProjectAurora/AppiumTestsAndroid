START /B appium -a 127.0.0.1 -p 4723
TIMEOUT 10
robot %* --argumentfile default_arguments_hw.txt
npx kill-port 4723

