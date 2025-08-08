class DisJointSet:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.size = [1]*n 
        self.unique_emails = {}
    def findParent(self,node):
        if node == self.parent[node]:
            return node 
        else:
            self.parent[node] = self.findParent(self.parent[node])
            return self.parent[node]
    def UnionbySize(self,u,v):
        ulp_u = self.findParent(u)
        ulp_v = self.findParent(v)
        if self.size[ulp_v] > self.size[ulp_u]:
            self.size[ulp_v] += self.size[ulp_u]
            self.parent[ulp_u] = ulp_v
        else:
            self.size[ulp_u] += self.size[ulp_v]
            self.parent[ulp_v] = ulp_u
    def Unique_set(self,mails,index):
        for i in range(len(mails)):
            if mails[i] not in self.unique_emails:
                self.unique_emails[mails[i]] = index
            elif mails[i] in self.unique_emails:
                for j in range(i+1,len(mails)):
                    self.UnionbySize(i,index)
                    self.unique_emails[mails[j]] = index
                break 
    def UnionbyMails(self):
        result = [[] for _ in range(len(self.parent))]
        for i in self.unique_emails:
            result[self.findParent(self.unique_emails[i])].append(i)
        for i in result:
            i.sort()
        return result

n = int(input("Enter the total no. of Accounts List "))
Ds = DisJointSet(n) 
acc = []
"""for i in range(n):
    L = eval(input("Enter the Account Details : "))
    acc.append(L)"""
acc = [["John","J1@com","J2@com","J3@com"],["John","J4@com"],["raj","r1@com","r2@com"],["John","J1@com","J5@com"],["raj","r2@com","r3@com"],["Mary","M1@com"]]
for i in range(len(acc)):
    Ds.Unique_set(acc[i][1:],i)
result = Ds.UnionbyMails()
ans = [[]for _ in range(n)]
for i in range(len(acc)):
    if len(result[i]) != 0:
        ans[i].append(acc[i][0])
        ans[i].extend(result[i])
print(ans)


        
