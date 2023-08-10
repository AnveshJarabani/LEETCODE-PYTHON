from pyvis import network
network= network.Network(height=500,width=1000,notebook=True,directed=True)
network.add_nodes(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])
network. add_edges([ ('A','B'),('A','C'),('B','D'),('B','E'),('C','F'),('C','G'),('F','H'),('F','I')])
network.show_buttons(filter_=['physics'])
network. show('test.html')
