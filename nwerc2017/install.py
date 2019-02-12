from collections import namedtuple
#int n,m,i,j,x,f[N][M],g[N][M],w[N][M],q[N],cnt;
app = namedtuple('app',['p','w','t'])

if __name__ ==  "__main__":
    n, m = [int(i) for i in input().strip().split()]
    a = [app(0,0,0)]
    for i in range(1,n+1):
        d,s = [int(i) for i in input().strip().split()]
        a.append(app(i, max(d,s), max(d,s) - s))
    
    a = a[0:1] + sorted(a[1:],key = lambda x:x.t, reverse = True)
    #print(a)
    f,g,w,q = [], [], [], []
    for i in range(n + 1):
        f.append([])
        g.append([])
        w.append([])
        q.append(0)
        for j in range(m + 1):
            f[i].append(-10010)
            g[i].append(0)
            w[i].append(0)
            
    f[0][m]=0
    #print(f)
    for i in range(1, n+1):
        for j in range(m+1):
            f[i][j]=f[i-1][j]
            g[i][j]=j
            w[i][j]=0
        
        for j in range(m+1):
            if(f[i-1][j]>=0):
                if(j<a[i].w):
                    continue
                if(f[i-1][j]+1>f[i][j-a[i].w+a[i].t]):
                    f[i][j-a[i].w+a[i].t]=f[i-1][j]+1
                    g[i][j-a[i].w+a[i].t]=j
                    w[i][j-a[i].w+a[i].t]=a[i].p
    x = 0        
    for i in range(m+1):
        if(f[n][i]>f[n][x]):
            x=i
            
    print(f[n][x])
    cnt = 0
    for i in range(n, -1, -1):
        cnt += 1
        if(w[i][x]):
            q[cnt]=w[i][x]
        x=g[i][x]
    
    for i in range(cnt - 1, 0, -1):
        if q[i] != 0:
            print(q[i], end = ' ')

