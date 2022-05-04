"""
    pip freeze > requirements.txt
    SciView > true/false
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime
#import PySimpleGUI as sg
from XMLRefact import *



def print_week(list_fio):
    fio_list = list_fio[:1]
    date_priz = list_fio[1:]
    list_res = [[],[]]
    for i in range(0, len(fio_list[0])):
        res_date = datetime.now() - datetime.strptime(str(date_priz[0][i]), '%d/%m/%Y')
        if int(str(res_date.days)) > 182:
            str_zvan = "Ефрейтор"
        else:
            str_zvan = "Рядовой"
        res_str = "ФИО: " + fio_list[0][i] + "\n"
        res_str += "Звание:\t" + str_zvan + "\n\n"
        res_str += "*** Прошло ***\n"
        res_str += "Дней прошло:\t" + str(res_date.days) + "\n"
        res_str += "Недель прошло:\t" + str(round(res_date.days/7, 2)) + "\n"
        res_str += "Месяцев прошло:\t" + str(round(res_date.days/30, 1)) + "\n"
        res_str += "Итог:\t\t" + str(round(res_date.days * 100 / 365, 1)) + "%\n\n"
        res_str += "*** Осталось ***\n"
        res_str += "Дней осталось:\t" + str(365 - res_date.days) + "\n"
        res_str += "Недель осталось:\t" + str(52 - round(res_date.days / 7, 2)) + "\n"
        res_str += "Месяцев осталось:\t" + str(12 - round(res_date.days / 30, 1)) + "\n"
        res_str += "Итог:\t\t" + str(100 - round(res_date.days * 100 / 365, 1)) + "%\n"
        res_str += "***********************\n"
        print(res_str)
        list_res[0].append(str_zvan + " " + fio_list[0][i])
        list_res[1].append(res_date.days)
    create_graph(list_res[0], list_res[1])


def create_graph(names_list, res_date):
    series1 = np.array(res_date)
    series2 = np.array([365-res_date[i] for i in range(0, len(res_date))])
    index = np.arange(len(res_date))
    plt.title('Прогресс')
    plt.bar(index, series1, color='orange')
    plt.bar(index, series2, color='blue', bottom=series1)
    for i in range(0, len(res_date)):
        names_list[i] += "  " + str(round(res_date[i] * 100 / 365, 2)) + "% " + str(res_date[i]) + " дн."
    plt.xticks(index, names_list)
    plt.xticks(rotation=8)
    plt.legend(['Прошло', 'Осталось'], loc='upper left')
    #fig = plt.gcf()
    #fig.canvas.set_window_title('Диаграмма')
    plt.show()


if __name__ == '__main__':
    list_fio = load_xml_files()
    print_week(list_fio)

# <?xml version='1.0' encoding='UTF-8'?>
# <root>
#   <FIOs>
#     <FIO><FIO/>
#   </FIOs>
#   <Dates>
#     <Date></Date>
#   </Dates>
# </root>

