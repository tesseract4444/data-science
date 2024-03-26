from typing import Dict


def calculate_bmi(height_cm: int, weight_kg: int) -> float:
    return weight_kg / (height_cm / 100) ** 2


def calculate_reindeer_bmis(reindeers: Dict[str, Dict[str, int]]) -> Dict[str, float]:
    bmis: Dict[str, float] = {}

    for name, values in reindeers.items():
        bmis[name] = calculate_bmi(values['height_cm'], values['weight_kg'])

    return bmis

all_reindeers: Dict[str, Dict[str, int]] = {
  "Rudolph": {"age_years": 2, "height_cm": 200, "weight_kg": 120},
  "Comet": {"age_years": 1, "height_cm": 180, "weight_kg": 100},
  "Doner": {"age_years": 3, "height_cm": 210, "weight_kg": 90},
  "Blizzen": {"age_years": 4, "height_cm": 190, "weight_kg": 200},
  "Cupid": {"age_years": 2, "height_cm": 192, "weight_kg": 121},
  "Prancer": {"age_years": 4, "height_cm": 215, "weight_kg": 134},
  "Vixen": {"age_years": 6, "height_cm": 230, "weight_kg": 143},
  "Dancer": {"age_years": 1, "height_cm": 176, "weight_kg": 82},
  "Dasher": {"age_years": 5, "height_cm": 197, "weight_kg": 101}
}

print('Mein BMI:', calculate_bmi(172, 60))

bmis = calculate_reindeer_bmis(all_reindeers)
print('Comet:', (bmis['Comet']))

print(calculate_reindeer_bmis(all_reindeers))

