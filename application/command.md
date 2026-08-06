### Pyinstaller command (onedir)
```bash
pyinstaller --noconfirm --onedir --windowed \
--name FCD \
--hidden-import=mplcyberpunk \
--collect-all mplcyberpunk \
--target-architecture arm64 \
--add-data "data:data" \
--add-data "controller:controller" \
--add-data "tools:tools" \
./main.py
```
**Setup wizard**
```bash
pkgbuild \
  --root dist/FCD.app \
  --identifier com.nexgenppt.fcd \
  --version 0.0.0 \
  --install-location /Applications \
  FCD_Installer.pkg
```

#### Push arduino code to controller command:
**compile** 
```bash
arduino-cli compile --fqbn rp2040:rp2040:adafruit_feather_can controller
```

**upload** 
```bash
arduino-cli upload -p /dev/tty.usbmodem101 --fqbn rp2040:rp2040:adafruit_feather_can controller
```

**installer:** https://github.com/arduino/arduino-cli/releases 







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

pyinstaller --noconfirm --onedir --windowed \ 
  --hidden-import=mplcyberpunk \
  --collect-all mplcyberpunk \
  --add-data "/Users/zying/Desktop/ISU/Work/NexGenPPT/fcd-gui-tests-main/fcd-gui-tests/application/data:data/" \
  --add-data "/Users/zying/Desktop/ISU/Work/NexGenPPT/fcd-gui-tests-main/fcd-gui-tests/controller:controller/" \
  "/Users/zying/Desktop/ISU/Work/NexGenPPT/fcd-gui-tests-main/fcd-gui-tests/application/main.py"

pyinstaller --noconfirm --onedir --noconsole \
--hidden-import=mplcyberpunk \
--collect-all mplcyberpunk \
--add-data "/Users/zying/Desktop/ISU/Work/NexGenPPT/fcd-gui-tests-main/fcd-gui-tests/application/data:data/" \
--add-data "/Users/zying/Desktop/ISU/Work/NexGenPPT/fcd-gui-tests-main/fcd-gui-tests/application/controller:controller/" \
--add-data "/Users/zying/Desktop/ISU/Work/NexGenPPT/fcd-gui-tests-main/fcd-gui-tests/application/tools:tools/" \
"/Users/zying/Desktop/ISU/Work/NexGenPPT/fcd-gui-tests-main/fcd-gui-tests/application/main.py"