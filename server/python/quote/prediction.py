import sys
import os
import json
import numpy as np
import tensorflow as tf
from tensorflow.contrib import learn
from nltk.tokenize import sent_tokenize
from text_cnn_ import TextCNN
import data_helpers as dh

os.chdir(os.path.abspath(os.path.dirname(sys.argv[0])))

# Eval Parameters
tf.flags.DEFINE_integer("batch_size", 64, "Batch Size (default: 64)")
tf.flags.DEFINE_string("checkpoint_dir", "", "Checkpoint directory from training run")
tf.flags.DEFINE_boolean("eval_train", False, "Evaluate on all training data")

# Misc Parameters
tf.flags.DEFINE_boolean("allow_soft_placement", True, "Allow device soft device placement")
tf.flags.DEFINE_boolean("log_device_placement", False, "Log placement of ops on devices")

FLAGS = tf.flags.FLAGS
FLAGS(sys.argv)
# print("\nParameters:")
# for attr, value in sorted(FLAGS.__flags.items()):
#     print("{}={}".format(attr.upper(), value))
# print("")

# load essay
import pymongo
from bson.objectid import ObjectId
essayId = sys.argv[1]
conn = pymongo.MongoClient('localhost')
db = conn.get_database('mongodb_tutorial')
essayCollection = db.get_collection('essays')
result = essayCollection.find({"_id": ObjectId(essayId)})[0]
inputEssay = result.get('paragraph', 'Hi~')
inputOpinion = result.get('opinion', 'Hi~')
nameAuthor = result.get('author', 'customer')

x = dh.clean_str(inputEssay)
vocab_path = os.path.join(FLAGS.checkpoint_dir, "..", "vocab.npy")
vocabulary = np.load(vocab_path, allow_pickle=True).item()
x_test = dh.testpreprocess(inputEssay, vocabulary)


# print("\nEvaluating\n")

checkpoint_file = tf.train.latest_checkpoint(FLAGS.checkpoint_dir)
graph = tf.Graph()
with graph.as_default():
    session_conf = tf.ConfigProto(
        allow_soft_placement=FLAGS.allow_soft_placement,
        log_device_placement=FLAGS.log_device_placement)
    sess = tf.Session(config=session_conf)
    with sess.as_default():
        # Load the saved meta graph and restore variables
        saver = tf.train.import_meta_graph("{}.meta".format(checkpoint_file))
        saver.restore(sess, checkpoint_file)

        # Get the placeholders from the graph by name
        input_x = graph.get_operation_by_name("input_x").outputs[0]
        dropout_keep_prob = graph.get_operation_by_name("dropout_keep_prob").outputs[0]

        # Tensors we want to evaluate
        predictions = graph.get_operation_by_name("output/predictions").outputs[0]

        # Generate batches for one epoch
        batches = dh.batch_iter(list(x_test), FLAGS.batch_size, 1, shuffle=False)

        all_predictions = []

        for x_test_batch in batches:
            batch_predictions = sess.run(predictions, {input_x: x_test_batch, dropout_keep_prob: 1.0})
            all_predictions = np.concatenate([all_predictions, batch_predictions])

        ret = dict()
        ret['results'] = list()
        pred_sentence = sent_tokenize(inputEssay)
        for i in range(len(all_predictions)):
            if(all_predictions[i] == 1):
                ret['results'].append(pred_sentence[i])
        print(json.dumps(ret))
# print(inputEssay)
