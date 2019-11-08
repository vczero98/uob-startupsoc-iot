const express    = require('express');
	  app        = express(),
	  bodyParser = require('body-parser'),
	  path       = require('path'),
	  server     = require('http').createServer(app),
	  https      = require('https');

const port          = process.env.PORT,
	  serverAddress = process.env.ADDRESS;
	  
app.set("view engine", "ejs");
app.use(express.static(path.join(__dirname, "public")));
app.use(bodyParser.urlencoded({extended: true}));
app.set('views', path.join(__dirname, '/views'));

// Routes
var apiRoutes = require("./routes/api");

app.use('/api', apiRoutes);

app.get("/", (req, res) => {
	res.send('main page here');
});

server.listen(port, serverAddress, () => {
	console.log('Server listening at ' + serverAddress + ":" + port);
});