#13주차에 수정 예정
v, e = map(int, input().split()) # 정점,간선 갯수
edges = list()

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

def is_connected(te, v) -> bool:
    if not edges:
        return v <= 1

    graph = [[] for _ in range(v+1)]
    #vertieces = 

print(edges)
edges.sort(reverse=True)
print(edges)

selected_edges = edges[:]
total_cost =  sum(cost for cost, a, b in edges)

for cost, a, b in edges:
    temp_edges = [(c, x, y) for c, x, y in selected_edges if not (c==cost and x==a and y==b)]
    if is_connected(temp_edges, v):
        selected_edges = temp_edges
        total_cost -= cost
        print(f"간선 ({a}----{b}, 가중치 : {cost}), 현시점 총가중치 : {total_cost}")
    else:
        print(f"간선 ({a}----{b}, 가중치 : {cost}), 유지(제거하면 연결 끊어짐)")

print(f"\n최소 신장 트리의 총 가중치 : {total_cost}")
for cost, a, b in sorted(selected_edges):
    print(f"{a}----{b}, {cost}")