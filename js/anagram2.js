exports.anagramsFor = function(word, listOfWords) {
    //answer array to push matches into
let ansArray = []
//taking the target word, removing any spaces, taking any alpha characters to upper and then sorting and joining back to a string
let str1 = word.split('').map(elem => elem.replace(' ', '')).map(elem => elem.match(/[a-zA-Z]/) ? elem.toUpperCase() : elem).sort().join('')
//looping through the array doing the same to each word as the target word
for (let word2 of listOfWords) {
    let str2 =word2.split('').map(elem => elem.replace(' ', '')).map(elem => elem.match(/[a-zA-Z]/) ? elem.toUpperCase() : elem).sort().join('')
    //if they match I am pushing them into the ansArray
    if(str2 === str1) {
        ansArray.push(word2)
    }
}
return ansArray
};
