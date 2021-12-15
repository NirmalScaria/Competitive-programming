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
    int n, totalSum=0, mySum = 0;
    cin>>n;
    vi a(n);
    for(int i=0; i<n; i++){
        cin>>a[i];
        totalSum+=a[i];
    }
    sort( a.begin(), a.end());
    for(int i=n-1; i>=0; i--){
        mySum += a[i];
        if(totalSum - mySum < mySum){
            cout<<n-i<<"\n";
            return;
        }
    }
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