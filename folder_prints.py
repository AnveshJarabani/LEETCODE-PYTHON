file_paths = [
    "/home/jack/diary/2023-04-01.txt",
    "/home/jack/diary/2023-04-02.txt",
    "/home/jack/photos/1.jpg",
    "/home/jack/diary/2023-04-03.txt",
]


class node:
    def __init__(self, name=None):
        self.name: str = name
        self.files: list = []
        self.folders = {}

    def add_folder(self, path_list):
        cur_node = self
        for i in path_list:
            if i not in cur_node.folders:
                cur_node.folders[i] = node(i)
            cur_node = cur_node.folders[i]

    def add_files(self, path_list, file):
        cur_node = self
        for i in path_list:
            if i not in cur_node.folders:
                cur_node.folders[i] = node(i)
            cur_node = cur_node.folders[i]
        cur_node.files.append(file)

    def print_structure(self, cur_node=None, indent=0):
        if not cur_node:
            return None
        for name, next_nodes in cur_node.folders.items():
            print("  " * (indent) + "-" + name)
            self.print_structure(next_nodes, indent + 1)
            for file in self.files:
                print(" " * (indent + 1) + "-" + file)


structure = node()
for i in file_paths:
    nodes = i.split("/")[1:]
    files = nodes[-1]
    folders = nodes[:-1]
    structure.add_folder(folders)
    structure.add_files(folders, files)
structure.print_structure(structure)
