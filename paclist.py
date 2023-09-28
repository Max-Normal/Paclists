#!/usr/bin/python3
# Coded by MaxNormal
from core.colors import *
from core.banner import *
from sys import platform, exit
from shutil import which
from time import sleep
from os import system

system("clear")

VERSION = "1.0.0"


print(C + banner)

if platform != "linux":
	exit(1)
else:
	pass


print(C + "[" + G + "+" + C + "]" + B + " Version: " + R + VERSION)
print(C + "[" + G + "+" + C + "]" + B + " Platform: " + R + platform)
print(C + "[" + G + "*" + C + "]" + B + " Checking compatibility: ")

path_pacman = which("pacman")
sleep(1)

if path_pacman == None:
	print('\n' + R + "Pacman (package manager) is not installed! ")
else:
	print(C + "[" + G + "*" + C + "]" + R + " Success")

sleep(1)

print("\n" + C + "[" + G + "+" + C + "]" + B + " [1] Install packages from paclst (Pacman): " + W)
print("\n" + C + "[" + G + "+" + C + "]" + B + " [2] Install packages from paclst (Yay): " + W)
print(C + "[" + G + "+" + C + "]" + B + " [3] Create paclst: ")

option = int(input(C + "[" + G + "?" + C + "]" + B + " What do you want to do? : " + W))


if option == 1:
	filename = input("\n" + C + "[" + G + "?" + C + "]" + B + " Enter paclst filename without .paclst: " + W)
	filename = filename + ".paclst"
	f = open(filename, 'r')
	for word in f:
		system("sudo pacman -S --noconfirm " + word)
if option == 2:
	filename = input("\n" + C + "[" + G + "?" + C + "]" + B + " Enter paclst filename without .paclst: " + W)
	filename = filename + ".paclst"
	f = open(filename, 'r')
	for word in f:
		system("yay -S --noconfirm " + word)
elif option == 3:
	filename = input("\n" + C + "[" + G + "?" + C + "]" + B + " Enter new paclst filename without .paclst: " + W)
	filename = filename + ".paclst"
	f = open(filename, 'a')
	try:
		while True:
			package = input("\n" + C + "[" + G + "?" + C + "]" + B + " Enter package name ! Press Ctrl + C to save: " + W)
			package = package + "\n"
			f.write(package)
	except KeyboardInterrupt:
		print("\n" + C + "[" + G + "+" + C + "]" + B + " Goodbye! All changes saved to : " + filename)
		f.close()

else:
	print(C + "[" + G + "-" + C + "]" + R + " Wrong number! Please, restart program")
	exit(1)
