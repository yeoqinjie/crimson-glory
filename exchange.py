class ExchangeRate:
    SGDUSD = 0.7
    USDSGD = 1.4

    @classmethod
    def sgd_to_usd(cls, amt):
        return cls.SGDUSD * amt

    @classmethod
    def usd_to_sgd(cls, amt):
        return cls.USDSGD * amt
