
if __name__ == "__main__":
    num = int(input().strip())
    
    dirt = [int(i) for i in input().strip().split()]

    dirt_ctr = 0
    clean_ctr = 0
    has_dirt = 0
    for i in range(1,366):
        if dirt_ctr >= 20:
            dirt_ctr = 0
            clean_ctr += 1
            has_dirt = False
            #print(i)
        if i in dirt:
            has_dirt += 1
        if has_dirt:
            dirt_ctr += has_dirt
        
            
        

    if has_dirt:
        clean_ctr += 1

    print(clean_ctr)
