import pytest

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.calculator import Calculator
from src.bank_account import BankAccount

@pytest.fixture(scope="session")
def calculator():
    return Calculator()

@pytest.fixture(scope="session")
def bank_account():
    return BankAccount("Misha", initial_balance=1000)