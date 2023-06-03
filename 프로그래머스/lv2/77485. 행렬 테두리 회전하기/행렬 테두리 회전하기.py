import sys

def solution(rows, columns, queries):
    answer = []
    
    # 행렬 값 초기화
    i = 1
    board = []
    for r in range(rows) :
        one_row = []
        for c in range(columns) :
            one_row.append(i)
            i+= 1
        board.append(one_row)
        
            
            
    
    for query in queries :
        min_value = sys.maxsize
        x1, y1, x2, y2 = query
        # 인덱싱을 위해 1씩 빼줌
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        
        ## 테두리에 해당하는 값들을 읽어옴
        # 업데이트할 방향에 따라 테두리값 구분
        to_right = [(x1, y, board[x1][y]) for y in range(y1, y2)]
        to_down  = [(x, y2, board[x][y2]) for x in range(x1, x2)]
        to_left  = [(x2, y, board[x2][y]) for y in range(y1+1, y2+1)]
        to_up    = [(x, y1, board[x][y1]) for x in range(x1+1, x2+1)]
        
        # 전체 테두리값 정보
        all_posinfo = [to_right, to_down, to_left, to_up]
        
        right = [ 0,  1]
        down  = [ 1,  0]
        left  = [ 0, -1]
        up    = [-1,  0]
        
        update_direction_list = [right, down, left, up]
        
        
        for update_direction, pos_info_ls in zip(update_direction_list, all_posinfo) :
            dx, dy = update_direction
            
            for pos_info in pos_info_ls : 
                x, y, num = pos_info
                
                # 전체 테두리값 중 가장 작은 테두리값 업데이트
                min_value = min(min_value, num)
                board[x+dx][y+dy] = num # 방향대로 업데이트
        
        # print(query)
        # for b in board :
        #     print(b)
    
        answer.append(min_value)
        
    
            
        
        
        
        
    
    
    
    return answer