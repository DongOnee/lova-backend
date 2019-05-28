let {PythonShell} = require('python-shell')

PythonShell.defaultOptions = {
    mode: 'text',
    pythonPath: '/Users/a01082705520/anaconda/envs/LOVA/bin/python',
    scriptPath: 'server/python/logical',
    args: [essay_id]
};
