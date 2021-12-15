#include <bits/stdc++.h>

using namespace std;

#ifdef LOCAL
#define dbg(...) cerr << "(" << #__VA_ARGS__ << "):", dbg_out(__VA_ARGS__)
#else
#define dbg(...)
#endif

#define ar array
#define ll long long
#define ld long double
#define sza(x) ((int)x.size())
#define all(a) (a).begin(), (a).end()

const int MAX_N = 1e5 + 5;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;



void solve() {
    int n, sum=0;
    cin>>n;
    vector<int> x(n);
    for(int i=0; i<n;i++){
        cin>>x[i];
        sum+=x[i];
    }
    int abc = sum/(((n+1)*n)/2);
    vector<int> result(n);
    int flag = 0;
    int ans = 0;
    for(int i=0;i<n-1;i++){
        ans = x[i] + abc - x[i+1];
        if(ans%n!=0 || ans<=0){
            cout<<"NO"<<endl;
            return;
        }
        ans/=n;
        result[i+1]=ans;
    }
    if(flag==0){
        ans = x[n-1] + abc - x[0];
        if(ans%n!=0 || ans<=0){
            cout<<"NO"<<endl;
            return;
        }
        ans/=n;
        result[0]=ans;
        cout<<"YES"<<endl;
        for(int i=0; i<n; i++){
            cout<<result[i]<<" ";
        }
        cout<<endl;


    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    cin >> tc;
    while(tc--){
        solve();
    }
}