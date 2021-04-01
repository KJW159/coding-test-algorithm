#include <string>
#include <deque>
#include <numeric>
#include <vector>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 0;
    deque <int> que;
    for (int i=0; i<bridge_length; ++i){
        que.push_back(0);
    }


    int cnt = 0;
    while(!que.empty()){
        ++cnt;
        que.pop_front();
        if (!truck_weights.empty()){
            int init_num = 0;
            int weight_sum = accumulate(que.begin(), que.end(), init_num);
            if (truck_weights[0]+weight_sum <= weight){
                que.push_back(truck_weights.front());
                truck_weights.erase(truck_weights.begin());
            }
            else{
                que.push_back(0);
            }
        }
    }

    return answer;
}