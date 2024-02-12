def load_goods(capacity, goods):
    loaded_goods = []
    total_weight =  0
    
    for good in sorted(goods, key=lambda x: x['cost'], reverse=True):
        if total_weight + good['weight'] <= capacity:
            loaded_goods.append(good)
            total_weight += good['weight']
        else:
            portion = capacity - total_weight
            loaded_goods.append({**good, 'weight': portion})
            break
            
    return loaded_goods

def print_loaded_goods(loaded_goods):
    for good in loaded_goods:
        print(f"{good['name']} {round(good['weight'],  2)} {round(good['cost'],  2)}")

if __name__ == "__main__":
    n, m = map(int, input().split())
    goods = []
    
    for _ in range(m):
        name, weight, cost = input().split()
        goods.append({'name': name, 'weight': int(weight), 'cost': int(cost)})
    
    loaded_goods = load_goods(n, goods)
    print_loaded_goods(loaded_goods)