// title:              returning strings
// category:           string, fundamentals
// Description:        Make a function that will return a greeting statement that
//                     uses an input; your program should return,
//                     "Hello, <name> how are you doing today?".
//                     [Make sure you type the exact thing I wrote or the program may not execute 
//                     properly]

export function greet(name: string): string {
    let greetings: string = `Hello ${name}, how is your day going?`;
    return greetings;
};

// greet('dalius');
console.log(greet('dalius'));