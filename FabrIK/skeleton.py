import pygame
import math


def distance_vec2(v1, v2):
    diff_x = v1[0] - v2[0]
    diff_y = v1[1] - v2[1]
    return math.sqrt(diff_x ** 2 + diff_y ** 2)


class Joint:

    def __init__(self, joint=None):
        self.position = (0, 0)
        self.child_joint = []
        self.joint_name = ""
        self.parent_joint = joint
        if joint is not None:
            joint.attach_child(self)

    def attach_child(self, joint):
        self.child_joint.append(joint)

    def render(self, window):
        pygame.draw.circle(window, (0, 0, 255), self.position, 4)
        for child in self.child_joint:
            pygame.draw.line(window, (0, 0, 0), self.position, child.position, 1)


class Skeleton:

    def __init__(self, root: Joint = None):
        self.bone_length: dict[tuple[Joint, Joint], float] = {}
        self.root_joint = root
        self.max_length = 0
        if Joint is not None:
            self.init_bone_length(root)

    def set_root(self, joint):
        self.root_joint = joint

    def render(self, window):
        self.render_interval(window, self.root_joint)

    def render_interval(self, window, joint):
        joint.render(window)
        for child in joint.child_joint:
            self.render_interval(window, child)

    def init_bone_length(self, joint: Joint):
        for child in joint.child_joint:
            self.bone_length[(joint, child)] = distance_vec2(child.position, joint.position)
            self.bone_length[(child, joint)] = distance_vec2(child.position, joint.position)
            self.init_bone_length(child)

    def get_bone_length(self, joint1: Joint, joint2: Joint):
        return self.bone_length[(joint1, joint2)]
