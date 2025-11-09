impl Solution {
    pub fn smallest_number(n: i32) -> i32 {
        let mut result = 1;
        let mut n = n;
        n = n >> 1;
        while n > 0 {
            n = n >> 1;
            result = result << 1 + 1;
        }
        result
    }
}
