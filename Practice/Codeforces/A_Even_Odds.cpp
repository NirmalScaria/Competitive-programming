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
    ull n,k;
    cin>>n>>k;
    if(k<=(n+1)/2){
        cout<< (k-1) * 2 +1;
        return;
    }
    else{
        cout<< (k-(n+1)/2 ) * 2 ;
        return;
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