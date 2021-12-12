from typing import final
import requests
from requests.api import head
from requests.structures import CaseInsensitiveDict
import json

def getCodechefResponse(contUrl):
    creds=open('Configuration/codechefRequest.txt','r').read()
    contestCode=contUrl.split('/')[-1]
    print("Fetching Codechef Results")
    credsl=creds.lower()
    url = "https://www.codechef.com/api/rankings/"+contestCode+"?sortBy=rank&order=asc&page=1&itemsPerPage=25"
    useragent=creds[credsl.find("user-agent")+12:credsl.find("'",credsl.find('user-agent')+13)]
    cookiee=creds[credsl.find("cookie")+8:credsl.find("'",credsl.find('cookie')+9)]
    headers = CaseInsensitiveDict()
    headers["Pragma"] = "no-cache"
    headers["Accept"] = "application/json, text/javascript, */*; q=0.01"
    headers["Accept-Language"] = "en-GB,en;q=0.9"
    headers["Accept-Encoding"] = "gzip, deflate, br"
    headers["Cache-Control"] = "no-cache"
    headers["Host"] = "www.codechef.com"
    headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15"
    headers["Connection"] = "keep-alive"
    headers["Referer"] = contUrl
    headers["Cookie"] = cookiee
    headers["X-Requested-With"] = "XMLHttpRequest"
    headers["x-csrf-token"] = "2afb417ca5f7ff3149bf011645361b4c9656189c14831fc98a8c406090bc6ba2"
    response=requests.get("https://www.codechef.com/api/contests/"+contestCode,headers=headers).content
    response=json.loads(response)
    print(response["problemsstats"])
    contestName=response["name"]
    totalProblems=0
    solvedProblems=0
    print("Contest name : ",contestName)
    problems={}
    print("Number of problems : ",len(response["problems"]))
    print("Succesful problems are : ",response["problemsstats"]["solved"])
    for item in response["problems"]:
        totalProblems+=1
        problems[item]=[response["problems"][item]["name"]]
        problems[item]+=[contUrl+response["problems"][item]["problem_url"]]
        problems[item]+=["Unattempted"]
    for item in response["problemsstats"]["attempted"]:
        problems[item][2]="Failed"
    for item in response["problemsstats"]["partially_solved"]:
        problems[item][2]="Partially Solved"
    for item in response["problemsstats"]["solved"]:
        solvedProblems+=1
        problems[item][2]="Solved"
    print(problems)
    response=requests.get(url,headers=headers).content
    response=json.loads(response)
    if("totalItems" not in response):
        print("Enter total number of participants.\n> ")
        totalparticipants=int(input())
    else:
        totalparticipants=response["totalItems"]
    if("rank_and_score" not in response):
        print("Enter your rank.\n> ",end="")
        myrank=int(input())
    else:
        myrank=response["rank_and_score"]["rank"]
    finalresult=""
    finalresult+="# CODECHEF CONTEST "+contestCode+"\n\n"
    finalresult+="## "+contestName+'\n\n'
    finalresult+="**Contest link:** "+contUrl+"\n\n"
    finalresult+="**Standing:** **"+str(myrank)+"** out of **"+str(totalparticipants)+"** participants\n\n"
    finalresult+="**Status:** Solved **"+str(solvedProblems)+"** out of **"+str(totalProblems)+"** problems\n\n"
    finalresult+="## PROBLEMS\n\n"
    for item in problems:
        finalresult+="- ["
        finalresult+='x' if problems[item][2]=="Solved" else ' '
        finalresult+="] **"+item+" : "+problems[item][0]+"**\n\n"
        finalresult+="> LINK : "+problems[item][1]+"\n"
        finalresult+='>\n'
        finalresult+=">STATUS : **"+problems[item][2]+"**\n\n"
    # print(finalresult)
    return(finalresult)


def getCodeforcesResponse(contUrl):
    creds=open('Configuration/codeforcesRequest.txt','r').read()
    useragent=creds[creds.find("user-agent")+12:creds.find("'",creds.find('user-agent')+13)]
    cookie=creds[creds.find("cookie")+8:creds.find("'",creds.find('cookie')+9)]
    print("Fetching Codeforces data ")
    headers = {
    'authority': 'codeforces.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'upgrade-insecure-requests': '1',
    'user-agent': useragent,
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'same-origin',
    'sec-fetch-dest': 'empty',
    'referer': 'https://codeforces.com/service-worker-78545.js',
    'accept-language': 'en-US,en;q=0.9,ml;q=0.8,mt;q=0.7',
    'cookie': cookie,
    }
    response=str(requests.get(contUrl+'/standings',headers=headers).content)
    title=response[response.find('og:title')+31:response.find('"',response.find('og:title')+25)].split(' - Codeforces')[0]
    customlinktext=response[response.find('custom-links-pagination'):response.find('</div>',response.find('custom-links-pagination'))]
    customlinktext=customlinktext.split('<nobr>')[-1]
    totalparticipants=customlinktext.split(' </a>')[0].split('&nbsp;-&nbsp;')[1].replace('\\n','').replace('\\r','').replace(" ","")


    myname = response[response.find('"',response.find('var handle ='))+1:response.find('"',response.find('"',response.find('var handle ='))+1)]
    print('Handle : @',myname)
    print('Total contestants : ',totalparticipants)
    response=str(requests.get('https://codeforces.com/contests/with/'+myname+'/',headers=headers).content)
    myrank="-"
    if(len(response[response.find('title="'+title):].split("<td>"))>1):
        myrank=response[response.find('title="'+title):].split("<td>")[2].split("</td")[0]
    print('CONTEST NAME: ',title)
    print('Your rank:', myrank)
    response=str(requests.get(contUrl,headers=headers).content)
    problems=response.split('<th>Name</th>')[1].split('</tbody>')[0].split('&nbsp;x')[:-1]
    problemlist=[]
    solvedcount=0
    problemcount=0
    for item in problems:
        problemcount+=1
        if(item.find('accepted')!=-1):
            problemlist+=[['Solved']]
            solvedcount+=1
        elif(item.find('rejected')!=-1):
            problemlist+=[['Rejected']]
        else:
            problemlist+=[['Unattempted']]
    for i in range(len(problems)):
        link='https://codeforces.com'+problems[i][problems[i].find('href="')+6:problems[i].find('"',problems[i].find('href="')+8)]
        problemlist[i]+=[link]
        problemcode=link.split('/')[-1]
        problemlist[i]+=[problemcode]
        name=problems[i][problems[i].find("-->")+3:problems[i].find('<!--',problems[i].find('-->'))]
        problemlist[i]+=[name]
    h1="CODEFORCES CONTEST "+contUrl.split('/')[-1]
    print('-'*100)
    finalresult=""
    finalresult+="# "+h1+"\n\n"
    finalresult+="## "+title+'\n\n'
    finalresult+="**Contest link:** "+contUrl+"\n\n"
    finalresult+="**Standing:** **"+myrank+"** out of **"+totalparticipants+"** participants\n\n"
    finalresult+="**Status:** Solved **"+str(solvedcount)+"** out of **"+str(problemcount)+"** problems\n\n"
    finalresult+="## PROBLEMS\n\n"
    for item in problemlist:
        finalresult+="- ["
        finalresult+='x' if item[0]=="Solved" else ' '
        finalresult+="] **"+item[2]+" : "+item[3]+"**\n\n"
        finalresult+="> LINK : "+item[1]+"\n"
        finalresult+='>\n'
        finalresult+="> STATUS : **"+item[0]+"**\n\n"

    return(finalresult)
    # print("My rank:",myrank)
