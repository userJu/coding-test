function getGcd(w,h){
    const val = w%h
    return val === 0 ? h : getGcd(h,val)
}

function solution(w, h) {
    
    const answer = w*h -(w+h-getGcd(w,h))
    return answer;
}