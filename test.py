#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "pyfiglet>=1.0.4",
# ]
# ///

# -*- coding: utf-8 -*-

from time import sleep
import pyfiglet

with open("pyfigletfonts.txt", "r") as file:
    fonts = file.read().splitlines()

for fonty in fonts:
    print("Testing font " + fonty)
    f = pyfiglet.Figlet(font=fonty, width=80)
    print(f.renderText('FooBar'))
    sleep(0.8)