def multiplicar(a: int | float, b: int | float) -> int | float:
    """
    Lo mismo, pero para multiplicar a*b, que original
    """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a * b
    
    raise TypeError("Solo se aceptan números")
