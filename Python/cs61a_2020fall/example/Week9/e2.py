def search(query,ranking=lambda r:-r.starts):
    results=[r for r in Restaurant.all if query in r.name]
    return sorted(results,key=ranking)

def reviewed_both(r,s):
    return fast_overlap(r.reviewers,s.reviewers)

class Restaurant:
    all=[]
    def __init__(self,name,starts,reviewers):
        self.name,self.start=name,starts
        self.reviewers=reviewers
        Restaurant.all.append(self)
    
    def similar(self,k,similarity=reviewed_both):
        others=list(Restaurant.all)
        others.remove(self)
        return sorted(others,key=lambda r:-similarity(self,r))[:k]
    
    def __repr__(self):
        return '<'+self.name+'>'
    
def fast_overlap(s,t):
    i,j,count=0,0,0
    while i <len(s) and j<len(t):
        if s[i]==t[j]:
            count,i,j=count+1,i+1,j+1
        elif s[i]<t[j]:
            i+=1
        else:
            j+=1
    return count

import json
reviewers_for_restaurant={}
for line in open('reviews.json'):
    r=json.loads(line)
    biz=r['business_id']
    if biz not in reviewers_for_restaurant:
        reviewers_for_restaurant[biz]=[r['user_id']]
    else:
        reviewers_for_restaurant[biz].append(r['user_id'])

for line in open('restaurants.json'):
    r=json.loads(line)
    reviewers=reviewers_for_restaurant[r['business_id']]
    Restaurant(r['name'],r['starts'],sorted(reviewers))

result=search('Thai')
for r in result:
    print(r,'is similar to',r.similar(3))