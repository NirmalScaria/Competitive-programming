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
    int n,m,a,b;
    cin>>n>>m>>a>>b;
    if(b>=m*a){
        cout<<n*a<<endl; 
    }
    else{
        int res=0;
        res+=n/m;
        n-=res*m;
        res*=b;
        if(n*a>b){
            res+=b;
        }
        else{
            res+=n*a;
        }
        cout<<res;
    }
}
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int t=1;
    // cin>>t;
    while(t--){
        solve();
    }
    return 0;
}