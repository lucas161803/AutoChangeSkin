def alter(file,old_str,new_str):
    """
    替換檔案中的字串
    :param file:檔名
    :param old_str:就字串
    :param new_str:新字串
    :return:
    """
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str,new_str)
            file_data += line
    with open(file, "w", encoding="utf-8") as f:
        f.write(file_data)
 
alter("file1.txt", "python", "測試")