class AirConditioner:
    """A room air-conditioner. Reported buggy by the QA team - fix it!"""
    VALID_MODES = ("cool", "fan", "dry", "auto")
    MIN_TEMP = 16
    MAX_TEMP = 30

    def __init__(self, brand, room_name, temperature=25, mode="cool", fan_speed=1):
        self.brand = brand
        self.room_name = room_name
        self.is_on = False
        self.temperature = temperature
        self.mode = mode
        self.fan_speed = fan_speed

    def __str__(self):
        return (
            f"{self.brand} {self.room_name}: "
            f"{self.temperature}C, mode={self.mode}, "
            f"energy-saving={self.is_energy_saving}"
        )

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < self.MIN_TEMP or value > self.MAX_TEMP:
            raise ValueError(f"Temperature must be {self.MIN_TEMP}-{self.MAX_TEMP} C.")
        self._temperature = value

    @property
    def is_energy_saving(self):
        return self.temperature >= 26

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        if value not in self.VALID_MODES:
            raise ValueError(f"Mode must be one of {self.VALID_MODES}.")
        self._mode = value

    @property
    def fan_speed(self):
        return self._fan_speed

    @fan_speed.setter
    def fan_speed(self, value):
        if not isinstance(value, int) or value < 1 or value > 3:
            raise ValueError("Fan speed must be 1, 2, or 3.")
        self._fan_speed = value

    def cooler(self):
        self.temperature = max(self.MIN_TEMP, self.temperature - 1)
        return self.temperature

    def warmer(self):
        self.temperature = min(self.MAX_TEMP, self.temperature + 1)
        return self.temperature
