## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Sample](#sample)
* [Problem](#problem)

## General info
Dictonary App with text-to-Speech and Speech-to-text

Short Keys -
* Control + r = Clear
* Control + w = Close
* Escape = Clear
* Enter = Focus on TextBox
	
## Technologies
Project is created using following libraries:
* Python 
* Tkinter 
* Pillow 
* difflib 
* json 
* speech recognition
* pyttsx3

## Setup
To run this project, download it locally:

```
$ cd /path/of/file
$ py app.py
```
before running make sure you 
install pyttsx3 and speech recognition
```
$ pip install pyttsx3
$ pip install SpeechRecognition
```

While running pyttxs3 
if you get this error 
`ImportError: No system module 'pywintypes' (pywintypes38.dll)`

As for me it worked by copying pythoncon38.dll and pywintypes38.dll from:

> C:\users\"YourUserName"\AppData\Roaming\Python\Python38\site-packages\pywin32_system32

to 
> C:\users\"YourUserName"\AppData\Roaming\Python\Python38\site-packages\win32\lib

> C:\users\"YourUserName"\AppData\Roaming\Python\Python38\site-packages\win32

## Sample
- Dictionary App  
![](sample.gif)

## Problem
1. While read other function stop working.
2. Converting audio to text is done by google translator, So internet is required.
