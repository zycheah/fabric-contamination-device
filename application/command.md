pyinstaller --noconfirm --onefile --console \
  --hidden-import=mplcyberpunk \
  --collect-all mplcyberpunk \
  --add-data "/Users/zying/Downloads/fcd-gui-tests-main/fcd-gui-tests/application/data:data/" \
  --add-data "/Users/zying/Downloads/fcd-gui-tests-main/fcd-gui-tests/controller:controller/" \
  "/Users/zying/Downloads/fcd-gui-tests-main/fcd-gui-tests/application/main.py"



pyinstaller --noconfirm --onedir --windowed \
  --hidden-import=mplcyberpunk \
  --collect-all mplcyberpunk 
  --add-data "/Users/zying/Downloads/fcd-gui-tests-main/fcd-gui-tests/application/data:data/" \
  --add-data "/Users/zying/Downloads/fcd-gui-tests-main/fcd-gui-tests/controller:controller/" \
  "/Users/zying/Downloads/fcd-gui-tests-main/fcd-gui-tests/application/main.py"


  --target-architecture universal2 \

**Pyinstaller command (onedir)**
pyinstaller --noconfirm --onedir --windowed \ 
  --hidden-import=mplcyberpunk \
  --collect-all mplcyberpunk \
  --add-data "/Users/zying/Desktop/ISU/Work/NexGenPPT/fcd-gui-tests-main/fcd-gui-tests/application/data:data/" \
  --add-data "/Users/zying/Desktop/ISU/Work/NexGenPPT/fcd-gui-tests-main/fcd-gui-tests/controller:controller/" \
  "/Users/zying/Desktop/ISU/Work/NexGenPPT/fcd-gui-tests-main/fcd-gui-tests/application/main.py"


**Push arduino code to controller command:**
**compile** arduino-cli compile --fqbn rp2040:rp2040:adafruit_feather_can controller
**upload** arduino-cli upload -p /dev/tty.usbmodem101 --fqbn rp2040:rp2040:adafruit_feather_can controller
**installer** https://github.com/arduino/arduino-cli/releases 