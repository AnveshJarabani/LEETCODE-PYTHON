from pyvis import network
network1= network.Network(height=500,width=1000,notebook=True,directed=False)
network1.add_nodes(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])
network1. add_edges([ ('A','B'),('A','C'),('B','D'),('B','E'),('C','F'),('C','G'),('F','H'),('F','I')])
network1.show_buttons(filter_=['physics'])

network1.show('test.html')

network_llist= network.Network(height=500,width=1000,notebook=True,directed=False)
network_llist.add_nodes([1,2,3,4,5])
network_llist.add_edges([(1,2),(2,3),(3,4),(4,5)])
network_llist.show_buttons(filter_=['physics'])
network_llist.show('test1.html')