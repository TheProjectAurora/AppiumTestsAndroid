The wikipedia APK file can be downloaded from:
https://www.apkmirror.com/apk/wikimedia-foundation/wikipedia/wikipedia-2-7-50324-release/wikipedia-2-7-50324-r-2020-06-29-android-apk-download/

# To install the app to the phone:
adb install C:\Users\<username>\Documents\<PathToApkFile>\<filename>.apk

# Check the available phones:
	adb devices
	List of devices attached
	<device name>        device

# in order to lauch the app in robot, we need the package name and the activity name
# <packagename> is wikipedia
# i.e. appPackage=app.com.<packagename>  appActivity=app.com.View.SplashScreen

> npm cache clean --force
> C:\Users\<username>\AppData\Local\Android\Sdk\platform-tools\adb.exe -s <device name> install
> -r C:\Users\<PathToApkFile>\appium-uiautomator2-server-v4.5.5.apk

# How to retrive package name
# Check the packages installed on the phone
> adb -s <device name> shell   (opens a shell in the phone)
> pm list packages
	...
	package:app.com.<packagename>  << our package
	...
	FRT:/ $

# How to retrive the activity name?
# i.e. appActivity=app.com.View.SplashScreen
	#1. List the full path to <packagename> apk file from the phone
		> adb shell pm list packages -f
			...
			package:/data/app/app.com.<packagename>-j2-hqvOFSwArr4UHTKvs5A==/base.apk=app.com.<packagename>
			...

			where /data/app/app.com.<packagename>-j2-hqvOFSwArr4UHTKvs5A==/base.apk is the full path to the apk file in the phone

	#2. Download the apk file using the full path in #1
		> adb pull /data/app/app.com.<packagename>-j2-hqvOFSwArr4UHTKvs5A==/base.apk
		> C:\Users\<username>\Downloads> dir
			> base.apk    << downloaded to local machine

	#3. Retrieve the default launchable activity from the package
		> C:\Users\<username>\Downloads>aapt dump badging base.apk
			...
			launchable-activity: name='app.com.View.SplashScreen'  label='' icon=''
			...

------------------------------------------------------------------------------------------------------------------------------

C:\Users\<username>\AppData\Local\Android\Sdk
adb shell am start -n com.<packagename>/com.package.name.MainActivity
adb shell dumpsys package | grep -Eo "^[[:space:]]+[0-9a-f]+[[:space:]]+com.<packagename>/[^[:space:]]+" | grep -oE "[^[:space:]]+$"
adb shell "dumpsys package | grep -i com.<packagename> | grep Activity"


C:\Users\<username>\AnyFolder>adb -s <device name> shell
FRT:/ $ dumpsys package | grep -i com.<packagename> | grep Activity   <<< DONT USE THIS
1|FRT:/ $ dumpsys package | grep -i com.<packagename>                 <<< USE THIS


am start -n app.com.<packagename>/androidx.core.content.FileProvider



