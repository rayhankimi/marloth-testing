import playerstat as ps
import playerattr as pa


def provoke(base=30) -> int:
    vitMul = ps.vitality() * 0.1
    strnMul = ps.strength() * 0.05
    damage = base + (base * vitMul) + (base * strnMul) + (pa.patk() * 0.3)
    return damage


def rendersword(base=70) -> int:
    strnMul = ps.strength() * 0.1
    damage = base + (base * strnMul) + (pa.patk() * 0.5)
    return damage


def combosword(base=100) -> int:
    strnMul = ps.strength() * 0.1
    damage = base + (base * strnMul) + (pa.patk() * 0.5)
    return damage


def cutthrough(base=100) -> int:
    damage = base
    return damage
