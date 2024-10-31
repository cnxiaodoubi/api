import os  
import random  
import string  
  
def generate_random_string(length=12):  
    """生成一个由英文和数字组成的指定长度的随机字符串"""  
    characters = string.ascii_letters + string.digits  
    return ''.join(random.choice(characters) for _ in range(length))  
  
def rename_files_in_directory(directory_path):  
    """批量修改指定目录中的文件名，保留扩展名"""  
    try:  
        # 列出目录中的所有文件  
        files = os.listdir(directory_path)  
          
        for file_name in files:  
            # 跳过目录，只处理文件  
            if os.path.isfile(os.path.join(directory_path, file_name)):  
                # 分离文件名和扩展名  
                file_base, file_ext = os.path.splitext(file_name)  
                  
                # 生成新的文件名（不包含扩展名）  
                new_file_base = generate_random_string()  
                  
                # 构造新的完整文件名  
                new_file_name = new_file_base + file_ext  
                  
                # 获取文件的完整路径  
                old_file_path = os.path.join(directory_path, file_name)  
                new_file_path = os.path.join(directory_path, new_file_name)  
                  
                # 重命名文件  
                os.rename(old_file_path, new_file_path)  
                print(f"Renamed '{file_name}' to '{new_file_name}'")  
            else:  
                print(f"'{file_name}' is not a file, skipping.")  
    except Exception as e:  
        print(f"An error occurred: {e}")  
  
# 指定你的文件夹路径  
directory_to_rename = r"C:\Users\77514\Desktop\mimage"  
  
# 调用函数进行重命名  
rename_files_in_directory(directory_to_rename)