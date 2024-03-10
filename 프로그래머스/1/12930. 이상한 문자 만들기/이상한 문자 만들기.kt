class Solution {
    fun solution(s: String): String {
        var i = 0;
        var ret = ""
        for(c in s) {
            val empty = " "
            if(c == empty.single()) {
                ret += c
                i = 0
                continue
            }
            if(i % 2 == 0) {
                ret += c.uppercase()
                i++
            } else {
                ret += c.lowercase()
                i++
            }
        }    
        
        return ret
    
    }
}