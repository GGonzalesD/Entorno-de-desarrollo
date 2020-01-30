#!/usr/bin/python3

import os, sys, json, colorama, glob
from pathlib import Path

sys.argv.pop(0)

colorama.init()

PATH = os.getcwd()
returnw = lambda : os.chdir(PATH)

HOME = Path.home().__str__()

# Colores
CRESET = colorama.Style.RESET_ALL
CRED	= lambda txt: colorama.Fore.LIGHTRED_EX + txt + CRESET
CBLU	= lambda txt: colorama.Fore.LIGHTBLUE_EX + txt + CRESET
CYEL	= lambda txt: colorama.Fore.LIGHTYELLOW_EX + txt + CRESET
CMAG	= lambda txt: colorama.Fore.LIGHTMAGENTA_EX + txt + CRESET
CCYA	= lambda txt: colorama.Fore.LIGHTCYAN_EX + txt + CRESET
CGRE	= lambda txt: colorama.Fore.LIGHTGREEN_EX + txt + CRESET

FILEEDIT = ".py_programming"

for i in sys.argv:
	if i[0] != '-':
		FILEEDIT = i
		break

INFO = {
	"editor": "nano",
	"leng": "cpp",
}

# Cargar Configuracion
def read_config():
	global INFO

	os.chdir(HOME)
	with open(".py_programming.json", "r") as f:
		INFO = json.loads(f.read())
	returnw()


def save_config():
	global INFO
	os.chdir(HOME)
	with open(".py_programming.json", "w") as w:
		w.write( json.dumps(INFO, indent="\t") )
	returnw()

os.chdir(HOME)
if not (".py_programming.json" in glob.glob(".*")):
	save_config()
read_config()


def new_file():
	returnw()
	with open(f"{FILEEDIT}.{INFO['leng']}", "w") as f:
		if INFO["leng"].upper() == "CPP":
			f.write("#include<iostream>\n\n")
			f.write("using namespace std;\n\n")
			f.write("int main(){\n\n}\n")
		if INFO["leng"].upper() == "PY":
			f.write("#!/usr/bin/python3\n\n")
			f.write("def main(*argv, **kargv):\n\tpass\n")
			f.write("\nif __name__ == '__main__':\n\tmain()\n")

def execute_file():
	returnw()
	if INFO["leng"].upper() == "CPP":
		os.system(f"sudo chmod +x {FILEEDIT}.o")
		os.system(f"./{FILEEDIT}.o")
	if INFO["leng"].upper() == "PY":
		os.system(f"sudo chmod +x {FILEEDIT}.{INFO['leng']}")
		os.system(f"./{FILEEDIT}.{INFO['leng']}")

	input("____________________________\n")

def compil_file():
	returnw()
	if INFO["leng"].upper() == "CPP":
		return os.system(f"g++ {FILEEDIT}.{INFO['leng']} -o {FILEEDIT}.o")
	if INFO["leng"].upper() == "PY":
		return 0

def edit_file():
	returnw()
	os.system(f"{INFO['editor']} {FILEEDIT}.{INFO['leng']}")
	if compil_file() == 0:
		execute_file()
	else:
		input("ERROR: Error de codigo o compilacion")

def save_file():
	input("Aun no :/")

def config():
	global INFO

	os.chdir(HOME)
	txt = input(CCYA("Editor") + CYEL("[") + CGRE(f"\"{INFO['editor']}\"") + CYEL("]: "))
	if txt != '':
		INFO["editor"] = txt

	print()
	print(CMAG("* ") + CBLU("cpp"))
	print(CMAG("* ") + CBLU("py"))
	txt = input(CCYA("Leng") + CYEL("[") + CGRE(f"\"{INFO['leng']}\"") + CYEL("]: "))
	if txt != '':
		INFO["leng"] = txt.lower()

	save_config()
	read_config()
	returnw()

def chooce_options():
	while True:
		returnw()
		if not (f"{FILEEDIT}.{INFO['leng'].lower()}" in glob.glob(".*") + glob.glob("*")):
			new_file()

		os.system("clear")
		print(f"filename: {FILEEDIT}.{INFO['leng'.lower()]}")

		print()
		with open(f"{FILEEDIT}.{INFO['leng']}", "r") as f:
			for i in range(6):
				print(end=CRED(f"{i+1}.  ") + CYEL(f"{f.readline()}"))
		print()

		_ = input(CYEL("[") + CRED(" X exit") +\
			CYEL(" / ") + CGRE("E edit") +\
			CYEL(" / ") + CMAG("C exec") +\
			CYEL(" / ") + CCYA("S Save") +\
			CYEL(" / ") + CBLU("N new") +\
			CYEL(" / ") + CYEL("O Conf ") +\
			 CYEL("]: "))
		_ = _.upper()

		os.system("clear")

		if _ == "X":
			exit(0)
		elif _ == "N":
			new_file()
		elif _ == "C":
			execute_file()
		elif _ == "E":
			edit_file()
		elif _ == "O":
			config()

for i in sys.argv:
	if i == "-new":
		new_file()
	if "-len=" in i:
		i = i.replace("-len=", "")
		INFO["leng"] = i
	if "-edit=" in i:
		i = i.replace("-edit=", "")
		INFO["edit"] = i
	if "-name=" in i:
		i = i.replace("-name=", "")
		FILEEDIT = i
		i = i.split(".")[-1]
		if i in ("py", "cpp"):
			INFO["leng"] = i


	if "-help" == i:
		print("-new=	: Nuevo Archivo")
		print("-edit=	: Editor de archivo")
		print("-len=	: Lenguaje")
		print("-name=	: File name")
		exit()

chooce_options()
