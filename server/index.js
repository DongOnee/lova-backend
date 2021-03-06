let express = require('e xpress')
let Essay = require('./models/essay')
let {PythonShell} = require('python-shell')

const router = express.Router();

// Insert Essay to moongodb
router.post('/essay', (req, res) => {
    const post = req.body

    let essay = new Essay()
    essay = Object.assign(essay, post)
    essay.save((err) => {
        if (err) res.json({ success: false })
        else res.json({ success: true, id: essay._id });
    })
});

router.get('/essay/:youtube_id', (req, res) => {
    let youtube_id = req.params.youtube_id

    let options = {
        mode: 'text',
        pythonPath: '/home/cap/miniconda3/envs/lova36/bin/python',
        scriptPath: 'server/python',
        args: [youtube_id]
    };

    PythonShell.run('youtube_script_api.py', options, function (err, result) {
        if (err) throw err;

        let essay = new Essay()
        essay = Object.assign(essay, result[0])                       
        essay.save((err) => {                                    
            if (err) res.json({ success: false })                
            else res.json({ success: true, id: essay._id });
        })
    })
});

// Logical Validation
router.get('/lv/:essay_id', (req, res) => {
    let essay_id = req.params.essay_id

    let options = {
        mode: 'text',
        pythonPath: '/home/cap/miniconda3/envs/lova36/bin/python',
        scriptPath: 'server/python/logical',
        args: [essay_id]
    };

    PythonShell.run('logical.py', options, function (err, result) {
        if (err) throw err;
        string2json = JSON.parse(result[0])
        res.json(string2json)
    });
});

// Quote Extraction
router.get('/ec/:essay_id', (req, res) => {
    let essay_id = req.params.essay_id
    let options = {
        mode: 'text',
        pythonPath: '/home/cap/miniconda3/envs/lova36/bin/python',
        scriptPath: 'server/python/quote',
        args: [essay_id, "--checkpoint_dir=1554271027/checkpoints"]
    };

    PythonShell.run('prediction.py', options, function (err, result) {
        if (err) throw err;
        string2json = JSON.parse(result[0])
        res.json(string2json)
    });
});

// Truth Judgement
router.post('/tv', (req, res) => {
    let sentence = req.body.sentence

    let options = {
        mode: 'text',
        pythonPath: '/home/cap/miniconda3/envs/lova27/bin/python',
        scriptPath: 'server/python/nlstc-master',
        args: ["-v /tmp/usb/capstone/1551248019/checkpoints/vocab", "-m /tmp/usb/capstone/1551248019/checkpoints", "-s '"+sentence+"'"]
    };

    PythonShell.run('run.py', options, function (err, result) {
        if (err) throw err;

        try
        {
            res.json(JSON.parse(result[0]))
        }
        catch (e)
        {
            console.log("Truth Judgement Error:"+e)
            res.json({"result": 0})
        }
    });
});

module.exports = router
