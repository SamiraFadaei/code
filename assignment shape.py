# =============================================
# ASSIGNMENT: SHAPES
# Abstraction with Shape Hierarchy
# =============================================

from abc import ABC, abstractmethod  
import math                          

# Shape 
class Shape(ABC):

    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        
        return self.name

    @abstractmethod
    def area(self) -> float:
        
        pass



class Rectangle(Shape):
    
    
    def __init__(self, width: float, height: float):
        super().__init__("Rectangle")  
        self.width = width
        self.height = height

    def area(self) -> float:
   
        return self.width * self.height


 
class Circle(Shape):
    
    def __init__(self, radius: float):
        super().__init__("Circle")
        self.radius = radius

    def area(self) -> float:
        """مساحت دایره: π × شعاع²"""
        return math.pi * (self.radius ** 2)  
        


#زیرکلاس Triangle 
class Triangle(Shape):
    """مثلث - فرزند Shape"""
    
    def __init__(self, base: float, height: float):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self) -> float:
        """مساحت مثلث: (قاعده × ارتفاع) / ۲"""
        return 0.5 * self.base * self.height



def main():
    # ایجاد یک لیست از اشکال مختلف
    shapes = [
        Rectangle(5, 10),
        Circle(3),
        Triangle(6, 4)
    ]

    # نمایش مساحت هر شکل
    print("--- Area of Shapes ---")
    for shape in shapes:
        
        print(f"Area of {shape.get_name()}: {shape.area():.2f}")


if __name__ == "__main__":
    main()