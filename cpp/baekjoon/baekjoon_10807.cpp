#include <iostream>
#include <vector>

int main(){
    int N, finding_num, num;
    int res = 0;
    std::cin >> N;
    std::vector<int> vec;
    for (int i=0; i<N; ++i){
        std::cin >> num;
        vec.push_back(num);
    }
    std:: cin >> finding_num;
    for (int i=0; i<N; ++i){
        if(finding_num ==vec[i]){
            res = res+1;
        }
    }
    std::cout << res << '\n';

}