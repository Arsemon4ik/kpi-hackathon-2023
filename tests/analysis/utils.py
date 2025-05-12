def get_logs_text(file_path):
    with open(file_path, "r") as file:
        return file.readlines()
