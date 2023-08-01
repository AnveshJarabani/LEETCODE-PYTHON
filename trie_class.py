from dataclasses import dataclass,field
from typing import Dict,List

@dataclass
class directory_node:
    folder: Dict[str,'directory_node'] = field(default_factory=dict)
    files: List[str] = field(default_factory=list)

    def insert_folder(self,folder_path:str) -> None:
        node=self
        for folder_name in folder_path:
            if folder_name not in node.folder:
                node.folder[folder_name]=directory_node()
            node=node.folder[folder_name]
    def insert_file(self,folder_path:str,file_name:str) -> None:
        node=self
        for folder_name in folder_path:
            if folder_name not in node.folder:
                node.folder[folder_name]=directory_node()
            node=node.folder[folder_name]
        node.files.append(file_name)
    def print_directory(self,node=None,indent=0):
        if not node:
            return
        for folder_name,child_node in node.folder.items():
            print("  "*indent +f"-{folder_name}")
            self.print_directory(child_node,indent+1)
            for file_name in child_node.files:
                print("  "*(indent+1)+f"-{file_name}")
            
""" INITIALIZE THE TRIE"""                
trie=directory_node()

""" PROCESS THE FILE PATHS AND CREATE THE FOLDER STRUCTURE"""
file_paths = [
    "/home/jack/diary/2023-04-01.txt",
    "/home/jack/diary/2023-04-02.txt",
    "/home/jack/photos/1.jpg",
    "/home/jack/diary/2023-04-03.txt"
]

for file_path in file_paths:
    tokens=file_path.split("/")
    path_list=tokens[1:-1]
    file_name=tokens[-1]
    trie.insert_folder(path_list)
    trie.insert_file(path_list,file_name)
trie.print_directory(trie)
    
    
    
        
            
        
        
        
    
    