# PDF-Rapid ![image](https://user-images.githubusercontent.com/89847158/152180139-ed977a1d-c66c-4242-b4a9-a087eed931af.png)

![image](https://user-images.githubusercontent.com/89847158/152192610-7f2410c1-d7e2-47b5-8024-3943a82a030b.png)


PDF-Rapid is a handsfree fully automated python script that can run the **pdf-id** legendery tool on multiple files.
This tool is not a PDF parser, but it will scan a file to look for certain PDF keywords, allowing you to identify PDF documents that contain (for example) JavaScript or execute an action when opened. PDFiD will also handle name obfuscation.

**The idea**

This tool is designed for a Cyber security analyst who deals with PDF file investigations and finds himself spending a lot of time in front of CLI.
Instead of re-running the pdf-id on each file individually, PDF-Rapid will do it independently and quickly. Each submission to PDF-ID is done by a new subprocess which sends the stdout to a new file called Log.txt which will open in the folder where the EXE file is stored.

**How to use**

PDF-Rapid is build to be simple , download or copy the source code for rep and save it as python file at you local computer.
You can put it any where you would like to, my recommendation is to open new directory for it. 
The directory that PDF-Radpid located will be the main operating dir.
Grab as many as PDF-Files you want and just paste them at the same folder the script located.
Open CMD and run "python pdf-rapid1.0.py" , then let the tool do his work.

**The Script FLOW**

the script will load when you run the command , then it will start his flow by the following -
1. Run search for pdf-id on the local machine.
2. when found , the script will then search for any PDF files at the same **CWD**, if not found the script will print an error and ask you to move the files to the CWD and type again when moved.
3. the script will list all the files found and print it
4. The script will then open new subprocess for pdf-id and will pass the pdf file by order for analysis.
5. All outputs will be saved in CWD as one file named log.txt

**VT Scans**

There is an exe version which is 100% self-running but identified due to the approaches to process and os as a malicious tool. I enclose for you both the source code and the EXE file.
I will also attach the original HASH and VT scans for it.

![image](https://user-images.githubusercontent.com/89847158/152184645-636c59ef-a575-4e8e-b0a1-b8c139bf1605.png)

![image](https://user-images.githubusercontent.com/89847158/152184796-36323055-82f9-4dd8-8cde-91d88d9e10ac.png)

![image](https://user-images.githubusercontent.com/89847158/152189875-805e3c26-ffbf-4639-a3f6-6aad9a6ed1e1.png)

![image](https://user-images.githubusercontent.com/89847158/152192124-deb68a62-9fce-48dd-84dd-d2299128b5e9.png)



**Compatibility requirements:**

Python 2.7 and above
pdf-id original script can be found here : 
https://github.com/Rafiot/pdfid OR at https://blog.didierstevens.com/programs/pdf-tools/


**Copyright is for the original script creators only ! I did not edit, modify or add anything other than the build of the automation script which was built by me**


**Misc**

This is my first foray into creating a theme, so if you see something amiss, please feel free to [file an issue!](https://github.com/R4wraith/PDF-Rapid/issues) I'm sure there are things I missed.

Any relevant changes for each version are documented in the changelog. Please update and check the changelog before filing any issues, as they may have already been taken care of.

