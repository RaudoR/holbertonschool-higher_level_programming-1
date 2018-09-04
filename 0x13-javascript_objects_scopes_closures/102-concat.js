#!/usr/bin/node
const args = process.argv.slice(2);
let fs = require("fs");
let textA = fs.readFileSync("./" + args[0]);
let textB = fs.readFileSync("./" + args[1]);
fs.writeFileSync("./" + args[2], textA + textB);
