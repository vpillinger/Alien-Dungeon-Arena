import random, numpy as np

# columns are (N,E,S,W)
def generate_maze(size):
    dx = {"E": 0, "W": 0, "N": -1, "S": 1}
    dy = {"E": 1, "W": -1, "N": 0, "S": 0}
    directions = ["N", "S", "E", "W"]
    opposite_directions = {"E": "W", "W": "E", "N": "S", "S": "N"}
    columns = {"N": 0, "E": 1, "S": 2, "W": 3}
    

    def walk(maze, i, j, to_visited = 0):
        random.shuffle(directions)
        for dir in directions:
            ni, nj = i + dx[dir], j + dy[dir]
            if ni >= 0 and ni < len(maze) and nj >= 0 and nj < len(maze) and maze[ni,nj,4] == to_visited:
                maze[i, j, columns[dir]], maze[i, j, 4] = 1, 1
                maze[ni, nj, columns[opposite_directions[dir]]], maze[ni, nj, 4] = 1,1
                return ni,nj
        return None,None

    def hunt(maze):
        ni, nj = None, None
        for i in range(len(maze)):
            for j in range(len(maze)):
                if maze[i,j,4] == 0:
                    ni, nj = walk(maze,i,j,1)
                if ni != None:
                    return ni,nj
        return None,None

    # columns are (N,E,S,W,Visited)
    maze = np.zeros((size,size,5), dtype=np.uint8)

    # start in random place
    i,j = random.randrange(size), random.randrange(size)

    while 1:
        #print_maze(maze)
        i,j = walk(maze, i, j)
        if i is None:
            i,j = hunt(maze)
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

print_maze(generate_maze(50))