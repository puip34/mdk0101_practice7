class Vector3D:
    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.start = (x1, y1, z1)  # координаты начала вектора
        self.end = (x2, y2, z2)    # координаты конца вектора

    def __add__(self, other):
        # сложение векторов
        return Vector3D(self.start[0], self.start[1], self.start[2],
                        self.end[0]+other.end[0], self.end[1]+other.end[1], self.end[2]+other.end[2])

    def __sub__(self, other):
        # вычитание векторов
        return Vector3D(self.start[0], self.start[1], self.start[2],
                        self.end[0]-other.end[0], self.end[1]-other.end[1], self.end[2]-other.end[2])

    def scalar_product(self, other):
        # скалярное произведение векторов
        return (self.end[0]-self.start[0])*(other.end[0]-other.start[0]) + \
               (self.end[1]-self.start[1])*(other.end[1]-other.start[1]) + \
               (self.end[2]-self.start[2])*(other.end[2]-other.start[2])

    def length(self):
        # длина вектора
        return ((self.end[0]-self.start[0])**2 + (self.end[1]-self.start[1])**2 + (self.end[2]-self.start[2])**2)**0.5

    def cosine_angle(self, other):
        # косинус угла между векторами
        return self.scalar_product(other) / (self.length() * other.length())