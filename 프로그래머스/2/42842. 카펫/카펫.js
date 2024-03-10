function solution(b, y) {
    var k = b + y
    for(var i = 3; i < k/2; i++) {
        if(k % i !== 0) continue
        var w = (k / i)
        var h = i
        if(y == (w - 2) * (h-2)) {
            return [w, h]
        }
    }
    
}