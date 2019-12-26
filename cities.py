import random

road_map = [()]

def read_cities(file_name):
    """
    Read in the cities from the given `file_name`, and return 
    them as a list of four-tuples: 

      [(state, city, latitude, longitude), ...] 

    Use this as your initial `road_map`, that is, the cycle 

      Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.
    """
    infile = open(file_name,"r")

    inline = infile.readlines()
    listt = [tuple(line.strip().split('/t')) for line in inline]
    infile.close()
    return listt

    #read_cities('city-data.txt')

    #for i in listt: 

#split split(/t) line where /t and create a 4 element tuple. Then add to roadmap.

# divide each string into 4 strings at "t"
# remove "n" ()
# tranform into tuple 
# add to listt
# return listt
road_map = read_cities('city-data.txt')
print(road_map)



def print_cities(road_map):
    """
    Prints a list of cities, along with their locations. 
    Print only one or two digits after the decimal point.
    """
    
    road_map2 = [(i[1],float(i[2]),float(i[3])) for i in road_map]
    print(road_map2)
    #rounded_road_map = [(i[0],round((i[1],i[2]), 2)) for i in road_map2]
    #rounded_road_map= []
    #for i in road_map2: 
    #  float((i[1],i[2]))
    #   round((i[1],i[2]),2)

    return road_map2

print(print_cities(road_map))

def compute_total_distance(road_map):
    """
    Returns, as a floating point number, the sum of the distances of all 
    the connections in the `road_map`. Remember that it's a cycle, so that 
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """
    return (7.0)


def swap_cities(road_map, index1, index2):
    """
    Take the city at location `index` in the `road_map`, and the 
    city at location `index2`, swap their positions in the `road_map`, 
    compute the new total distance, and return the tuple 

        (new_road_map, new_total_distance)

    Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    """
    new_roadmap = [0]
    new_total_distance = 0.0
    return (new_roadmap,new_total_distance)

def shift_cities(road_map):
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map. 
    """
    new_roadmap_2 = [1]
    return (new_roadmap_2)

def find_best_cycle(road_map):
    """
    Using a combination of `swap_cities` and `shift_cities`, 
    try `10000` swaps/shifts, and each time keep the best cycle found so far. 
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    """
    pass

def print_map(road_map):
    """
    Prints, in an easily understandable format, the cities and 
    their connections, along with the cost for each connection 
    and the total cost.
    """
    pass

def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    pass

"""
if __name__ == "__main__": #keep this in
    main()
    return "main name"
"""
