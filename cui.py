import os
from os import system



def login():
	os.system('clear')
	system('python demo.py')
	input("Press Enter to continue...")
	os.system('clear')


def register():
	os.system('clear')
	system('python sound_recorder.py')
	os.system('clear')
	from train import train
	train ()
	input("Press Enter to continue...")
	os.system('clear')


def sound_recorder():
	os.system('clear')
	system("python sound_recorder.py")
	input("Press Enter to continue...")
	os.system('clear')


def login_file():
	os.system('clear')
	system('python demo_file.py')
	input("Press Enter to continue...")
	os.system('clear')



def plot_data():
	os.system('clear')
	system('python demo_file_trial.py')
	input("Press Enter to continue...")
	os.system('clear')



def plot_voice():
	os.system('clear')
	system('python demo_trial.py')
	input("Press Enter to continue...")
	os.system('clear')


def train():
	os.system('clear')
	print("Train data...")
	from train import train
	train ()
	input("Press Enter to continue...")
	os.system('clear')



def gpio():
	os.system('clear')
	system('python test_lamp_success.py')
	system('python test_lamp_fail.py')
	system('python test_servo.py')
	system('python test_sms.py')
	input("Press Enter to continue...")
	os.system('clear')



# fungsi untuk sub_menu
def sub_menu():
	menu = 0
	while (menu !=7):
		os.system('clear')
		print ("[1] Sound Recorder")
		print ("[2] Login from file")
		print ("[3] Plot audio data from file")
		print ("[4] Plot audio data from voice recorder")
		print ("[5] Manual train data")
		print ("[6] Test GPIO and SMS sender")
		print ("[7] Back")
		
		menu = input("\nWhat would you like to do?\n")

		if menu == "1":
			sound_recorder()
		elif menu == "2":
			login_file()
		elif menu == "3":
			plot_data()

		elif menu == "4":
			plot_voice()
		elif menu == "5":
			train()
		elif menu == "6":
			gpio()
		elif menu == "7":
			return main_menu ()
		else:
			os.system('clear')
			print("\nNot Valid Choice Try again")
			input("Press Enter to continue...")
			os.system('clear')


# fungsi untuk menampilkan menu
def main_menu():
	os.system('clear')
	print ("\n SISTEM AUTENTIFIKASI SUARA")
	print ("----------- MENU ------------")
	print ("[1] Login")
	print ("[2] Register")
	print ("[3] Advanced Tools")
	print ("[4] Exit")
	
	menu = input("\nWhat would you like to do?\n")

	if menu == "1":
		login()
	elif menu == "2":
		register()
	elif menu == "3":
		sub_menu()
	elif menu == "4":
		os.system('clear')
		print("\nGoodbye") 
		exit()
	else:
		os.system('clear')
		print("\nNot Valid Choice Try again")
		input("Press Enter to continue...")
		os.system('clear')


if __name__ == "__main__":

	while(True):
		main_menu()
