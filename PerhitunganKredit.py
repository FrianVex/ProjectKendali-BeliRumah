from FrontUIVer110 import Ui_MainWindow
import numpy as np

class HitungKredit():

    def __init__(self) -> None:
        pass

    # Hitung Fixed Rate
    def fixed_rate(self, parse_property_value: float, parse_down_payment: float, parse_interest_rate: float, parse_fixed_rate_tenor: float, parse_maximum_payment_time: float):
        
        fixed_rate_base = {
            "lended_nominal": parse_property_value - parse_down_payment,
            "monthly_interest_fixed_first_rate": (parse_interest_rate / 12) / 100,
            "monthly_interest_fixed_second_rate": (12 / 12) / 100,
            "months_in_years": parse_fixed_rate_tenor * 12,
            "not_so_months_in_years": (parse_maximum_payment_time - parse_fixed_rate_tenor) * 12,
            "added_costs": ( parse_property_value - parse_down_payment ) * 0.06
        }

        calculated_monthly_fixed_rate_payment = {
            "monthly_fixed_first_rate": fixed_rate_base["lended_nominal"] * fixed_rate_base["monthly_interest_fixed_first_rate"] * (1 + fixed_rate_base["monthly_interest_fixed_first_rate"]) ** fixed_rate_base["months_in_years"] / ((1 + fixed_rate_base["monthly_interest_fixed_first_rate"]) ** fixed_rate_base["months_in_years"]) - 1,
            "monthly_fixed_second_rate": fixed_rate_base["lended_nominal"] * fixed_rate_base["monthly_interest_fixed_second_rate"] * (1 + fixed_rate_base["monthly_interest_fixed_second_rate"]) ** fixed_rate_base["not_so_months_in_years"] / ((1 + fixed_rate_base["monthly_interest_fixed_second_rate"]) ** fixed_rate_base["not_so_months_in_years"]) - 1
        }

        calculated_total_payment = {
            "total_first_fixed_payment": parse_down_payment + calculated_monthly_fixed_rate_payment["monthly_fixed_first_rate"] + fixed_rate_base["added_costs"],
            "total_monthly_payment": ( calculated_monthly_fixed_rate_payment["monthly_fixed_first_rate"] * fixed_rate_base["months_in_years"] ) + ( calculated_monthly_fixed_rate_payment["monthly_fixed_second_rate"] * fixed_rate_base["not_so_months_in_years"] )
        }

        total_payment_without_interest = {
            "total_payment_without_interest": calculated_total_payment["total_monthly_payment"] - fixed_rate_base["lended_nominal"]
        }

        return fixed_rate_base["lended_nominal"], fixed_rate_base["added_costs"], calculated_monthly_fixed_rate_payment["monthly_fixed_first_rate"], calculated_monthly_fixed_rate_payment["monthly_fixed_second_rate"],calculated_total_payment["total_first_fixed_payment"], calculated_total_payment["total_monthly_payment"], total_payment_without_interest["total_payment_without_interest"]
    
    # Hitung Floating Rate
    def floating_rate(self, parse_property_value: float, parse_down_payment: float, parse_numbers_of_layers: float, parse_first_interest_rate: float, parse_increment_interest_rate: float, parse_layered_rate_tenor: float):
        
        lended_nominal = parse_property_value - parse_down_payment
        last_interest = 12 / 12 / 100
        not_so_months_in_years = (parse_layered_rate_tenor - parse_numbers_of_layers) * 12
        added_costs = (parse_property_value - parse_down_payment) * 0.06

        yearly_payment_rates = []
        summed_yearly_payment = []
        current_interest_rate = ( parse_first_interest_rate / 12 ) / 100
        for _ in range(int(parse_numbers_of_layers)):
            current_interest_payment = lended_nominal * current_interest_rate * (1 + current_interest_rate) ** 12 / ((1 + current_interest_rate) ** 12) - 1
            summed_yearly_payment.append(current_interest_payment * 12)
            yearly_payment_rates.append(current_interest_payment)
            current_interest_rate += ( parse_increment_interest_rate / 12 ) / 100

        last_interest_payment = lended_nominal * last_interest * (1 + last_interest) ** not_so_months_in_years / ((1 + last_interest) ** not_so_months_in_years) - 1

        total_first_floating_payment = parse_down_payment + yearly_payment_rates[0] + added_costs
        total_monthly_payment = ((sum(summed_yearly_payment)) + last_interest_payment * not_so_months_in_years)

        total_payment_without_interest = total_monthly_payment - lended_nominal

        return lended_nominal, added_costs, yearly_payment_rates, last_interest_payment, total_first_floating_payment, total_monthly_payment, total_payment_without_interest