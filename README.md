# Loan Qualification Application 

**Welcome to the Loan Qualifcation App!** 
The loan qualifier application will help home loan companies streamline their application process.

By inputting details at the comman line the homeowner will get list of banks.
---
## Technologies
*Built using Python 3.7.9 64-bit
This Loan Qualification Application makes use of the Python Programming language and the Command Line Interface. Need to import the following libraries [SYS, Fire, Questionary, CVS. 

The follwing Libraries require the (From, Import) method of import(load_csv, calculate_monthly_debt_ratio, calculate_loan_to_value_ratio, filter_max_loan_size, filter_credit_score, filter_debt_to_income, filter_loan_to_value)
---
## Installation Guide and Examples
```python
import sys
import csv
import fire
import questionary
import csv 
from pathlib import Path
from qualifier.utils.fileio import load_csv, save_csv
from qualifier.utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio,
)
from qualifier.filters.max_loan_size import filter_max_loan_size
from qualifier.filters.credit_score import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value import filter_loan_to_value
```
---
## Usage
This section should include screenshots, code blocks, or animations explaining how to use your project.
---
## Contributors
In this section, list all the people who contribute to this project; since you may want to be reached by recruiters or potential collaborators, include your contact e-mail, and optionally your LinkedIn or Twitter profile.
---
## License
When you share a project on a repository, especially a public one, it's important to choose the right license to specify others what they can and can not do with your source code and files. Use this section to include the licence you want to use.
