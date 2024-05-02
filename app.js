const express = require("express");
const bodyParser = require("body-parser");
const ejs = require("ejs");

const app = express();

app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static("public"));
app.set('view engine', 'ejs');

app.get("/", function(req, res){
    res.render('index.ejs');
})

app.get("/about", function(req, res){
    res.render('about')
})

app.listen(3000, function(){
    console.log("server is running on port 3000");
})