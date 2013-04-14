function highlightTheFour(gridNumber) {
  document.getElementById('board').className = 'board arrow' + gridNumber;
  var offsets = [0, 4, 6, 8];
  for (var index = 0; index < 12; ++index) {
    document.getElementById('grid' + index).className = 'grid'
  }
  document.getElementById('grid' + gridNumber).className = 'grid ming-grid'
  document.getElementById('grid' + ((gridNumber + 4) % 12)).className = 'grid triad-grid'
  document.getElementById('grid' + ((gridNumber + 8) % 12)).className = 'grid triad-grid'
  document.getElementById('grid' + ((gridNumber + 6) % 12)).className = 'grid opposite-grid'
}

window.onload = function() {
  for (var gridNumber = 0; gridNumber < 12; ++gridNumber) {
    document.getElementById('grid' + gridNumber).onclick = (function(gridNumber) {
      return function() {
        highlightTheFour(gridNumber);
      }
    })(gridNumber);
  }
}
