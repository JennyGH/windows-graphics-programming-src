@ECHO OFF
@CALL python GenerateCMakeLists.py
@MKDIR build
@CD build
@CALL cmake ..
