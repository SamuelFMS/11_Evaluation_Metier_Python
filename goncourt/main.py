from utils import input_utils
from views.president_view import PresidentView
from views.user_view import UserView

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("1- Souhaitez vous etre president")
    print("2- Souhaitez vous etre visiteur")
    choice: int = input_utils.input_number("Votre choix: ", 1, 2)
    if choice == 1:
        PresidentView.display()
    elif choice == 2:
        UserView.display()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
