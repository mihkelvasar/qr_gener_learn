# QR Gener Learn

## What is it?
This is a QR Code generation program, written fully in Python, currently existing as program run an interacted with from a commandline.  
It uses one public library - the qrcode 7.4.2  
I am currently writing it at a hobbyist's pace one can see on my activity bar.  
Hopefully this can be part of my portfolio allowing me to find work as a tester or a developer in 2024.  

## How does refactor branch differ from main branch?
Main branch was written as a proof of concept. It is functional code but it is also bad code. 
As it cannot be easily extended or modified without breaking major (for the code) functionality.  
Refactor branch is the current working directory where new features are added. The filesnames between master
and refactor are different because:  
1. this is my first branching
2. I did not feel comfortable tearing apart the only local copy of a (then) high-value code for me

## What does it do?
This program generates QR Codes from input data.
Input data can be text entered into cmd or as a name of text file in working directory. 
Contents of text files can be processed in 2 ways: in entirety or read line by line, treating 
every line as separate piece of input data to be processed (ergo batch processing).

In input-based menu one can select predetermined manual conversion settings or specify their own,
with full input verification and processing for passing the data to qrcode library.

One can also specify a name of source file from cmd, name of output file, and for batch processing
there is an inbuilt counter in file naming for the sake of clarity.

As of latest commit it also now allows selecting foreground and backgroud colors as rgb values.
Currently it does not work. The data gets entered, verified and passed around fine, but nothing
makes use of it. It might require Pillow I think.

## But why?
This little project is above all a learning experience. It allows me to get comfortable with:  
*interacting with code I have not personally written  
*simple Python data structures, return values and argument passing  
*making use of external APIs and packages passing data to them and getting data in return  
*version control and github interactions. Atomic commits, pushing to remote, branching, Markdown 
and doing it regularily and with intent as part of normal workflow.  
*adding features incementally  
*refactoring and performance improvements, including knowing when to abstract and refactor  

## What's next?
1. I want to  
-get colored QR code output working  
-add a global externally saved counter to tell me how many items I have converted total  
-add buffer overflow exception handling if data to converted is too long for even default
settings  
-perhaps add caching for reading data from file in batch processing  
-add an after-menu, offering redirects to main menu or exit  

2. future ideas  
-fully automated testing using unittest  
-build a DOS or early Windows-style GUI with TKinter or other GUI library  
-compile it into a separate executable.  
-rewrite it all in JavaScript  

## Updates
See commit history of the readme.
