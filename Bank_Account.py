class BankAccount:

  def __init__(self, account_number, account_holder_name, account_balance=0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = account_balance

  def deposit(self, amount):
    self.__account_balance += amount
    return self.__account_balance

  def withdraw(self, amount):
    if amount > self.__account_balance:
      print("Insufficient balance!")
      return
    self.__account_balance -= amount
    return self.__account_balance

  def display(self):
    return f"Account Balance: {self.__account_balance}"


# Create an instance of the BankAccount class
account = BankAccount("123456789", "John Doe")

# Test the deposit functionality
print(account.deposit(5000))  # Output: 5000

# Test the withdrawal functionality
print(account.withdraw(2000))  # Output: 3000
print(account.withdraw(5000))  # Output: Insufficient balance!

# Display the account balance
print(account.display())  # Output: Account Balance: 3000
