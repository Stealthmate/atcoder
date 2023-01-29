#include<bits/stdc++.h>
using namespace std;

int main() {
  int n, m;
  cin >> n >> m;
  vector< vector<int> > edgelist;
  edgelist.resize(n, {});

  for(int i=0;i<m;i++) {
    int u, v;
    cin >> u >> v;
    edgelist[u-1].push_back(v - 1);
  }

  int start;
  int target;
  cin >> start >> target;
  start -=1;
  target -=1;

  long long ans = -1;

  queue< pair<int, int> > q;
  set<int> visited;
  q.push({start, 0});
  while(!q.empty()) {
    pair<int, int> node = q.front();
    q.pop();
    if(visited.find(node.first) != visited.end()) continue;
    visited.insert(node.first);

    // cout << "Am at " << node.first << endl;
    for(auto &n1 : edgelist[node.first]) {
      for(auto &n2 : edgelist[n1]) {
        for(auto &n3 : edgelist[n2]) {
          if(visited.find(n3) != visited.end()) continue;
          if(n3 == target) {
            ans = node.second + 1;
            break;
          }
          // cout << "PUSH " << n3 << endl;
          q.push({n3, node.second + 1});
        }
      }
    }
  }

  cout << ans << endl;
}
