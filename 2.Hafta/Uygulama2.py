import math

# İstenilen fonksiyon
def euclideanDistance(point1, point2):
  x1, y1 = point1
  x2, y2 = point2
  return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Points ve demet(x,y)
points = [(5, 2), (13, 94), (55, 76), (65, 81)]

# Mesafe için distances listesi
distances = []

# Her nokta çifti için Öklid mesafesini hesaplayın
for i in range(len(points)):
  for j in range(i + 1, len(points)):
    distance = euclideanDistance(points[i], points[j])
    distances.append(distance)

# Minimum mesafeyi bulun ve yazdırın
mesafe = min(distances)
print("Mesafe:", mesafe)
