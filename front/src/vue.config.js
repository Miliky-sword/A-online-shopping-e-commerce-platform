module.exports = {
  assetsDir: 'static',
  devServer: {
    host: '47.108.209.135',
    port: 8080,
    headers: {
      'Access-Control-Allow-Origin': '*'
    },
    hotOnly: false,
    disableHostCheck: true
  }
}
