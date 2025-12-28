from itertools import combinations
n=int(input ("enter umber of trasactions:"))
transactions=[]
for i in range(n):
    t=input(f"Trasaction{i+1}: ").split()
    transactions.append(set(t))

min_sup=int(input("enter minimu support"))
min_conff=int(input("enter minimum cofidence(in %):"))

unique_items=sorted(list({items for t in transactions for items in t}))
frequent=[]

for item in unique_items:
    count=sum(item in t for t in transactions)
    if count>=min_sup:
        frequent.append({item})

print("frequent 1-itemsets:",frequent)

k=2
final_ferquent=frequent.copy()
while True:
    candidates=[]
    for i in frequent:
        for j in frequent:
            if i !=j:
                union_set=i.union(j)
                if len(union_set)==k and union_set not in candidates:
                    candidates.append(union_set)
    new_frequent=[]
    for c in candidates:
        count=sum(c.issubset(t) for t in transactions)
        if count>=min_sup:
            new_frequent.append(c)
    if not new_frequent:
        break
    frequent=new_frequent
    final_ferquent.extend(frequent)  
    k+=1

print("\n all frequent itemsets:")
for i in final_ferquent:
    print(set(i))

print("\n assosiatio rule:")
for itemset in final_ferquent:
    if len(itemset)>=2:
        for r in range(1,len(itemset)):
            for left in combinations(itemset,r):   
                left=set(left)
                right=itemset-left
                if right:
                    left_supp=sum(left.issubset(t) for t in transactions )
                    both_supp=sum(itemset.issubset(t) for t in transactions )
                    conff=(both_supp/left_supp)*100
                    if conff>=min_conff:
                        print(f"{left}=>{right}(conff:{conff:.2f}%)") 