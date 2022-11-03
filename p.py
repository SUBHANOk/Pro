import os, platform

try:

        import requests

except:

        os.system('pip2 install requests')

import requests

bit = platform.architecture()[0]

if bit == "64bit":

        from Pro_64 import m

        m()

elif bit == "32bit":

        from Pro_32 import m

        m()







