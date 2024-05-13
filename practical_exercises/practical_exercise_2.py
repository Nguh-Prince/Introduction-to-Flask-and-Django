from math import pi, hypot

def validate_number(n):
    if not isinstance(n, (int, float)):
        raise TypeError("Arguments must be numeric")
    if n <= 0:
        raise ValueError("Numbers must be greater than 0")

# decorator
def validate_lengths(func):
    def wrapper(*args, **kwargs):
        for index, arg in enumerate(args):
            # skip the first argument as it is the cls
            if index == 0:
                continue

            if not isinstance(arg, (int, float, list)):
                breakpoint()
                raise TypeError(f"Arguments must be numeric or a list of numbers")
            if isinstance(arg, (int, float)) and arg <= 0:
                raise ValueError("Arguments must be positive")
            else:
                for i in arg:
                    validate_number(i)
            
        for value in kwargs.values():
            if not isinstance(value, (int, float)):
                raise ValueError("Arguments must be numeric")
            if value < 0:
                raise ValueError("Arguments must be positive")
        
        return func(*args, **kwargs)
    return wrapper

# Factory methods
class Shape:
    number_of_shapes_created = 0
    total_area_of_shapes_created = 0

    def __init__(
            self, type=None, radius=None, sides=None, 
            side_length=None, length=None, width=None, 
            area=None, perimeter=None
    ) -> None:
        self.type = type
        self.radius = radius
        self.sides = sides
        self.side_length = side_length
        self.length = length
        self.width = width
        self.area = area
        self.perimeter = perimeter

        self.__class__.number_of_shapes_created += 1
        self.__class__.total_area_of_shapes_created += self.area
    
    def __del__(self):
        self.__class__.number_of_shapes_created -= 1
        self.__class__.total_area_of_shapes_created -= self.area

    @classmethod
    def average_area_of_shapes(cls):
        return cls.total_area_of_shapes_created / cls.number_of_shapes_created

    @classmethod
    def create_circle(cls, radius):
        return cls(radius=radius, type='circle', perimeter=2*pi*radius, area=pi*(radius**2))

    @classmethod
    @validate_lengths
    def create_semicircle(cls, radius):
        return cls(
            radius=radius, type='semi-circle', 
            perimeter=(pi*radius + 2*radius), area=pi*(radius**2)
        )

    @classmethod
    @validate_lengths
    def create_square(cls, side_length):
        return cls(side_length=side_length, type='square', 
            area=side_length**2, perimeter=4*side_length)
    
    @classmethod
    @validate_lengths
    def create_rectangle(cls, length, width):
        return cls(
            length=length, width=width, type='rectangle', 
            area=length*width, perimeter=2*(length+width)
        )
    
    @classmethod
    @validate_lengths
    def create_triangle(cls, sides):
        perimeter = sum(sides)

         # s is the semi-perimeter, it will help us to calculate the area
        s = 0.5 * perimeter
        a, b, c = sides

        return cls(
            sides=sides, type='triangle', perimeter=sum(sides), 
            area= ( s * (s-a) * (s-b) * (s-c) )**0.5
        )
    
    @classmethod
    @validate_lengths
    def create_right_angle_triangle(cls, base, height):
        hyp = hypot(base, height)

        return cls.create_triangle([base, height, hyp])