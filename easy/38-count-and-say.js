/* Time/Space ? (would love some input on this) - I believe this is O(N^2) on time
 * This was interesting, but understanding the problem is incredibly frustrating, and
 * it was hard to know what the rules of countAndSay were, even with examples
 * Sorry if the comments get a bit redundant but this was a very confusing prompt
 * so I went overboard.
 */ 


/** Helper function to count the number of simultaneous occurences of the first char in a string n
 * @param {string} n
 * @return {number}
 * 
 * countSimultaneousOccurences("aaab") --> 3
 * countSimultaneousOccurences("1121") --> 2
 * countSimultaneousOccurences("1312") --> 1
 * 
 * When called on empty string it returns 0, but that doesn't happen with the way it's used in countAndSay
 */
var countSimultaneousOccurences = function(n) {
    let occurences = 0
    let target = ""
    for (i = 0; i < n.length; i++) {
        if (i == 0) {
            target = n.charAt(i); // Set target to first char of string
        } else if (target != n.charAt(i)) {
            break; // Can just be done, no need to see the rest of the string
        }
        occurences++;
    }
    
    return occurences 
};


/**
 * @param {number} n
 * @return {string}
 */
var countAndSay = function(n) {
    /* countAndSay(n) is really just "saying" countAndSay(n-1) out loud
     * This is kind of like an inductive proof type thing
     */
    if (n == 1) {
        return "1" // Base case from prompt
    } else {
        
    let countedAndSaid = countAndSay(n-1); // Grab the string to "say"

    // The process of "saying" the string countedAndSaid
    let out = "";
    let idx = 0
    while (idx < countedAndSaid.length) {
        /* This loop relies on the way each string encodes info about how to say it
         * for ex. countAndSay(4) --> 1211
         * how to find countAndSay(5)?
         * They break up into chunks when you read them
         * So the first index of countAndSay(4) = 1211 is 1, which is read off as "11" (one occurence of 1)
         * Then 2 is "12" (one occurence of 2)
         * Then 11 is "21" (two occurences of 1)
         * To get the next one up, read it off literally
         * So its "one occurence of 1", "one occurence of 2", "two occurences of 1" --> 11,12,21 --> 111221
         * Even indices store number of occurences of the digit
         * Odd indices store the digit itself
         */
        let num = countSimultaneousOccurences(countedAndSaid.slice(idx, countedAndSaid.length))
        // num is the number of occurences, so add it to the string
        out += (num)
        // the number we want to add is the number we counted occurences of, stored at idx
        out += (countedAndSaid.charAt(idx))

        // increment idx by the number of simultaneous occurences to skip repeats that we've accounted for
        /* For example, say we are working on 111221
         * The first time we run this, we're working on 1 (we'll get "31", 3 occurences of 1)
         * But if we were to increment by 1, we'd be working on 1 again (and get "21")
         * We actually want to go to 2 now, which is 3 indices away from where we are
         */
        idx += num
    }
        
    return out
    }
};