import os, read_config, shutil

def find(target, start):
    for root, dirs, files in os.walk(start):
        for name in files:
            if name.lower().find(target) >= 0:
                return root, name
                # old_path = os.path.join(root, name)
                # print(old_path)
                # new_name = name.replace(target, "Test666")
                # new_path = os.path.join(root, new_name)
                # shutil.copy(old_path, new_path)
        for name in dirs:
            if name.lower().find(target) >= 0:
                return root, name
# return file


if __name__ == "__main__":
    print(find("folder1", read_config.ReadConfig().config["test"]["plateLogic"]))