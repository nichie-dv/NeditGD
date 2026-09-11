@echo off
echo Uninstalling NeditGD...
py -3.12 -m pip uninstall NeditGD -y

echo.
echo Installing NeditGD from local folder...
py -3.12 -m pip install --force-reinstall .

echo.
echo Verifying installation...
py -3.12 -c "import NeditGD; print(NeditGD.__file__)"