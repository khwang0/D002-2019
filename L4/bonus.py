#design rrectangle overlapping?
def overlap(x1,x2,x3,x4,y1,y2,y3,y4):
    '''first 4 coordinates for 1 rectangle
next 4 for the other one'''
    if x1[0]==x2[0] :
        if (x1[1]>=y1[1]>=x2[1]) or (x2[1]>=y1[1]>=x1[1]) or (x1[1]>=y2[1]>=x2[1]) or (x2[1]>=y2[1]>=x1[1]) or (x1[1]>=y3[1]>=x2[1]) or (x2[1]>=y3[1]>=x1[1]) or (x1[1]>=y4[1]>=x2[1]) or (x2[1]>=y4[1]>=x1[1]):
            status = 1 # y ok
    if x1[1]==x2[1]:
        if (x1[0]>=y1[0]>=x2[0]) or (x2[0]>=y1[0]>=x1[0]) or (x1[0]>=y2[0]>=x2[0]) or (x2[0]>=y2[0]>=x1[0]) or (x1[0]>=y3[0]>=x2[0]) or (x2[0]>=y3[0]>=x1[0]) or (x1[0]>=y4[0]>=x2[0]) or (x2[0]>=y4[0]>=x1[0]):
            status = 2 # x ok
    if status == 1:
        if (x1[0]>=y1[0]>=x3[0]) or (x2[0]>=y1[0]>=x3[0]) or (x1[0]>=y2[0]>=x3[0]) or (x2[0]>=y2[0]>=x3[0]) or (x1[0]>=y3[0]>=x3[0]) or (x2[0]>=y3[0]>=x3[0]) or (x1[0]>=y4[0]>=x3[0]) or (x2[0]>=y4[0]>=x1[0]):
            status = 3
    if status == 2:
        if (x1[1]>=y1[1]>=x3[1]) or (x2[1]>=y1[1]>=x3[1]) or (x1[1]>=y2[1]>=x3[0]) or (x2[1]>=y2[1]>=x3[1]) or (x1[1]>=y3[1]>=x3[1]) or (x2[1]>=y3[1]>=x3[1]) or (x1[1]>=y4[1]>=x3[1]) or (x2[1]>=y4[1]>=x3[1]):
            status = 3
    if status == 3 :
        print('they overlap')
    else :
        print('they do not overlap')
        
