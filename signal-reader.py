from frontrear import FrontRear
from maxgain import MaxGain
from widebeam import WideBeam


def main():
    # Prompt the user for input
    print("1. Front/Rear")
    print("2. Max Gain")
    print("3. Wide Beam")
    user_input = input("Enter your selection (number only): ")
    
    # Check the user input
    if user_input == "1":
        option = FrontRear()
    elif user_input == "2":
        option = MaxGain()
    elif user_input == "3":
        option = WideBeam()
    else:
        print("Invalid input")
    

    # excute the option
    option.execute()

if __name__ == '__main__':
    main()
