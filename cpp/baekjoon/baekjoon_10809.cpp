#include <iostream>
#include <string>
#include <vector>

// v1
// int main() {
//     std::string word;
//     int arr[26];
//     std::fill_n(arr, 26, -1);
//     std::cin >> word;

//     for (int i=0; i<word.length(); ++i){
//         if(arr[word[i]-97] == -1){
//             arr[word[i]-97] = i;
//         }
//     }
//     for (int i=0; i<26; ++i){
//         std::cout << arr[i] << ' ';
//     }
// }

// v2
int main() {
    std::string word;
    std::vector<int> vec(26, -1);
    std::cin >> word;
    
    for (int i=0; i<word.length(); ++i){
        if(vec[word[i]-97] == -1){
            vec[word[i]-97] = i;
        }
    }
    for (int i=0; i<26; ++i){
        std::cout << vec[i] << ' ';
    }
}