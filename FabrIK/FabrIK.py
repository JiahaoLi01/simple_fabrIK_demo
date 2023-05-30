import copy

from skeleton import Joint
from skeleton import Skeleton
from skeleton import distance_vec2


def vector_multi(t, f, cardinality):
    r = tuple(i * f for i in t)
    return r


def vector_add(t1, t2):
    result = tuple(a + b for a, b in zip(t1, t2))
    return result


def fabr_ik(skeleton: Skeleton, effector: Joint, target: (float, float), iteration: int):
    chain = []
    current_joint = effector
    chain_max_length = 0
    while current_joint.parent_joint is not None:
        chain.append(current_joint)
        chain_max_length += distance_vec2(current_joint.position, current_joint.parent_joint.position)
        current_joint = current_joint.parent_joint

    chain.append(skeleton.root_joint)

    bone_num = len(chain)
    target_length_to_root = distance_vec2(target, skeleton.root_joint.position)

    if chain_max_length < target_length_to_root:
        return False

    chain[0].position = target

    for j in range(0, iteration, 1):
        for i in range(1, bone_num - 1, 1):
            lam = skeleton.get_bone_length(chain[i], chain[i - 1]) / distance_vec2(chain[i].position,
                                                                                   chain[i - 1].position)
            new_position = vector_add(vector_multi(chain[i].position, lam, 2),
                                      vector_multi(chain[i - 1].position, 1 - lam, 2))
            chain[i].position = new_position

        for i in range(bone_num - 2, 0, -1):
            lam = skeleton.get_bone_length(chain[i + 1], chain[i]) / distance_vec2(chain[i].position,
                                                                                   chain[i + 1].position)
            new_position = vector_add(vector_multi(chain[i].position, lam, 2),
                                      vector_multi(chain[i + 1].position, 1 - lam, 2))
            chain[i].position = new_position
    return True

