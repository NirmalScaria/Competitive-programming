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
    string inp;
    cin>>inp;
    for(int i=0; i<inp.length(); i++){
        if(inp[i]=='H' || inp[i]=='Q' || inp[i]=='9' ){
            cout<<"YES"<<endl;
            return;
        }
    }
    cout<<"NO"<<endl;
    return;
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