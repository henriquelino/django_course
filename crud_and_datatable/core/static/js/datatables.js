
$(document).ready(function () {
    $('#datatable').DataTable(
        {
            // https://datatables.net/reference/option/
            "deferRender": true,
            "orderMulti": true,
            "pagingType": "full_numbers",
            // "pageLength": 1
        }
    );
});