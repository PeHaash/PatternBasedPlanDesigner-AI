:: This is a simple build file to compile .cpp files separately.
:: build "FileName"     :: will update the FileName.o from FileName.cpp & link them & run them
:: build all            :: will update all of the build files & link them & run them
:: flag -nl             :: Do not like and execute the code
:: flag -nr             :: will link but do not run the code

@echo OFF

set flag=%2
if [%1]==[] (exit /b)
if [%2]==[] (set flag=xx)

echo [BUILD] COMPILING STARTED!
if %1 ==all (g++ *.cpp -std=c++20 -Wall -c) else (g++ %1.cpp -std=c++20 -Wall -c)
if %ERRORLEVEL% NEQ 0    (echo [BUILD] END UNSUCCESSFUL && exit /b)
if %flag% ==-nl          (echo [BUILD] COMPILE IS DONE BUT WILL NOT LINK - END SUCCESSFUL && exit /b)

echo [BUILD] LINKING STARTED!
g++ *.o -std=c++20 -Wall -o main.exe 
if %ERRORLEVEL% NEQ 0   (echo [BUILD] END UNSUCCESSFUL && exit /b)
if %flag% ==-nr         (echo [BUILD] MAIN.EXE IS READY BUT WILL NOT RUN - END SUCCESSFUL && exit /b)

echo [BUILD] LET'S RUN!
main.exe

echo [BUILD] END SUCCESSFUL
exit /b