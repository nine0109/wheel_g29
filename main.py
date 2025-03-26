import pygame
import pyautogui
import time

# pygame 초기화
pygame.init()
pygame.joystick.init()

# 조이스틱(휠) 연결 확인
joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    print("연결된 조이스틱이 없습니다.")
    exit()

# 첫 번째 조이스틱(G29 휠) 초기화
wheel = pygame.joystick.Joystick(0)
wheel.init()
print(f"감지된 컨트롤러: {wheel.get_name()}")

# 화면 크기 가져오기
screen_width, screen_height = pyautogui.size()
print(f"화면 크기: {screen_width} x {screen_height}")

# 현재 마우스 위치
current_x, current_y = pyautogui.position()

# 휠 감도 설정 (값이 클수록 더 민감)
sensitivity = 20

try:
    running = True
    while running:
        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # 휠 위치 가져오기 (보통 축 0이 스티어링)
        # 값의 범위는 -1.0에서 1.0 사이
        wheel_position = wheel.get_axis(0)
        
        # 휠 위치에 따라 마우스 X 좌표 업데이트
        # 작은 움직임은 무시 (데드존)
        if abs(wheel_position) > 0.05:
            movement = wheel_position * sensitivity
            current_x += movement
            
            # 화면 경계 확인
            current_x = max(0, min(current_x, screen_width))
            
            # 마우스 포인터 이동
            pyautogui.moveTo(current_x, current_y)
        
        # 약간의 딜레이
        time.sleep(0.01)
        
finally:
    pygame.quit()
    print("프로그램 종료")