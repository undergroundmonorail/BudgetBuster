rgbasm -o%~n1.obj %1
rgblink -m%~n1.map -n%~n1.sym -o%~n1.gb %~n1.obj
rgbfix -p255 -v %~n1.gb
pause