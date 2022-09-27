function toDecimal(odd, type) {
    switch (type) {
        case 0:
            let american = parseInt(odd.slice(1,))
            if (odd[0] == '+') {
                return (american / 100 + 1).toFixed(2)
            } else if (odd[0] == '-') {
                return (100 / american + 1).toFixed(2)
            }
            break
        case 1:
            return math.number(math.fraction(odd)) + 1
            break
    }
}

function toAmerican(odd, type) {
    switch (type) {
        case 1:
            let decimal = toDecimal(odd, 1)
            if (decimal < 2) {
                return '-' + 100 / (decimal - 1);
            } else {
                return '+' + (decimal - 1) * 100;
            }
            break
        case 2:
            if (odd < 2) {
                return '-' + 100 / (odd - 1);
            } else {
                return '+' + (odd - 1) * 100;
            }
            break
    }
}

function toFractional(odd, type) {
    switch (type) {
        case 0:
            let decimal = toDecimal(odd, 0)
            return math.fraction(decimal - 1)['n'] + '/' + math.fraction(decimal - 1)['d']
            break
        case 2:
            return math.fraction(odd - 1)['n'] + '/' + math.fraction(odd - 1)['d']
            break
    }
}

const arbitraje = document.getElementById('arbitraje')
const options3 = document.getElementById('options3')
const totalbet_el = document.getElementById('totalbet')
const gain = document.getElementById('gain')
const profit = document.getElementById('profit')
const options = arbitraje['options']
const odd1 = arbitraje['odd1']
const odd2 = arbitraje['odd2']
const odd3 = arbitraje['odd3']
const bet1 = arbitraje['bet1']
const bet2 = arbitraje['bet2']
const bet3 = arbitraje['bet3']
const gain1 = arbitraje['gain1']
const gain2 = arbitraje['gain2']
const gain3 = arbitraje['gain3']


function calculate(rate) {
    const calc = document.getElementById('cuotas');
    const d = calc['decimal'].value;
    const a = calc['american'].value;
    const f = calc['fractional'].value;
    //console.log(math.fraction(0.2)['n']+'/'+math.fraction(0.2)['d']);
    if (rate == 0 && d != '') {
        calc['american'].value = toAmerican(parseInt(d), 2)
        calc['fractional'].value = toFractional(parseInt(d), 2)
    } else if (rate == 1 && a != '') {
        calc['decimal'].value = toDecimal(a, 0)
        calc['fractional'].value = toFractional(a, 0)
    } else if (rate == 2 && f != '') {
        calc['american'].value = toAmerican(f, 1)
        calc['decimal'].value = toDecimal(f, 1)
    }
}


options.addEventListener('change', () => {
    if (options.value === '2') {
        //options2.hidden = false
        options3.hidden = true
    } else if (options.value === '3') {
        //options2.hidden = true
        options3.hidden = false
    }
})

function sureBet() {
    let totalbet
    let ready=false
    if (options.value === '2'){

        if (odd1.value != '' && odd2.value != '' && bet1.value != '') {
            gain1.value = odd1.value * bet1.value
            gain2.value = odd1.value * bet1.value
            bet2.value = gain1.value / odd2.value
            totalbet=parseInt(bet1.value)+parseInt(bet2.value)
            ready=true
        }
    } else if (options.value === '3') {
        if (odd1.value !== '' && odd2.value !== '' && odd3.value !== '' && bet1.value !== '') {
            gain1.value = odd1.value * bet1.value
            gain2.value = odd1.value * bet1.value
            gain3.value = odd1.value * bet1.value
            bet2.value = gain1.value / odd2.value
            bet3.value = gain1.value / odd3.value
            totalbet=parseInt(bet1.value)+parseInt(bet2.value)+parseInt(bet3.value)
            ready=true
        }
    }
    if (ready) {
        totalbet_el.innerText = '$'+totalbet
        gain.innerText = '$'+gain1.value
        profit.innerText = '$'+(gain1.value - totalbet).toString()
    }
}