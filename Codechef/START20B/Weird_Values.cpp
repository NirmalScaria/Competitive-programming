#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define ull unsigned long long
#define PI 3.14
#define vi vector<int> 
#define vll vector<long long>
#define vull vector<unsigned long long>
#define mod 1000000007
#define endl "\n"
#define vvi vector<vector<ind>>
#define vvll vector<vector<long long>>
#define pb push_back
void solve(){
  int n;
  cin>>n;
  vector<int> a(n);
  for(auto &i : a) {cin >>i;}
  map<int,vi> d;
  for(int i=0; i<n; i++){
      if(d.count(a[i]))
          d[a[i]].pb(i);
      else
          d[a[i]]={-1,i};
  }
    int result = 0;
    map<int,vi>::iterator it;
    for(it = d.begin(); it!=d.end(); it++){
        int val = it->first;
        d[val].pb(n);
        int l=1, r=val;
        while(r<d[val].size()-1){
            int scnt = (d[val][l] - d[val][l-1]) * (d[val][r+1]-d[val][r]) * val;
            result += scnt;
            l+=1;
            r+=1;
        }
    }
    cout<<result<<endl;
    return;
}
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int t=1;
    cin>>t;
    while(t--){
        solve();
    }
    return 0;
}