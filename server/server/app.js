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

const deviceState = {
	lights: [true, true, true, true, true, true, true],
	flame: false,
	handleLightsUpdated: () => {},
	handleFlameUpdated: () => {}
}

// Socket IO
const client = require("./io/client")(io, deviceState);
const pi = require("./io/pi")(io, deviceState);

// Toggle flame

function toggleFlame() {
	deviceState.flame = !deviceState.flame;
	deviceState.handleFlameUpdated();
	console.log(`flame is ${deviceState.flame}...`);
	setTimeout(toggleFlame, 5000);
}
toggleFlame();

app.use('/api', apiRoutes);

app.get("/", (req, res) => {
	res.render('index');
});

server.listen(port, serverAddress, () => {
	console.log('Server listening at ' + serverAddress + ":" + port);
});