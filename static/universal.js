

// This creates a new Leaflet map instance and associates it with the HTML element with the id "map." 
// .fitWorld(): This method adjusts the map's view to fit the world bounds. It sets the initial zoom level and center of the map based on the available geographic data.


L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);
