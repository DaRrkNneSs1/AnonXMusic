from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="PersonaL.",
                callback_data="get_playlist_playmode",
            ),
            InlineKeyboardButton(
                text="GlobaL.", callback_data="get_top_playlists"
            ),
        ],
        [
            InlineKeyboardButton(
                text="CLOSE.", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ToP 10 Playlist.", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="PersonaL.", callback_data="SERVERTOP user"
            )
        ],
        [
            InlineKeyboardButton(
                text="GlobaL.", callback_data="SERVERTOP global"
            ),
            InlineKeyboardButton(
                text="GrouP's", callback_data="SERVERTOP chat"
            )
        ],
        [
            InlineKeyboardButton(
                text="BACK.", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="CLOSE.", callback_data="close"
            ),
        ],
    ]
    return buttons


def get_playlist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="AUDIO", callback_data="play_playlist a"
            ),
            InlineKeyboardButton(
                text="Video.", callback_data="play_playlist v"
            ),
        ],
        [
            InlineKeyboardButton(
                text="BACK.", callback_data="home_play"
            ),
            InlineKeyboardButton(
                text="CLOSE.", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ToP 10 Playlist.", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="PersonaL.", callback_data="SERVERTOP Personal"
            )
        ],
        [
            InlineKeyboardButton(
                text="GlobaL.", callback_data="SERVERTOP Global"
            ),
            InlineKeyboardButton(
                text="GrouP'S", callback_data="SERVERTOP Group"
            )
        ],
        [
            InlineKeyboardButton(
                text="BACK.", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="CLOSE.", callback_data="close"
            ),
        ],
    ]
    return buttons


def failed_top_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="BACK.",
                callback_data="get_top_playlists",
            ),
            InlineKeyboardButton(
                text="CLOSE.", callback_data="close"
            ),
        ],
    ]
    return buttons


def warning_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="DELETE.",
                    callback_data="delete_whole_playlist",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="BACK",
                    callback_data="del_back_playlist",
                ),
                InlineKeyboardButton(
                    text="CLOSE.",
                    callback_data="close",
                ),
            ],
        ]
    )
    return upl


def close_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="CLOSE.",
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl
