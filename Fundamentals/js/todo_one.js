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
// console.log(set_swap('Dalius', 42 ))

// ------------------------------------------------------------------------------------------------------

// Print -52 to 1066

// Print integers from -52 to 1066 using a FOR loop. 

function loopty_loop() {
    for (let i = -52; i <= 1066; i++) {
        console.log(i);
    }
}

// console.log(loopty_loop());

// -------------------------------------------------------------------------------------


// Don’t Worry, Be Happy

// Create beCheerful(). Within it, console.log string "good morning!" Call it 98 times.

// note: this is a for loop if we are going to call this 98 times in the console
// I think we would have to do the .length() function for this one or maybe not...
function beCheerful() {
    for (let i = 1; i <= 98; i++) {
        console.log("good morning!");
    }
}
// console.log(beCheerful());

// ------------------------------------------------------------------------

// Multiples of Three – but Not All

// Using FOR, print multiples of 3 from -300 to 0. Skip -3 and -6.

function multiple_of_three() {
    for (let i = -300; i <= 0; i += 3) {
        if (i === -3 || i === -6) {
          continue; // Skip -3 and -6
        }
        console.log(i);
    }
}
// console.log(multiple_of_three());

// ---------------------------------------------------------------------

// Printing Integers with While

// Print integers from 2000 to 5280, using a WHILE.

// explanation: In this code, we initialize the variable num to 2000,
// and then we use a while loop to repeatedly execute the block of code inside it until 
// the condition num <= 5280 becomes false. Inside the loop, 
// we print the value of num to the console, and then we increment its value by 1 using the num++ statement.

// The loop will keep running as long as num is less than or equal to 5280,
// so it will print all integers from 2000 to 5280, inclusive.

function while_int(x,y) {
    let num = x;

    while (num <= y) {
        console.log(num);
        num++;
    }

} 
console.log(while_int(2000, 5280))
// ---------------------------------------------------------------------