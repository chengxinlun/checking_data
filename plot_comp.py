import pickle
try:
    import easygui
    noGui = False
except Exception:
    noGui = True
    print("Install module easygui for gui. (Optional)")
    pass
import numpy as np
import matplotlib.pyplot as plt


def plot_comp(lines, rmid_list):
    raw_data = list()
    for each in lines:
        file_in = open("data/" + str(each) + ".pkl")
        raw_data.append(pickle.load(file_in))
        file_in.close()
    if len(rmid_list) == 0:
        rmid_list = raw_data[0].keys()
    # All the rmid valid and needed
    note = [i for i in rmid_list if raw_data[0][i][1] != -1]
    note = [each for each in note if raw_data[1][each][1] != -1]
    note = [each for each in note if raw_data[2][each][1] != -1]
    y = np.array([raw_data[0][each][0] - raw_data[1][each][0] for each in note])
    ey = np.array([np.sqrt(raw_data[0][each][1] ** 2.0 + raw_data[1][each][1] ** 2.0) for each in note])
    x = np.array([raw_data[2][each][0] for each in note])
    ex = np.array([raw_data[2][each][1] for each in note])
    plt.errorbar(x, y, xerr = ex, yerr = ey, linestyle = "None", marker = ".")
    plt.show()


def get_link():
    link_file = open("link.pkl", "rb")
    link = pickle.load(link_file)
    link_file.close()
    return link


def save_link(link):
    link_file = open("link.pkl", "wb")
    pickle.dump(link, link_file)
    link_file.close()


# Default link
link = {"CAII3934": "LOGL3000", "CIII": "LOGL1350", "CIIIA": "LOGL1350",
        "CIV": "LOGL1700", "HBETA_BR": "LOGL5100", "HEII1640": "LOGL1700",
        "MGII": "LOGL3000", "NEV3426": "LOGL3000", "OII3728": "LOGL3000",
        "OIII5008A": "LOGL5100", "OIII5008C": "LOGL5100"}
print("Press Control C to exit.")
try:
    link = get_link()
except Exception:
    save_link(link)
print("Lines      |Continuum used")
print("--------------------------")
for each in link.keys():
    print(each + " | " + link[each])
print("--------------------------")
while True:
    try:
        link = get_link()
    except Exception:
        save_link(link)
    if noGui:
        line1 = raw_input("Please enter the name of the first line:")
        line2 = raw_input("Please enter the name of the second line:")
        if line1 == '' or line2 == "":
            print("Exiting")
            break
    else:
        try:
            line1, line2 = easygui.multenterbox("Please enter the line.", "Line", ["Line1", "Line2"])
        except Exception:
            print("Exiting")
            break
    print("Using " + str(link[line1]) + " as continuum")
    try:
        plot_comp([line1, line2, link[line1]], [])
    except Exception:
        print("One of the lines does not exist.")
