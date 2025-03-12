def validate(object, attribute):
    try:
        return object[attribute]
    except:
        return False