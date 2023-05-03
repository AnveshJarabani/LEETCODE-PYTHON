import heapq
from bigtree import dataframe_to_tree_by_relation,print_tree
from treelib import Node,Tree
'''
T1 -5
T2 - 4
T3 - 7
T4 - 9
T5 - 2
T6 - 6
'''

data = [10,20,43,1,2,65,17,44,2,3,1]
heapq.heapify(data)
def par_chil_dict(heap):
    temp=[f'{val} ind({i})' for i,val in enumerate(heap)]
    dct={}
    for i in range(len(temp)):
        dct[temp[i]]=[temp[2*i+1],temp[2*i+2]]
        if (2*i+2) == len(temp)-1:
            break
    return dct
tree_dct=par_chil_dict(data)
# print(tree_dct)
import pandas as pd
df=pd.DataFrame(columns=['child','parent'])
count=0
for i,val in tree_dct.items():
    for x in val:
        y=str(x)
        df.loc[len(df)]=[str(x),str(i)]
root=dataframe_to_tree_by_relation(df)
print(data)
print_tree(root)