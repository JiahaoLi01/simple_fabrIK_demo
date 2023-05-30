import pygame
from skeleton import Skeleton
from skeleton import Joint
from FabrIK import fabr_ik

# 初始化pygame
pygame.init()

# 定义窗口大小
win_width, win_height = 800, 600
window = pygame.display.set_mode((win_width, win_height))

# 定义两个点的坐标
point1 = (100, 200)
point2 = (300, 400)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 用白色背景清除窗口
    window.fill((255, 255, 255))

    joint_1 = Joint()
    joint_2 = Joint(joint_1)
    joint_3 = Joint(joint_2)
    joint_4 = Joint(joint_3)
    joint_5 = Joint(joint_4)
    joint_1.position = (200, 300)
    joint_2.position = (300, 400)
    joint_3.position = (400, 450)
    joint_4.position = (600, 400)
    joint_5.position = (700, 500)
    joint_1.joint_name = "thigh"
    joint_2.joint_name = "mid1"
    joint_3.joint_name = "calf"
    joint_4.joint_name = "mid2"
    joint_5.joint_name = "foot"
    demo_skeleton = Skeleton(joint_1)
    mouse_location = pygame.mouse.get_pos()
    fabr_ik(demo_skeleton, joint_5, mouse_location, 8)

    demo_skeleton.render(window)

    # 刷新屏幕显示
    pygame.display.flip()

# 退出pygame
pygame.quit()
