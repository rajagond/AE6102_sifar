import os
import numpy as np
from automan.api import Automator, Problem


class SegyToNumPy(Problem):
    def get_name(self):
        return "npy_data"

    def get_commands(self):
        data_dir = "../data"
        log_dir = "../logs"
        print(data_dir)
        commands = []
        for file in os.listdir(data_dir):
            if file.endswith(".sgy"):
                print(file)
                file_path = data_dir + "/" + file[:-4]
                output_path = data_dir + "/npy_data" + "/" + file[:-4]
                print(file_path)
                print(output_path)
                cmd = f'python3 data_to_numpy.py --data {file_path} --output {output_path} --silent'
                commands.append((log_dir, cmd, None))
        return commands

if __name__ == "__main__":
    automator = Automator(
        simulation_dir="../data",
        output_dir="../data",
        all_problems=[SegyToNumPy],
    )
    automator.run()