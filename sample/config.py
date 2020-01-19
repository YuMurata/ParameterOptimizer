class TargetValue:
    MAX = 100
    MIN = 0

    @classmethod
    def normalize(cls, x: int) -> float:
        return x * (cls.MAX - cls.MIN) / (2**50 - 1) + cls.MIN
