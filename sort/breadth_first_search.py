def breadth_first_search(H, W, s, g, S):
    """
    H: 迷路の高さ
    W: 迷路の幅
    s: スタート地点(y, x)
    g: ゴール地点(y, x)
    S: 迷路図（文字列のリスト）
    """
    # write code here
    maze_list = [list(s) for s in S]  # [['#', '#' ...], ['#', '.', ...]]
    maze_list[s[0]-1][s[1]-1] = 0
    search_position = []  # 探索する[y, x]
    search_position.append([s[0]-1, s[1]-1])
    while current_position := search_position.pop(0):  # 一番最初に入った要素を取り出す
        current_y, current_x = current_position[0], current_position[1]
        current_position_counts = maze_list[current_y][current_x]  # 今いる場所の値
        for append_y, append_x in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
            next_y, next_x = current_y + append_y, current_x + append_x
            if any((next_y < 0, next_x < 0, next_y >= H, next_x >= W)):
                continue
            if maze_list[next_y][next_x] == '.':
                maze_list[next_y][next_x] = current_position_counts + 1
                search_position.append([next_y, next_x])  # 次の探索場所を追加してwhileで取り出される
                if next_y == g[0]-1 and next_x == g[1]-1:
                    print(current_position_counts+1)
                    return


# インデックス番号[0]
# '########'
# '#......#'
# '#.######'
# '#..#...#'
# '#..##..#'
# '##.....#'
# '########'


Hs = [7, 5, 50]
Ws = [8, 8, 50]
ss = [[2, 2], [2, 2], [2, 2]]
gs = [[4, 5], [2, 4], [49, 49]]
Ss = [
    ['########', '#......#', '#.######', '#..#...#',
        '#..##..#', '##.....#', '########'],
    ['########', '#.#....#', '#.###..#', '#......#', '########'],
    ['##################################################', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#',
        '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '#................................................#', '##################################################']
]
breadth_first_search(Hs[0], Ws[0], ss[0], gs[0], Ss[0])  # 11
breadth_first_search(Hs[1], Ws[1], ss[1], gs[1], Ss[1])  # 10
breadth_first_search(Hs[2], Ws[2], ss[2], gs[2], Ss[2])  # 94
