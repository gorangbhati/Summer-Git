import os
import platform
import pywhatkit
import time

def system_details():
    print("\nSystem Details:")
    print("System:", platform.system())
    print("Node Name:", platform.node())
    print("Release:", platform.release())
    print("Version:", platform.version())
    print("Machine:", platform.machine())
    print("Processor:", platform.processor())

def create_folder():
    folder_name = input("Enter the folder name: ")
    try:
        os.makedirs(folder_name)
        print(f"Folder '{folder_name}' created successfully.")
    except FileExistsError:
        print("Folder already exists.")
    except Exception as e:
        print("Error:", e)

def create_file():
    file_name = input("Enter the file name (with extension, e.g. file.txt): ")
    try:
        with open(file_name, 'w') as file:
            file.write("This is a new file.\n")
        print(f"File '{file_name}' created successfully.")
    except Exception as e:
        print("Error:", e)

def send_whatsapp_message():
    number = input("Enter your friend's WhatsApp number (with country code, e.g. +911234567890): ")
    message = input("Enter the message to send: ")
    try:
        current_time = time.localtime()
        hour = current_time.tm_hour
        minute = current_time.tm_min + 1  # send one minute later
        pywhatkit.sendwhatmsg(number, message, hour, minute)
        print("Message scheduled to be sent.")
    except Exception as e:
        print("Error:", e)

def shutdown_system():
    confirm = input("Are you sure you want to shut down the system? (yes/no): ")
    if confirm.lower() == "yes":
        os.system("shutdown /s /t 1" if platform.system() == "Windows" else "shutdown now")
    else:
        print("Shutdown cancelled.")

print("Choose an option:\n1. System Details\n2. Create Folder\n3. Create File\n4. Send WhatsApp Message\n5. Shutdown System")
choice = input("Enter your choice (1-5): ")

if choice == '1':
    system_details()
elif choice == '2':
    create_folder()
elif choice == '3':
    create_file()
elif choice == '4':
    send_whatsapp_message()
elif choice == '5':
    shutdown_system()
else:
    print("Invalid choice. Please enter a number from 1 to 5.")
