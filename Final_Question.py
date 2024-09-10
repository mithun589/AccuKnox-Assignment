class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    # Define an iterator method
    def __iter__(self):
        yield {'length': self.length}  # First yield the length
        yield {'width': self.width}    # Then yield the width

# Example usage
rect = Rectangle(10, 5)

# Iterating over the rectangle instance
for dimension in rect:
    print(dimension)
