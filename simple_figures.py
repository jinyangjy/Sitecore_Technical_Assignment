import math

class GeometricFigure:
    """
    Class Description: Base class for all geometric figures and contains the common methods
    such as move and rotate
    """
    def move(self, horizontal, vertical):
        """
        Function Description: moves the figure by the given horizontal and vertical values
        """

    def rotate(self, degree_angle):
        """
        Function Description: rotates the figure by the given angle
        """
class Point(GeometricFigure):
    """
    Class Description: A point in a 2D space defined by its x and y coordinate
    """
    def __init__(self, x_coordinate, y_coordinate) -> None:
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def distance_between(self, other_point):
        """
        Function Description: Using Pythagorean distance theorem, to find the distance
        between two points in a 2D space.
        """
        return math.sqrt((self.x_coordinate - other_point.x_coordinate)**2
                         + (self.y_coordinate - other_point.y_coordinate)**2)

    def __str__(self) -> str:
        return f"Point({self.x_coordinate:.1f}, {self.y_coordinate:.1f})"

    def move(self, horizontal, vertical):
        """
        Function Description: moves the point by the given horizontal and vertical values
        """
        self.x_coordinate += horizontal
        self.y_coordinate += vertical

class Line(GeometricFigure):
    """
    Class Description: A line defined by its start and end point
    """
    def __init__(self, start_point, end_point) -> None:
        self.start_point = start_point
        self.end_point = end_point

    def length(self):
        """
        Function Description: calculate the length of the line
        """
        return self.start_point.distance_between(self.end_point)

    def __str__(self) -> str:
        return f"Line({self.start_point}, {self.end_point})"

    def move(self, horizontal, vertical):
        self.start_point.x_coordinate += horizontal
        self.end_point.x_coordinate += horizontal

        self.start_point.y_coordinate += vertical
        self.end_point.y_coordinate += vertical

    def rotate(self, degree_angle):
        """
        Function Description: rotates the line by the given angle
        """
        # find the angle between the x axis and a vector from the difference between the end and start point
        current_angle = math.atan2(self.end_point.y_coordinate - self.start_point.y_coordinate,
                                   self.end_point.x_coordinate - self.start_point.x_coordinate)

        # add the given angle, converted into radians, to the current angle
        new_angle = current_angle + math.radians(degree_angle)

        #Finding the new x coordinate after rotation, using the cosine of the new angle. Cosine function gives
        #the x coordinate of a vector with the given length and adding the original point x coordinate to it.
        length = self.length()
        new_end_point_x = self.start_point.x_coordinate + length * math.cos(new_angle)
        new_end_point_y = self.start_point.y_coordinate + length * math.sin(new_angle)

        self.end_point.x_coordinate = new_end_point_x
        self.end_point.y_coordinate = new_end_point_y

class Circle(GeometricFigure):
    """
    Class Description: A circle is defined by its center and radius
    """
    def __init__(self, centre, radius) -> None:
        self.center = centre
        self.radius = radius

    def area(self):
        """
        Function Description: calculate the area of the circle pi * r^2
        """
        return math.pi * self.radius**2

    def circumference(self):
        """
        Function Description: calculate the circumference of the circle 2 * pi * r
        """
        return 2 * math.pi * self.radius**2

    def __str__(self) -> str:
        return f"Circle({self.center}, {self.radius:.1f})"

    def move(self, horizontal, vertical):
        self.center.x_coordinate += horizontal
        self.center.y_coordinate += vertical

    def rotate(self, degree_angle):
        """
        Function Description: rotates the circle by the given angle
        """
        # find the angle between the x axis and a vector from the difference between the end and start point
        current_angle = math.atan2(self.center.y_coordinate, self.center.x_coordinate)

        # add the given angle, converted into radians, to the current angle\
        new_angle = current_angle + math.radians(degree_angle)

        #Finding the new x coordinate after rotation, using the cosine of the new angle. Cosine function gives
        #the x coordinate of a vector with the given length and adding the original point x coordinate to it.
        self.center.x_coordinate = self.radius * math.cos(new_angle)
        self.center.y_coordinate = self.radius * math.sin(new_angle)

class Aggregation(GeometricFigure):
    """
    Class Description: A aggregation of geometric figures
    """
    def __init__(self, figure_list = None) -> None:
        """
        Function Description: initialize the aggregation with a list of geometric figures
        """
        if figure_list is None:
            self.figure_list = []
        else:
            self.figure_list = figure_list

    def add_figure(self, figure):
        """
        Function Description: add a geometric figure to the aggregation
        """
        if isinstance(figure, GeometricFigure):
            self.figure_list.append(figure)
        else:
            return "Cannot add " + type(figure).__name__ + " to Aggregation."

    def move(self, horizontal, vertical):
        """
        Function Description: moves the aggregation by the given horizontal and vertical values
        """
        for figure in self.figure_list:
            figure.move(horizontal, vertical)

    def rotate(self, degree_angle):
        """
        Function Description: rotates the aggregation by the given angle
        """
        for figure in self.figure_list:
            figure.rotate(degree_angle)

    def __str__(self) -> str:
        return "Aggregation contains of: " + ", ".join(str(figure) for figure in self.figure_list)

# Test case
if __name__ == "__main__":
    # Create 3 points, a line and a circle
    point1 = Point(1, 2)
    point2 = Point(3, 4)
    point3 = Point(5, 6)
    line1 = Line(point1, point2)
    circle_center = Point(0, 0)
    circle = Circle(circle_center, 5)

    # Create an aggregation and add points, line and the circle to it
    aggregation = Aggregation()
    aggregation.add_figure(point1)
    aggregation.add_figure(point2)
    aggregation.add_figure(point3)
    aggregation.add_figure(line1)
    aggregation.add_figure(circle)

    # Print the initial state of the aggregation
    print("Initial State: " + str(aggregation))

    # Move and rotate the aggregation
    aggregation.move(2, 3)  # Move the aggregation and its figures
    aggregation.rotate(45)   # Rotate the aggregation and its figures

    # Print the updated state of the aggregation
    print("Updated State: " + str(aggregation))