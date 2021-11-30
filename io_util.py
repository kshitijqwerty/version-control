def background(code):
    return "\33[{code}m".format(code=code)


def style_text(code):
    return "\33[{code}m".format(code=code)


def color_text(code):
    return "\33[{code}m".format(code=code)


def print_red(message):
    encoding = background(1) + color_text(49) + style_text(
        31) + message
    encoding += background(0) + color_text(0) + style_text(0)
    print(encoding)


def print_yellow(message):
    encoding = background(0) + color_text(49) + style_text(
        93) + message
    encoding += background(0) + color_text(0) + style_text(0)
    print(encoding)


def print_green(message):
    encoding = background(1) + color_text(49) + style_text(
        32) + message
    encoding += background(0) + color_text(0) + style_text(0)
    print(encoding)


def print_purple(message):
    encoding = background(1) + color_text(49) + style_text(
        95) + message
    encoding += background(0) + color_text(0) + style_text(0)
    print(encoding)
