from titanic.templates.plot import Plot

if __name__ == '__main__':
    while 1:
        menu = input('0-exit 1-DataVisualization 2-Modeling 3-Machine Learning 4-Machine Relase')
        if menu =='0':
            break
        elif menu =='1':
            plot = Plot()
            plot.show_plot_sex()
            #plot.show_plot_pclass()
            #plot.show_plot_Embarked()
