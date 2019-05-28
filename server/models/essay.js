let mongoose = require('mongoose')

const Schema = mongoose.Schema;

const Essay = new Schema({
    author: {type: String, default: "customer"},
    opinion: {type: String, default: "Hi."},
    paragraph: {type: String, default: "I am a boy."},
    created: { type: Date, default: Date.now }
});

module.exports = mongoose.model('essays', Essay);
