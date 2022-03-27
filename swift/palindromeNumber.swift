class Solution {
    func isPalindrome(_ x: Int) -> Bool {
        if x < 0 {
            return false
        }
        var y: Int = 0
        var xCopy: Int = x
        while xCopy > 0 {
            y *= 10
            y += xCopy % 10
            xCopy /= 10
        }
        return x == y
    }
}
