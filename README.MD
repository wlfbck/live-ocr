What is this?
=====

A small python program which captures text continuously from designated rectangle on your screen using tesseract OCR.
Everything it recognizes will be sent via network to the configured IP and port using ZeroMQ.

I suggest making the text as clear as possible, for example by having a solid background color and a normal font like Arial or
Times New Roman. Also font size 16 or higher is strongly recommended.

Prerequisites
-----

It is assumed that Tesseract OCR v5 are installed and on the Path.

Starting the program
-----

If you have downloaded the .exe, simply launch it.

If you have downloaded the whole repo, simply launch via `python main.py`. Requires Python 3.10 to be installed.

Configuration
-----

Inside config.ini You can specify the corners of the rectangle for OCR as well as the IP and port of the target to send data to.