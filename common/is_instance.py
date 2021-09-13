class IsInstance:

    def get_instance(self, value, check):
        flag = False
        if isinstance(value, str):
            if check == value:
                flag = True
        elif isinstance(value, float):
            if value - float(check) == 0:
                flag = True
        elif isinstance(value, int):
            if value - int(check) == 0:
                flag = True
        elif not value:
            if str(value) == check:
                flag = True
        return flag