function solution(n) {
    var cnt = n.toString(2).replaceAll("0","").length
    
    while(true) {
        n = n + 1
        var next_cnt = n.toString(2).replaceAll("0","").length
        if(cnt === next_cnt) {
            return n
        }
    }
}