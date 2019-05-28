import tensorflow as tf
import tensorflow_hub as hub

########################
# Model 1
#


def embedding_layer():
    input_sent = tf.placeholder(tf.string, [None], name='input')
    elmo_module = hub.Module("https://tfhub.dev/google/elmo/2", trainable=False)
    embedding = elmo_module(input_sent, signature="default", as_dict=True)['default']
    return input_sent, embedding


def model_inputs():
    """
    Create the model inputs
    """
    inputs_ = tf.placeholder(tf.float32, [None, 100, 1024], name='essays')
    scores_ = tf.placeholder(tf.float32, [None, 1], name='scores')
    lens_ = tf.placeholder(tf.int32, [None], name='essay_lengths')
    indice_ = tf.placeholder(tf.int32, [None, 2], name='indice')
    keep_prob_ = tf.placeholder(tf.float32, name='keep_prob')

    return inputs_, lens_, indice_, scores_, keep_prob_


def build_lstm_layers(sentences, sentences_length, hidden_layer, keep_prob_):
    """
    Create the LSTM layers
    :parm "sentences"   : sentences [batchsize, max_len, ???]
    :parm "lstm_sizes"  : stacked lstm hidden layer size
    :parm "keep_prob_"  : drop out value
    """
    fw_cells = [tf.contrib.rnn.LSTMCell(layer, name='basic_lstm_cell') for layer in hidden_layer]
    fw_drops = [tf.contrib.rnn.DropoutWrapper(lstm, output_keep_prob=keep_prob_) for lstm in fw_cells]
    fw_stacked_cell = tf.contrib.rnn.MultiRNNCell(fw_drops)

    bw_cells = [tf.contrib.rnn.LSTMCell(layer, name='basic_lstm_cell') for layer in hidden_layer]
    bw_drops = [tf.contrib.rnn.DropoutWrapper(lstm, output_keep_prob=keep_prob_) for lstm in bw_cells]
    bw_stacked_cell = tf.contrib.rnn.MultiRNNCell(bw_drops)

    outputs, _ = tf.nn.bidirectional_dynamic_rnn(fw_stacked_cell, bw_stacked_cell, sentences,
                                                 sequence_length=sentences_length, dtype=tf.float32)

    outputs = tf.identity(outputs, name="outputs")

    return outputs


def build_cost_fn_and_opt(lstm_outputs, indice,  scores_, learning_rate, n_hidden):
    """
    Create the Loss function and Optimizer
    :parm "lstm_outputs"    : output of lstm layers
    :parm "embed_len"       : length of output of lstm
    :parm "scores_"         : true score value
    :parm "learning_rate"   : learning rate
    """
    outputs_fw = tf.gather_nd(lstm_outputs[0], indice)
    outputs_bw = tf.gather_nd(lstm_outputs[1], indice)
    outputs_concat = tf.concat([outputs_fw, outputs_bw], axis=1)
    weights = tf.Variable(tf.random_normal([n_hidden * 2, 1], seed=10))
    bias = tf.Variable(tf.random_normal([1], seed=10))
    predictions = tf.matmul(outputs_concat, weights) + bias
    predictions = tf.identity(predictions, name="predictions")

    loss = tf.losses.mean_squared_error(scores_, predictions)
    optimzer = tf.train.AdamOptimizer(learning_rate).minimize(loss)

    return predictions, loss, optimzer

