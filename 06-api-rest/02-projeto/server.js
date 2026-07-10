const express = require("express");
const app = express();

let data = [{ id: 1, nome: "caneta" }];

app.use(express.json());

app.get("/itens", function(req, res) {
    res.json(data);
});

app.post("/itens", function(req, res) {
    const { id, nome } = req.body;
    data.push({ id, nome });
    res.json({ id, nome });
});

app.listen(3000, function() {
    console.log("Server is running");
});