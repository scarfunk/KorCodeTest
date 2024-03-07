function solution(numbers, hand) {
    var order = [[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]];
//     % 3 = 1 is L, 0 is R, 2 는 센터
    var prevL = "*";
    var prevR = "#"
    var ret = [];
    for(var n of numbers) {
        mod = n % 3;
        if(n === 0) mod = 2
        if(mod === 1) {
            ret.push("L")
            prevL = n
        } else if (mod === 0) {
            ret.push("R")
            prevR = n
        } else {
            var ldist = getDist(n, prevL, order)
            var rdist = getDist(n, prevR, order)
            
            var x;
            if(ldist === rdist){
                x = hand[0].toUpperCase()
            } else {
                x = ldist < rdist ? "L" : "R"
            }
            ret.push(x)
            if(x == "L") prevL = n
            if(x == "R") prevR = n
        }
    }
    return ret.join("")
    
    function getDist(t, now, o) {
        var tij;
        var nowij;
        for(var i = 0; i < o.length; i++) {
            for(var j = 0; j < o.length; j++) {
                if(o[i][j] == t) tij = i+""+j 
                if(o[i][j] == now) nowij = i+""+j 
            }   
        }
        return Math.abs(tij[0] - nowij[0]) + Math.abs(tij[1] - nowij[1])
    }
}