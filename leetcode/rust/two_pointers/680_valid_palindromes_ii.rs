struct Solution {}

fn is_palindrome(s: &Vec<char>, mut start: usize, mut end: usize) -> bool {
    while start <= end {
        if s[start] != s[end] {
            return false;
        }
        start += 1;
        end -= 1;
    }

    true
}

impl Solution {
    pub fn valid_palindrome(s: String) -> bool {
        /*
         * Logic:
         * Start iterating from start and end.
         * As soon as you find some different char, try either (left+1, right) or (left, right-1)
         * If either of them are palindrome return true, otherwise return false
         */
        let s: Vec<char> = s.chars().collect();
        if s.len() == 0 {
            return true;
        }

        let (mut start, mut end) = (0, s.len() - 1);
        while start < end {
            if s[start] != s[end] {
                return is_palindrome(&s, start + 1, end) || is_palindrome(&s, start, end - 1);
            }
            start += 1;
            end -= 1;
        }
        true
    }
}

fn main() {
    let result = Solution::valid_palindrome("abab".to_string());
    println!("Result is {}", result);
}
