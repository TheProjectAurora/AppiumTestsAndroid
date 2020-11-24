from robot.api import logger

def get_variables(environment='local_on_device_hw'):
    variables = {
        "DEVICE_NAME":"<device name>",
        "PLATFORM_VERSION":"10",
        "IMPLICIT_WAIT_PERIOD":"5", # in seconds
        "APPIUM_SERVER":"http://127.0.0.1:4723/wd/hub",
        "VALID_USERNAME": '<username>',
        "VALID_PASSWORD": '<password>',
    }
    if 'emulator' in environment:
        variables['DEVICE_NAME'] = 'Android Emulator'
        variables['PLATFORM_VERSION'] = '11'

    return variables