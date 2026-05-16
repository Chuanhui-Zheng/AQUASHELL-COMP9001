import textwrap


YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
GREEN = "\033[92m"
RESET = "\033[0m"


def art(text):
    return textwrap.dedent(text).strip("\n")


STARTER_CREATURES = [
    {
        "name": "Little Dory",
        "kind": "fish",
        "source": "starter",
        "capacity": 1,
        "sell_price": 0,
        "sprite": "𓆝",
    },
    {
        "name": "Starglow Fish",
        "kind": "fish",
        "source": "starter",
        "capacity": 1,
        "sell_price": 0,
        "sprite": "⋆.˚𓆟",
    },
    {
        "name": "Shell Snail",
        "kind": "pet",
        "source": "starter",
        "capacity": 1,
        "sell_price": 0,
        "sprite": "_@/",
        "bottom": True,
    },
]


BIG_FISH = [
    {
        "name": "Seahorse",
        "kind": "fish",
        "source": "fishing",
        "size": "large",
        "min_rod": 1,
        "capacity": 1,
        "sell_price": 22,
        "sprite": art(
            r"""
              ,_. 
              /.\ 
             {>) `
             `((_,
               `"`
            """
        ),
    },
    {
        "name": "Starfish",
        "kind": "fish",
        "source": "fishing",
        "size": "large",
        "min_rod": 1,
        "capacity": 2,
        "sell_price": 22,
        "bottom": True,
        "stationary": True,
        "sprite": art(
            r"""
⠀⠀⠀⠀⠀⠀⢀⣦⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡜⣞⠂⠀⠀⠀⠀⠀⠀
⠙⠛⠥⣲⣒⢖⡹⣚⡴⣤⣲⣢⠶⠶⠂
⠀⠀⠀⠉⣛⣩⣁⡸⡉⠓⠉⠉⠀⠀⠀
⠀⠀⢀⠾⡥⠚⠁⠈⠫⢍⣰⡀⠀⠀⠀
⠀⠀⠚⠉⠀⠀⠀⠀⠀⠀⠈⠙⠂⠀⠀
            """
        ),
    },
    {
        "name": "Jellyfish",
        "kind": "fish",
        "source": "fishing",
        "size": "large",
        "min_rod":2,
        "capacity": 4,
        "sell_price": 22,
        "sprite": art(
            r"""
⠀⠀⠀⢀⣤⡶⠗⠛⠚⠛⠛⢦⣄⠀⠀⠀⠀
⠀⢀⡔⠃⠑⠀⠄⢀⠑⢈⠀⠈⠝⠳⣦⠀⠀
⣠⠏⠀⠄⡔⡂⠀⡑⢀⠐⠠⠀⢂⠀⠈⠹⡄
⡯⠂⠆⢀⣀⠠⢀⡂⢠⣄⡁⠠⠀⡃⠂⠀⢳
⢿⡀⠀⠂⠋⠠⠀⠀⠂⠄⠈⢀⠂⠠⠈⢠⡏
⠀⡑⠶⠤⡴⣲⣷⢿⡟⢣⣿⡗⢆⠤⠖⠋⠀
⠀⣠⢎⡵⡿⠉⡼⢣⡈⢧⠳⣌⡓⠢⡄⠀⠀
⠰⡇⠺⣅⠳⡄⠳⣄⡷⠀⡇⡴⢃⡤⠇⠀⠀
⠀⠀⠙⢢⡈⡇⠹⠴⢻⢀⡞⠁⠳⠜⠀⠀⠀
            """
        ),
    },
    {
        "name": "Paralichthys olivaceus",
        "kind": "fish",
        "source": "fishing",
        "size": "large",
        "min_rod": 2,
        "capacity": 5,
        "sell_price": 30,
        "starts_left": True,
        "sprite": art(
            r"""
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣶⣶⣶⡶⢶⣶⣦⣤⣤⠤⠀
⠀⠀⠀⠀⠀⢠⢾⣿⠿⢻⠲⠉⡫⣰⢑⠘⣛⡋⢈⠩⣹⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣠⢴⡾⠀⢠⠈⠏⢥⢄⡞⡨⠃⢹⡩⡅⠀⠶⣿⠀⠀⣀⣤⡴⠶⠶⠒⠂
⠀⢀⣾⠏⠃⡀⢐⣨⠶⠝⢚⠅⢠⣈⡀⢀⠟⢡⣲⢰⡧⢐⡝⣸⡿⢀⠀⠀⠀⠀
⢰⣿⢤⣬⢀⠊⠊⠡⠒⠬⣧⠋⠏⠰⠰⣒⠁⣊⡍⠀⡇⡃⠊⠀⠀⣿⠀⠀⠀⠀
⠹⢿⣤⡠⠨⢸⠿⢘⢆⣁⢠⢇⠭⢉⠘⡃⢪⠑⢐⡠⢓⡴⢡⣾⣼⡟⠀⠀⠀⠀
⠀⠀⠙⢿⡌⠤⡤⡀⠘⢔⣑⠅⢬⡃⠆⠄⠂⠀⠌⠐⢾⡇⠀⠉⠙⠛⠓⠲⠤⡀
⠀⠀⠀⠀⠈⠐⢿⣧⣤⣿⡟⠛⢳⡏⠐⢢⠡⠀⠀⢘⣼⣇⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⡄⠀⠀⠻⠿⠷⠾⠶⠞⠛⠛⠛⠛⠛⠓⠂⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            """
        ),
    },
    {
        "name": "Siamese fighting fish",
        "kind": "fish",
        "source": "fishing",
        "size": "large",
        "min_rod": 3,
        "capacity": 5,
        "sell_price": 15,
        "sprite": art(
            r"""
⣠⡴⠒⠒⢒⣦⣤⣀⡀⠀⠀⠀⠛⡦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣤⠤⣦⣤⣄⡐⠟⠐⢊⢦⠀⠀⠉⣿⣿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⠞⠉⠀⠀⣉⡉⣻⠿⢷⣄⠈⣷⣇⠒⠲⣮⡻⣆⢻⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠸⡷⠀⠀⠀⠁⠰⠜⢘⠠⠈⠳⣬⡻⣑⢦⣾⡿⢹⣜⠻⣦⣄⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⢶⣂⣈⣘⣛⢻⣇⣘⣇⣌⡉⢩⣌⡛⠿⣷⣦⣄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡇⠉⢉⣽⡈⡀⢊⢉⠉⣩⣭⠀⠫⠭⡅⡽⠆⣹⣷
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡐⡞⢃⢂⢡⡉⢈⣰⠐⣣⡌⠭⣉⠻⣠⠟⠋⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣩⠇⡁⣰⠏⣄⢲⢠⡿⣸⠉⠸⣘⠈⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⢋⡭⢕⣠⠵⠟⠁⠼⢋⣴⢉⡶⠃⣴⡡⠁⠀⠀⠀⠀⠀
⠀⢀⡰⠶⠿⠛⠒⠪⠯⠵⠖⠚⠋⠁⠀⠀⣤⣴⠟⠁⢀⣠⠞⠉⠀⠀⠀⠀⠀⠀⠀
⠀⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠊⠁⣠⠞⡉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⠶⠖⠋⠁⠀⠀⠐⠷⠞⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            """
        ),
    },
    {
        "name": "Dolphin",
        "kind": "fish",
        "source": "fishing",
        "size": "large",
        "min_rod": 3,
        "capacity": 5,
        "sell_price": 32,
        "starts_left": True,
        "sprite": art(
            r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⡶⣗⡂⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⠖⠛⠉⢉⠛⢴⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣼⠃⠐⠰⢈⠀⠠⢫⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣾⠃⠀⠁⠀⢀⣠⡕⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣴⡾⢛⠈⠈⢐⡄⢨⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⢡⠊⠀⠊⠀⠁⣑⡷⠉⢾⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣷⠯⠭⣸⠐⠀⢀⡳⡇⠀⡎⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢹⡆⢠⢀⡈⡇⠀⡗⠿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⣧⠠⠀⠘⡇⢀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠸⡆⣐⠀⠹⣬⡽⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠱⡜⠢⣠⠱⠊⠙⠧⣀⠀⠀⠀⠀⠀⢀⣀⣀⡀
⠀⠀⠀⠀⠀⠀⠈⠺⢥⣨⣀⣁⡀⠹⠽⠶⠴⢶⢋⢝⠍⡍⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠙⠛⠫⢍⡥⠌⣴⡋⠉⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣰⣜⠛⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⢿⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀
            """
        ),
    },
    {
        "name": "Manta Ray",
        "kind": "fish",
        "source": "fishing",
        "size": "large",
        "min_rod": 4,
        "capacity": 7,
        "sell_price": 42,
        "sprite": art(
            r"""
⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠹⣟⣓⠶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠘⢡⡀⢀⠈⠀⠛⠿⠶⣦⣤⣀⠀⠀⠀⠀⢀⡴⠛⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢹⣦⠐⠈⠀⠐⠀⠨⠉⠙⠛⠓⣒⣖⢿⣧⠀⠀⠀⠀⢀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠱⡜⠀⢈⠀⠈⠻⣷⣆⠄⢀⠀⠈⠈⠢⠨⣵⣤⣀⣠⠟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢻⡄⢠⣾⣦⡈⢙⣿⡆⠀⠀⠈⢀⡀⠀⠈⣿⡟⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⡇⠄⠙⢻⣟⡄⠘⠋⠄⠀⠀⠀⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡕⠀⠄⠀⠻⠙⠀⠀⠄⠀⠟⣷⣤⠐⠀⠀⠹⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣾⠀⠈⠄⢀⠀⢀⣒⢢⣄⠀⠈⢻⣿⣮⣀⠀⢹⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢧⣮⡄⠈⢀⠀⠐⣈⠘⠽⣿⣤⠀⠀⠉⠀⠀⠀⣧⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣤⣴⠾⠞⣦⢈⡀⣀⣁⠀⢀⠀⠈⠀⠁⠀⠀⠂⠀⢿⡄⠀⠀⠀
⠀⠀⠀⢀⣾⠛⠉⠀⠀⠀⠙⠛⠛⠛⠛⠓⠚⠢⠤⣀⣄⡀⠀⢀⠈⠐⢰⠀⠀⠀
⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠒⠥⣐⠢⡙⣇⠀⠀
⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀
            """
        ),
    },
    {
        "name": "Celestial Whale",
        "kind": "fish",
        "source": "fishing",
        "size": "large",
        "min_rod": 4,
        "capacity": 8,
        "sell_price": 45,
        "sprite": art(
            r"""
⠀⠀⠀⠀⢠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠻⣿⢶⣤⡀⠀⠀⠀⠀⠀⠟⢂⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠒⢤⢙⢳⣤⡀⠀⠀⠸⢸⠛⢲⠶⠶⠶⠶⠶⢤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣵⠪⡻⡄⠟⢣⣅⡤⡠⣘⣦⠣⠣⢂⡕⠖⠛⠓⠙⠛⠛⠲⠶⠒⢤⡤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣦⣬⡜⠂⡻⣖⢓⡢⠟⢚⡾⣗⣟⠚⠫⡃⡜⠀⠀⠀⠀⠀⠀⠁⠈⠉⠏⡉⠖⠢⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡯⢻⠏⢻⣯⣶⣛⠽⡵⠠⠷⢐⣚⣞⡲⠒⢕⡶⠤⠀⠀⠀⢀⡀⠀⢀⣈⣀⣀⣒⣼⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢢⠳⠏⠢⣀⢻⣯⢣⠮⣓⣗⣏⣌⠝⣼⠎⣶⣺⡙⡩⣄⢉⢈⣄⠤⠈⠈⠂⢐⠖⠉⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡤⠤⣖⣈⣩⣅⣌⢤⢨⣹⣽⣰⣌⣛⣿⣬⣳⡽⠘⢐⣖⣛⣺⣾⡢⣦⣎⣨⣛⣪⡿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠸⠟⠛⠛⠉⠉⠉⠁⠀⠀⠀⠉⠻⢦⣀⠀⠀⠈⠉⠉⠉⠉⠀⠗⠊⠴⠿⠷⠷⠿⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            """
        ),
    },
    {
        "name": "Hammerhead shark",
        "kind": "fish",
        "source": "fishing",
        "size": "large",
        "min_rod": 5,
        "capacity": 8,
        "sell_price": 45,
        "sprite": art(
            r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡏⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡒⠳⠍⠉⠢⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⠟⣓⣬⣷⣶⣶⣿⠛⠒⢒⣒⡶⠖⠃⠀⠀⠀⠀⠈⢣⡀⠀
⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⢴⣚⣋⠉⠉⡈⠽⣿⣿⣿⡟⠀⠀⠉⠀⠀⠘⠓⠲⢶⣄⠀⠀⠀⢹⠀
⠈⠻⢶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⣀⣴⡞⠻⠿⡏⠉⠀⠀⠀⠠⠴⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠜⠿⣆⡀⠀⠘⣧
⠀⠀⠀⠙⢿⣿⣷⣦⣄⡀⠀⠀⢀⣠⣾⣿⣿⣿⣿⠾⠶⠾⠓⠒⠒⠚⠉⠉⠀⠀⠀⠀⠀⣀⣀⡠⠤⠴⠚⠉⠀⠀⠀⠀⠙⠛⠛⠋
⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣶⣶⠿⢿⡿⠟⠋⣨⠁⠀⠀⠀⢀⣀⣀⡠⠤⠤⢤⣤⠖⠒⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⠓⠒⢶⣶⠖⠛⠛⠦⣄⢠⠏⠉⠀⠀⠀⠀⠀⠀⠈⠳⡄⠀⣻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣴⡿⢟⠷⠃⠀⠀⠋⠁⠀⠀⠀⠀⠘⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣴⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠛⠙⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

            """
        ),
    },
    {
        "name": "Megalodon",
        "kind": "fish",
        "source": "fishing",
        "size": "large",
        "min_rod": 5,
        "capacity": 8,
        "sell_price": 45,
        "starts_left": True,
        "sprite": art(
            r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠲⠶⡦⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢭⠱⣄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠹⣄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⢀⣼⠥⠚⢻⣆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡔⠉⡽⠀⠀⠀⠀⠀⠀⠈⠀⠀⢀⣼⡿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠁⣀⣇⠀⠀⠀⠀⢀⣀⣠⡶⡒⢟⣲⠃
⢀⣀⣀⣀⣠⣤⡤⠤⠶⢶⠶⠖⠰⠟⠵⠰⠄⠂⠙⠟⠛⠛⡩⢉⠁⣨⡴⠟⠃⠀
⠈⠛⢧⣤⡉⠉⠀⠀⢁⣒⡰⠐⢋⠆⠑⠋⠩⠭⠉⠋⢍⣁⣀⣦⣼⠏⠀⠀⠀⠀
⠀⠀⠀⠐⠺⠿⢭⣁⣀⡈⠴⡖⠆⠈⠤⣉⣉⣥⡴⠿⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⢹⡇⣨⡝⢉⣛⠻⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣶⡟⠀⠀⠈⠂⠥⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            """
        ),
    },
]


SHOP_STOCK = [
    {
        "name": "Little Dory",
        "kind": "fish",
        "source": "shop",
        "price": 12,
        "capacity": 1,
        "sell_price": 4,
        "sprite": "𓆝"
    },

    {
        "name": "Tiny Angelfish",
        "kind": "fish",
        "source": "shop",
        "price": 16,
        "capacity": 1,
        "sell_price": 5,
        "sprite": "𓆟"
    },

    {
        "name": "Round Fish",
        "kind": "fish",
        "source": "shop",
        "price": 18,
        "capacity": 1,
        "sell_price": 6,
        "sprite": "𓆞"
    },

    {
        "name": "Starglow Fish",
        "kind": "fish",
        "source": "shop",
        "price": 24,
        "capacity": 1,
        "sell_price": 8,
        "sprite": "⋆.˚𓆟"
    },

    {
        "name": "Shell Snail",
        "kind": "pet",
        "source": "shop",
        "price": 10,
        "capacity": 1,
        "sell_price": 3,
        "sprite": "_@/",
        "bottom": True
    },

    {
        "name": "Seahorse",
        "kind": "fish",
        "source": "shop",
        "price": 66,
        "capacity": 1,
        "sell_price": 22,
        "sprite": "🐎"
    },
]


FISHING_CATCHES = [
    {"name": "Little Dory", "kind": "fish", "source": "fishing",
        "size": "small", "capacity": 1, "sell_price": 3, "sprite": "𓆝"},
    {"name": "Tiny Angelfish", "kind": "fish", "source": "fishing",
        "size": "small", "capacity": 1, "sell_price": 3, "sprite": "𓆟"},
    {"name": "Round Fish", "kind": "fish", "source": "fishing",
        "size": "small", "capacity": 1, "sell_price": 3, "sprite": "𓆞"},
    {"name": "Starglow Fish", "kind": "fish", "source": "fishing",
        "size": "small", "capacity": 1, "sell_price": 4, "sprite": "⋆.˚𓆟"},
    {"name": "Shell Snail", "kind": "pet", "source": "fishing", "size": "small",
        "capacity": 2, "sell_price": 2, "sprite": "_@/", "bottom": True},
]


ALL_CREATURES = STARTER_CREATURES + SHOP_STOCK + FISHING_CATCHES + BIG_FISH
CREATURES_BY_NAME = {creature["name"]: creature for creature in ALL_CREATURES}
STARTER_NAMES = [creature["name"] for creature in STARTER_CREATURES]
BIG_FISH_NAMES = [fish["name"] for fish in BIG_FISH]


def normalize_entry(entry):
    if isinstance(entry, dict):
        return {"name": entry.get("name"), "shiny": bool(entry.get("shiny", False))}
    return {"name": entry, "shiny": False}


def get_creature(name):
    return CREATURES_BY_NAME.get(name)


def get_owned_creatures(data):
    creatures = []
    for raw_entry in data.get("inventory", []):
        entry = normalize_entry(raw_entry)
        creature = get_creature(entry["name"])
        if creature:
            copy = creature.copy()
            copy["sprite"] = copy.get("tank_sprite", copy["sprite"])
            copy["shiny"] = entry["shiny"]
            creatures.append(copy)
    return creatures


def count_owned(data, name, shiny=None):
    total = 0
    for raw_entry in data.get("inventory", []):
        entry = normalize_entry(raw_entry)
        if entry["name"] != name:
            continue
        if shiny is None or entry["shiny"] == shiny:
            total += 1
    return total


def capacity_used(data):
    total = 0
    for creature in get_owned_creatures(data):
        total += creature.get("capacity", 1)
    return total


def capacity_limit(data):
    return data.get("tank_capacity", 10)


def has_capacity_for(data, name):
    creature = get_creature(name)
    if not creature:
        return False
    return capacity_used(data) + creature.get("capacity", 1) <= capacity_limit(data)


def add_creature(data, name, shiny=False):
    if not has_capacity_for(data, name):
        return False
    data.setdefault("inventory", []).append({"name": name, "shiny": shiny})
    return True


def remove_creatures(data, name, quantity, allow_shiny=False):
    removed = 0
    kept = []
    for raw_entry in data.get("inventory", []):
        entry = normalize_entry(raw_entry)
        if entry["name"] == name and removed < quantity and (allow_shiny or not entry["shiny"]):
            removed += 1
        else:
            kept.append(entry)
    data["inventory"] = kept
    return removed


def find_creature_name(text):
    lowered = text.strip().lower()
    for name in CREATURES_BY_NAME:
        if name.lower() == lowered:
            return name
    return None


def sprite_lines(item):
    return str(item["sprite"]).splitlines()


def sprite_width(item):
    return max((len(line) for line in sprite_lines(item)), default=0)


def sprite_height(item):
    return len(sprite_lines(item))


def preview_sprite(item):
    for line in sprite_lines(item):
        if line.strip():
            return line.strip()
    return item["name"]


def color_text(text, color):
    return f"{color}{text}{RESET}"


def display_name(item):
    if item.get("shiny"):
        return color_text(f"Shiny {item['name']}", YELLOW)
    return item["name"]


def show_handbook(data, print_header, pause):
    print_header(data, "Fish Handbook")
    print("This guide shows small fish and pets, plus rod-locked big creatures.")

    sections = [
        ("Small Fish & Pets", FISHING_CATCHES),
        ("Rod-Locked Big Creatures", BIG_FISH),
    ]

    owned_names = {normalize_entry(item)["name"]
                   for item in data.get("inventory", [])}
    for title, items in sections:
        print(f"\n{color_text(title, CYAN)}")
        print("-" * len(title))
        for item in items:
            owned_mark = "Owned" if item["name"] in owned_names else "Not owned"
            price = f" | {item['price']} coins" if "price" in item else ""
            rod = f" | Rod Level {item['min_rod']}+" if "min_rod" in item else ""
            capacity = f" | Capacity {item.get('capacity', 1)}"
            print(
                f"{item['name']} ({item['kind']}) - {owned_mark}{price}{rod}{capacity}")
            display_sprite = item["sprite"] if item.get(
                "source") == "shop" else item.get("tank_sprite", item["sprite"])
            for line in sprite_lines({"sprite": display_sprite}):
                print(f"  {line}")
            print()

    pause()
