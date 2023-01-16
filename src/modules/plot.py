import seaborn as sns

import matplotlib
# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
sns.set(style="darkgrid")
from pathlib import Path

def plot_revisions(df, dirname):
    tp="revisions"
    sns.boxplot(x=df["is_added_satd"], y=df[tp])
    plt.yscale('log')
    plt.ylim([0,1000])
    path = Path(dirname)
    path.mkdir(parents=True, exist_ok=True)
    plt.savefig(f'{dirname}/{tp}.png')
    plt.close()


def plot_timing(arr_for_plot, dirname):
    sns.histplot(data=arr_for_plot, binwidth=1)
    plt.ylim([0,15000])
    plt.xlim([1,30])
    path = Path(dirname)
    path.mkdir(parents=True, exist_ok=True)
    plt.savefig(f"{dirname}/timing.png")
    plt.close()