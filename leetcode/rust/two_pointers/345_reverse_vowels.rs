struct Solution {}
fn is_vowel(c: char) -> bool {
    let lower_c = c.to_ascii_lowercase();
    matches!(lower_c, 'a' | 'e' | 'i' | 'o' | 'u')
}

impl Solution {
    pub fn reverse_vowels(s: String) -> String {
        let (mut left, mut right) = (0, s.len() - 1);
        let mut s = s.as_bytes().to_vec();
        while left < right {
            while left < right && !is_vowel(s[left] as char) {
                left += 1;
            }
            while left < right && !is_vowel(s[right] as char) {
                right -= 1;
            }
            let temp = s[left];
            s[left] = s[right];
            s[right] = temp;

            left += 1;

            if right == 0 {
                break;
            }
            right -= 1;
        }
        return str::from_utf8(&s).unwrap().to_string();
    }
}

fn main() {
    let result = Solution::reverse_vowels("naresh".to_string());
    println!("{}", result);
}
