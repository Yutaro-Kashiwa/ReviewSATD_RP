import pandas


def calc_rate(a, b, default_val = "-"):
    try:
        return a/b
    except ZeroDivisionError:
        return default_val

# NEED TO FIX
def make_manual_inspection_list(df, data_col, out_filename):
    csv_contents = []
    for _, vals in df.iterrows():
        csv_line = []
        id = vals['id']
        print(vals)
        for comment, d in vals[data_col]:
            url = d['url']
            revision = d['revision']
            filename = d['filename']
            start_line = d['start_line']
            csv_line.append(id)
            csv_line.append(filename)
            csv_line.append(revision)
            csv_line.append(start_line)
            csv_line.append(f"{url}/{revision}/{filename}@{start_line}")
            csv_line.append(url)
            csv_line.append(comment)

            csv_contents.append(csv_line)
    out_df = pandas.DataFrame(csv_contents)
    out_df.to_csv(out_filename)
    pass


