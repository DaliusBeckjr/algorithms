"use strict";
// title:              returning strings
// category:           string, fundamentals
// Description:        Make a function that will return a greeting statement that
//                     uses an input; your program should return,
//                     "Hello, <name> how are you doing today?".
//                     [Make sure you type the exact thing I wrote or the program may not execute 
//                     properly]
Object.defineProperty(exports, "__esModule", { value: true });
exports.greet = void 0;
function greet(name) {
    var greetings = "Hello ".concat(name, ", how is your day going?");
    return greetings;
}
exports.greet = greet;
;
greet('dalius');
console.log(greet('dalius'));
