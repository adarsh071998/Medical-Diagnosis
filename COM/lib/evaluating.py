import numpy as np
import tensorflow as tf


#imagePath = '/home/pritesh/Desktop/COM/lib/data/Prediction/c.jpeg'
def model(imagePath):
    return(run_inference_on_image(imagePath))


def create_graph():
    """Creates a graph from saved GraphDef file and returns a saver."""
    # Creates graph from saved graph_def.pb.
    modelFullPath = '/home/pritesh/Desktop/COM/lib/data/output_graph.pb'
    labelsFullPath = '/home/pritesh/Desktop/COM/lib/data/output_labels.txt'
    with tf.gfile.FastGFile(modelFullPath, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

def run_inference_on_image(imagePath):
    answer = None
    modelFullPath = '/home/pritesh/Desktop/COM/lib/data/output_graph.pb'
    labelsFullPath = '/home/pritesh/Desktop/COM/lib/data/output_labels.txt'

    if not tf.gfile.Exists(imagePath):
        tf.logging.fatal('File does not exist %s', imagePath)
        return answer

    image_data = tf.gfile.FastGFile(imagePath, 'rb').read()

    # Creates graph from saved GraphDef.
    create_graph()

    with tf.Session() as sess:

        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        predictions = sess.run(softmax_tensor,
                               {'DecodeJpeg/contents:0': image_data})
        predictions = np.squeeze(predictions)

        top_k = predictions.argsort()[-5:][::-1]  # Getting top 5 predictions
        f = open(labelsFullPath, 'rb')
        lines = f.readlines()
        labels = [str(w).replace("\n", "") for w in lines]
        dic = {}
        for node_id in top_k:
            human_string = labels[node_id]
            score = predictions[node_id]
            print('%s (score = %.5f)' % (human_string, score))
            dic[human_string]=score	
        print(dic)    	
        answer = labels[top_k[0]]
       # return answer
        return dic        
    