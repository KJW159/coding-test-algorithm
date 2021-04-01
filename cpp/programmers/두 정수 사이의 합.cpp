#include <string>
#include <vector>

using namespace std;

long long solution(int a, int b) {
    long long answer = 0;
    if (a == b){
        answer = a;
    }
    else{
        if (a > b){
            int num_tmp = a;
            a = b;
            b = num_tmp;
        }
        for (int i=a; i<b+1; ++i){
            answer += i;
        }
    }
    return answer;
}