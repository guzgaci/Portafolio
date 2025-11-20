"""
Cálculos de valor presente y futuro para anualidades, perpetuidades
y anualidades con crecimiento aritmético y geométrico.
"""

def vp_anualidad_vencida(R, i, n):
    return R * (1 - (1 + i) ** -n) / i

def vf_anualidad_vencida(R, i, n):
    return R * ((1 + i) ** n - 1) / i

def vp_perpetuidad(R, i):
    return R / i

def vp_anualidad_vencida_crec_aritmetico(R, d, i, n):
    # R, R+d, R+2d, ...
    vp = 0
    for k in range(n):
        pago = R + k * d
        vp += pago / (1 + i) ** (k + 1)
    return vp

def vp_anualidad_vencida_crec_geometrico(R, g, i, n):
    # R, R(1+g), R(1+g)^2, ...
    vp = 0
    for k in range(n):
        pago = R * (1 + g) ** k
        vp += pago / (1 + i) ** (k + 1)
    return vp

if __name__ == "__main__":
    R = 2500
    i = 0.08
    n = 10
    print("VP anualidad vencida:", vp_anualidad_vencida(R, i, n))
    print("VF anualidad vencida:", vf_anualidad_vencida(R, i, n))
    print("VP perpetuidad:", vp_perpetuidad(R, i))
