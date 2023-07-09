def count(s,value):
    """Count the number of occurrences of value in sequence s."""
    total=0
    for elem in s:
        if elem ==value:
            total+=1
    return total

def divisors(n):
    return [1]+[x for x in range(2,n) if n %x==0]

def width(area,height):
    return area//height

def perimeter(width,height):
    return 2*width+2*height

def minimum_perimeter(area):
    heights=divisors(area)
    perimeters=[perimeter(width(area,h),h) for h in heights ]
    return min(perimeters)

def apply_to_all(map_fn,s):
    return [map_fn(x) for x in s]

def keep_if(filter_fn,s):
    return [x for x in s if filter_fn(x)]