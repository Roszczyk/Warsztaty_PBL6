const express = require("express")
const path = require('path')
const app = express()

var PORT = 8080
// View Engine Setup
app.set("views", path.join(__dirname))
app.set("view engine", "ejs")

app.get("/add", function (req, res) {

    var first = req.query.first
    var second = req.query.second

    console.log("first :", first, "second :", second)
    var result = add(first, second);
    console.log("result:   " + result);
    res.setHeader('content-type', 'application/json');
    res.send(JSON.stringify(result))
})

app.listen(PORT, function (error) {
    if (error) throw error
    console.log("Server created Successfully on PORT", PORT)
})

var add = function (a, b) {
    return Number(a) + Number(b) + 100;
}
