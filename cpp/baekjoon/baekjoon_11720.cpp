#include <iostream>
#include <string>

int main(){
    int N, num;
    int res = 0;
    std::string nums_str, tmp;
    std::cin >> N;
    std::cin >> nums_str;

    for(int i=0; i<N; ++i){
        tmp = nums_str[i];
        res += stoi(tmp);
    }
    std::cout << res;

}