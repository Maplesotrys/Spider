import pandas as pd

def excel_one_line_to_list():
    df = pd.read_excel("上市公司另类数据.xlsx", usecols=[0],
                       names=None)  # 读取项目名称列,不要列名
    df_li = df.values.tolist()
    result = []
    for s_li in df_li:
        result.append(s_li[0])
    result = list(map(lambda x:"%06d" % x,result))
    print(result)

excel_one_line_to_list()