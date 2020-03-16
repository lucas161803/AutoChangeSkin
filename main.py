import os, read_config, find_target_file, alter_file

old_str = "Test666"
new_str = "Test777"
def change(start):
    t = find_target_file.find(old_str, start)
    print(t)
    alter_file.alter(os.path.join(t[0],t[1]), old_str, new_str)
    # return t

if __name__ == "__main__":
    root = read_config.ReadConfig().config["test"]["PlateLogic"]
    print(root)
    print(change(root))
    # change("D:/test_data/plateLogic")