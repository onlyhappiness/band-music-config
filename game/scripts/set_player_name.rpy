default player_name = "Unknown"


# 플레이어 이름 받기
label set_player_name:
    scene black

    $ protagonist_name = renpy.input("당신의 이름은 무엇인가요? (2글자 이상 입력해주세요)")
    if not protagonist_name or len(protagonist_name) < 2:
        "이름은 2글자 이상으로 입력해주세요."
        jump get_player_name
    return
