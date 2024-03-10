function solution(s)
{
    var arr = s.split('')
    var stack = [arr[0]]
    
    for(var i = 1 ; i < arr.length ; i++){
        var poped = stack.pop()
        if(poped == arr[i]) {
            continue
        } else {
            if(poped) stack.push(poped)
            stack.push(arr[i])
        }
    }
    return stack.length == 0 ? 1 : 0
}