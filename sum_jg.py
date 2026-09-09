def suma(a: int | float, b: int | float) -> int | float:
    """
    Sumo a+b por que soy un crack y lo hago función.
    """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    
    raise TypeError("Solo se aceptan números")
