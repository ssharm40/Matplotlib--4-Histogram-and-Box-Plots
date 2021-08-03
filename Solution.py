import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
#Write your code here

#task1

def test_hist_of_a_sample_normal_distribution():
    fig = plt.figure(figsize = (8,6)) 
    ax = fig.add_subplot(111)
    np.random.seed(100)
    x1=np.random.normal(25,3.0,1000)
    ax.set(title='Histogram of a Single Dataset',xlabel='X1', ylabel='Bin Count')
    ax.hist(x1,bins=30)
    plt.savefig("histogram_normal.png")
    
test_hist_of_a_sample_normal_distribution()


#Task2

def test_boxplot_of_four_normal_distribution():
    fig = plt.figure(figsize = (8,6))
    ax = fig.add_subplot(111)
    np.random.seed(100)
    x1=np.random.normal(25,3.0,1000)
    x2=np.random.normal(35,5.0,1000)
    x3=np.random.normal(55,10.0,1000)
    x4=np.random.normal(45,3.0,1000)
    labels=['X1', 'X2', 'X3', 'X4']
    ax.boxplot([x1, x2, x3, x4], labels=['X1', 'X2', 'X3', 'X4'],patch_artist = "True", sym='+',notch=True, bootstrap=10000)
    ax.set(title='Box plot of Multiple Datasets',xlabel='Dataset', ylabel='Value')
    plt.savefig('box_distribution.png')
    
test_boxplot_of_four_normal_distribution()    
