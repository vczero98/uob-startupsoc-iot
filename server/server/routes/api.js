const express    = require("express"),
      router     = express.Router();

router.get("/test", (req, res) => {
	res.send(JSON.stringify({success: true}));
});

module.exports = router;