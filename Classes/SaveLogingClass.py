import os
from datetime import datetime


class SaveLogging:

    def __init__(self, logfilename, extension="log"):

        self.log_name = logfilename
        self.extension = extension
        self.log_folder_name = "logs"

        current_date_to_string = str(datetime.now()).split(".")[0].replace(" ", "_").replace(":", "-") + "_"
        self.new_file_name = current_date_to_string + self.log_name + "." + self.extension

        print(str(datetime.now()))

    def get_time_stamp(self):

        return str(datetime.now())

    def write_initial_line(self, line):

        current_time_stamp = str(datetime.now())

        with open(self.new_file_name, "w") as file:
            file.write(current_time_stamp + " [  INFO]" + "  " + line + "\n")

    def append_lines(self, line):

        current_time_stamp = str(datetime.now())

        with open(self.new_file_name, "a") as file:
            file.write(current_time_stamp + " [  INFO]" + "  " + line + "\n")

    def move_to_logging_folder(self):

        abs_path = os.path.abspath(__file__)
        print(abs_path)
        file = abs_path.split("\\")[-1]
        over_folder = abs_path.split("\\")[-2]
        abs_path_to_logging_files = abs_path.replace(over_folder, self.log_folder_name).replace(file, "")

        # print(abs_path_to_logging_files)
        move_statement = "move " + self.new_file_name + " " + abs_path_to_logging_files

        try:
            os.system(move_statement)
        except:
            print("Logging file can not be moved to : ", over_folder)
            print("File stored in actual location : ", abs_path)



if __name__ == '__main__':
    log = SaveLogging(logfilename="LoggingTest")
    log.write_initial_line(line="line1")
    log.append_lines(line="line2")
    log.move_to_logging_folder()
