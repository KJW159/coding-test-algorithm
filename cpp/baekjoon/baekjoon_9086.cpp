#include <iostream>
#include <string>

int main(){
    int T;
    std::string word,word1,word2;
    std::cin >> T;
    for(int i=0; i<T; ++i){
        std::cin >> word;
        word1 = word.front();
        word2 = word.back();
        std::cout << word1 << word2 <<'\n';
    }
}