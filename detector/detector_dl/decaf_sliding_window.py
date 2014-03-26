# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# # DeCAF - Sliding Window

# <codecell>

%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from numpy.lib.stride_tricks import as_strided as ast
from PIL import Image
from decaf.scripts import imagenet

# <codecell>

# Sliding Window - http://www.johnvinyard.com/blog/?p=268

def norm_shape(shape):
    '''
    Normalize numpy array shapes so they're always expressed as a tuple, 
    even for one-dimensional shapes.
     
    Parameters
        shape - an int, or a tuple of ints
     
    Returns
        a shape tuple
    '''
    try:
        i = int(shape)
        return (i,)
    except TypeError:
        # shape was not a number
        pass
 
    try:
        t = tuple(shape)
        return t
    except TypeError:
        # shape was not iterable
        pass
     
    raise TypeError('shape must be an int, or a tuple of ints')

def sliding_window(a,ws,ss = None,flatten = True):
    '''
    Return a sliding window over a in any number of dimensions
     
    Parameters:
        a  - an n-dimensional numpy array
        ws - an int (a is 1D) or tuple (a is 2D or greater) representing the size 
             of each dimension of the window
        ss - an int (a is 1D) or tuple (a is 2D or greater) representing the 
             amount to slide the window in each dimension. If not specified, it
             defaults to ws.
        flatten - if True, all slices are flattened, otherwise, there is an 
                  extra dimension for each dimension of the input.
     
    Returns
        an array containing each n-dimensional window from a
    '''
     
    if None is ss:
        # ss was not provided. the windows will not overlap in any direction.
        ss = ws
    ws = norm_shape(ws)
    ss = norm_shape(ss)
     
    # convert ws, ss, and a.shape to numpy arrays so that we can do math in every 
    # dimension at once.
    ws = np.array(ws)
    ss = np.array(ss)
    shape = np.array(a.shape)
     
     
    # ensure that ws, ss, and a.shape all have the same number of dimensions
    ls = [len(shape),len(ws),len(ss)]
    if 1 != len(set(ls)):
        raise ValueError('a.shape, ws and ss must all have the same length. They were %s' % str(ls))
     
    # ensure that ws is smaller than a in every dimension
    if np.any(ws > shape):
        raise ValueError('ws cannot be larger than a in any dimension.a.shape was %s and ws was %s' % (str(a.shape),str(ws)))
     
    # how many slices will there be in each dimension?
    newshape = norm_shape(((shape - ws) // ss) + 1)
    # the shape of the strided array will be the number of slices in each dimension
    # plus the shape of the window (tuple addition)
    newshape += norm_shape(ws)
    # the strides tuple will be the array's strides multiplied by step size, plus
    # the array's strides (tuple addition)
    newstrides = norm_shape(np.array(a.strides) * ss) + a.strides
    strided = ast(a,shape = newshape,strides = newstrides)
    if not flatten:
        return strided
     
    # Collapse strided so that it has one more dimension than the window.  I.e.,
    # the new array is a flat list of slices.
    meat = len(ws) if ws.shape else 0
    firstdim = (np.product(newshape[:-meat]),) if ws.shape else ()
    dim = firstdim + (newshape[-meat:])
    # remove any dimensions with size 1
    dim = filter(lambda i : i != 1,dim)
    return strided.reshape(dim)

# <codecell>

# Convert PIL image to numpy array
fn = "FeaturedImage.png" # http://lroc.sese.asu.edu/news/index.php?/archives/877-Faulted-Kipuka.html
Img = Image.open(fn).convert("L")
ImgArray = np.asarray(Img)
print ImgArray.shape

# <codecell>

# Display image
fig, ax = plt.subplots()
ax.imshow(ImgArray, cmap = cm.Greys_r)

# <codecell>

# Get windows
ws = min(ImgArray.shape)/5
ss = min(ImgArray.shape)/20 
ImgWindows = sliding_window(ImgArray,(ws,ws),(ss,ss))
numWindows = ImgWindows.shape[0]
print ws, ss
print ImgWindows.shape

# <codecell>

# DeCAF
net_root='decaf//imagenet_pretrained//'
net = imagenet.DecafNet(net_root+'imagenet.decafnet.epoch90', net_root+'imagenet.decafnet.meta')

# <codecell>

threshold = 0.7

for i in range(numWindows):
    scores = net.classify(ImgWindows[i], center_only=True)
    feat = net.feature('probs_cudanet_out')[0]
    pred_ind = net.top_k_prediction(scores, 1)[0]
    pred_class = net.top_k_prediction(scores, 1)[1]
    pred_prob = feat[pred_ind][0]
    
    if pred_prob > threshold:
        ImgDecaf = net.feature('data')[0,::-1]
        ImgDecaf -= ImgDecaf.min()
        ImgDecaf /= ImgDecaf.max()
        
        fig, ax = plt.subplots()
        ax.imshow(ImgDecaf, cmap = cm.Greys_r)
        ax.set_title('PredProb=' + str(feat[pred_ind][0].round(2)) + ' ' + pred_class[0])

