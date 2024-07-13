import math

points = [(3,1), (5,10), (2,15), (3,2)]
distances = []

def euclideanDistance(point1,point2):
    return math.sqrt( (point1[0]-point2[0])**2 + (point1[1]-point2[1])**2 )

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance( points[i], points[j] )
        distances.append( (distance, points[i], points[j]) )

minDistance, point1, point2 = min(distances) #ayrıştırma

print(f"The minimum distance is: {minDistance}")
print(f"Points are: {point1, point2}")