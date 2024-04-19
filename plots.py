import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def pie_plot(enable_plot=True):

    rn = pd.read_excel('E:/HIWI Bea/river_dictionaries.xlsx')
    rn['River'] = rn['River'].apply(lambda x: x.title())
    sorted_rn = rn.sort_values(by='Frequency', ascending=False)
    hf_rivers = sorted_rn[sorted_rn['Frequency'] > 10]

    min_cg_value = 0
    max_cg_value = 70
    colors = plt.cm.RdBu(np.linspace((min_cg_value - 1) / (max_cg_value - 1),
                                     1, len(hf_rivers['Frequency'])))

    plt.figure(figsize=(10, 10))
    plt.pie(hf_rivers['Frequency'], labels=hf_rivers['River'],
            autopct=lambda p: '{:.0f}'.format(p * sum(hf_rivers['Frequency']) /
                                              100), startangle=135,
            counterclock=False, colors=colors)

    plt.title('Rivers studied more than ten times')
    plt.show() if enable_plot else None


def bar_plot(enable_plot=True):

    rn = pd.read_excel('Inputs/river_dictionaries.xlsx')
    repetitions_counts = rn['Frequency'].value_counts()

    plt.figure(figsize=(10, 7))
    ax = repetitions_counts.sort_index().plot(kind='bar', color='skyblue')

    for p in ax.patches:
        ax.annotate(f'{p.get_height()}',
                    (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', xytext=(0, 10),
                    textcoords='offset points')

    plt.xlabel('Number of Studies')
    plt.ylabel('Number of Rivers')
    plt.title('Number of times rivers have been studied')

    plt.show() if enable_plot else None
