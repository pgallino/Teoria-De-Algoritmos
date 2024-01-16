import csv
from graph.graph import Graph

class GraphFactory:

    @staticmethod
    def Load(file_path):

        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            row1 = next(reader)
            row2 = next(reader)

            graph = Graph(row1[0], row2[0])

            for row in reader:
                graph.add_edge(row[0], row[1], int(row[2]), int(row[3]))
    
        file.close()

        return graph