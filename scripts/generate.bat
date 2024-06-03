@echo off
for %%f in ("ui\*") do python -m PyQt5.uic.pyuic -x ui/%%~nf.ui -o src/generated/%%~nf.py