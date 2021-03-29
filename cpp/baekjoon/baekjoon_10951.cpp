// v1
// #include <iostream>

// int main(){
//     int a, b;
    
//     while(std::cin >> a >> b){
//         std:: cout << a+b << std::endl;
//     }
//     return 0;
// }

// v2
#include <iostream>

int main(){
    int a, b;
    while(scanf("%d %d", &a, &b) != EOF){
        std::cout << a+b << std::endl; 
    }
}