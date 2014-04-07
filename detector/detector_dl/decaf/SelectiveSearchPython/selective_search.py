import tempfile
import subprocess
import shlex
import os
import numpy as np
import scipy.io
from PIL import Image, ImageDraw
import sys
import imagenet
import pickle

script_dirname = os.path.abspath(os.path.dirname(__file__))

def get_windows(image_fnames):
    """
    Run MATLAB Selective Search code on the given image filenames to
    generate window proposals.

    Parameters
    ----------
    image_filenames: strings
        Paths to images to run on.
    """
    # Form the MATLAB script command that processes images and write to
    # temporary results file.
    f, output_filename = tempfile.mkstemp(suffix='.mat')
    os.close(f)
    fnames_cell = '{' + ','.join("'{}'".format(x) for x in image_fnames) + '}'
    command = "selective_search({}, '{}')".format(fnames_cell, output_filename)
    print(command)

    # Execute command in MATLAB.
    mc = "matlab -nojvm -r \"try; {}; catch; exit; end; exit\"".format(command)
    pid = subprocess.Popen(
        shlex.split(mc), stdout=open('/dev/null', 'w'), cwd=script_dirname)
    retcode = pid.wait()
    if retcode != 0:
        raise Exception("Matlab script did not exit successfully!")

    # Read the results and undo Matlab's 1-based indexing.
    all_boxes = list(scipy.io.loadmat(output_filename)['all_boxes'][0])
    subtractor = np.array((1, 1, 0, 0))[np.newaxis, :]
    all_boxes = [boxes - subtractor for boxes in all_boxes]

    # Remove temporary file, and return.
    os.remove(output_filename)
    if len(all_boxes) != len(image_fnames):
        raise Exception("Something went wrong computing the windows!")
    return all_boxes

if __name__ == '__main__':
    """
    Run a demo.
    """
    import time
    import md5

    filename = sys.argv[1] 
    print filename
    
    cacheboxfilename = "/home/miyamamoto/Marsface/data/cache/" + md5.new(filename).hexdigest()+".bcash"
    #    cachefilename = "/tmp/" + filename + ".cache"
    print "-----------"
    print cacheboxfilename
    boxes = []
    
    if os.path.isfile(cacheboxfilename) == True:
        f = open(cacheboxfilename,'rb')
        boxes =  pickle.load(f)
        f.close()
    else:
        
        t = time.time()
        boxes = get_windows([filename])[0]
        print("Processed {} images in {:.3f} s".format(len(filename), time.time() - t))
        f = open(cacheboxfilename,'wb')
        pickle.dump(boxes,f)
        f.close()
        
    im = Image.open(filename)
#    net = imagenet.DecafNet()
    net = imagenet.DecafNet()

    for box in boxes:

        nim = np.asarray(im.crop(box))
        scores = net.classify(nim)
        feat = net.feature('probs_cudanet_out')[0]
        pred_ind = net.top_k_prediction(scores, 1)[0]
        pred_class = net.top_k_prediction(scores, 1)[1]
        pred_prob = feat[pred_ind][0]
        
        threshold = 0.8
        print pred_prob
        if pred_prob > threshold:
            savefilename = "/home/miyamamoto/Marsface/data/result/image/dl/" + str(pred_prob) +"_"+  os.path.basename(filename) + "_" + str(net.top_k_prediction(scores, 5)[1][0]) + "_" +  str(box[0]) + "_" + str(box[1]) +"_" + str(box[2]) +"_" + str(box[3]) + ".jpg"
        

            im.crop(box).save(savefilename ,"jpeg")
        
    #for box in 
    #    for j in range(len(boxes[i])):
    #        box = (boxes[i][j][1], boxes[i][j][0], boxes[i][j][3], boxes[i][j][2])
    #        dr = ImageDraw.Draw(im)
    #        dr.rectangle(box, outline="red")
    #    im.save(image_save_filenames[i], 'JPEG', quality=50)

    #csv_filenames = [
    #    script_dirname + '/csv/boxes_000015.csv',
    #    script_dirname + '/csv/boxes_cat.csv',
    #    script_dirname + '/csv/boxes_PIA00001.csv',
    #    script_dirname + '/csv/boxes_PIA00002.csv',
    #    script_dirname + '/csv/boxes_PIA00010.csv',
    #    script_dirname + '/csv/boxes_PIA02035.csv']
    #
    #for i in range(len(csv_filenames)):
    #    np.savetxt(csv_filenames[i], boxes[i], delimiter=',', fmt='%i')
    #
    # save images with bounding boxes
    #image_save_filenames = [
    #    script_dirname + '/images/000015_boundingbox.jpg',
    #    script_dirname + '/images/cat_boundingbox.jpg',        
    #    script_dirname + '/images/PIA00001_boundingbox.jpg',
    #    script_dirname + '/images/PIA00002_boundingbox.jpg',
    #    script_dirname + '/images/PIA00010_boundingbox.jpg',
    #    script_dirname + '/images/PIA02035_boindingbox.jpg']
        
    #for i in range(len(filenames)):
    #    im = Image.open(filenames[i])
    #    for j in range(len(boxes[i])):
    #        box = (boxes[i][j][1], boxes[i][j][0], boxes[i][j][3], boxes[i][j][2])
    #        dr = ImageDraw.Draw(im)
    #        dr.rectangle(box, outline="red")
    #    im.save(image_save_filenames[i], 'JPEG', quality=50)
