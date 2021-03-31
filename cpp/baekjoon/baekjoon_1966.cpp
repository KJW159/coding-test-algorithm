// v1
// #include <iostream>
// #include <queue>
// #include <utility>
// #include <algorithm>

// using namespace std;

// int main() {
//     int T, res, N, M, doc_imp, doc, pos, pos_tmp, doc_tmp;
//     queue<pair<int, int>> que;
//     cin >> T;
//     for (int i=0; i<T; ++i){
//         cin >> N >> M;
//         int max_imp = 0, res = 0;

//         for (int j=0; j<N; ++j){
//             cin >> doc_imp;
//             max_imp = max(max_imp, doc_imp);
//             que.push({j, doc_imp});
//         }

//         int cnt = 0;
//         while (true){
//             pos = que.front().first;
//             doc = que.front().second;
//             que.pop();
//             if (pos==M && doc == max_imp){

//                 ++cnt;
//                 res = cnt;
//                 break;
//             }
//             if (doc < max_imp){
//                 que.push({pos, doc});
                
//             }
//             if (doc == max_imp){
//                 ++cnt;
//             }

            
//             int len = que.size();
//             max_imp = 0;
//             for (int k=0; k <len; ++k){
//                 pos_tmp = que.front().first;
//                 doc_tmp = que.front().second;
//                 que.pop();
//                 max_imp = max(max_imp, doc_tmp);
//                 que.push({pos_tmp, doc_tmp});
//             }

//         }
//         cout << res << endl;

//     }
// }


// v2
// #include <iostream>
// #include <queue>
// #include <utility>
// #include <algorithm>
// using namespace std;


// int main() {
//     int T, res, N, M, doc_imp, doc, pos, pos_tmp, doc_tmp;
//     cin >> T;
//     for (int i=0; i<T; ++i){
//         queue<pair<int, int>> que;
//         cin >> N >> M;
//         int max_imp = 0, res = 0;

//         for (int j=0; j<N; ++j){
//             cin >> doc_imp;
//             max_imp = max(max_imp, doc_imp);
//             que.push({j, doc_imp});
//         }

//         int cnt = 0;
//         while (true){
//             pos = que.front().first;
//             doc = que.front().second;
//             que.pop();
//             if (pos==M && doc == max_imp){

//                 ++cnt;
//                 res = cnt;
//                 break;
//             }
//             if (doc < max_imp){
//                 que.push({pos, doc});
                
//             }
//             if (doc == max_imp){
//                 ++cnt;
//             }

            
//             int len = que.size();
//             max_imp = 0;
//             for (int k=0; k <len; ++k){
//                 pos_tmp = que.front().first;
//                 doc_tmp = que.front().second;
//                 que.pop();
//                 max_imp = max(max_imp, doc_tmp);
//                 que.push({pos_tmp, doc_tmp});
//             }

//         }
//         cout << res << endl;

//     }
// }


// v3
#include <iostream>
#include <queue>
#include <utility>

using namespace std;


int main() {
    int T, res, N, M, doc, pos;
    cin >> T;
    for (int i=0; i<T; ++i){
        queue<pair<int, int>> que;
        priority_queue<int> pq;
        cin >> N >> M;
        int max_imp = 0, res = 0;

        for (int j=0; j<N; ++j){
            cin >> doc;
            que.push({j, doc});
            pq.push(doc);
        }

        int cnt = 0;
        while (true){
            pos = que.front().first;
            doc = que.front().second;
            que.pop();

            if (doc == pq.top()){
                ++cnt;
                pq.pop();
                if (pos==M) {
                    res = cnt;
                    break;
                }
            }
            else{
                que.push({pos, doc});
            }

        }
        cout << res << endl;

    }
}