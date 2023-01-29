#include <iostream>
#include <vector>
#include <utility>
using namespace std;

vector<long long> a;
long long K;

int main() {
  long long N;
  cin >> N >> K;
  for(long long i=0;i<N;i++) {
    long long x;
    cin >> x;
    a.push_back(x);
  }


  long long ans = 0;

  long long i = 0;
  long long j = 0;
  long long lastSum = a[0];
  while(i < a.size() && j < a.size()) {
    if(lastSum >= K) {
      ans += N - j;
      lastSum -= a[i];
      i++;
    }
    else {
      j++;
      // cout << "Small sum " << lastSum << " added " << j << " " << a[j] << endl;
      lastSum += a[j];
      if(lastSum >= K) {
        // cout << "YEY" << endl;
        ans += N - j;
        lastSum -= a[i];
        i++;
      }
    }
  }

  cout << ans << endl;
}
