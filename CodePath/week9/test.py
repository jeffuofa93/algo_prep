import os,sys
def main():
    if(os.path.exists("/sys/firmware/efi")):
        print("System is booted with uefi!")
    else:
        print("System is booted with rom bios")
main()
sys.exit(0)