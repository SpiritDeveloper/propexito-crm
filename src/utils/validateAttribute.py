def validateAttribute(object, attribute):
    try:
        return object[attribute]
    except KeyError:
        return False
