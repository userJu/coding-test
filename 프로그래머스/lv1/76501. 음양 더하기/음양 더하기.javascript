function solution(absolutes, signs) {
    let res = 0
    for(i in absolutes){
        if (signs[i]){
            res +=absolutes[i] 
        }else{
            res-=absolutes[i]
        }
    }
    
    return res;
}