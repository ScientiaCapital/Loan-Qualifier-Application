# Import pathlib
from app import load_bank_data
from pathlib import Path

#Import fileio
from qualifier.utils import fileio

# Import Calculators
from qualifier.utils import calculators

# Import Filters
from qualifier.filters import credit_score
from qualifier.filters import debt_to_income
from qualifier.filters import loan_to_value
from qualifier.filters import max_loan_size

def test_save_csv():
    # @TODO: Your code here!
    # Use Path from pathlib to output the test csv to ./data/output/qualifying_loans.csv
    csv_file = Path("../data/daily_rate_sheet.csv")
    header = ["A", "b", "c"]
    qualifying_loans = ['1', '2', '3']
    save_csv(csv_file, header, qualifying_loans)
    assert csv_file.exists()

def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84

def test_filters():
    bank_data = fileio.load_csv(Path('../data/daily_rate_sheet.csv'))
    current_credit_score = 750
    debt = 1500
    income = 4000
    loan = 210000
    home_value = 250000
    monthly_debt_ratio = 0.375
    loan_to_value_ratio = 0.84

    # @TODO: Test the new save_csv code!
banks = max_loan_size.filter_max_loan_size(loan_to_value, load_bank_data)
print(len(banks))
assert len(banks) == 18
current_credit_score = credit_score.filter_credit_score(current_credit_score, banks)
assert len(current_credit_score) == 9
test_save_csv(Path(save_csv).exists())

