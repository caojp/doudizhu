from enum import IntEnum


class Protocol(IntEnum):
    REQ_LOGIN = 11
    RSP_LOGIN = 12

    REQ_ROOM_LIST = 13
    RSP_ROOM_LIST = 14

    REQ_TABLE_LIST = 15
    RSP_TABLE_LIST = 16

    REQ_JOIN_TABLE = 17
    RSP_JOIN_TABLE = 18

    REQ_DEAL_POKER = 21
    RSP_DEAL_POKER = 22

    REQ_CALL_SCORE = 23
    RSP_CALL_SCORE = 24

    REQ_SHOW_POKER = 25
    RSP_SHOW_POKER = 26

    REQ_SHOT_POKER = 31
    RSP_SHOT_POKER = 32

    REQ_NO_SHOT = 33
    RSP_NO_SHOT = 34

    REQ_GAME_OVER = 41
    RSP_GAME_OVER = 42
