from map import *
from plots import *


def main():
    print('Plot of number of times rivers have been studied.')
    print('Plot of rivers studied more than ten times.')
    enable_plot = False
    pie_plot(enable_plot)
    enable_plot = True
    bar_plot(enable_plot)

    plotter = MapPlotter(merged_file='Inputs/merged_excel.xlsx')
    plotter.process_and_plot()

    print('Intensity map successfully plotted.')


if __name__ == '__main__':
    main()
