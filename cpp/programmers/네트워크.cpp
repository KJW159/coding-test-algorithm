#include <string>
#include <vector>

using namespace std;

// v1
// void dfs(int i, int n, int (&visited)[200], vector<vector<int>>& computers){
//     vector<int> stack;
//     stack.push_back(i);
//     visited[i] = 1;

//     while (!stack.empty()){
//         int i = stack.back();
//         stack.pop_back();
//         for (int j=0; j<computers.size(); ++j){
//             if (computers[i][j] == 1 && visited[j] == 0){
//                 stack.push_back(j);
//                 visited[j] = 1;
//             }
//         }
//     }
// }


// int solution(int n, vector<vector<int>> computers) {
//     int answer = 0;
//     int visited[200] = {0};
    
    
//     for (int i=0; i<n; ++i){
//         if (visited[i] == 0){
//             dfs(i, n,visited, computers);
//             ++answer;
//         }
//     }
    
//     return answer;
// }


// v2
void dfs(int i, int n, vector<int>& visited, vector<vector<int>>& computers){
    vector<int> stack;
    stack.push_back(i);
    visited[i] = 1;

    while (!stack.empty()){
        int i = stack.back();
        stack.pop_back();
        for (int j=0; j<computers.size(); ++j){
            if (computers[i][j] == 1 && visited[j] == 0){
                stack.push_back(j);
                visited[j] = 1;
            }
        }
    }
}


int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    vector<int> visited(n,0);
    
    for (int i=0; i<n; ++i){
        if (visited[i] == 0){
            dfs(i, n, visited, computers);
            ++answer;
        }
    }
    
    return answer;
}