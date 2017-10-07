const grid = new tui.Grid({
    el: document.getElementById('grid'),
    data: data,
    rowHeaders: ['rowNum'],
    bodyHeight: 500,
    summary: {
      height: 40,
      position: 'bottom', // or 'top'
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
    columns: [
        {
            header: 'Name',
            name: 'key',
            filter: { 
              type: 'text',
              showClearBtn: true
            },
            ellipsis: true
        },
        {
          header: 'Difference?',
          name: 'difference',
          width: 100,
          align: 'center',
          resizable: false,
          filter: 'select'
        },
        {
            header: 'acg.r01.ana.soa',
            name: 'acg.r01.ana.soa',
            align: 'center',
            ellipsis: true,
            filter: { 
              type: 'text',
              showClearBtn: true
            }
        },
        {
            header: 'acg.r01.dit.soa',
            name: 'acg.r01.dit.soa',
            align: 'center',
            ellipsis: true,
            filter: { 
              type: 'text',
              showClearBtn: true
            }
        },
        {
          header: 'acg.r01.bld.soa',
          name: 'acg.r01.bld.soa',
          align: 'center',
          ellipsis: true,
          filter: { 
            type: 'text',
            showClearBtn: true
          }
        },
        {
          header: 'acg.r01.drd.soa',
          name: 'acg.r01.drd.soa',
          align: 'center',
          ellipsis: true,
          filter: { 
            type: 'text',
            showClearBtn: true
          }
        },
        {
          header: 'acg.r01.trn.soa',
          name: 'acg.r01.trn.soa',
          align: 'center',
          ellipsis: true,
          filter: { 
            type: 'text',
            showClearBtn: true
          }
        },
        // {
        //   header: 'acg.r99.upg.soa',
        //   name: 'acg.r99.upg.soa',
        //   align: 'center',
        //   ellipsis: true,
        //   filter: { 
        //     type: 'text',
        //     showClearBtn: true
        //   }
        // },
        {
          header: 'acg.r01.eft.soa',
          name: 'acg.r01.eft.soa',
          align: 'center',
          ellipsis: true,
          filter: { 
            type: 'text',
            showClearBtn: true
          }
        },
        {
          header: 'acg.r01.sit.soa',
          name: 'acg.r01.sit.soa',
          align: 'center',
          ellipsis: true,
          filter: { 
            type: 'text',
            showClearBtn: true
          }
        },
        {
          header: 'acg.r01.cit.soa',
          name: 'acg.r01.cit.soa',
          align: 'center',
          ellipsis: true,
          filter: { 
            type: 'text',
            showClearBtn: true
          }
        },
        {
          header: 'acg.r01.spt.soa',
          name: 'acg.r01.spt.soa',
          align: 'center',
          ellipsis: true,
          filter: { 
            type: 'text',
            showClearBtn: true
          }
        },
        {
          header: 'acg.r01.pst.soa',
          name: 'acg.r01.pst.soa',
          align: 'center',
          ellipsis: true,
          filter: { 
            type: 'text',
            showClearBtn: true
          }
        }
    ]
    });
