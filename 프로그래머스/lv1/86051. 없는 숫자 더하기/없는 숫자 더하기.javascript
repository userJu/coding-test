function solution(numbers) {
    let res = 0
    for(let i = 0 ; i < 10 ; i++){
        res+=i
    }
    
    for(i in numbers){
        res-=numbers[i]
    }
    
    
    return res;
}