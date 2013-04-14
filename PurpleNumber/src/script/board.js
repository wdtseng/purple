function highlightTheFour(gridNumber) {
  document.getElementById('board').className = 'board arrow' + gridNumber;
  var offsets = [0, 4, 6, 8];
  for (var index = 0; index < 12; ++index) {
    document.getElementById('grid' + index).className = 'grid'
  }
  for (var index = 0; index < offsets.length; ++index) {
    var gridToHighlight = (gridNumber + offsets[index]) % 12;
    document.getElementById('grid' + gridToHighlight).className = 'grid the-four'
  }
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
