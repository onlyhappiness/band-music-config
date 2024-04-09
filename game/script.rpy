# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.


# 여기에서부터 게임이 시작합니다.
# label start:

#     call set_player_name 

#     return

# 퀴즈 데이터: 질문, 선택지, 정답 인덱스
define e = Character('Eileen')

label start:
    e "퀴즈 게임에 오신 것을 환영합니다!"

    $ score = 0

    label question1:
        e "첫 번째 질문입니다: 세계에서 가장 큰 섬은 무엇일까요?"
        menu:
            "그린란드":
                $ score += 1
                e "정답입니다! +1 점"
            "뉴기니":
                e "틀렸습니다!"
            "마다가스카르":
                e "틀렸습니다!"

    e "현재 점수: [score]점"

    label question2:
        e "두 번째 질문입니다: 파이썬이 공개된 년도는 언제일까요?"
        menu:
            "1991년":
                $ score += 1
                e "정확합니다! +1 점"
            "2000년":
                e "아니오, 그렇지 않습니다."
            "1989년":
                e "아니오, 그렇지 않습니다."

    e "최종 점수: [score]점"

    if score == 2:
        e "축하합니다! 모든 질문에 정답을 맞혔습니다."
    elif score == 1:
        e "잘 했어요! 하나의 질문에 정답을 맞혔습니다."
    else:
        e "아쉽지만, 모든 질문을 틀렸습니다."

    return
