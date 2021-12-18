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
    string s;
    cin>>s;
    while(s.substr(0,3) == "WUB"){
        s=s.substr(3);
    }
    while(s.substr(s.length()-3,s.length()) == "WUB"){
        s=s.substr(0,s.length()-3);
    }
    
    cout<<s;
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