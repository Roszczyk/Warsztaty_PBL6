const express = require("express")
const path = require('path')
const app = express()

var PORT = 8080
// View Engine Setup
app.set("views", path.join(__dirname))
app.set("view engine", "ejs")

function sleep(milliseconds) {
    const date = Date.now();
    let currentDate = null;
    do {
      currentDate = Date.now();
    } while (currentDate - date < milliseconds);
  }

app.get("/DivideServer", function (req, res) {

    var first = req.query.first
    var second = req.query.second

    console.log("first :", first, "second :", second)
    const start = Date.now();
    var result = divideDelayed(first, second);
    console.log("result:   " + result);
    var done = Date.now()
    console.log("time: " + (done - start) )
    res.setHeader('content-type', 'application/json');
    res.send(JSON.stringify(result))
})

app.listen(PORT, function (error) {
    if (error) throw error
    console.log("Server created Successfully on PORT", PORT)
})

var divide = function (a, b) {
    if (Number(b) == 0){
        console.log("Dzielenie przez 0")
        return 0.0;
    }
    return Number(a) / Number(b);
}

var divideDelayed = function (a, b) {
    sleep(2000);
    if (Number(b) == 0){
        console.log("Dzielenie przez 0")
        return 0.0;
    }
    return Number(a) / Number(b);
}
