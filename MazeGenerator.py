import random, numpy as np

# columns are (N,E,S,W)
def generate_maze(length):

    def walk(maze, i, j, is_visited = 0):
        """Randomly connect a node to an unvisited neighbor two adjacent nodes
        if is_visited=1 then connect to an already visited node"""
        dx = {"E": 0, "W": 0, "N": -1, "S": 1}
        dy = {"E": 1, "W": -1, "N": 0, "S": 0}
        directions = ["N", "S", "E", "W"]
        opposite_directions = {"E": "W", "W": "E", "N": "S", "S": "N"}
        columns = {"N": 0, "E": 1, "S": 2, "W": 3}

        random.shuffle(directions)
        for dir in directions:
            ni, nj = i + dx[dir], j + dy[dir]
            if ni >= 0 and ni < len(maze) and nj >= 0 and nj < len(maze) \
                    and maze[ni,nj,4] == is_visited:
                maze[i, j, columns[dir]], maze[i, j, 4] = 1, 1
                maze[ni, nj, columns[opposite_directions[dir]]], maze[ni, nj, 4] = 1,1
                return ni,nj
        return None,None

    def hunt(maze, skip_rows = 0):
        """top->bottom left->right search for an unvisited node adjacent to a visited node
        and connect them"""
        ni, nj = None, None
        for i in range(skip_rows, len(maze)):
            row_count = 0
            for j in range(len(maze)):
                if maze[i,j,4] == 0:
                    ni, nj = walk(maze,i,j,1)
                else:
                    row_count += 1
                if ni != None:
                    return ni,nj,skip_rows
            if(row_count == len(maze)):
                skip_rows += 1

        return None,None,skip_rows

    #---- Method Start ----
    # Trivial Case
    if(length == 0):
        return np.zeros(0)

    # columns are (N,E,S,W,Visited)
    maze = np.zeros((length, length, 5), dtype=np.uint8)

    # start in random place
    i,j,done_rows = random.randrange(length), random.randrange(length), 0

    while 1:
        #print_maze(maze)
        i,j = walk(maze, i, j)
        if i is None:
            i,j,done_rows = hunt(maze, done_rows)
            if i is None:
                break

    # We don't need visited column anymore
    return maze[:,:,0:4]



def print_maze(maze):
    # top of maze
    line = ""
    for i in range(len(maze)):
        line += " _"
    print(line)

    # we only need to do one side of each connection: so start in top-left look east&south
    for i in range(len(maze)):
        # left of maze
        line = "|"
        for j in range(len(maze)):
            if (maze[i, j, 2] == 0):
                line += "_"
            else:
                line += " "
            if (maze[i, j, 1] == 0):
                line += "|"
            else:
                line += " "
        print(line)