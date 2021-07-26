from common.menu import print_menu
from modu.template.basic_plot import plot_show, plot_two_list_show, plot_label, plot_marker, scatter
from modu.template.changed_temperature_on_my_birthday import ChangedTemperaturesOnMyBirthday

if __name__ == '__main__':
    while 1:
        menu = print_menu(['exit', 'Plot Show','Plot tow list show','plot_label','plot_marker','scatter','Blank','ChangedTemperaturesOnMyBirthday'])
        if menu == 0:
            break
        elif menu == 1:
            plot_show()
        elif menu == 2:
            plot_two_list_show()
        elif menu == 3:
            plot_label()
        elif menu == 4:
            plot_marker()
        elif menu == 5:
            scatter()
        elif menu == 6:
            pass
        elif menu == 7:
            ChangedTemperaturesOnMyBirthday().processing()
            pass