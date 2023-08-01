# Given the list of strings in the Sample Input below, display the Sample Output in the console.

dirs_list= ["home/jack/diary/2023-04-01.txt",
"home/jack/diary/2023-04-02.txt",
"home/jack/photos/1.jpg",
"home/jack/diary/2023-04-03.txt",
"home/jack/2025-04-03.txt",
]

# Sample Output
# - home
#   - jack
#     - diary
#       - 2023-04-01.txt
#       - 2023-04-02.txt
#     - photos
#       - 1.jpg

from typing import Dict,List
from dataclasses import dataclass,field

@dataclass 
class directory_node:
    folder : Dict[str ,'directory_node'] = field(default_factory=dict)
    files : List[str] = field(default_factory=list)
    
    def insert_folder(self,path_list:List[str]) -> None:
        node = self
        for folder in path_list:
            if folder not in node.folder:
                node.folder[folder]=directory_node()
            node=node.folder[folder]
    def insert_file(self,file_path:List[str],file:str) -> None:
        node=self
        for folder in file_path:
            node=node.folder[folder]
        node.files.append(file)
    def print_directory(self,node=None,indent=0):
        if not node:
            return
        for folder_name,child_node in node.folder.items():
            print(f"{'----'*indent}-{folder_name}")
            for file in child_node.files:
                print("----"*(indent+1)+f'-{file}')
            self.print_directory(child_node,indent+1)

root=directory_node()


for path in dirs_list:
    path_list=path.split("/")
    folder_path=path_list[:-1]
    file=path_list[-1]
    root.insert_folder(folder_path)
    root.insert_file(folder_path,file)
root.print_directory(root)
            


