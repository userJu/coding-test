function solution(participant, completion) {
    
    dict = {}
    
    for(i in participant){
        dict[participant[i]] = (dict[participant[i]] || 0) +1
    }
    for(i in completion){
        dict[completion[i]] = dict[completion[i]] -1
    }

    resarr = Object.entries(dict) 
    for(i in resarr){
        if (resarr[i][1] !=0){
            return resarr[i][0]
        }
    }
    
}