#include <iostream>
#include <string>

int main(){
    std::string word;
    int word_len;
    std::getline(std::cin, word);
    int arr[26] = {};
    word_len = word.length();

    for(int i=0; i<word_len; ++i){
        // arr[word[i] - 97] += 1;
        ++arr[word[i] - 97];
    }
    
    for(int i=0; i<26; ++i){
        std::cout<< arr[i] << ' ';
    }

    return 0;

}