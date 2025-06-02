
def czy_palindrom(tekst: str) -> bool:
    return tekst == tekst[::-1]
print(czy_palindrom("kajak"))  # True
print(czy_palindrom("potop"))  # True   
print(czy_palindrom("python"))  # False
print(czy_palindrom("level"))  # True   
print(czy_palindrom("gucz"))