function solution(arr)
{
    var ret = []
    for(var i = 0; i < arr.length; i++){
        if(arr[i] !== arr[i+1])
            ret.push(arr[i])
    }
    return ret;
}