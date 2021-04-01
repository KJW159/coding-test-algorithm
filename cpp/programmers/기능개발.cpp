// #include <string>
// #include <vector>

// using namespace std;

// vector<int> solution(vector<int> progresses, vector<int> speeds) {
//     vector<int> answer;
    
//     while (!progresses.empty()){
//         int cnt = 0;
//         int work_num = progresses.size();
//         for (int i=0; i<work_num; ++i){
//             progresses[i] += speeds[i];
//         }
//         if (progresses[0] >= 100){
//             for (int i=0; i<work_num; ++i){
//                 if (progresses[i] >= 100){
//                     ++cnt;
//                 }
//                 else{
//                     break;
//                 }
//             }
//             for (int j=0; j<cnt; ++j){
//                 progresses.erase(progresses.begin()+j);
//                 speeds.erase(speeds.begin()+j);
//             }
//         }
//         if (cnt > 0){
//         answer.push_back(cnt);
//         }
    
//     }
//     return answer;
// }


#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    
    while (!progresses.empty()){
        int cnt = 0;
        int work_num = progresses.size();
        for (int i=0; i<work_num; ++i){
            progresses[i] += speeds[i];
        }
        if (progresses[0] >= 100){
            for (int i=0; i<work_num; ++i){
                if (progresses[i] >= 100){
                    ++cnt;
                }
                else{
                    break;
                }
            }
            for (int j=0; j<cnt; ++j){
                progresses.erase(progresses.begin());
                speeds.erase(speeds.begin());
            }
        }
        if (cnt > 0){
        answer.push_back(cnt);
        }
    
    }
    return answer;
}