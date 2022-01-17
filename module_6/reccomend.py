import numpy as np
import pandas as pd
import json


# with open('src/meta_Grocery_and_Gourmet_Food.json', encoding="utf8") as f:
#     meta_list = []
#     for line in f.readlines():
#         meta_list.append(json.loads(line))
#
# meta = pd.DataFrame(meta_list)
# meta.to_csv('src/meta.csv', index=False)
df = pd.read_csv('src/meta.csv')
print(df.columns)


