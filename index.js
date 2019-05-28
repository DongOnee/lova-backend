let express = require('express')
let bodyParser =require('body-parser')
let path =require('path')
let morgan =require('morgan')
let mongoose =require('mongoose')
let api =require('./server')

const app = express();
const port = 8997;

/* mongodb connection */
const db = mongoose.connection;
db.on('error', console.error);
db.once('open', () => { console.log('Connected to mongodb server'); });
mongoose.connect('mongodb://localhost/mongodb_tutorial', { useNewUrlParser: true });

app.use('/', express.static(path.join(__dirname, './public')));
app.use(morgan('dev'));
app.use(bodyParser.json());

app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});

app.use('/api', api);

app.listen(port, () => {
    console.log('Express is listening on port', port);
});
