import requests
import os.path
import Configuration.getResponse as rsp
print("Enter the link to contest page.")
print("Examples : \nhttps://codeforces.com/contest/1609 \nhttps://www.codechef.com/FOUR21C\n> ",end="")
contesturl=input()
if(contesturl[-1]=="/"):
    contesturl=contesturl[:-1]
if(contesturl.find('codeforces.com')!=-1):
    #Codeforces contest
    if(os.path.exists('Configuration/codeforcesRequest.txt')==False):
        print("ERROR")
        print("Please generate a copy of Curl request to codeforcesRequest.txt and retry")
        exit()
    readmedata=rsp.getCodeforcesResponse(contesturl)
    pathurl="Codeforces/CONTEST"+contesturl.split("/")[-1]+"/README.MD"
    f=open(pathurl,"w")
    f.write(readmedata)
    f.close()
elif(contesturl.find("codechef.com")!=-1):
    #Codechef contest
    pass
else:
    print("Invalid URL")
    exit()
