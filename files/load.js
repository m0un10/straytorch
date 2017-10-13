const grid = new tui.Grid({
    el: document.getElementById('grid'),
    data: data,
    rowHeaders: ['rowNum'],
    bodyHeight: gridBodyHeight,
    summary: {
      height: 40,
      position: 'bottom',
      columnContent: {
        'key': {
          template: function(valueMap) {
            return `TOTAL: ${valueMap.cnt}`;
          }
        },
        'difference': {
          template: function(valueMap) {
            return `${valueMap.filtered.cnt} selected`;
          }
        }
      }
    },
    columnOptions: {
      resizable: true
    },
    columns: columns
});
