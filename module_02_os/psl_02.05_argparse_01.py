# CodingGears.io
# argparse

BANDS = {
    "CG1": "Band 11",
    "CG2": "Band 12",
    "CG3": "Band 13",
    "CG4": "Band 14",
    "CG5": "Band 15"
}


def band_base_bonus(band_code):
    if band_code == "CG1":
        return 0.05
    elif band_code == "CG2":
        return 0.08
    elif band_code == "CG3":
        return 0.10
    elif band_code == "CG4":
        return 0.15
    elif band_code == "CG5":
        return 0.20


def additional_bonus_by_years_of_employment(years_of_employment):
    if 2 < years_of_employment <= 5:
        return 0.02
    elif 5 < years_of_employment <= 10:
        return 0.05
    elif 10 < years_of_employment <= 15:
        return 0.08
    elif 15 < years_of_employment <= 20:
        return 0.10
    elif years_of_employment > 20:
        return 0.15
    else:
        return 0


def calculate_bonus(salary, band, years_of_employment):
    bonus_by_band = band_base_bonus(band)
    bonus_by_years_of_emp = additional_bonus_by_years_of_employment(years_of_employment)
    bonus_total = bonus_by_band + bonus_by_years_of_emp
    bonus_amount = salary * bonus_total
    return bonus_amount


if __name__ == "__main__":
    total_bonus_amount = calculate_bonus(50000, "CG5", 10)
    print("Total Bonus Amount : {:,.2f}".format(total_bonus_amount))
