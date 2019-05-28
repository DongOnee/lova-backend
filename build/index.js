import express from 'express';
import bodyParser from 'body-parser';
import path from 'path';
import morgan from 'morgan'; // HTTP REQUEST LOGGER
import mongoose from 'mongoose';
import api from './routes';

const app = express();
const port = 3000;
/* mongodb connection */
const db = mongoose.connection;
db.on('error', console.error);
db.once('open', () => {
    console.log('Connected to mongodb server');
});
mongoose.connect('mongodb://localhost/mongodb_tutorial');

app.use('/', express.static(path.join(__dirname, './public')));
app.use(morgan('dev'));
app.use(bodyParser.json());

app.use('/api', api);

app.listen(port, () => {
    console.log('Express is listening on port', port);
});