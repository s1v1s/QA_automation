class BuilderBaseClass:
    def __init__(self) -> None:
        self.result = {}

    def update_inner_generator(self, key_route, value):
        if not isinstance(key_route, list):
            self.result[key_route] = value
        else:
            temp = self.result
            for current_key in key_route[:-1]:
                if current_key not in temp.keys():
                    temp[current_key] = {}
                temp = temp[current_key]
            temp[key_route[-1]] = value
        return self

    def build(self):
        return self.result
