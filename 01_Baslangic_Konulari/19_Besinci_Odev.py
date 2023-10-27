"""
PROBLEM 1:
Math modülündeki hazır fonksiyonları kullanarak gelişmiş bir hesap makinesi geliştirmeye çalışın

PROBLEM 2:
Math modülünde kullandığınız fonksiyonları kendiniz de ayrı bir modüle (Python dosyasına) yazmaya çalışın ve bu yazdığınız modulü kullanarak gelişmiş bir hesap makinesi yazın.


help(math)

    This module provides access to the mathematical functions
    defined by the C standard.

FUNCTIONS
    acos(x, /)
        Return the arc cosine (measured in radians) of x.
        The result is between 0 and pi.     

    acosh(x, /)
        Return the inverse hyperbolic cosine of x.
    asin(x, /)
        Return the arc sine (measured in radians) of x.

        The result is between -pi/2 and pi/2.

    asinh(x, /)
        Return the inverse hyperbolic sine of x.

    atan(x, /)
        Return the arc tangent (measured in radians) of x.

        The result is between -pi/2 and pi/2.

    atan2(y, x, /)
        Return the arc tangent (measured in radians) of y/x.

        Unlike atan(y/x), the signs of both x and y are considered.

    atanh(x, /)
        Return the inverse hyperbolic tangent of x.

    ceil(x, /)
        Return the ceiling of x as an Integral.

        This is the smallest integer >= x. 

    comb(n, k, /)
        Number of ways to choose k items from n items without repetition and without order.

        Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
        to zero when k > n.

        Also called the binomial coefficient because it is equivalent
        to the coefficient of k-th term in polynomial expansion of the
        expression (1 + x)**n.

        Raises TypeError if either of the arguments are not integers.
        Raises ValueError if either of the arguments are negative.

    copysign(x, y, /)
        Return a float with the magnitude (absolute value) of x but the sign of y.     

        On platforms that support signed zeros, copysign(1.0, -0.0)
        returns -1.0.

    cos(x, /)
        Return the cosine of x (measured in radians).

    cosh(x, /)
        Return the hyperbolic cosine of x. 

    degrees(x, /)
        Convert angle x from radians to degrees.

    dist(p, q, /)
        Return the Euclidean distance between two points p and q.

        The points should be specified as sequences (or iterables) of
        coordinates.  Both inputs must have the same dimension.

        Roughly equivalent to:
            sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))

    erf(x, /)
        Error function at x.

    erfc(x, /)
        Complementary error function at x. 

    exp(x, /)
        Return e raised to the power of x. 

    expm1(x, /)
        Return exp(x)-1.

        This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.

    fabs(x, /)
        Return the absolute value of the float x.

    factorial(x, /)
        Find x!.

        Raise a ValueError if x is negative or non-integral.

    floor(x, /)
        Return the floor of x as an Integral.

        This is the largest integer <= x.  

    fmod(x, y, /)
        Return fmod(x, y), according to platform C.

        x % y may differ.

    frexp(x, /)
        Return the mantissa and exponent of x, as pair (m, e).

        m is a float and e is an int, such that x = m * 2.**e.
        If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.

    fsum(seq, /)
        Return an accurate floating point sum of values in the iterable seq.

        Assumes IEEE-754 floating point arithmetic.

    gamma(x, /)
        Gamma function at x.
    
    gcd(*integers)
        Greatest Common Divisor.

    hypot(...)
        hypot(*coordinates) -> value       

        Multidimensional Euclidean distance from the origin to a point.

        Roughly equivalent to:
            sqrt(sum(x**2 for x in coordinates))

        For a two dimensional point (x, y), gives the hypotenuse
        using the Pythagorean theorem:  sqrt(x*x + y*y).

        For example, the hypotenuse of a 3/4/5 right triangle is:

            >>> hypot(3.0, 4.0)
            5.0

    isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
        Determine whether two floating point numbers are close in value.

          rel_tol
            maximum difference for being considered "close", relative to the
            magnitude of the input values  
          abs_tol
            maximum difference for being considered "close", regardless of the
            magnitude of the input values  

        Return True if a is close in value to b, and False otherwise.

        For the values to be considered close, the difference between them
        must be smaller than at least one of the tolerances.

        -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
        is, NaN is not close to anything, even itself.  inf and -inf are
        only close to themselves.

    isfinite(x, /)
        Return True if x is neither an infinity nor a NaN, and False otherwise.        

    isinf(x, /)
        Return True if x is a positive or negative infinity, and False otherwise.      

    isnan(x, /)
        Return True if x is a NaN (not a number), and False otherwise.

    isqrt(n, /)
        Return the integer part of the square root of the input.

    lcm(*integers)
        Least Common Multiple.

    ldexp(x, i, /)
        Return x * (2**i).

        This is essentially the inverse of frexp().

    lgamma(x, /)
        Natural logarithm of absolute value of Gamma function at x.

    log(...)
        log(x, [base=math.e])
        Return the logarithm of x to the given base.

        If the base not specified, returns the natural logarithm (base e) of x.        

    log10(x, /)
        Return the base 10 logarithm of x. 

    log1p(x, /)
        Return the natural logarithm of 1+x (base e).

        The result is computed in a way which is accurate for x near zero.

    log2(x, /)
        Return the base 2 logarithm of x.  

    modf(x, /)
        Return the fractional and integer parts of x.

        Both results carry the sign of x and are floats.

    nextafter(x, y, /)
        Return the next floating-point value after x towards y.

    perm(n, k=None, /)
        Number of ways to choose k items from n items without repetition and with order.
        Evaluates to n! / (n - k)! when k <= n and evaluates
        to zero when k > n.

        If k is not specified or is None, then k defaults to n
        and the function returns n!.       

        Raises TypeError if either of the arguments are not integers.
        Raises ValueError if either of the arguments are negative.

    pow(x, y, /)
        Return x**y (x to the power of y). 

    prod(iterable, /, *, start=1)
        Calculate the product of all the elements in the input iterable.

        The default start value for the product is 1.

        When the iterable is empty, return the start value.  This function is
        intended specifically for use with numeric values and may reject
        non-numeric types.

    radians(x, /)
        Convert angle x from degrees to radians.

    remainder(x, y, /)
        Difference between x and the closest integer multiple of y.

        Return x - n*y where n*y is the closest integer multiple of y.
        In the case where x is exactly halfway between two multiples of
        y, the nearest even value of n is used. The result is always exact.

    sin(x, /)
        Return the sine of x (measured in radians).

    sinh(x, /)
        Return the hyperbolic sine of x.   

    sqrt(x, /)
        Return the square root of x.       

    tan(x, /)
        Return the tangent of x (measured in radians).

    tanh(x, /)
        Return the hyperbolic tangent of x.

    trunc(x, /)
        Truncates the Real x to the nearest Integral toward 0.

        Uses the __trunc__ magic method.   

    ulp(x, /)
        Return the value of the least significant bit of the float x.

DATA
    e = 2.718281828459045
    inf = inf
    nan = nan
    pi = 3.141592653589793
    tau = 6.283185307179586

FILE
    (built-in)
"""

#kullanacağım fonksiyonlar:  
# comb(n, k, /) : Number of ways to choose k items from n items without repetition and without order. Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates to zero when k > n.
# cos(x, /) : Return the cosine of x (measured in radians).
# degrees(x, /) : Convert angle x from radians to degrees.
# fabs(x, /) : Return the absolute value of the float x.
# factorial(x, /) : Find x!.
# fmod(x, y, /) : Return fmod(x, y), according to platform C.
# gcd(*integers) : Greatest Common Divisor.
# hypot(...) : For a two dimensional point (x, y), gives the hypotenuse using the Pythagorean theorem:  sqrt(x*x + y*y).
# lcm(*integers) : Least Common Multiple.
# log(...) : log(x, [base=math.e]) Return the logarithm of x to the given base. If the base not specified, returns the natural logarithm (base e) of x.
# log10(x, /) : Return the base 10 logarithm of x.
# log2(x, /) : Return the base 2 logarithm of x.
# perm(n, k=None, /) : Number of ways to choose k items from n items without repetition and with order. Evaluates to n! / (n - k)! when k <= n and evaluates to zero when k > n.
# pow(x, y, /) : Return x**y (x to the power of y).
# radians(x, /) : Convert angle x from degrees to radians.
# sin(x, /) : Return the sine of x (measured in radians).
# sqrt(x, /) : Return the square root of x
# tan(x, /) : Return the tangent of x (measured in radians).


#------------------ PROBLEM 1-----------------


import math
import time
import os

print("HESAP MAKİNESİ")
   
print("1-Toplama= +\n2-Çıkarma= -\n3-Çarpma= *\n4-Bölme= /\n5-Üs Alma= **\n6-Karekök Alma= karekök\n7-Faktöriyel Hesaplama= fak\n8-Mod Hesaplama= %\n9-Sin= sin\n10-Cos= cos\n11-Tan= tan\n12-EBOB Hesaplama= ebob\n13-EKOK Hesaplama= ekok\n14-Permutasyon= per\n15-Kombinasyon= kom\n16-log= log\n17-log10= log10\n18-log2= log2\n19-Mutlak Değer Hesaplama= mutlak\n20-Hipotenüs Hesaplama= hip\n21-Derece-Radyan Dönüşümü= radyan\n22-Radyan-Derece Dönüşümü= derece")
    
print("İşlem sonucunuzu görmek için 'e' ye basınız.")
print("Hesap makinesini resetlemek için ise 'r' ye basınız.")



#İşlemlerin fonksiyonları:



def Toplama():
    sayi = input()
    global sonuc
    sonuc+=int(sayi)
    print("=",sonuc)

def Cikarma():
    sayi = input()
    global sonuc
    sonuc-=int(sayi)
    print("=",sonuc)


def Carpma():
    sayi = input()
    global sonuc
    sonuc*=int(sayi)
    print("=",sonuc)

def Bolme():
    sayi = input()
    global sonuc
    sonuc/=int(sayi)
    print("=",sonuc)

def UsAlma():
    sayi = input()
    global sonuc
    sonuc= math.pow(sonuc,int(sayi))
    print("=",sonuc)

def KarekokAlma():
    global sonuc
    sonuc= math.sqrt(sonuc)
    print("=",sonuc)

def Faktoriyel():
    global sonuc
    sonuc= math.factorial(sonuc)
    print("=",sonuc)

def Mod():
    sayi = input()
    global sonuc
    sonuc= math.fmod(sonuc,int(sayi))
    print("=",sonuc)    

def Sin():
    global sonuc
    sonuc= math.sin(sonuc)
    print("=",sonuc)

def Cos():
    global sonuc
    sonuc= math.cos(sonuc)
    print("=",sonuc)

def Tan():
    global sonuc
    sonuc= math.tan(sonuc)
    print("=",sonuc)

def EBOB():
    sayi = input()
    global sonuc
    sonuc= math.gcd(sonuc,int(sayi))
    print("=",sonuc)  

def EKOK():
    sayi = input()
    global sonuc
    sonuc= math.lcm(sonuc,int(sayi))
    print("=",sonuc) 

def Permutasyon():
    sayi = input()
    global sonuc
    sonuc= math.perm(sonuc,int(sayi))
    print("=",sonuc) 

def Kombinasyon():
    sayi = input()
    global sonuc
    sonuc= math.comb(sonuc,int(sayi))
    print("=",sonuc) 

def Log():
    sayi = input()
    global sonuc
    sonuc= math.log(sonuc,int(sayi))
    print("=",sonuc) 

def LogOn():
    global sonuc
    sonuc= math.log10(sonuc)
    print("=",sonuc)

def LogIki():
    global sonuc
    sonuc= math.log2(sonuc)
    print("=",sonuc)

def Mutlak():
    global sonuc
    sonuc= math.fabs(sonuc)
    print("=",sonuc)

def Hipotenus():
    sayi = input()
    global sonuc
    sonuc= math.hypot(sonuc,int(sayi))
    print("=",sonuc) 

def Radyan():
    global sonuc
    sonuc= math.radians(sonuc)
    print("=",sonuc)

def Derece():
    global sonuc
    sonuc= math.degrees(sonuc)
    print("=",sonuc)

ilkSayi=int(input())
sonuc=ilkSayi

def Reset():
    global ilkSayi, sonuc
    ilkSayi=int(input())
    sonuc=ilkSayi

while(True):
    giris= input()
    if(giris=="+"):
        Toplama()
    elif(giris=="-"):
        Cikarma()
    elif(giris=="*"):
        Carpma()
    elif(giris=="/"):
        Bolme()
    elif(giris=="**"):
        UsAlma()
    elif(giris=="karekök"):
        KarekokAlma()
    elif(giris=="fak"):
        Faktoriyel()   
    elif(giris=="%"):
        Mod() 
    elif(giris=="sin"):
        Sin()  
    elif(giris=="cos"):
        Cos() 
    elif(giris=="tan"):
        Tan()   
    elif(giris=="ebob"):
        EBOB()   
    elif(giris=="ekok"):
        EKOK()
    elif(giris=="per"):
        Permutasyon()    
    elif(giris=="kom"):
        Kombinasyon()   
    elif(giris=="log"):
        Log()
    elif(giris=="log10"):
        LogOn()
    elif(giris=="log2"):
        LogIki() 
    elif(giris=="mutlak"):
        Mutlak() 
    elif(giris=="hip"):
        Hipotenus() 
    elif(giris=="radyan"):
        Radyan()
    elif(giris=="derece"):
        Derece()
    elif(giris=="e"):
        os.system('cls')
        print(sonuc)
    elif(giris=="r"):
        os.system('cls')
        print("1-Toplama= +\n2-Çıkarma= -\n3-Çarpma= *\n4-Bölme= /\n5-Üs Alma= **\n6-Karekök Alma= karekök\n7-Faktöriyel Hesaplama= fak\n8-Mod Hesaplama= %\n9-Sin= sin\n10-Cos= cos\n11-Tan= tan\n12-EBOB Hesaplama= ebob\n13-EKOK Hesaplama= ekok\n14-Permutasyon= per\n15-Kombinasyon= kom\n16-log= log\n17-log10= log10\n18-log2= log2\n19-Mutlak Değer Hesaplama= mutlak\n20-Hipotenüs Hesaplama= hip\n21-Derece-Radyan Dönüşümü= radyan\n22-Radyan-Derece Dönüşümü= derece")
        print("İşlem sonucunuzu görmek için 'e' ye basınız.")
        print("Hesap makinesini resetlemek için ise 'r' ye basınız.")
        Reset()
        
