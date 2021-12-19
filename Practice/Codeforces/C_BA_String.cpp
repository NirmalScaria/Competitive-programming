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
    int n,k,x;
    cin>>n>>k>>x;
    string s;
    cin>>s;
    vi arr;
    for(int i=0; i<n;i++){
        if(s[i]=='a'){
            arr.pb(0);
        }
        else{
            int count = 1; 
            int j=i;
            while(j<n && s[j]=='*'){
                j++;
            }
            arr.pb(j-i);
            i=j-1;
        }
    }
    
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