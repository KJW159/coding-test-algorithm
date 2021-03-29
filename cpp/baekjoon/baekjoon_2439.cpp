#include <iostream>

int main(){
    int N, cnt_tmp;
    std::cin >> N;
    for(int i=0; i<N; ++i){
        cnt_tmp = N-i-1;
        for(int j=0; j < cnt_tmp; ++j){
            std::cout << ' ';
        }
        for(int k=0; k<(N-cnt_tmp); ++k){
            std::cout << '*';
        }
        std::cout << '\n';
    }
}