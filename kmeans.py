from random import randint
def euclideanDist(a,b):
    dist=0
    for i in range(len(a)):
        dist+=(a[i]-b[i])**2
    return dist**0.5

def printer(dp,centroids,clusterlist,dists):
    line="_"*(len(centroids)+1)*15
    print(line)
    print("{:<12}".format("datapoint"),end=' ')
    for i in range(len(centroids)):
        print("{:<12}".format("centroid"+str(i)),end='')
    print()
    print(line)
    for i in range(len(dp)):
        print("{:<12}".format(str(dp[i])),end='')
        for j in range(len(centroids)):
            print("{:<12}".format(str(round(dists[i][j],2))),end='')
        print()
    print(line)

with open("data.txt",'r') as f: 
    lines=f.readlines()
dp=[list(map(int,line.strip().split(',')))for line in lines]
num_dp=len(dp)
num_attr=len(dp[0])

k=int(input(f"enter number of cluster(2 to {num_dp-1}):"))


centroids=[]
while len(centroids)!=k:
    temp=randint(0,num_dp-1)
    if dp[temp] not in centroids:
        centroids.append(dp[temp])
print("randomly  choosen initial cetroid",centroids)


clusterlist=[-1]*num_dp
check=True
itercount=1

while check:
    check=False
    dists=[]
    for pno,p in enumerate(dp):
        closestcentroid,valclosestcetroid=-1,float('inf')
        dist_list=[]
        for ci,cent in enumerate(centroids):
            dist=euclideanDist(p,cent)
            dist_list.append(dist)
            if dist<valclosestcetroid:
                valclosestcetroid=dist
                closestcentroid=ci
        dists.append(dist_list)
        if clusterlist[pno]!=closestcentroid:
            check=True
            clusterlist[pno]=closestcentroid
    print(f"\niteration:{itercount}")
    printer(dp,centroids,clusterlist,dists)
    itercount+=1

    for ind in range(len(centroids)):
        mean=[0]*num_attr
        count=0
        for i,cl in enumerate(clusterlist):
            if cl==ind:
                count+=1
                for j in range (num_attr):
                    mean[j]+=dp[i][j]
        if count >0:

            mean=[round(x/count,2)for x in mean]
            centroids[ind]=mean

print("final cetroid",centroids)       
            