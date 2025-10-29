const speciesInfo = {
    'Iris-setosa': {
        icon: '🌼',
        description: 'Iris Setosa is characterized by short petals and typically grows in arctic and subarctic regions.'
    },
    'Iris-versicolor': {
        icon: '🌸',
        description: 'Iris Versicolor has medium-sized petals and is commonly found in wetlands of eastern North America.'
    },
    'Iris-virginica': {
        icon: '🌺',
        description: 'Iris Virginica features the longest petals and grows in southern and eastern United States.'
    }
};

function classifyIris(sepalLength, sepalWidth, petalLength, petalWidth) {
    if (petalLength < 2.5) {
        return 'Iris-setosa';
    } else if (petalWidth < 1.8) {
        return 'Iris-versicolor';
    } else {
        return 'Iris-virginica';
    }
}

document.getElementById('irisForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const sepalLength = parseFloat(document.getElementById('sepalLength').value);
    const sepalWidth = parseFloat(document.getElementById('sepalWidth').value);
    const petalLength = parseFloat(document.getElementById('petalLength').value);
    const petalWidth = parseFloat(document.getElementById('petalWidth').value);

    const species = classifyIris(sepalLength, sepalWidth, petalLength, petalWidth);
    const info = speciesInfo[species];

    document.querySelector('.flower-icon').textContent = info.icon;
    document.getElementById('speciesName').textContent = species;
    document.getElementById('infoText').textContent = info.description;

    const resultDiv = document.getElementById('result');
    resultDiv.classList.remove('show');
    setTimeout(() => {
        resultDiv.classList.add('show');
    }, 100);
});