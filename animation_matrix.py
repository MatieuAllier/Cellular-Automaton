import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as mpatches

from matrix_rule import apply_rule_to_matrix, rule_rock_paper_scissor


def init(size, iteration, rule_function):
    """ Create a list of matrix that follow a specific rule

    :param size: Size of the matrix
    :param iteration: Number of step of the automation
    :param rule_function: the function that define the rule 
    :returns: the list of the different iteration (matrix) of the automation
    :raises keyError: raises an exception
    """
    matrix = np.random.randint(3, size=(size,size))
    snapshots = [matrix]
    for i in range(0,iteration):
        matrix = apply_rule_to_matrix(matrix, rule_function)
        snapshots.append(matrix)
    return snapshots

def create_video(snapshots:list):
    """ Create animation based on a list of matrix
    """
    list_X = snapshots
    X = list_X[0]

    fig = plt.figure()
    im = plt.imshow(X, interpolation='none')
    # Create graph legend
    values = [0, 1, 2]
    colors = [ im.cmap(im.norm(value)) for value in values]
    match_dict = {0: "Rock", 1: "Paper", 2: "Scissor"}
    patches = [ mpatches.Patch(color=colors[i], label="{l}".format(l=match_dict[values[i]]) ) for i in range(len(values)) ]
    plt.tight_layout()
    leg = plt.legend(handles=patches, loc="lower left", bbox_to_anchor=(1, 0))
    def animate(i):
        X = list_X[i]
        im.set_array(X)
        return im,

    anim = animation.FuncAnimation(
        fig,
        animate,
        frames = len(list_X),
        interval = 100,
        blit = True
    )

    plt.show()

    return anim

if __name__ == "__main__":
    size = 50
    iteration = 50
    anim = create_video(init(size, iteration, rule_rock_paper_scissor))
