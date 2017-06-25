var tb = document.getElementById('tb');
var sentence = 'Dogs are nice.'
// document.write(s);

function renderSentence (value) {

    for (var i = 0; i < value.length; ++i) {
        // loop through chars in value string
        // and create a span for each char
        // each span uses id of index of char
        // with default class
        var span = document.createElement('span');
        span.setAttribute('id', 's{}'.replace(/{}/, i));
        span.setAttribute('class', 'default');
        document.getElementById('s').appendChild(span);
        span.innerHTML = value[i];
    }


    // var sentence = document.createElement('span');
    // sentence.setAttribute('class', 'default');
    // document.getElementById('s').appendChild(sentence);
    // sentence.innerHTML = value;
}

renderSentence(sentence);

tb.addEventListener('input', function (e) {
    var correct = verifyInput(tb.value);
    console.log(tb.value);
    console.log(correct);

    if (correct) {

        for (var i = 0; i < tb.value.length; ++i) {
            document.getElementById('s{}'.replace(/{}/, i)).className = 'green';

        }
        //console.log(s.innerHTML.substr(0, tb.value.length));
        //s.innerHTML.substr(0, tb.value.length).style.color = '#00ff00';
        //console.log(s);
        //s.style.color('green');
    } else {
        for (var i = 0; i < tb.value.length; ++i) {
            document.getElementById('s{}'.replace(/{}/, i)).className = 'red';

        }
        
        //s.innerHTML.substr(0, tb.value.length);
        //s.style.color('red');
    }

});

function verifyInput(input) {
    var result = true;
    for (var i = 0; i < input.length ; ++i) {
        if (input[i] != sentence[i]) {
            result = false;
            break;
        }
    }
    return result;
}