from platform import platform

BLUE = chr(27) + "[0;34m"
GREEN = chr(27) + "[0;32m"
RED = chr(27) + "[0;31m"
YELLOW = chr(27) + "[1;33m"
RESET = chr(27) + "[0m"

if "win" in platform().lower():
    BLUE = ""
    GREEN = ""
    RED = ""
    YELLOW = ""
    RESET = ""


