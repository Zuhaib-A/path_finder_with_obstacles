import collections
import random

def create_grid(r, c):
        global mapgrid
        mapgrid = []
        for i in range(0, r):
                temp_list = ["0"] * c
                mapgrid.append(temp_list)
        return mapgrid

def start_end_positions(grid, start_r, start_c, end_r, end_c):
        grid[start_r][start_c] = "s"
        grid[end_r][end_c] = "f"
        return grid

def create_obstacles(grid, start_r, start_c, end_r, end_c):
        global all_obs
        default = [(start_c, start_r), (end_c, end_r)]
        
        #Phase 1:
        orig_obs = [(9, 7), (8, 7), (6, 7), (6, 8)]
        all_obs = []
        
        #Phase 2:
        new_obs = []
        obs_count = 0
        while obs_count < 20:
                taken = True
                while taken == True:
                        x1 = random.randrange(0, col)
                        y1 = random.randrange(0, rows)
                        if ((x1, y1) in orig_obs) or ((x1, y1) in new_obs) or ((x1, y1) in default):
                                taken = True
                        else:
                                taken = False
                                new_obs.append((x1, y1))
                                obs_count = obs_count + 1                 
        print("The added obstacles have the following coordinates:\n " + str(new_obs) +"\n")
        all_obs = all_obs + new_obs
        all_obs = all_obs + orig_obs

        return grid

def draw_obstacles(grid, all_obs):
        for i in all_obs:
                y, x = i
                grid[y][x]= "#"
        return grid

def bfs(grid, start_r, start_c, end_r, end_c):
        #Treat the start as the first node, from there we explore neighbouring nodes until no node is left in the queue
        start = (start_r ,start_c)
        queue = collections.deque([[start]])
        explored = set([start])
        while queue:
                path = queue.popleft()
                y, x = path[-1]
                if (y, x) == (end_r, end_c):
                        return path
                #Checking horizontal, vertical and diagnol directions.
                for y2, x2 in ((y+1,x), (y-1,x), (y,x+1), (y,x-1), (y+1, x+1), (y-1, x-1), (y-1, x+1), (y+1, x-1)):
                        if 0 <= x2 < rows and 0 <= y2 < col and grid[y2][x2] != "#" and (y2, x2) not in explored:
                                queue.append(path + [(y2, x2)])
                                explored.add((y2, x2))
        
                                
def draw_path(grid, path):
        if path == None:
                print("\nNo path could be found.")
                quit()
        else:
                for i in path:
                        y, x = i
                        grid[y][x]= "@"
                return grid        

#Grid size is defined
rows = 10
col = 10

#The start and finish of the path is defined
start_r = 0
start_c = 0
end_r = 9
end_c = 9

#Grid is created again to show the final path
grid = create_grid(rows, col)
start_end_positions(grid, start_r, start_c, end_r, end_c)
create_obstacles(grid, start_r, start_c, end_r, end_c)
draw_obstacles(grid, all_obs)
for i in grid:
        print(i)

path = bfs(grid, start_r, start_c, end_r, end_c)
grid = create_grid(10, 10)
draw_path(grid, path)
start_end_positions(grid, start_r, start_c, end_r, end_c)
draw_obstacles(grid, all_obs)

print("\nThere are " + str(len(path)) + " steps needed to traverse the shortest path, here they are:\n" + str(path))
print("\nPlease follow the @ symbols from s to f for the path:\n")

for i in grid:
        print(i)
