#include <iostream>
#include <vector>

int main(){
    int student;
    std::vector<int> vec(31);
    std::vector<int> missing_stu;
    for (int i=0; i<28; ++i){
        std::cin >> student;
        vec[student] = 1;
    }

    for (int i=1; i<31; ++i){
        if (vec[i] != 1){
            missing_stu.push_back(i);
        }
    }
    for (int i=0; i<missing_stu.size(); ++i){
        std::cout << missing_stu[i] << '\n';
    }

}