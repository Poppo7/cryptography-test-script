class BankVault:
    def __init__(self, capacity=500):  # Capacity in dollars
        self.capacity = capacity
        self.balance = 0  # Initial amount of money in the vault

    def deposit(self, amount):
        if self.balance + amount <= self.capacity:
            self.balance += amount
            print(f"Deposited ${amount}. Current balance: ${self.balance}")
        else:
            print("Deposit failed. Vault capacity exceeded.")

    def get_internal_fragmentation(self):
        return self.capacity - self.balance

    def display_vault_state(self):
        print(f"Vault Balance: ${self.balance}")
        print(f"Vault Capacity: ${self.capacity}")
        print(f"Internal Fragmentation (Unused Space): ${self.get_internal_fragmentation()}")

# Example
my_vault = BankVault()

my_vault.deposit(200)
my_vault.display_vault_state()

my_vault.deposit(100)
my_vault.display_vault_state()

my_vault.deposit(300) #should fail

# In Summary:
# Internal fragmentation is wasted memory space occurring within an 
# allocated memory block because the allocated block is larger than the requested memory.