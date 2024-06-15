# QR Gener Learn

## What is it?
This is a QR Code generation program, written fully in Python, currently existing as program run an interacted with from a commandline.  
It uses one public library - the qrcode 7.4.2  
I am currently writing it at a hobbyist's pace one can see on my activity bar.  
Hopefully this can be part of my portfolio allowing me to find work as a tester or a developer in 2024.  

## What does it do?
This program generates QR Codes from input data.
Input data can be text entered into cmd or as a name of text file in working directory. 
Contents of text files can be processed in 2 ways: in entirety or read line by line, treating 
every line as separate piece of input data to be processed (ergo batch processing).
One can also specify output settings manually. The entered settings get processed and passed in 
correct format to the underlying qrcode library 

### This branch is currently inactive. 
It was my first push and a proof-of-concept. The code is bad and for each of the features 
(input to qr-code, text in file to qr-code, each line in file to a separate qr-code)
there is a separate function of conversion. It works though and taught me a lot about plain Python.  

I am currently working in the refactor branch and will rebase pull request back into the main once I figure out
how to do it without failing in a spectacular way and having to redo this project's github from scratch.

## But why?
This little project is above all a learning experience. It allows me to get comfortable with:  
*interacting with code I have not personally written  
*simple Python data structures, return values and argument passing  
*making use of external APIs and packages passing data to them and getting data in return  
*version control and github interactions. Atomic commits, pushing to remote, branching, Markdown 
and doing it regularily and with intent as part of normal workflow.  
*adding features incementally  
*refactoring and performance improvements, including knowing when to abstract and refactor  

## Updates
See refactor branch
