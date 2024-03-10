function solution(s) {
    var str = s
    
    var mem = {
        "{" : "}",
        "[" : "]",
        "(" : ")"
    }
    var ret = 0
    for(var i = 0 ; i < str.length ; i++) {
        var openstack = []
        var valid = true
        for(var c of str) {
            if(openstack.length == 0 && !mem[c]) {
                valid = false
                break;
            }
            if(mem[c]) { // 오픈이면 넣고 다음
                openstack.push(c)
                continue
            }
            var poped = openstack.pop()
            if(mem[poped] === c) { // { } 같이 매칭되면 성공
                
            } else {
                // 매칭이 안되면 그냥 실패
                valid = false
                break;
            }
        }
        if(valid && openstack.length == 0) ret++
        
        str = str.slice(1) + str[0]
    }
    return ret
}