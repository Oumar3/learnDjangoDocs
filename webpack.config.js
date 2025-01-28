const path = require('path');
module.exports = {
    resolve: {
        fallback: {
            "path": require.resolve("path-browserify")  // Utilisation du polyfill pour le navigateur
        }
    },
    entry: './assets/js/index.js',
    output: {
        path: path.resolve(__dirname,'static'),
        filename: 'bundle.js'
    }
};
