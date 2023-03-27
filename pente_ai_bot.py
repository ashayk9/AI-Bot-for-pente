import sys
import time
import copy



# ==================================================================================================


    
def evaluate(board,capture_count,turn,depth,min_i,max_i,min_j,max_j):
    def check_horizontal_surround(i,j,k,colour):
        space_fill_count_w=0
        # horizontal
        if j+k-1>=0 and board[i][j+k-1]!=' ':
            space_fill_count_w+=((2 if board[i][j+k-1]==colour else 1)*close)
        if j+k-2>=0 and board[i][j+k-2]!=' ':
            space_fill_count_w+=((2 if board[i][j+k-2]==colour else 1)*far)    
        if j+k+1<19 and board[i][j+k+1]!=' ':
            space_fill_count_w+=((2 if board[i][j+k+1]==colour else 1)*close)
        if j+k+2<19 and board[i][j+k+2]!=' ':
            space_fill_count_w+=((2 if board[i][j+k+2]==colour else 1)*far)
        # vertical
        if i-1>=0 and board[i-1][j+k]!=' ':
            space_fill_count_w+=((2 if board[i-1][j+k]==colour else 1)*close)
        if i-2>=0 and board[i-2][j+k]!=' ':
            space_fill_count_w+=((2 if board[i-2][j+k]==colour else 1)*far)
        if i+1<19 and board[i+1][j+k]!=' ':
            space_fill_count_w+=((2 if board[i+1][j+k]==colour else 1)*close)
        if i+2<19 and board[i+2][j+k]!=' ':
            space_fill_count_w+=((2 if board[i+2][j+k]==colour else 1)*far)
        # diagonal
        if i-1>=0 and j+k-1>=0 and board[i-1][j+k-1]!=' ':
            space_fill_count_w+=((2 if board[i-1][j+k-1]==colour else 1)*close)
        if i-2>=0 and j+k-2>=0 and board[i-2][j+k-2]!=' ':
            space_fill_count_w+=((2 if board[i-2][j+k-2]==colour else 1)*far)
        if i+1<19 and j+k+1<19 and board[i+1][j+k+1]!=' ':
            space_fill_count_w+=((2 if board[i+1][j+k+1]==colour else 1)*close)
        if i+2<19 and j+k+2<19 and board[i+2][j+k+2]!=' ':
            space_fill_count_w+=((2 if board[i+2][j+k+2]==colour else 1)*far)
        # antidiagonal
        if i-1>=0 and j+k+1<19 and board[i-1][j+k+1]!=' ':
            space_fill_count_w+=((2 if board[i-1][j+k-1]==colour else 1)*close)
        if i-2>=0 and j+k+2<19 and board[i-2][j+k+2]!=' ':
            space_fill_count_w+=((2 if board[i-2][j+k-2]==colour else 1)*far)
        if i+1<19 and j+k-1>=0 and board[i+1][j+k-1]!=' ':
            space_fill_count_w+=((2 if board[i+1][j+k-1]==colour else 1)*close)
        if i+2<19 and j+k-2>=0 and board[i+2][j+k-2]!=' ':
            space_fill_count_w+=((2 if board[i+2][j+k-2]==colour else 1)*far)
        index=(i,j+k)
        return space_fill_count_w,index
    def check_vertical_surround(i,j,k,colour):
        space_fill_count_w=0
        # vertical
        if i+k-1>=0 and board[i+k-1][j]!=' ':
            space_fill_count_w+=((2 if board[i+k-1][j]==colour else 1)*close)
        if i+k-2>=0 and board[i+k-2][j]!=' ':
            space_fill_count_w+=((2 if board[i+k-2][j]==colour else 1)*far)
        if i+k+1<19 and board[i+k+1][j]!=' ':
            space_fill_count_w+=((2 if board[i+k+1][j]==colour else 1)*close)
        if i+k+2<19 and board[i+k+2][j]!=' ':
            space_fill_count_w+=((2 if board[i+k+2][j]==colour else 1)*far)
        # horizontal
        if j-1>=0 and board[i+k][j-1]!=' ': 
            space_fill_count_w+=((2 if board[i+k][j-1]==colour else 1)*close)
        if j-2>=0 and board[i+k][j-2]!=' ':
            space_fill_count_w+=((2 if board[i+k][j-2]==colour else 1)*far)
        if j+1<19 and board[i+k][j+1]!=' ':
            space_fill_count_w+=((2 if board[i+k][j+1]==colour else 1)*close)
        if j+2<19 and board[i+k][j+2]!=' ':
            space_fill_count_w+=((2 if board[i+k][j+2]==colour else 1)*far)
        # diagonal
        if i+k-1>=0 and j-1>=0 and board[i+k-1][j-1]!=' ':
            space_fill_count_w+=((2 if board[i+k-1][j-1]==colour else 1)*close)
        if i+k-2>=0 and j-2>=0 and board[i+k-2][j-2]!=' ':
            space_fill_count_w+=((2 if board[i+k-2][j-2]==colour else 1)*far)
        if i+k+1<19 and j+1<19 and board[i+k+1][j+1]!=' ':
            space_fill_count_w+=((2 if board[i+k+1][j+1]==colour else 1)*close)
        if i+k+2<19 and j+2<19 and board[i+k+2][j+2]!=' ': 
            space_fill_count_w+=((2 if board[i+k+2][j+2]==colour else 1)*far)
        # antidiagonal
        if i+k-1>=0 and j+1<19 and board[i+k-1][j+1]!=' ':
            space_fill_count_w+=((2 if board[i+k-1][j+1]==colour else 1)*close)
        if i+k-2>=0 and j+2<19 and board[i+k-2][j+2]!=' ':
            space_fill_count_w+=((2 if board[i+k-2][j+2]==colour else 1)*far)
        if i+k+1<19 and j-1>=0 and board[i+k+1][j-1]!=' ':
            space_fill_count_w+=((2 if board[i+k+1][j-1]==colour else 1)*close)
        if i+k+2<19 and j-2>=0 and board[i+k+2][j-2]!=' ':
            space_fill_count_w+=((2 if board[i+k+2][j-2]==colour else 1)*far)
        index=(i+k,j)
        return space_fill_count_w,index

    def check_diagnol_surround(i,j,k,colour):
        space_fill_count_w=0
        # vertical
        if i+k-1>=0 and board[i+k-1][j+k]!=' ':
            space_fill_count_w+=((2 if board[i+k-1][j+k]==colour else 1)*close)
        if i+k-2>=0 and board[i+k-2][j+k]!=' ': 
            space_fill_count_w+=((2 if board[i+k-2][j+k]==colour else 1)*far)
        if i+k+1<19 and board[i+k+1][j+k]!=' ':
            space_fill_count_w+=((2 if board[i+k+1][j+k]==colour else 1)*close)
        if i+k+2<19 and board[i+k+2][j+k]!=' ':
            space_fill_count_w+=((2 if board[i+k+2][j+k]==colour else 1)*far)
        # horizontal
        if j+k-1>=0 and board[i+k][j+k-1]!=' ': 
            space_fill_count_w+=((2 if board[i+k][j+k-1]==colour else 1)*close)
        if j+k-2>=0 and board[i+k][j+k-2]!=' ':
            space_fill_count_w+=((2 if board[i+k][j+k-2]==colour else 1)*far)
        if j+k+1<19 and board[i+k][j+k+1]!=' ':
            space_fill_count_w+=((2 if board[i+k][j+k+1]==colour else 1)*close)
        if j+k+2<19 and board[i+k][j+k+2]!=' ':
            space_fill_count_w+=((2 if board[i+k][j+k+2]==colour else 1)*far)
        # diagonal
        if i+k-1>=0 and j+k-1>=0 and board[i+k-1][j+k-1]!=' ':
            space_fill_count_w+=((2 if board[i+k-1][j+k-1]==colour else 1)*close)
        if i+k-2>=0 and j+k-2>=0 and board[i+k-2][j+k-2]!=' ':
            space_fill_count_w+=((2 if board[i+k-2][j+k-2]==colour else 1)*far)
        if i+k+1<19 and j+k+1<19 and board[i+k+1][j+k+1]!=' ':
            space_fill_count_w+=((2 if board[i+k+1][j+k+1]==colour else 1)*close)
        if i+k+2<19 and j+k+2<19 and board[i+k+2][j+k+2]!=' ':
            space_fill_count_w+=((2 if board[i+k+2][j+k+2]==colour else 1)*far)
        # anti-diagonal
        if i+k-1>=0 and j+k+1<19 and board[i+k-1][j+k+1]!=' ':
            space_fill_count_w+=((2 if board[i+k-1][j+k+1]==colour else 1)*close)
        if i+k-2>=0 and j+k+2<19 and board[i+k-2][j+k+2]!=' ':
            space_fill_count_w+=((2 if board[i+k-2][j+k+2]==colour else 1)*far)
        if i+k+1<19 and j+k-1>=0 and board[i+k+1][j+k-1]!=' ':
            space_fill_count_w+=((2 if board[i+k+1][j+k-1]==colour else 1)*close)
        if i+k+2<19 and j+k-2>=0 and board[i+k+2][j+k-2]!=' ':
            space_fill_count_w+=((2 if board[i+k+2][j+k-2]==colour else 1)*far)
        index=(i+k,j+k)
        return space_fill_count_w,index
    def check_antidiagnol_surround(i,j,k,colour):
        
        space_fill_count_w=0
        if i-k-1>=0 and board[i-k-1][j+k]!=' ':
            space_fill_count_w+=((2 if board[i-k-1][j+k]==colour else 1)*close)
        if i-k-2>=0 and board[i-k-2][j+k]!=' ': 
            space_fill_count_w+=((2 if board[i-k-2][j+k]==colour else 1)*far)
        if i-k+1<19 and board[i-k+1][j+k]!=' ':
            space_fill_count_w+=((2 if board[i-k+1][j+k]==colour else 1)*close)
        if i-k+2<19 and board[i-k+2][j+k]!=' ':
            space_fill_count_w+=((2 if board[i-k+2][j+k]==colour else 1)*far)
        # horizontal
        if j+k-1>=0 and board[i-k][j+k-1]!=' ': 
            space_fill_count_w+=((2 if board[i-k][j+k-1]==colour else 1)*close)
        if j+k-2>=0 and board[i-k][j+k-2]!=' ':
            space_fill_count_w+=((2 if board[i-k][j+k-2]==colour else 1)*far)
        if j+k+1<19 and board[i-k][j+k+1]!=' ':
            space_fill_count_w+=((2 if board[i-k][j+k+1]==colour else 1)*close)
        if j+k+2<19 and board[i-k][j+k+2]!=' ':
            space_fill_count_w+=((2 if board[i-k][j+k+2]==colour else 1)*far)
        # diagonal
        if i-k-1>=0 and j+k-1>=0 and board[i-k-1][j+k-1]!=' ':
            space_fill_count_w+=((2 if board[i-k-1][j+k-1]==colour else 1)*close)
        if i-k-2>=0 and j+k-2>=0 and board[i-k-2][j+k-2]!=' ':
            space_fill_count_w+=((2 if board[i-k-2][j+k-2]==colour else 1)*far)
        if i-k+1<19 and j+k+1<19 and board[i-k+1][j+k+1]!=' ':
            space_fill_count_w+=((2 if board[i-k+1][j+k+1]==colour else 1)*close)
        if i-k+2<19 and j+k+2<19 and board[i-k+2][j+k+2]!=' ':
            space_fill_count_w+=((2 if board[i-k+2][j+k+2]==colour else 1)*far)
        # antidiagonal
        if i-k-1>=0 and j+k+1<19 and board[i-k-1][j+k+1]!=' ':
            space_fill_count_w+=((2 if board[i-k-1][j+k+1]==colour else 1)*close)
        if i-k-2>=0 and j+k+2<19 and board[i-k-2][j+k+2]!=' ':
            space_fill_count_w+=((2 if board[i-k-2][j+k+2]==colour else 1)*far)
        if i-k+1<19 and j+k-1>=0 and board[i-k+1][j+k-1]!=' ':
            space_fill_count_w+=((2 if board[i-k+1][j+k-1]==colour else 1)*close)
        if i-k+2<19 and j+k-2>=0 and board[i-k+2][j+k-2]!=' ':
            space_fill_count_w+=((2 if board[i-k+2][j+k-2]==colour else 1)*far)
        # print("space_fill_count_w",space_fill_count_w)
        # print("i-k,j+k",i-k,j+k)
        index=(i-k,j+k)
        return space_fill_count_w,index
    #white_win_index=(-1,-1)
    
    last_value={
        'last_option_value':-1,
        'last_option_index':(-1,-1)
    }
    
    white_win_index={}
    black_win_index={}#(-1,-1)
    white_3_in_5={}
    black_3_in_5={}

    #less priority
    white_3_in_4={}
    black_3_in_4={}
    white_2_in_3={}
    black_2_in_3={}
    #===============
    
    black_capture_count=0
    white_capture_count=0
    black_cps={}
    white_cps={}

    far=2
    close=3
    evaluation=0
    
    white_prevent5_till_now=0
    white_prevent4_till_now=0
    white_prevent3_till_now=0
    white_prevent2_till_now=0
    black_prevent5_till_now=0
    black_prevent4_till_now=0
    black_prevent3_till_now=0
    black_prevent2_till_now=0
    return_index=(-1,-1)

    black_possible_wins=0

    
    for i in range(min_i,max_i+1):
        for j in range(min_j,max_j+1):
            if j<15:
                w_count=0
                b_count=0
                

                for k in range(5):
                    if board[i][j+k]=='b':
                        b_count+=1
                    elif board[i][j+k]=='w':
                        w_count+=1
                    
                #4 in 5
                if w_count==4 and b_count==0:
                    for k in range(5):
                        if board[i][j+k]==' ':
                            white_win_index['score']=1000000000000000000
                            white_win_index['index']=(i,j+k)
                if b_count==4 and w_count==0:
                    black_possible_wins+=1
                    for k in range(5):
                        if board[i][j+k]==' ':
                            black_win_index['score']=10000000000000000
                            black_win_index['index']=(i,j+k)
                #3 in 5
                if w_count==3 and b_count==0:
                    for k in range(5):
                        if board[i][j+k]==' ':
                            space_fill_count_w,index=check_horizontal_surround(i,j,k,'w')
                            
                            if white_3_in_5:
                                if space_fill_count_w>white_3_in_5['space_fill_count_w']:
                                    white_3_in_5['space_fill_count_w']=space_fill_count_w
                                    white_3_in_5['index']=index
                            else:
                                white_3_in_5['space_fill_count_w']=space_fill_count_w
                                white_3_in_5['index']=index

                if b_count==3 and w_count==0:
                    for k in range(5):
                        if board[i][j+k]==' ':
                            space_fill_count_b,index=check_horizontal_surround(i,j,k,'b')

                            if black_3_in_5:
                                if space_fill_count_b>black_3_in_5['space_fill_count_b']:
                                    black_3_in_5['space_fill_count_b']=space_fill_count_b
                                    black_3_in_5['index']=index
                            else:
                                black_3_in_5['space_fill_count_b']=space_fill_count_b
                                black_3_in_5['index']=index
            
            # horizontal in 4
            #for j in range(min_j,min(max_j+1,16)):
            if j<16:
                w_count=0
                b_count=0
                for k in range(4):
                    if board[i][j+k]=='w':
                        w_count+=1
                    elif board[i][j+k]=='b':
                        b_count+=1
                if w_count==3 and b_count==0:
                    for k in range(4):
                        if board[i][j+k]==' ':
                            space_fill_count_w,index=check_horizontal_surround(i,j,k,'w')
                            

                            if white_3_in_4:
                                if space_fill_count_w>white_3_in_4['space_fill_count_w']:
                                    white_3_in_4['space_fill_count_w']=space_fill_count_w
                                    white_3_in_4['index']=index
                            else:
                                white_3_in_4['space_fill_count_w']=space_fill_count_w
                                white_3_in_4['index']=index

                if b_count==3 and w_count==0:
                    for k in range(4):
                        if board[i][j+k]==' ':
                            space_fill_count_b,index=check_horizontal_surround(i,j,k,'b')
                            
                            if black_3_in_4:
                                if space_fill_count_b>black_3_in_4['space_fill_count_b']:
                                    black_3_in_4['space_fill_count_b']=space_fill_count_b
                                    black_3_in_4['index']=index
                            else:
                                black_3_in_4['space_fill_count_b']=space_fill_count_b
                                black_3_in_4['index']=index
                if ((board[i][j]=='w'and board[i][j+3]==' ') or (board[i][j]==' 'and board[i][j+3]=='w'))  and  board[i][j+1]=='b' and board[i][j+2]=='b':
                    #print(i,j)
                    black_capture_count+=1
                    white_surround_count=0
                    if board[i][j]==' ':
                        t=j
                    elif board[i][j+3]==' ':
                        t=j+3
                    white_surround_count,index=check_horizontal_surround(i,t,0,'w')
                    if black_cps:
                        if white_surround_count>black_cps['white_surround_count']:
                            black_cps['white_surround_count']=white_surround_count
                            black_cps['index']=index
                    else:
                        black_cps['white_surround_count']=white_surround_count
                        black_cps['index']=index
                    #print(black_cps)
                
                if ((board[i][j]=='b'and board[i][j+3]==' ') or (board[i][j]==' 'and board[i][j+3]=='b'))  and  board[i][j+1]=='w' and board[i][j+2]=='w':
                    white_capture_count+=1
                    black_surround_count=0
                    
                    if board[i][j]==' ':
                        t=j
                    elif board[i][j+3]==' ':
                        t=j+3
                    black_surround_count,index=check_horizontal_surround(i,t,0,'b')
                    if white_cps:
                        if black_surround_count>white_cps['black_surround_count']:
                            white_cps['black_surround_count']=black_surround_count
                            white_cps['index']=index
                    else:
                        white_cps['black_surround_count']=black_surround_count
                        white_cps['index']=index
            #horizontal in 3
            if j<17:
                w_count=0
                b_count=0
                for k in range(3):
                    if board[i][j+k]=='w':
                        w_count+=1
                    elif board[i][j+k]=='b':
                        b_count+=1
                
                if w_count==2 and b_count==0:
                    for k in range(3):
                        if board[i][j+k]==' ':
                            space_fill_count_w,index=check_horizontal_surround(i,j,k,'w')
                            
                            if white_2_in_3:
                                if space_fill_count_w>white_2_in_3['space_fill_count_w']:
                                    white_2_in_3['space_fill_count_w']=space_fill_count_w
                                    white_2_in_3['index']=index
                            else:
                                white_2_in_3['space_fill_count_w']=space_fill_count_w
                                white_2_in_3['index']=index
                if w_count==0 and b_count==2:
                    for k in range(3):
                        if board[i][j+k]==' ':
                            space_fill_count_b,index=check_horizontal_surround(i,j,k,'b')
                            
                            if black_2_in_3:
                                if space_fill_count_b>black_2_in_3['space_fill_count_b']:
                                    black_2_in_3['space_fill_count_b']=space_fill_count_b
                                    black_2_in_3['index']=index
                            else:
                                black_2_in_3['space_fill_count_b']=space_fill_count_b
                                black_2_in_3['index']=index

        # vertcal in 5
        for j in range(min_j,max_j+1):
            if i<15:
            
                w_count=0
                b_count=0
                for k in range(5):
                    if board[i+k][j]=='w':
                        w_count+=1
                    elif board[i+k][j]=='b':
                        b_count+=1
                if w_count==4 and b_count==0:
                    if board[i+k][j]==' ':
                            white_win_index['score']=1000000000000000000
                            white_win_index['index']=(i+k,j)
                if b_count==4 and w_count==0:
                    black_possible_wins+=1
                    for k in range(5):
                        if board[i+k][j]==' ':
                            black_win_index['score']=10000000000000000
                            black_win_index['index']=(i+k,j)
                if w_count==3 and b_count==0:
                    for k in range(5):
                        if board[i+k][j]==' ':
                            space_fill_count_w,index=check_vertical_surround(i,j,k,'w')
                            
                            if white_3_in_5:
                                if space_fill_count_w>white_3_in_5['space_fill_count_w']:
                                    white_3_in_5['space_fill_count_w']=space_fill_count_w
                                    white_3_in_5['index']=index
                            else:
                                white_3_in_5['space_fill_count_w']=space_fill_count_w
                                white_3_in_5['index']=index
                if b_count==3 and w_count==0:
                    for k in range(5):
                        if board[i+k][j]==' ':
                            space_fill_count_b,index=check_vertical_surround(i,j,k,'b')
                            
                            if black_3_in_5:
                                if space_fill_count_b>black_3_in_5['space_fill_count_b']:
                                    black_3_in_5['space_fill_count_b']=space_fill_count_b
                                    black_3_in_5['index']=index
                            else:
                                black_3_in_5['space_fill_count_b']=space_fill_count_b
                                black_3_in_5['index']=index
            # vertical 3 in 4
            if i<16:
                w_count=0
                b_count=0
                for k in range(4):
                    if board[i+k][j]=='w':
                        w_count+=1
                    elif board[i+k][j]=='b':
                        b_count+=1
                if w_count==3 and b_count==0:
                    if board[i+k][j]==' ':
                        space_fill_count_w,index=check_vertical_surround(i,j,k,'w')
                        
                        if white_3_in_4:
                            if space_fill_count_w>white_3_in_4['space_fill_count_w']:
                                white_3_in_4['space_fill_count_w']=space_fill_count_w
                                white_3_in_4['index']=index
                        else:
                            white_3_in_4['space_fill_count_w']=space_fill_count_w
                            white_3_in_4['index']=index

                if w_count==0 and b_count==3:
                    if board[i+k][j]==' ':
                        space_fill_count_b,index=check_vertical_surround(i,j,k,'b')
                        
                        
                        if black_3_in_4:
                            if space_fill_count_b>black_3_in_4['space_fill_count_b']:
                                black_3_in_4['space_fill_count_b']=space_fill_count_b
                                black_3_in_4['index']=index
                        else:
                            black_3_in_4['space_fill_count_b']=space_fill_count_b
                            black_3_in_4['index']=index
                #captures
                if board[i+1][j]=='b' and board[i+2][j]=='b' and ((board[i][j]=='w' and board[i+3][j]==' ') or (board[i+3][j]=='w' and board[i][j]==' ')):
                    black_capture_count+=1
                    white_surround_count=0
                    if board[i][j]==' ':
                        t=j
                    elif board[i+3][j]==' ':
                        t=i+3
                    white_surround_count,index=check_vertical_surround(t,j,0,'w')
                    if black_cps:
                        if white_surround_count>black_cps['white_surround_count']:
                            black_cps['white_surround_count']=white_surround_count
                            black_cps['index']=index
                    else:
                        black_cps['white_surround_count']=white_surround_count
                        black_cps['index']=index

                if board[i+1][j]=='w' and board[i+2][j]=='w' and ((board[i][j]=='b' and board[i+3][j]==' ') or (board[i+3][j]=='b' and board[i][j]==' ')):
                    white_capture_count+=1
                    black_surround_count=0
                    if board[i][j]==' ':
                        t=j
                    elif board[i+3][j]==' ':
                        t=i+3
                    black_surround_count,index=check_vertical_surround(t,j,0,'b')
                    if white_cps:
                        if black_surround_count>white_cps['black_surround_count']:
                            white_cps['black_surround_count']=black_surround_count
                            white_cps['index']=index
                    else:
                        white_cps['black_surround_count']=black_surround_count
                        white_cps['index']=index
            # vertical 2 in 3
            if i<17:
                w_count=0
                b_count=0
                for k in range(3):
                    if board[i+k][j]=='w':
                        w_count+=1
                    elif board[i+k][j]=='b':
                        b_count+=1
                if w_count==2 and b_count==0:
                    if board[i+k][j]==' ':
                        space_fill_count_w,index=check_vertical_surround(i,j,k,'w')
                
                        if white_2_in_3:            
                            if space_fill_count_w>white_2_in_3['space_fill_count_w']:
                                white_2_in_3['space_fill_count_w']=space_fill_count_w
                                white_2_in_3['index']=index
                        else:
                            white_2_in_3['space_fill_count_w']=space_fill_count_w
                            white_2_in_3['index']=index
                if b_count==2 and w_count==0:
                    if board[i+k][j]==' ':
                        space_fill_count_b,index=check_vertical_surround(i,j,k,'b')

                        if black_2_in_3:
                            if space_fill_count_b>black_2_in_3['space_fill_count_b']:
                                black_2_in_3['space_fill_count_b']=space_fill_count_b
                                black_2_in_3['index']=index
                        else:
                            black_2_in_3['space_fill_count_b']=space_fill_count_b
                            black_2_in_3['index']=index
        
        # diagnal in 5
        for j in range(min_j,max_j+1):
            if i<15 and j<15:
                b_count=0
                w_count=0
                for k in range(5):
                    if board[i+k][j+k]=='b':
                        b_count+=1
                    elif board[i+k][j+k]=='w':
                        w_count+=1
                if b_count==0 and w_count==4:
                    if board[i+k][j+k]==' ':
                        white_win_index['score']=1000000000000000000
                        white_win_index['index']=(i+k,j+k)
                if b_count==4 and w_count==0:
                    black_possible_wins+=1
                    if board[i+k][j+k]==' ':
                        black_win_index['score']=10000000000000000
                        black_win_index['index']=(i+k,j+k)
                if b_count==0 and w_count==3:
                    for k in range(5):
                        if board[i+k][j+k]==' ':
                            space_fill_count_w,index=check_diagnol_surround(i,j,k,'w')
                            if white_3_in_5:
                                if space_fill_count_w>white_3_in_5['space_fill_count_w']:
                                    white_3_in_5['space_fill_count_w']=space_fill_count_w
                                    white_3_in_5['index']=index
                            else:
                                white_3_in_5['space_fill_count_w']=space_fill_count_w
                                white_3_in_5['index']=index
                if b_count==3 and w_count==0:
                    for k in range(4):
                        if board[i+k][j+k]==' ':
                            space_fill_count_b,index=check_diagnol_surround(i,j,k,'b')
                            
                            if black_3_in_5:
                                if space_fill_count_b>black_3_in_5['space_fill_count_b']:
                                    black_3_in_5['space_fill_count_b']=space_fill_count_b
                                    black_3_in_5['index']=index
                            else:
                                black_3_in_5['space_fill_count_b']=space_fill_count_b
                                black_3_in_5['index']=index

            #diagonal 3 in 4
            if i<16 and j<16:
                w_count=0
                b_count=0
                for k in range(4):
                    if board[i+k][j+k]=='w':
                        w_count+=1
                    elif board[i+k][j+k]=='b':
                        b_count+=1
                if w_count==3 and b_count==0:
                    for k in range(4):
                        if board[i+k][j+k]==' ':
                            space_fill_count_w,index=check_diagnol_surround(i,j,k,'w')
                            
                            if white_3_in_4:
                                if space_fill_count_w>white_3_in_4['space_fill_count_w']:
                                    white_3_in_4['space_fill_count_w']=space_fill_count_w
                                    white_3_in_4['index']=index
                            else:
                                white_3_in_4['space_fill_count_w']=space_fill_count_w
                                white_3_in_4['index']=index

                if w_count==0 and b_count==3:
                    for k in range(4):
                        if board[i+k][j+k]==' ':
                            space_fill_count_b,index=check_diagnol_surround(i,j,k,'b')
                            # vertical
                            
                            if black_3_in_4:
                                if space_fill_count_b>black_3_in_4['space_fill_count_b']:
                                    black_3_in_4['space_fill_count_b']=space_fill_count_b
                                    black_3_in_4['index']=index
                            else:
                                black_3_in_4['space_fill_count_b']=space_fill_count_b
                                black_3_in_4['index']=index
                #captures
                if board[i+1][j+1]=='b' and board[i+2][j+2]=='b' and ((board[i+3][j+3]=='w' and board[i][j]==' ') or (board[i+3][j+3]==' ' and board[i][j]=='w')):
                    black_capture_count+=1
                    white_surround_count=0
                    if board[i][j]==' ':
                        t1=i
                        t2=j
                    elif board[i+3][j+3]==' ':
                        t1=i+3
                        t2=j+3
                    white_surround_count,index=check_diagnol_surround(t1,t2,0,'w')
                    if black_cps:
                        if white_surround_count>black_cps['white_surround_count']:
                            black_cps['white_surround_count']=white_surround_count
                            black_cps['index']=index
                    else:
                        black_cps['white_surround_count']=white_surround_count
                        black_cps['index']=index
                if board[i+1][j+1]=='w' and board[i+2][j+2]=='w' and ((board[i+3][j+3]=='b' and board[i][j]==' ') or (board[i+3][j+3]==' ' and board[i][j]=='b')):
                    white_capture_count+=1
                    black_surround_count=0
                    if board[i][j]==' ':
                        t1=i
                        t2=j
                    elif board[i+3][j+3]==' ':
                        t1=i+3
                        t2=j+3
                    black_surround_count,index=check_diagnol_surround(t1,t2,0,'b')
                    if white_cps:
                        if black_surround_count>white_cps['black_surround_count']:
                            white_cps['black_surround_count']=black_surround_count
                            white_cps['index']=index
                    else:
                        white_cps['black_surround_count']=black_surround_count
                        white_cps['index']=index

                    

            # diagnol 2 in 3
            if i<17 and j<17:
                w_count=0
                b_count=0
                for k in range(3):
                    if board[i+k][j+k]=='w':
                        w_count+=1
                    if board[i+k][j+k]=='b':
                        b_count+=1
                if w_count==2 and b_count==0:
                    for k in range(3):
                        if board[i+k][j+k]==' ':
                            space_fill_count_w,index=check_diagnol_surround(i,j,k,'w')
                            
                            if white_2_in_3:
                                if space_fill_count_w>white_2_in_3['space_fill_count_w']:
                                    white_2_in_3['space_fill_count_w']=space_fill_count_w
                                    white_2_in_3['index']=index
                            else:
                                white_2_in_3['space_fill_count_w']=space_fill_count_w
                                white_2_in_3['index']=index
                if b_count==2 and w_count==0:
                    for k in range(3):
                        if board[i+k][j+k]==' ':
                            space_fill_count_b,index=check_diagnol_surround(i,j,k,'b')
                            
                            if black_2_in_3:
                                if space_fill_count_b>black_2_in_3['space_fill_count_b']:
                                    black_2_in_3['space_fill_count_b']=space_fill_count_b
                                    black_2_in_3['index']=(i+k,j+k)
                            else:
                                black_2_in_3['space_fill_count_b']=space_fill_count_b
                                black_2_in_3['index']=(i+k,j+k)

        # antidiagnol in 5
        for j in range(min_j,max_j+1):
            if i>=4 and j<15:
                w_count=0
                b_count=0
                for k in range(5):
                    if board[i-k][j+k]=='w':
                        w_count+=1
                    elif board[i-k][j+k]=='b':
                        b_count+=1
                #print(w_count,b_count)
                if w_count==4 and b_count==0:
                    white_win_index['score']=1000000000000000000
                    white_win_index['index']=(i-k,j+k)
                    
                if b_count==4 and w_count==0:
                    black_possible_wins+=1
                    black_win_index['score']=10000000000000000
                    black_win_index['index']=(i-k,j+k)
                # 3 in 5(antidiagnol)
                if w_count==3 and b_count==0:
                    for k in range(5):
                        if board[i-k][j+k]==' ':
                            
                            space_fill_count_w,index=check_antidiagnol_surround(i,j,k,'w')
                            if white_3_in_5:
                                if space_fill_count_w>white_3_in_5['space_fill_count_w']:
                                    white_3_in_5['space_fill_count_w']=space_fill_count_w
                                    white_3_in_5['index']=index
                            else:
                                white_3_in_5['space_fill_count_w']=space_fill_count_w
                                white_3_in_5['index']=index
                            
                if b_count==3 and w_count==0:
                    for k in range(5):
                        if board[i-k][j+k]==' ':
                            space_fill_count_b,index=check_antidiagnol_surround(i,j,k,'b')
                            if black_3_in_5:
                                if space_fill_count_b>black_3_in_5['space_fill_count_b']:
                                    black_3_in_5['space_fill_count_b']=space_fill_count_b
                                    black_3_in_5['index']=index
                            else:
                                black_3_in_5['space_fill_count_b']=space_fill_count_b
                                black_3_in_5['index']=index

            # antidiagnol 3 in 4                   
            if i>=3 and j<16:
                w_count=0
                b_count=0
                for k in range(4):
                    if board[i-k][j+k]=='w':
                        w_count+=1
                    elif board[i-k][j+k]=='b':
                        b_count+=1

                if w_count==3 and b_count==0:
                    for k in range(4):
                        if board[i-k][j+k]==' ':
                            space_fill_count_w,index=check_antidiagnol_surround(i,j,k,'w')
                            if white_3_in_4:
                                if space_fill_count_w>white_3_in_4['space_fill_count_w']:
                                    white_3_in_4['space_fill_count_w']=space_fill_count_w
                                    white_3_in_4['index']=index
                            else:
                                white_3_in_4['space_fill_count_w']=space_fill_count_w
                                white_3_in_4['index']=index
                if w_count==0 and b_count==3:
                    for k in range(4):
                        if board[i-k][j+k]==' ':
                            space_fill_count_b,index=check_antidiagnol_surround(i,j,k,'b')
                            if black_3_in_4:
                                if space_fill_count_b>black_3_in_4['space_fill_count_b']:
                                    black_3_in_4['space_fill_count_b']=space_fill_count_b
                                    black_3_in_4['index']=index
                            else:
                                black_3_in_4['space_fill_count_b']=space_fill_count_b
                                black_3_in_4['index']=index
                #captures
                if board[i-1][j+1]=='b' and board[i-2][j+2]=='b' and ((board[i-3][j+3]=='w' and board[i][j]==' ') or (board[i-3][j+3]==' ' and board[i][j]=='w')):
                    black_capture_count+=1
                    white_surround_count=0
                    if board[i][j]==' ':
                        t1=i
                        t2=j
                    elif board[i-3][j+3]==' ':
                        t1=i-3
                        t2=j+3
                    white_surround_count,index=check_antidiagnol_surround(t1,t2,0,'w')
                    if black_cps:
                        if white_surround_count>black_cps['white_surround_count']:
                            black_cps['white_surround_count']=white_surround_count
                            black_cps['index']=index
                    else:
                        black_cps['white_surround_count']=white_surround_count
                        black_cps['index']=index

                if board[i-1][j+1]=='w' and board[i-2][j+2]=='w' and ((board[i-3][j+3]=='b' and board[i][j]==' ') or (board[i-3][j+3]==' ' and board[i][j]=='b')):
                    white_capture_count+=1
                    black_surround_count=0
                    if board[i][j]==' ':
                        t1=i
                        t2=j
                    elif board[i-3][j+3]==' ':
                        t1=i-3
                        t2=j+3
                    black_surround_count,index=check_antidiagnol_surround(t1,t2,0,'w')
                    if white_cps:
                        if black_surround_count>white_cps['black_surround_count']:
                            white_cps['black_surround_count']=black_surround_count
                            white_cps['index']=index
                    else:
                        white_cps['black_surround_count']=black_surround_count
                        white_cps['index']=index

            # antidiagnol 2 in 3
            if i>=2 and j<17:
                w_count=0
                b_count=0
                for k in range(3):
                    if board[i-k][j+k]=='w':
                        w_count+=1
                    elif board[i-k][j+k]=='b':
                        b_count+=1
                if w_count==2 and b_count==0:
                    for k in range(3):
                        if board[i-k][j+k]==' ':
                            space_fill_count_w,index=check_antidiagnol_surround(i,j,k,'w')
                            if white_2_in_3:
                                if space_fill_count_w>white_2_in_3['space_fill_count_w']:
                                    white_2_in_3['space_fill_count_w']=space_fill_count_w
                                    white_2_in_3['index']=index
                            else:
                                white_2_in_3['space_fill_count_w']=space_fill_count_w
                                white_2_in_3['index']=index
                if w_count==0 and b_count==2:
                    for k in range(3):
                        if board[i-k][j+k]==' ':
                            space_fill_count_b,index=check_antidiagnol_surround(i,j,k,'b')
                            if black_2_in_3:
                                if space_fill_count_b>black_2_in_3['space_fill_count_b']:
                                    black_2_in_3['space_fill_count_b']=space_fill_count_b
                                    black_2_in_3['index']=index
                            else:
                                black_2_in_3['space_fill_count_b']=space_fill_count_b
                                black_2_in_3['index']=index

    for i in range(min_i,max_i+1):
        for j in range(min_j,max_j+1):
            
            if board[i][j]!=' ':
                #vertical
                if i<16 and board[i+1][j]==board[i][j] and board[i+2][j]==board[i][j] and board[i+3][j]==board[i][j]:
                    if board[i][j]=='w':
                        white_prevent4_till_now+=1
                    elif board[i][j]=='b':
                        black_prevent4_till_now+=1
                if i<17 and board[i+1][j]==board[i][j] and board[i+2][j]==board[i][j]:
                    if board[i][j]=='w':
                        white_prevent3_till_now+=1
                    elif board[i][j]=='b':
                        black_prevent3_till_now+=1
                if i<18 and board[i+1][j]==board[i][j]:
                    if board[i][j]=='w':
                        white_prevent2_till_now+=1
                    elif board[i][j]=='b':
                        black_prevent2_till_now+=1
                #horizontal
                if j<16 and board[i][j+1]==board[i][j] and board[i][j+2]==board[i][j] and board[i][j+3]==board[i][j]:
                    if board[i][j]=='w':
                        white_prevent4_till_now+=1
                    elif board[i][j]=='b':
                        black_prevent4_till_now+=1
                if j<17 and board[i][j+1]==board[i][j] and board[i][j+2]==board[i][j]:
                    if board[i][j]=='w':
                        white_prevent3_till_now+=1
                    elif board[i][j]=='b':
                        black_prevent3_till_now+=1
                if j<18 and board[i][j+1]==board[i][j]:
                    if board[i][j]=='w':
                        white_prevent2_till_now+=1
                    elif board[i][j]=='b':
                        black_prevent2_till_now+=1
                #diagnol
                if i<16 and j<16 and board[i+1][j+1]==board[i][j] and board[i+2][j+2]==board[i][j] and board[i+3][j+3]==board[i][j]:
                    if board[i][j]=='w':
                        white_prevent4_till_now+=1
                    elif board[i][j]=='b':
                        black_prevent4_till_now+=1
                if i<17 and j<17 and board[i+1][j+1]==board[i][j] and board[i+2][j+2]==board[i][j]:
                    if board[i][j]=='w':
                        white_prevent3_till_now+=1
                    elif board[i][j]=='b':
                        black_prevent3_till_now+=1
                if i<18 and j<18 and board[i+1][j+1]==board[i][j]:
                    if board[i][j]=='w':
                        white_prevent2_till_now+=1
                    elif board[i][j]=='b':
                        black_prevent2_till_now+=1
                #antidiagnol
                if j<16 and i>2 and board[i-1][j+1]==board[i][j] and board[i-2][j+2]==board[i][j] and board[i-3][j+3]==board[i][j]:
                    if board[i][j]=='w':
                        white_prevent4_till_now+=1
                    elif board[i][j]=='b':
                        black_prevent4_till_now+=1
                if j<17 and i>1 and board[i-1][j+1]==board[i][j] and board[i-2][j+2]==board[i][j]:
                    if board[i][j]=='w':
                        white_prevent3_till_now+=1
                    elif board[i][j]=='b':
                        black_prevent3_till_now+=1
                if j<18 and i>0 and board[i-1][j+1]==board[i][j]:
                    if board[i][j]=='w':
                        white_prevent2_till_now+=1
                    elif board[i][j]=='b':
                        black_prevent2_till_now+=1
    
    white_prevent3_till_now=white_prevent3_till_now-2*white_prevent4_till_now
    black_prevent3_till_now=black_prevent3_till_now-2*black_prevent4_till_now
    white_prevent2_till_now=white_prevent2_till_now-2*white_prevent3_till_now-3*white_prevent4_till_now
    black_prevent2_till_now=black_prevent2_till_now-2*black_prevent3_till_now-3*black_prevent4_till_now

    capture_diff=capture_count['b']-capture_count['w']
    evaluation+=1000000000000000*capture_diff
    evaluation+=1000000000000*(black_prevent4_till_now-white_prevent4_till_now)
    evaluation+=10000000000000*(black_prevent3_till_now-white_prevent3_till_now)
    evaluation+=100000000000000*(black_prevent2_till_now-white_prevent2_till_now)

    if white_win_index:
        evaluation+=1000000000000
        if return_index==(-1,-1):
            return_index=white_win_index['index']
    if capture_count['b']==4 and black_capture_count>0:
        evaluation+=1000000000000
        if return_index==(-1,-1):
            return_index=black_cps['index']
    if black_win_index:
        evaluation+=1000000000000
        if return_index==(-1,-1):
            return_index=black_win_index['index']
    if black_possible_wins>1:
        return ((-sys.maxsize-1),black_win_index['index'])
    if capture_count['w']==4 and white_capture_count>0:
        evaluation+=1000000000000
        if return_index==(-1,-1):
            return_index=white_cps['index']
    if white_3_in_5:
        evaluation+=10000000000*white_3_in_5['space_fill_count_w']
        if return_index==(-1,-1):
            return_index=white_3_in_5['index']
    if black_3_in_5:
        evaluation+=10000000000*black_3_in_5['space_fill_count_b']
        if return_index==(-1,-1):
            return_index=black_3_in_5['index']
    if black_capture_count>0:
        evaluation+=100000000*black_capture_count
        if return_index==(-1,-1):
            return_index=black_cps['index']
    if white_capture_count>0:
        evaluation+=100000000*white_capture_count
        if return_index==(-1,-1):
            return_index=white_cps['index']
    if white_3_in_4:
        evaluation+=1000000*white_3_in_4['space_fill_count_w']
        if return_index==(-1,-1):
            return_index=white_3_in_4['index']
    if black_3_in_4:
        evaluation+=100000*black_3_in_4['space_fill_count_b']
        if return_index==(-1,-1):
            return_index=black_3_in_4['index']
    if white_2_in_3:
        evaluation+=10000*white_2_in_3['space_fill_count_w']
        if return_index==(-1,-1):
            return_index=white_2_in_3['index']
    if black_2_in_3:
        evaluation+=100*black_2_in_3['space_fill_count_b']
        if return_index==(-1,-1):
            return_index=black_2_in_3['index']
    for i in range(min_i,max_i+1):
        for j in range(min_j,max_j+1):
            if board[i][j]==' ':
                if(i-1>=0 and i+2<19 and board[i+1][j]=='w' and ((board[i-1][j]=='b' and board[i+2][j]=='.') or (board[i-1][j]=='.' and board[i+2][j]=='b'))):
                    continue
                if(i-2>=0 and i+1<19 and board[i-1][j]=='w' and ((board[i+1][j]=='b' and board[i-2][j]=='.') or (board[i+1][j]=='.' and board[i-2][j]=='b'))):
                    continue
                if(j-1>=0 and j+2<19 and board[i][j+1]=='w' and ((board[i][j-1]=='b' and board[i][j+2]=='.') or (board[i][j-1]=='.' and board[i][j+2]=='b'))):
                    continue
                if(j-2>=0 and j+1<19 and board[i][j-1]=='w' and ((board[i][j+1]=='b' and board[i][j-2]=='.') or (board[i][j+1]=='.' and board[i][j-2]=='b'))):
                    continue
                if(i-1>=0 and i+2<19 and j-1>=0 and j+2<19 and board[i+1][j+1]=='w' and ((board[i-1][j-1]=='b' and board[i+2][j+2]=='.') or (board[i-1][j-1]=='.' and board[i+2][j+2]=='b'))):
                    continue
                if(i-2>=0 and i+1<19 and j-2>=0 and j+1<19 and board[i-1][j-1]=='w' and ((board[i+1][j+1]=='b' and board[i-2][j-2]=='.') or (board[i+1][j+1]=='.' and board[i-2][j-2]=='b'))):
                    continue
                if(i-1>=0 and i+2<19 and j-2>=0 and j+1<19 and board[i+1][j-1]=='w' and ((board[i-1][j+1]=='b' and board[i+2][j-2]=='.') or (board[i-1][j+1]=='.' and board[i+2][j-2]=='b'))):
                    continue
                if(i-2>=0 and i+1<19 and j-1>=0 and j+2<19 and board[i-1][j+1]=='w' and ((board[i+1][j-1]=='b' and board[i-2][j+2]=='.') or (board[i+1][j-1]=='.' and board[i-2][j+2]=='b'))):
                    continue
                temp_val,temp_index=check_horizontal_surround(i,j,0,'w')
                if last_value['last_option_value']<temp_val:
                    last_value['last_option_value']=temp_val
                    last_value['last_option_index']=temp_index
    
    evaluation+=5*last_value['last_option_value']
    if return_index==(-1,-1):
        return_index=last_value['last_option_index']

    if return_index!=(-1,-1):
        return evaluation,return_index
    for i in range(min_i,max_i+1):
        for j in range(min_j,max_j+1):
            if board[i][j]==' ':
                return evaluation,(i,j)

        

def check_win(board, value_i, value_j, colour):
    #print('check_win')
    i=value_i
    j=value_j
    same_right=same_left=same_down=same_up=same_right_up=same_right_down=same_left_up=same_left_down = 0
    
    if(i<18 and board[i][j]==board[i+1][j]):
        if(i<17 and board[i][j]==board[i+2][j]):
            if(i<16 and board[i][j]==board[i+3][j]):
                if(i<15 and board[i][j]==board[i+4][j]):
                    same_right = 4
                else:
                    same_right = 3
            else:
                same_right = 2
        else:
            same_right = 1

    if(i>0 and board[i][j]==board[i-1][j]):
        if(i>1 and board[i][j]==board[i-2][j]):
            if(i>2 and board[i][j]==board[i-3][j]):
                if(i>3 and board[i][j]==board[i-4][j]):
                    same_left = 4
                else:
                    same_left = 3
            else:
                same_left = 2
        else:
            same_left = 1

    if same_left + same_right >= 4:
        return True

    if(j<18 and board[i][j]==board[i][j+1]):
        if(j<17 and board[i][j]==board[i][j+2]):
            if(j<16 and board[i][j]==board[i][j+3]):
                if(j<15 and board[i][j]==board[i][j+4]):
                    same_down = 4
                else:
                    same_down = 3
            else:
                same_down = 2
        else:
            same_down = 1

    if(j>0 and board[i][j]==board[i][j-1]):
        if(j>1 and board[i][j]==board[i][j-2]):
            if(j>2 and board[i][j]==board[i][j-3]):
                if(j>3 and board[i][j]==board[i][j-4]):
                    same_up = 4
                else:
                    same_up = 3
            else:
                same_up = 2
        else:
            same_up = 1
    #print(same_up, same_down)
    if(same_up + same_down >= 4):
        print('win')
        return True
        
    if(i>0 and j<18 and board[i][j]==board[i-1][j+1]):
        if(i>1 and j<17 and board[i][j]==board[i-2][j+2]):
            if(i>2 and j<16 and board[i][j]==board[i-3][j+3]):
                if(i>3 and j<15 and board[i][j]==board[i-4][j+4]):
                    same_right_up = 4
                else:
                    same_right_up = 3
            else:	
                same_right_up = 2
        else:	
            same_right_up = 1
	  
    if(i<18 and j>0 and board[i][j]==board[i+1][j-1]):
        if(i<17 and j>1 and board[i][j]==board[i+2][j-2]):
            if(i<16 and j>2 and board[i][j]==board[i+3][j-3]):
                if(i<15 and j>3 and board[i][j]==board[i+4][j-4]):
                    same_left_down = 4
                else:
                    same_left_down = 3
            else:	
                same_left_down = 2
        else:	
            same_left_down = 1
	  
    if(same_right_up + same_left_down >= 4):
        return True

    if(i<18 and j<18 and board[i][j]==board[i+1][j+1]):
        if(i<17 and j<17 and board[i][j]==board[i+2][j+2]):
            if(i<16 and j<16 and board[i][j]==board[i+3][j+3]):
                if(i<15 and j<15 and board[i][j]==board[i+4][j+4]):
                    same_right_down = 4
                else:
                    same_right_down = 3
            else:
                same_right_down = 2
        else:	
            same_right_down = 1

    if(i>0 and j>0 and board[i][j]==board[i-1][j-1]):
        if(i>1 and j>1 and board[i][j]==board[i-2][j-2]):
            if(i>2 and j>2 and board[i][j]==board[i-3][j-3]):
                if(i>3 and j>3 and board[i][j]==board[i-4][j-4]):
                    same_left_up = 4
                else:
                    same_left_up = 3
            else:	
                same_left_up = 2
        else:	
            same_left_up = 1

    if(same_right_down + same_left_up >= 4):
        return True
        
    return False
        

        

def capture(board, i, j, colour):
    pos=[]
    if colour=='b':
        color_opp='w'
    else:
        color_opp='b'

    
    #vertical
    if i+1>=0 and i+1<19 and i+2>=0 and i+2<19 and i+3>=0 and i+3<19:#if exists then check
        if board[i+1][j]==color_opp and board[i+2][j]==color_opp and board[i+3][j]==colour:
            board[i+1][j]=' '
            board[i+2][j]=' '
            pos.append([(i+1,j),(i+2,j)])
    if i-1>=0 and i-1<19 and i-2>=0 and i-2<19 and i-3>=0 and i-3<19:
        if board[i-1][j]==color_opp and board[i-2][j]==color_opp and board[i-3][j]==colour:
            board[i-1][j]=' '
            board[i-2][j]=' '
            pos.append([(i-1,j),(i-2,j)])
    #horizontal
    if j+1>=0 and j+1<19 and j+2>=0 and j+2<19 and j+3>=0 and j+3<19:
        if board[i][j+1]==color_opp and board[i][j+2]==color_opp and board[i][j+3]==colour:
            board[i][j+1]=' '
            board[i][j+2]=' '
            pos.append([(i,j+1),(i,j+2)])
    if j-1>=0 and j-1<19 and j-2>=0 and j-2<19 and j-3>=0 and j-3<19:
        if board[i][j-1]==color_opp and board[i][j-2]==color_opp and board[i][j-3]==colour:
            board[i][j-1]=' '
            board[i][j-2]=' '
            pos.append([(i,j-1),(i,j-2)])
    #diagonal
    if i+1>=0 and i+1<19 and i+2>=0 and i+2<19 and i+3>=0 and i+3<19 and j+1>=0 and j+1<19 and j+2>=0 and j+2<19 and j+3>=0 and j+3<19:
        if board[i+1][j+1]==color_opp and board[i+2][j+2]==color_opp and board[i+3][j+3]==colour:
            board[i+1][j+1]=' '
            board[i+2][j+2]=' '
            pos.append([(i+1,j+1),(i+2,j+2)])
    if i-1>=0 and i-1<19 and i-2>=0 and i-2<19 and i-3>=0 and i-3<19 and j-1>=0 and j-1<19 and j-2>=0 and j-2<19 and j-3>=0 and j-3<19:
        if board[i-1][j-1]==color_opp and board[i-2][j-2]==color_opp and board[i-3][j-3]==colour:
            board[i-1][j-1]=' '
            board[i-2][j-2]=' '
            pos.append([(i-1,j-1),(i-2,j-2)])
    #anti-diagonal
    if i+1>=0 and i+1<19 and i+2>=0 and i+2<19 and i+3>=0 and i+3<19 and j-1>=0 and j-1<19 and j-2>=0 and j-2<19 and j-3>=0 and j-3<19:
        if board[i+1][j-1]==color_opp and board[i+2][j-2]==color_opp and board[i+3][j-3]==colour:
            board[i+1][j-1]=' '
            board[i+2][j-2]=' '
            pos.append([(i+1,j-1),(i+2,j-2)])
    if i-1>=0 and i-1<19 and i-2>=0 and i-2<19 and i-3>=0 and i-3<19 and j+1>=0 and j+1<19 and j+2>=0 and j+2<19 and j+3>=0 and j+3<19:
        if board[i-1][j+1]==color_opp and board[i-2][j+2]==color_opp and board[i-3][j+3]==colour:
            board[i-1][j+1]=' '
            board[i-2][j+2]=' '
            pos.append([(i-1,j+1),(i-2,j+2)])

    return (board,pos,color_opp)
        


def play_move(board, alpha, beta, depth, is_max,ur_colour,capture_count,min_i,max_i,min_j,max_j,depth_copy):
    pos=[]
    opp_colour=''

    #print('min_i',min_i,'max_i',max_i,'min_j',min_j,'max_j',max_j,'depth',depth)
    if not depth:
        #print('evaluate')
        return evaluate(board,capture_count,ur_colour,depth_copy,min_i,max_i,min_j,max_j)
    
    if is_max==True:

        #print("MAX")
        best_value = -sys.maxsize-1
        best_index=(-1,-1)
        return_value=-sys.maxsize-1
        return_index=(-1,-1)
        #index=(0,0)
        for i in range(min_i,max_i+1):
            for j in range(min_j,max_j+1):
                if board[i][j] == ' ':
                    board[i][j] = ur_colour
                    if check_win(board,i,j,ur_colour):
                        return (-sys.maxsize+1,(i,j))

                    board,pos,opp_colour=capture(board,i,j,ur_colour)
                    capture_count[opp_colour]=capture_count[opp_colour]+len(pos)
                    #print('i.j',i,j)
                    #print('capture_count',capture_count)
                    if capture_count[opp_colour]>=5:
                        return (-sys.maxsize+1,(i,j))

                    temp_colour=ur_colour
                    if ur_colour=='w':
                        temp_colour='b'
                    else:
                        temp_colour='w'
                    
                   
                    value,index = play_move(board, alpha, beta, depth - 1, False,temp_colour,capture_count,max(0,min(min_i,i-2)),min(18,max(max_i,i+2)),max(0,min(min_j,j-2)),min(18,max(max_j,j+2)),depth_copy)# (board, alpha, beta, depth , is_max)
                    
                    if value==(sys.maxsize):
                        return evaluate(board,capture_count,ur_colour,depth_copy,min_i,max_i,min_j,max_j)

                    if value>best_value:
                        best_value=value
                        best_index=(i,j)
                    if return_value<value:
                        return_value=value
                        return_index=(i,j)
                      
                    board[i][j] = ' '
                    if len(pos)>0:
                        for k in pos:
                            board[k[0][0]][k[0][1]]=opp_colour
                            board[k[1][0]][k[1][1]]=opp_colour
                    capture_count[opp_colour]=capture_count[opp_colour]-len(pos)
        
                    alpha = max(best_value, alpha)
                    # if beta <= alpha:
                    #     return [best_value,best_index]
                        
        return [return_value,return_index]
    elif is_max==False:
        #print("MIN")
        best_value = sys.maxsize
        best_index=(-1,-1)
        for i in range(min_i,max_i+1):
            for j in range(min_j,max_j+1):
                if board[i][j] == ' ':
                    board[i][j] = ur_colour
                    if check_win(board,i,j,ur_colour):
                        return (sys.maxsize,(i,j))
                    board,pos,opp_colour=capture(board,i,j,ur_colour)
                    capture_count[opp_colour]=capture_count[opp_colour]+len(pos)
                    if capture_count[opp_colour]>=5:
                        return (sys.maxsize,(i,j))

                    temp_colour=ur_colour
                    if ur_colour=='w':
                        temp_colour='b'
                    else:
                        temp_colour='w'
                    value,index = play_move(board, alpha, beta, depth - 1, True,temp_colour,capture_count,max(0,min(min_i,i-2)),min(18,max(max_i,i+2)),max(0,min(min_j,j-2)),min(18,max(max_j,j+2)),depth_copy)

                    
                    if value<best_value:
                       
                        best_value=value
                        best_index=(i,j)
                        
                    board[i][j] = ' '
                    for k in pos:
                        board[k[0][0]][k[0][1]]=opp_colour
                        board[k[1][0]][k[1][1]]=opp_colour
                    capture_count[opp_colour]=capture_count[opp_colour]-len(pos)
                    
                    
                    beta = min(best_value, beta)
                    # if beta <= alpha:
                    #     return [best_value,best_index]

        return [best_value,best_index]



if __name__ == '__main__':
    start_time = time.time()

    with open('input.txt') as fp:

        lines = fp.read().splitlines()
        cnt = 0

        ur_colour=lines[0]
        ur_colour=ur_colour.lower()[0]
        
        #print(ur_colour)


        t=float(lines[1])
        board=[[' ' for i in range(19)] for j in range(19)]
        captured_by_white=(int(lines[2].split(',')[0])//2)
        captured_by_black=(int(lines[2].split(',')[1])//2)
        min_i=18
        max_i=0
        min_j=18
        max_j=0
        c_w=0
        c_b=0
        for i in range(3,3+19):
            for j in range(0,19):
                if lines[i][j]=='w':
                    board[i-3][j]='w'
                    c_w=c_w+1
                    min_j=min(min_j,j)
                    max_j=max(max_j,j)
                    min_i=min(min_i,i-3)
                    max_i=max(max_i,i-3)
                elif lines[i][j]=='b':
                    board[i-3][j]='b'
                    c_b=c_b+1
                    min_j=min(min_j,j)
                    max_j=max(max_j,j)
                    min_i=min(min_i,i-3)
                    max_i=max(max_i,i-3)
                
        if ur_colour=='w':
            if c_w==0 and c_b==0:
                print((9,9))
                sys.exit()
            if c_w==1 and c_b==1:
                if board[12][12]==' ':
                    print((12,12))
                    sys.exit() 
                else:
                    print((6,6))
                    sys.exit() 
        #print(board)
        # for i in range(19):
        #     print(board[i])
        if ur_colour=='b':
            for i in range(19):
                for j in range(19):
                    if board[i][j]=='w':
                        board[i][j]='b'
                    elif board[i][j]=='b':
                        board[i][j]='w'
            captured_by_black,captured_by_white=captured_by_white,captured_by_black
            ur_colour='w'
            #print('n',board) 

    c=0
    alpha = -sys.maxsize-1
    beta = sys.maxsize
    depth = 0
    if max(max_i-min_i,max_j-min_j)<=7 and t>150:
        depth=2
    
    depth_copy=copy.deepcopy(depth)
    is_max=True
    # if ur_colour=='w':
    #     is_max=True
    # else:
    #     is_max=False

    capture_count={'w':captured_by_black,'b':captured_by_white}
    # capture count is a dictionary which stores the number of pieces captured of each colour
    # 'w' is no of white peices that are captured and 'b' is no of black pieces that are captured
    #print(max(0,min_i-2),min(18,max_i+2),max(0,min_j-2),min(18,max_j+2))
    value,index = play_move(board, alpha, beta, depth, is_max,ur_colour,capture_count,max(0,min_i-2),min(18,max_i+2),max(0,min_j-2),min(18,max_j+2),depth_copy)
    #print('last_value',value)
    #print('last_index',index)
    letters = ["A","B","C","D","E","F","G","H","J","K","L","M","N","O","P","Q","R","S","T"]
    num_row = ["19","18","17","16","15","14","13","12","11","10","9","8","7","6","5","4","3","2","1"]
    out=(num_row[index[0]]+letters[index[1]])
    output=open('output.txt','w')
    output.write(out)
    output.close()
    
    #print("--- %s seconds ---" % (time.time() - start_time))

