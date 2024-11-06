document.getElementById('form').onsubmit = function(event) {
    event.preventDefault();
    const name = document.getElementById('name').value;
    window.location.href = `/champion/${name}`; }