# Math2LS.py

class Math:
    "Math tools class."
    def __init__(self) -> None:
        "Initializes the math tools class."
        self.euler = __import__("math").e
        self.pi =  __import__("math").pi
        self.sqrt = __import__("math").sqrt
        self.inf = float("inf")
        self.true = 1 == 1
        self.false = 1 != 1
        self.phi = self.goldenratio = self.φ = 0.5 + (self.sqrt(5) / 2)

    def average(self, *args) -> float:
        "Returns the average of a list of numbers."
        return sum(args) / len(args)

    def xnor(self, a: bool, b: bool) -> bool:
        "Returns the inverse of the XOR of variables a and b."
        return bool(a) == bool(b)

    def xor(self, a: bool, b: bool) -> bool:
        "Returns the XOR of variables a and b."
        return bool(a) != bool(b)
    
    def not_(self, a: bool) -> bool:
        "Returns the inverse of the variable a."
        return self.xor(self.true, a)
    
    def or_(self, a: bool, b: bool) -> bool:
        "Returns True if either a or b is True."
        return self.nand(self.not_(a), self.not_(b))
    
    def and_(self, a: bool, b: bool) -> bool:
        "Returns True if both a and b are True."
        return self.xnor(a, b) == (bool(a) == self.true)
    
    def nand(self, a: bool, b: bool) -> bool:
        "Returns the inverse of the AND function for variables a and b."
        return self.not_(self.and_(a, b))
    
    def nthroot(self, power: float, number: float) -> float:
        "Returns the nth root of power."
        return power ** (1 / number)
    
    def exp(self, number: float) -> float:
        "Returns e^number."
        return self.euler ** number
    
    def pow(self, base: float, exponent: float) -> float:
        "Returns base^exponent."
        return base ** exponent
    
    def nor(self, a: bool, b: bool) -> bool:
        "Returns False if either a or b are True. Otherwise, return True."
        return self.not_(self.or_(a, b))

    
