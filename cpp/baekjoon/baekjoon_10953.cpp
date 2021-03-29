#include <iostream>

int main() {
    int cnt, a, b;
    char c;
    std::cin >> cnt;
    for(int i=0; i<cnt; ++i){
        std::cin >> a >> c >> b;
        std::cout << a+b << std::endl;
    }
    return 0;
}