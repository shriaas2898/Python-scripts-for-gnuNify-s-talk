import os
while(1):
	file = input("Enter file name")
	choice = int(input("Enter your choice\n1.Find file \n2.Delete a file"))
	if(choice == 1):
		path = os.path.abspath(file)
		print(path)
	elif choice == 2:
		if os.path.exists(file):
			os.remove(os.path.abspath(file))
			print("The file %s has been deleted successfully"%file)
		else:
			print("No such file is found")
	choice = input("Enter your choice\n1.Continue\n2.Exit")
	if choice!=1:
		break

