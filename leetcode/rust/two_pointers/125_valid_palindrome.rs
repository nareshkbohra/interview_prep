struct Solution {}

pub fn is_valid(c: u8) -> bool {
    return (c >= b'a' && c <= b'z') || (c >= b'0' && c <= b'9');
}

impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let mut left = 0;
        let mut right = s.len() - 1;
        let s = s.to_lowercase();
        let s = s.as_bytes();
        while left < right {
            while left < right && !is_valid(s[left]) {
                left += 1;
            }

            while left < right && !is_valid(s[right]) {
                right -= 1;
            }

            if s[left] != s[right] {
                return false;
            }

            if right == 0 {
                break;
            }

            left += 1;
            right -= 1;
        }
        true
    }
}

fn main() {
    let result = Solution::is_palindrome("0P".to_string());
    println!("{}", result);
}
