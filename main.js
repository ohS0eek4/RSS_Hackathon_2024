const express = require('express');
const app = express();
app.use(express.static(__dirname+'/static'));

app.get('/', (req, res) => {
  res.sendFile(__dirname+'/static/index.html');
});

app.listen(3000, () => {
  console.log('Server listening on port 3000');
});
