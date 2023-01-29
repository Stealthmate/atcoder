#include<bits/stdc++.h>
using namespace std;


typedef long long ll;
typedef pair<int,int> P;
typedef vector<int> VI;

#define _rep(i,n) repi(i,0,n)
#define repi(i,a,b) for(int i=int(a);i<int(b);++i)
#define all(x) (x).begin(),(x).end()
const int MOD1e97=1e9+7;

typedef pair<int, int> Node;

vector< vector< int > > A;
int N;

struct SimpleHash {
    size_t operator()(const Node& p) const {
        return p.first ^ p.second;
    }
};

unordered_map<Node, int, SimpleHash> paths;
unordered_set<Node, SimpleHash> st;

int dfs(int a, int b) {

  Node node = {min(a, b), max(a, b)};

  if(paths.find(node) != paths.end()) return paths[node];

  if(st.find(node) != st.end()) { cout << -1 << endl; exit(0); }

  st.insert(node);

  vector<int> rs = {1};

  auto i = find(A[a].begin(), A[a].end(), b);
  for(auto j = A[a].begin(); j != i; j++) {
    rs.push_back(1 + dfs(a, *j));
  }

  i = find(A[b].begin(), A[b].end(), a);
  for(auto j = A[b].begin(); j != i; j++) {
    rs.push_back(1 + dfs(b, *j));
  }


  st.erase(node);
  paths[node] = *max_element(rs.begin(), rs.end());
  return paths[node];

}

int main() {

  cin >> N;
  repi(i, 0, N) {
    A.push_back({});
    repi(j, 0, N - 1) {
      int x;
      cin >> x;
      A[i].push_back(x - 1);
    }
  }

  int ans = -1;
  repi(i, 0, N - 1) repi(j, 0, N) {
    ans = max(ans, dfs(j, A[j][i]));
  }

  cout << ans << endl;

}
