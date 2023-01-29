#include<bits/stdc++.h>
using namespace std;


typedef long long ll;
typedef pair<int,int> P;
typedef vector<int> VI;

#define _rep(i,n) repi(i,0,n)
#define repi(i,a,b) for(int i=int(a);i<int(b);++i)
#define all(x) (x).begin(),(x).end()
const int MOD1e97=1e9+7;

template< int mod >
struct ModInt {
  int x;

  ModInt() : x(0) {}

  ModInt(int64_t y) : x(y >= 0 ? y % mod : (mod - (-y) % mod)) {}

  ModInt &operator+=(const ModInt &p) {
    x = (x + p.x) % mod;
    return *this;
  }

  ModInt &operator-=(const ModInt &p) {
    x = (x + mod - p.x) % mod;
    return *this;
  }

  ModInt &operator*=(const ModInt &p) {
    x = static_cast<long long>(1LL * x * p.x % mod);
    return *this;
  }

  ModInt &operator/=(const ModInt &p) {
    *this *= p.inverse();
    return *this;
  }

  ModInt operator-() const { return ModInt(-x); }

  ModInt operator+(const ModInt &p) const { return ModInt(*this) += p; }

  ModInt operator-(const ModInt &p) const { return ModInt(*this) -= p; }

  ModInt operator*(const ModInt &p) const { return ModInt(*this) *= p; }

  ModInt operator/(const ModInt &p) const { return ModInt(*this) /= p; }

  bool operator==(const ModInt &p) const { return x == p.x; }

  bool operator!=(const ModInt &p) const { return !(*this == p); }

  ModInt inverse() const {
    int a = x, b = mod, u = 1, v = 0, t;
    while(b > 0) {
      t = a / b;
      a -= t * b;
      swap(a, b);
      u -= t * v;
      swap(u, v);
    }
    return ModInt(u);
  }

  ModInt pow(int64_t n) const {
    ModInt ret(1), mul(x);
    while(n > 0) {
      if(n & 1) ret *= mul;
      mul *= mul;
      n >>= 1;
    }
    return ret;
  }

  friend ostream &operator<<(ostream &os, const ModInt &p) {
    return os << p.x;
  }

  friend istream &operator>>(istream &is, ModInt &a) {
    int64_t t;
    is >> t;
    a = ModInt< mod >(t);
    return (is);
  }

  constexpr static int get_mod() { return mod; }
};

using modint = ModInt< MOD1e97 >;

int main() {
  string s;
  cin >> s;
  vector< vector<modint> > dp(s.size(), vector<modint>(2, 0));
  // cout << s << endl;
  dp[0][0] = 1;
  dp[0][1] = 2;

  repi(i, 1, s.size()) {
    if(s[i] == '0') {
      dp[i][0] = dp[i-1][0] * 3;
      dp[i][1] = dp[i-1][1];
    }
    else {
      dp[i][0] = dp[i-1][0]*3 + dp[i-1][1];
      dp[i][1] = dp[i-1][1] * 2;
    }
  }

  cout << dp[dp.size() - 1][0] + dp[dp.size() - 1][1] << endl;
}
