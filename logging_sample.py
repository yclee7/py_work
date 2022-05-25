import os, platform, logging

import time
import  keyboard
from PIL import ImageGrab


if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'),
                                os.getenv('HOMEPATH'),
                                'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'),
                                'test.log')

print(os.getenv('HOMEDRIVE'))
print(os.getenv('HOMEPATH'))
print("Logging to", logging_file)

#exe_path = os.get_exec_path()
#print(exe_path)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename = logging_file,
    filemode = 'w+',
)


def screenshot():
    cur_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(cur_time))
    logging.info("image{}.png".format(cur_time) + " write")


keyboard.add_hotkey("F9", screenshot)


logging.debug("Start of the program")
logging.info("second:Doing something")
logging.warning("Dying now")

keyboard.wait("esc")