import pickle


class PickleFile:
    def __init__(self, data_path):
        d = self.__dict__
        d["data_path"] = data_path
        d["data"] = {}
        self.__load_data__(d, data_path)
        return

    @staticmethod
    def __write_data__(d):
        # print("writing data")
        with open(d["data_path"], "wb") as f:
            pickle.dump(d["data"], f)
        return

    @staticmethod
    def __load_data__(d, path):
        # print("loading data")
        try:
            with open(path, "rb") as f:
                d["data"] = pickle.load(f)
        except FileNotFoundError:
            pass
        return

    def __setattr__(self, key, value):
        # print("setting attr {}: {}".format(key, value))
        d = self.__dict__
        d["data"][key] = value
        self.__write_data__(d)
        return

    def __getattribute__(self, item:str):
        if item.startswith("__") and item.endswith("__"):
            # print("get attr {}: {}".format(item, object.__getattribute__(self, item)))
            return object.__getattribute__(self, item)
        else:
            # print("get attr {}: {}".format(item, object.__getattribute__(self, "data")[item]))
            return object.__getattribute__(self, "data")[item]
