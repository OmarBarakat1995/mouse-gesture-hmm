import pickle


def save_to_disk(obj, file_path):
    with open(file_path, "wb") as fp:
        pickle.dump(obj, fp)


def load_from_disk(file_path):
    with open(file_path, "rb") as fp:
        b = pickle.load(fp)
        return b
