let people = [];
const colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#F06292', '#AED581', '#FFD54F'];
let currentDot = null;

function nextPage() {
    const name = document.getElementById('nameInput').value;
    const relationship = document.getElementById('relationshipInput').value;
    
    if (name && relationship) {
        people.push({ name, relationship });
        document.getElementById('page1').style.display = 'none';
        document.getElementById('page2').style.display = 'block';
        document.getElementById('personInfo').innerText = `▲ ${name} (${relationship})`;
        updateLegend();
    } else {
        alert('Please fill in both fields');
    }
}

function updateLegend() {
    const legend = document.getElementById('legend');
    legend.innerHTML = '';
    people.forEach((person, index) => {
        const item = document.createElement('div');
        item.className = 'legend-item';
        const colorSquare = document.createElement('span');
        colorSquare.className = 'legend-color';
        colorSquare.style.backgroundColor = colors[index % colors.length];
        item.appendChild(colorSquare);
        item.appendChild(document.createTextNode(`${person.name} (${person.relationship})`));
        legend.appendChild(item);
    });
}

document.getElementById('circleMap').addEventListener('click', function(e) {
    if (people.length === 0) return;

    const rect = this.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    
    const centerX = 150;
    const centerY = 150;
    const radius = Math.sqrt(Math.pow(x - centerX, 2) + Math.pow(y - centerY, 2));
    
    if (radius <= 150) {
        // Remove the previous dot if it exists
        if (currentDot) {
            currentDot.remove();
        }

        // Create and add the new dot
        const dot = document.createElement('div');
        dot.className = 'dot';
        dot.style.left = (x - 5) + 'px';
        dot.style.top = (y - 5) + 'px';
        dot.style.backgroundColor = colors[(people.length - 1) % colors.length];
        this.appendChild(dot);

        // Update the current dot reference
        currentDot = dot;

        // Update the distance for the current person
        people[people.length - 1].distance = radius;
    }
});

function addAnother() {
    document.getElementById('page1').style.display = 'block';
    document.getElementById('page2').style.display = 'none';
    document.getElementById('nameInput').value = '';
    document.getElementById('relationshipInput').value = '';
    // Reset the current dot when adding another person
    currentDot = null;
}

function finish() {
    // Sort people by distance before finishing
    people.sort((a, b) => a.distance - b.distance);
    updateLegend();
    alert('Thank you for completing the Circle of Intimacy exercise!');
}