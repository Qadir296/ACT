import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

rect=mpatches.Rectangle((31,),14,7, fill = False,color = "purple",linewidth = 2)
plt.gca().add_patch(rect)