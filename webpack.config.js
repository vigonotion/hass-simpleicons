const path = require('path');

const common = {
  mode: 'production',
  module: {
    rules: [
      {
        test: /\.svg$/i,
        use: 'raw-loader'
      },
    ],
  },
}

module.exports = [
  {
    entry: './js/si.js',
    output: {
      filename: 'custom_components/simpleicons/data/si.js',
      path: path.resolve(__dirname)
    },
    ...common,
  }
];
