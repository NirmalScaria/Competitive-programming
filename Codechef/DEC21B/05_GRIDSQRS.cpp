#include</Users/nirmalscaria/Documents/Support/stdc++.h>
using namespace std;
#define ll long long
#define ull unsigned long long
#define PI 3.14
#define vi vector<int> 
#define vll vector<long long>
#define vull vector<unsigned long long>
#define mod 1000000007
#define pb push_back
ll solve(){
	int n;
	cin>>n;
	vector<string> x(n);
	for(int i=0;i<n;i++){
			cin>>x[i];
	}
	int toLeft[n][n];
	int toUp[n][n];
	memset(toLeft,0,sizeof(toLeft[0][0])*n*n);
	memset(toUp,0,sizeof(toLeft[0][0])*n*n);
	for(int i=0;i<n;i++){
		if(x[i][0]=='1'){
			toLeft[i][0]=1;
		}
		if(x[0][i]=='1'){
			toUp[0][i]=1;
		}

		for(int j=1;j<n;j++){
			if(x[i][j]=='1'){
				toLeft[i][j]=toLeft[i][j-1]+1;
			}
			if(x[j][i]=='1'){
				toUp[j][i]=toUp[j-1][i]+1;
			}
		}
	}
	int count = 0;
	int ttt=0;
	for(int i=0;i<n;i++){
		for(int j =0 ;j<n;j++){
			if(x[i][j]=='1'){
				count+=1;
				ttt=min(min(i,j)+1,min(toUp[i][j],toLeft[i][j]));
				for(int kk=1;kk<ttt;kk++){
					if((toLeft[i-kk][j] > kk) && (toUp[i][j-kk]>kk)){
						count+=1;
					}
				}
			}
		}
	}

	return count;
}
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
	int q;
	cin>>q;
	while(q--){
			//solve();
			cout<<solve()<<"\n";
		//if(solve())cout<<"-1\n";
	}
	// your code goes here
	return 0;
}