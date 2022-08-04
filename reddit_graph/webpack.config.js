const path = require('path')

module.exports = {
  entry: './src/js/main.js',
  mode: 'development',
  output: {
	path: `${__dirname}/dist`,
	filename: 'bundle.js',
  },
  devServer: {
    static: {
      directory: path.join(__dirname, 'public'),
    },
    compress: true,
    port: 8080,
  },
};