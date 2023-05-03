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
print(data)
def par_chil_dict(heap):
    dct={}
    for i,val in enumerate(heap):
        parent_index=(i-1)//2
        if parent_index>=0:
            parent=heap[parent_index]
            if parent not in dct:
                dct[parent]=[]
            dct[parent].append(val)
    return dct
tree_dct=par_chil_dict(data)
print(tree_dct)
import pandas as pd
df=pd.DataFrame(columns=['parent','child'])
count=0
for i,val in tree_dct.items():
    for x in val:
        count+=1
        df.loc[len(df)]=[str(i),x]
print(df)
dx=df.loc[df['parent'].astype(int)!=df['child'].astype(int)].drop_duplicates()
tree=Tree()
for parent in df['parent']:
    if parent not in tree:
        tree.create_node(parent,parent)
for i,r in dx.iterrows():
    child=r['child']
    parent=r['parent']
    tree.create_node(child,child,parent=parent)
tree.show()
dx=dx[['child','parent']]
root=dataframe_to_tree_by_relation(dx)
print_tree(root)