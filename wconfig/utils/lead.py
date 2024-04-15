from json import loads

from wconfig.static.T import T

boolean = {
    True: ['True', '1'],
    False: ['False', '0'],
}


def lead(some, to: T) -> T | None:
    if to is bool:
        if some in boolean[True]:
            some = True
        elif some in boolean[False]:
            some = False
        else:
            some = None
    elif to is int or to is float:
        try:
            some = to(some)
        except:
            some = None

    return some
