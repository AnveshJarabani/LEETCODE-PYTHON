# Given the list of strings in the Sample Input below, display the Sample Output in the console.

# Sample Input
# create file /home/jack/diary/2023-04-01.txt
# create file /home/jack/diary/2023-04-02.txt
# create file /home/jack/photos/1.jpg
# create file /home/jack/diary/2023-04-03.txt


# Sample Output
# - home
#   - jack
#     - diary
#       - 2023-04-01.txt
#       - 2023-04-02.txt
#     - photos
#       - 1.jpg


class folder:
    def __init__(self, name: str, child=None, Parent=None):
        self.name: str = name
        self.child: folder = child
        self.Parent: folder = Parent


def folder_structure(paths_list: str):
    folder_structure_names_list = [i.split("/") for i in paths_list]
    for path_list in folder_structure_names_list:
        for indx, name in path_list[:-1]:
            parent_folder = folder(path_list[indx - 1])
            child_folder = folder(path_list[indx + 1])
            current_folder = folder(name, child=child_folder, Parent=parent_folder)


paths_list = [
    "/home/jack/diary/2023-04-01.txt",
    "/home/jack/diary/2023-04-02.txt",
    "/home/jack/photos/1.jpg",
]
print(folder_structure(paths_list))
