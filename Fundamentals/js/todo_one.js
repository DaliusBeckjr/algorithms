// Setting and Swapping

// Set myNumber to 42. Set myName to your name. Now swap myNumber into myName & vice versa. 

// these will be my global var

function set_swap(myNumber, myName ) {
    let temp = myNumber;
    myNumber = myName;
    myName = temp;
    console.log('my name is ' + myName)
    console.log('my number is ' + myNumber)
}


// swapped the name and number but I do have my name and the number but 'undefined' at the end of the run
// this was a successful swap so far
console.log(set_swap('Dalius', 42 ))


// Print -52 to 1066

// Print integers from -52 to 1066 using a FOR loop. 

function loopty_loop() {
    for (let i = -52; i <= 1066; i++) {
        console.log(i);
    }
}

console.log(loopty_loop());


// Don’t Worry, Be Happy

// Create beCheerful(). Within it, console.log string "good morning!" Call it 98 times.

// note: this is a for loop if we are going to call this 98 times in the console
// I think we would have to do the .length() function for this one or maybe not...
function beCheerful() {
    for(let i = 'good morning'; i<= 98; i++ ) {
        console.log(i)
    }
}

console.log(beCheerful());