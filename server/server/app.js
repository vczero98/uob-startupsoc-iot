const express    = require('express');
	  app        = express(),
	  bodyParser = require('body-parser'),
	  path       = require('path'),
	  http       = require('http')
	  server     = http.createServer(app),
	  io         = require('socket.io').listen(server),
	  https      = require('https');

const port          = process.env.PORT,
	  serverAddress = process.env.ADDRESS;
	  
app.set("view engine", "ejs");
app.use(express.static(path.join(__dirname, "public")));
app.use(bodyParser.urlencoded({extended: true}));
app.set('views', path.join(__dirname, '/views'));

// Routes
var apiRoutes = require("./routes/api");

// Socket IO
const pi = require("./io/pi")(io);

app.use('/api', apiRoutes);

app.get("/", (req, res) => {
	res.send('main page here');
});

server.listen(port, serverAddress, () => {
	console.log('Server listening at ' + serverAddress + ":" + port);
});