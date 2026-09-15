# This is a sample Python script.
from business.novel_business import NovelBusiness


# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    no = NovelBusiness()
    number = 1
    for novel in no.get_all():
        print(f"Roman n°{number}")
        print(novel)
        number+=1

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
