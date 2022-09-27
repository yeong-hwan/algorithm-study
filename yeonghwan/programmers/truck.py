from collections import list


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_now = list([0] * bridge_length)
    bridge_weight_now = 0
    truck_weights = list(truck_weights)

    while len(bridge_now):
        answer += 1
        truck_weight_remove = bridge_now.pop()
        bridge_weight_now -= truck_weight_remove

        if len(truck_weights):
            if bridge_weight_now + truck_weights[0] <= weight:
                truck_weight_add = truck_weights.popleft()
                bridge_now.appendleft(truck_weight_add)
                bridge_weight_now += truck_weight_add
            else:
                bridge_now.appendleft(0)

    return answer
