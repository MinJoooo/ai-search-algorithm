from math import inf
from queue import heappop, heappush
from collections import deque
from Initialization_Graph import Init_Problem


class Breadth_First(Init_Problem):
    def __init__(self):
        Init_Problem.__init__(self, directed=True)
        Init_Problem.__str__(self)

    def breadth_first(self, start, goal, count):
        found, fringe, visited, came_from =\
            False, deque([start]), set([start]), {start: None}

        while not found and len(fringe):
            current = fringe.pop()
            count = count + 1

            if current == goal:
                found = True
                break
            for node in self.neighbors(current):
                if node not in visited:
                    visited.add(node)
                    fringe.appendleft(node)
                    came_from[node] = current
                    count = count + 1

        if found:
            return came_from, count
        else:
            print('No path from {} to {}'.format(start, goal))
            return None, count


graph = Breadth_First()
graph.create_graph()
start, goal, count = 'A', 'Z', 0
trace, count = graph.breadth_first(start, goal, count)

if (trace):
    print('Path:', end=' ')
    graph.print_path(trace, goal)
    print('\nCount:', count)