const minmax =(size)=>{
    if (size == 0){
        return 6
    }
    return 7-size
}

function solution(lottos, win_nums) {
    let inLotto = 0
    let erasedNum = 0
    for (let i = 0; i <6; i++){
        if (win_nums.indexOf(lottos[i]) !== -1){
            inLotto++
        } 
        if (lottos[i] == 0){
            erasedNum++
        }
    }
    
    return [minmax(inLotto + erasedNum), minmax(inLotto)]
    
}