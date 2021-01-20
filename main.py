import math
import xml.etree.ElementTree as ET

ELLIPSE_TAG="{http://www.w3.org/2000/svg}ellipse" 
GROUP_TAG="{http://www.w3.org/2000/svg}g" 

def circle_to_point(circle):
    return (float(circle.attrib['cx']), float(circle.attrib['cy']))

def parse_svg(svg_file_name):
    return ET.parse(svg_file_name)

def get_points_in_tree(tree):
    return [circle_to_point(circle) for circle in tree.iter(ELLIPSE_TAG)]

def get_point_by_id(tree, point_id):
    return [circle_to_point(circle) 
            for circle in tree.iter(ELLIPSE_TAG)
            if 'id' in circle.attrib
            if circle.attrib['id'] == point_id]

def get_points_by_group_id(tree, group_id):
    return [point 
            for group in tree.iter(GROUP_TAG)
            if 'id' in group.attrib
            if group.attrib['id'] == group_id
            for point in get_points_in_tree(group)]

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    return math.sqrt(dx*dx + dy*dy)

def closest_neighbour(all_points, pivot):
    best_point = None
    best_distance = None
    for point in all_points:
        current_distance = distance(pivot,point)
        if best_distance is None or current_distance > best_distance:
            best_distance = current_distance
            best_point = point
    return best_point 
   
svg_file = './points.svg'
svg_tree = parse_svg(svg_file)
print(svg_tree)
[expected] = get_point_by_id(svg_tree,'closest')
points = get_points_by_group_id(svg_tree,'points')
[pivot] = get_point_by_id(svg_tree,'pivot')

    
