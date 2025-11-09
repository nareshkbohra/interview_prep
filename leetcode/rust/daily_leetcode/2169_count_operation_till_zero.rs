impl Solution {
    pub fn count_operations(num1: i32, num2: i32) -> i32 {
        let mut result = 0;
        let (mut num1, mut num2) = (num1, num2);
        while num1 != 0 && num2 != 0 {
            if num1 > num2 {
                num1 -= num2;
            } else {
                num2 -= num1;
            }
            result += 1
        }
        result
    }
}

struct Solution {}

fn main() {
    let result = Solution::count_operations(10, 1);
    println!("Result is {}", result);
}
