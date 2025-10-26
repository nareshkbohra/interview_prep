struct Bank {
    balances: Vec<i64>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Bank {
    fn new(balance: Vec<i64>) -> Self {
        let bank = Bank { balances: balance };
        bank
    }

    fn transfer(&mut self, account1: i32, account2: i32, money: i64) -> bool {
        let account1 = account1 as usize;
        let account2 = account2 as usize;

        if account1 > self.balances.len() || account2 > self.balances.len() {
            return false;
        }

        if self.balances[account1 - 1] < money {
            return false;
        }
        self.balances[account1 - 1] -= money;
        self.balances[account2 - 1] += money;
        true
    }

    fn deposit(&mut self, account: i32, money: i64) -> bool {
        let account = account as usize;
        if account > self.balances.len() {
            return false;
        }

        self.balances[account - 1] += money;
        true
    }

    fn withdraw(&mut self, account: i32, money: i64) -> bool {
        let account = account as usize;
        if account > self.balances.len() || self.balances[account - 1] < money {
            return false;
        }
        self.balances[account - 1] -= money;
        true
    }
}

/**
 * Your Bank object will be instantiated and called as such:
 * let obj = Bank::new(balance);
 * let ret_1: bool = obj.transfer(account1, account2, money);
 * let ret_2: bool = obj.deposit(account, money);
 * let ret_3: bool = obj.withdraw(account, money);
 */
fn main() {
    let balance = [10, 100, 20, 50, 30];
    let mut obj = Bank::new(balance.to_vec());
    let mut ret = obj.withdraw(3, 10);
    println!("{}", ret);
    ret = obj.transfer(5, 1, 20);
    println!("{}", ret);
}
