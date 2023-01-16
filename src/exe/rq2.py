import pandas

from exe import ENV
from modules.plot import plot_timing
from modules.revision import is_in_revised
from modules.utils import calc_rate
from pathlib import Path





def identify_timing(df, dirname):
    initial = 0
    revised = 0
    arr_for_plot = []
    for _, d in df.iterrows():
        for i in d["added_satd"]:
            rev = d["added_satd"][i]
            arr_for_plot.append(rev)
            if rev == 1:
                initial += 1
            elif rev > 1:
                revised += 1
            else:
                raise
    all = initial + revised
    header = ['', 'initial', 'revised']
    num = ['num', initial, revised]
    rate = ['rate', calc_rate(initial, all), calc_rate(revised, all)]
    out_df = pandas.DataFrame([num, rate], columns=header)
    path = Path(dirname)
    path.mkdir(parents=True, exist_ok=True)
    out_df.to_csv(f"{dirname}/rq2_summary.csv")

    plot_timing(arr_for_plot, dirname)




def run(project, df):
    print("**ADD timing (RQ2)**********************")
    df = df[(df['is_added_satd'] == True)].sort_values(by=["id"], ascending=True)
    df['is_in_revised'] = df.apply(lambda x: is_in_revised(x, 'added_satd'), axis=1)
    path = Path(ENV['output_dir'])
    path.mkdir(parents=True, exist_ok=True)
    # df[df.is_in_revised].drop('results', axis=1)\
    #     .drop('commit_message', axis=1)\
    #     .to_csv(f"{ENV['output_dir']}/{project}/rq2_rowdata.csv")

    # make_manual_inspection_list(df,'added_satd', f"{project}/{project}_rq2_manual_inspection.csv")

    identify_timing(df, f"{ENV['output_dir']}/{project}")
