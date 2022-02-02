import fnmatch
import os,time,pathlib,codecs,sys,subprocess,winsound

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
logo=""" 


                $$\  $$$$$$\                      $$$$$$$\   $$$$$$\  $$$$$$$\ $$$$$$\ $$$$$$$\  
                $$ |$$  __$$\                     $$  __$$\ $$  __$$\ $$  __$$\\_$$  _|$$  __$$\ 
 $$$$$$\   $$$$$$$ |$$ /  \__|                    $$ |  $$ |$$ /  $$ |$$ |  $$ | $$ |  $$ |  $$ |
$$  __$$\ $$  __$$ |$$$$\           $$$$$$\       $$$$$$$  |$$$$$$$$ |$$$$$$$  | $$ |  $$ |  $$ |
$$ /  $$ |$$ /  $$ |$$  _|          \______|      $$  __$$< $$  __$$ |$$  ____/  $$ |  $$ |  $$ |
$$ |  $$ |$$ |  $$ |$$ |                          $$ |  $$ |$$ |  $$ |$$ |       $$ |  $$ |  $$ |
$$$$$$$  |\$$$$$$$ |$$ |                          $$ |  $$ |$$ |  $$ |$$ |     $$$$$$\ $$$$$$$  |
$$  ____/  \_______|\__|                          \__|  \__|\__|  \__|\__|     \______|\_______/ 
$$ |                                                                                             
$$ |                                              all right reserved to Ofek Moalem                                             
\__|                                                                                             
                                                                                                 
"""
clearConsole()
winsound.PlaySound("1.wav", winsound.SND_LOOP | winsound.SND_ASYNC )
drives = ['C:\\','E:\\','F:\\','D:\\']
pattern = "pdfid.py"
def check():
  for rootPath in drives:
    print("Now searching in: ",rootPath)
    for root, dirs, files in os.walk(rootPath) :
        for filename in fnmatch.filter(files, pattern) :
            end = time.time()
            print(f"Great preformance ! .. it took only {round(end-start)} seconds to find it ..")
            return(f"{os.path.join(root, filename)}")

def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

def search_pdf():
	files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.pdf')]
	return files

def main():
	files=[]
	path=check()
	print(f"I have found PDF-ID in this location : {path}")
	time.sleep(2)
	print(f"About to clear the screen in few sec.. ")
	countdown(4)
	clearConsole()
	print(logo)
	print(f"Now searching for any PDF files in CWD -- {pathlib.Path.cwd()}")
	time.sleep(1.5)
	print("This is the list of files ive found .. About to export it to PDF-ID")
	print(' , '.join(files))
	if bool(files) is False : 
		clearConsole()
		print(logo)
	files=search_pdf()
	while bool(files) is False:
		chose=input('Your folder is empty , please copy all pdf files you want to analyze and write "again" to start over or "no" to exit.\n')
		if chose == "again":
			files=search_pdf()
			if bool(files):
				clearConsole()
				print(logo)
				print(f"I Have found this files : {' , '.join(files)}")
				time.sleep(1.5)
				continue
		elif chose == "no" :
			print("Aborted . Bye Bye ..")
			countdown(3)
			os.system("taskkill /f /im cmd.exe")
			break
	countdown(3)
	clearConsole()
	print(logo)
	print("Starting to analysis...")
	for file in files:
		cmd ='python.exe', path , file
		f = open("log.txt", "a")
		subprocess.call(cmd, stdout=f)
		print(f"Finished analysis for file : {file} , prepering the next one in few secounds")
		countdown(2)
	clearConsole()
	print(logo)
	print(f"All files has been analyzed , output data has been saved to log.txt at {pathlib.Path.cwd()}")
	print("Thanks for using PDF-Rapid! see you soon again :)")

start = time.time()
print(logo)
print("Wellcome to PDF-ID Automation ,\nthis script will now search for pdfid file in your pc\nit might take few sec..")
time.sleep(2)
main()
