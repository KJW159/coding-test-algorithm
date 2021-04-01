#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0, cnt = 0;
    priority_queue<int> pq;
    queue<pair<int, int>> que;
    
    for (int i=0; i<priorities.size(); ++i){
        que.push({priorities[i], i});
        pq.push(priorities[i]);
    }
    
    while (true){
        int priority = que.front().first;
        int position = que.front().second;
        int max_pri = pq.top();
        que.pop();
        if (priority == max_pri){
            ++cnt;
            if (position == location){
                answer = cnt;
                break;
            }
            else{
                pq.pop();
            }
        }
        else{
            que.push({priority, position});
        }
        
    }
    
    return answer;
}