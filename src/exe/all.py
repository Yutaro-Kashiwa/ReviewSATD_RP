
import pandas as pd

from exe import ENV
from exe import rq2, rq1


def read_pkl(project):
    return pd.read_pickle(f"{ENV['input_dir']}/{project}_df.pkl")


def run(project):
    print(project)
    df = read_pkl(project)
    rq1.run(project, df)
    rq2.run(project, df)



if __name__ == '__main__':
    run("qt")
    run("openstack")





