#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define ull unsigned long long
#define PI 3.14
#define vi vector<int> 
#define vll vector<long long>
#define vull vector<unsigned long long>
#define mod 1000000007
#define pb push_back
void solve(){
    string inp;
    cin>>inp;
    int longest=1;
    for(int i=1; i<inp.length(); i++){
        if(inp[i] == inp[i-1]){
            longest +=1 ;
            if(longest>=7){
                cout<<"YES"<<"\n";
                return;
            }
        }
        
        else{
            longest=1;
        }
    }
    cout<<"NO\n";
    return; 
}
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    // int t=1;
    // cin>>t;
    // while(t--){
        solve();
    // }
    return 0;
}