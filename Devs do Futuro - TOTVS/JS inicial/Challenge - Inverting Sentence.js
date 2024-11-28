var sentence = 'Python é mais joia do que JS'
var division_list_sentence = sentence.split(' ')
var sentence_inverting = ''

function inverting_sentence(sentence) {

    division_list_sentence.forEach(function(word) {
        sentence_inverting =  sentence_inverting + word.split('').reverse().join('')  + ' '
    })
    console.log(sentence_inverting)
}

inverting_sentence()
