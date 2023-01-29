#include<bits/stdc++.h>
using namespace std;

typedef pair<int, int> Job;

struct {
  bool operator()(Job a, Job b) const
  {
    return a.second < b.second;
  }
} custom;


int main() {
  int N;
  cin >> N;

  vector<Job> jobs;

  for(int i=0;i<N;i++) {
    int a, b;
    cin >> a >> b;
    jobs.push_back({a, b});
  }

  sort(jobs.begin(), jobs.end(), custom);

  long long required = 0;
  bool ans = true;
  for(int i=0;i<N;i++) {
    // cout << jobs[i].first << " " << jobs[i].second << endl;
    required += jobs[i].first;
    if(required > jobs[i].second) {
      ans = false;
      break;
    }
  }

  cout << (ans ? "Yes" : "No") << endl;

}
