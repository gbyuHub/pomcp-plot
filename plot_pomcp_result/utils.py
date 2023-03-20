import subprocess

def parse_rocks(filepath):
    mean = []
    std = []
    with open(filepath, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip('\n').split(' ')
            mean.append(float(line[4]))
            std.append(float(line[6]))
    return mean, std

def parse_returns(filepath):
    mean = []
    std = []
    with open(filepath, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip('\n').split(' ')
            mean.append(float(line[3]))
            std.append(float(line[5]))
    return mean, std

def parse_cv(filepath):
    mean = []
    std = []
    with open(filepath, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip('\n').split(' ')
            mean.append(float(line[5]))
            std.append(float(line[7]))
    return mean, std

def parse_ggf(filepath):
    mean = []
    std = []
    with open(filepath, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip('\n').split(' ')
            mean.append(float(line[3]))
            std.append(float(line[5]))
    return mean, std

def parse_file(log_path):
    # parse statistics of collected good rocks
    cmd_str = f"cat {log_path} | grep \"Collected good\" > /home/gbyu/pomcp_exp/plot_pomcp_result/data/good.txt"
    subprocess.run(cmd_str, shell=True)
    # parse statistics of collected bad rocks
    cmd_str = f"cat {log_path} | grep \"Collected bad\" > /home/gbyu/pomcp_exp/plot_pomcp_result/data/bad.txt"
    subprocess.run(cmd_str, shell=True)
    # parse statistics of undiscounted returns
    cmd_str = f"cat {log_path} | grep \"Undiscounted.*+\" > /home/gbyu/pomcp_exp/plot_pomcp_result/data/undiscounted_return.txt"
    subprocess.run(cmd_str, shell=True)
    # parse statistics of check actions
    cmd_str = f"cat {log_path} | grep \"Apply\" > /home/gbyu/pomcp_exp/plot_pomcp_result/data/check_action.txt"
    subprocess.run(cmd_str, shell=True)

def parse_cv_ggf(log_path):
    # parse statistics of CV
    cmd_str = f"cat {log_path} | grep \"CV of Undiscounted\" > /home/gbyu/pomcp_exp/plot_pomcp_result/data/cv.txt"
    subprocess.run(cmd_str, shell=True)
    # parse statistics of GGF score
    cmd_str = f"cat {log_path} | grep \"GGF.*+\" > /home/gbyu/pomcp_exp/plot_pomcp_result/data/ggf.txt"
    subprocess.run(cmd_str, shell=True)

if __name__ == "__main__":
    # good_rocks_mean, good_rocks_std = parse_rocks("D:/My workspace/My research/pomcp/good.txt")
    # bad_rocks_mean, bad_rocks_std = parse_rocks("D:/My workspace/My research/pomcp/bad.txt")
    # return_mean, return_std = parse_returns("D:/My workspace/My research/pomcp/undiscounted_return.txt")

    # print(return_mean, return_std)
    parse_cv_ggf("/home/gbyu/Fair-POMCP/src/ggf_log.txt")