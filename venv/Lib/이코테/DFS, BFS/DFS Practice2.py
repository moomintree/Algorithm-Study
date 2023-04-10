# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end = ' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)


'''
1. visited = [False][False][False][False][False][False][False][False][False] 로 선언
2. v = 1일 때 visited[1] = True로 1 방문처리하고, graph[1] = [2, 3, 8]로 인접노드 확인
3. 가장 최소값의 노드 2를 확인, if not visited[i]를 통해 boolean조건 true냐? 를 봄.
4. True가 아닌 것들을 하나하나 들어가며 반복. 근데 여기서 만약 더 볼 조건이 없다면 스택구조의 재귀함수이기 때문에 이전 노드 정보로 돌아가게 됨.
5. 결국 한쪽을 다 보면 초기값은 1로 가는데 거기서 다시 조건이 돌면 안봤던 노드인 3으로 가서 다시 반복.
6. 끝
'''